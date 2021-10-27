# Pensando PSM API Overview
The Pensando PSM is the central management component of the Pensando Distributed Services Platform. 
It provides a programmable, secure microservice-based infrastructure to control global policies and distributed services in a data center, such as Network, Security and  Storage services.
The PSM platform consists of an odd number of quorum controller nodes (e.g. 3, 5, 7) that provide consistent services to thousands of physical devices utilizing Pensando Distributed Services Cards (DSCs).  
The following figure is an architectural diagram of the PSM platform. 
![](img/PSM_Architecture.png)

PSM nodes run as virtual appliances, deployed as OVA or QCOW2 images.  
However, the physical nodes hosting the VMs should run on separate physical servers for greater fault tolerance. 
The key-value (KV) store is based on etcd and distributed across all PSM nodes.  Maintaining low latency between the nodes is critical to cluster performance.  
All PSM components use gRPC with TLS to communicate with DSCs and other PSM nodes.
In the PSM, the API gateways are distributed and run on all PSM nodes.  
At any point, there is a single instance of the API Server running.  
The API Server is highly available and will be restarted elsewhere by Kubernetes in case of a node failure.  
All cluster services such as Network, Storage, and Controllers, including the API Server, are distributed on the PSM Nodes, 
and are managed and scheduled by the Kubernetes Controller. 

The PSM REST API is asynchronous in nature.  
A client will describe a desired state (intent) via the API.  
The PSM then applies the desired state to the components as needed.   
The observed state (actual state) is maintained and updated by the PSM and describes the current state of each component.

## PSM Object Structure and Definition
In the PSM API, as with Kubernetes, a user specifies the intent, operations are idempotent, and status describes the actual state.   
Below are the primary attributes used to describe various managed objects.
```
Kind: type of the object
Version: object version (optional)
Meta: object metadata (common to all objects, all fields are optional)
Name: string name of the object (user-provided unique string for this kind of object)
Tenant: tenant name of the object (optional)
Labels: arbitrary tags associated with an object
Spec: Object Specific Schema
Status: Object Specific Status Schema
```

Example:

![](img/schema_example1.png)


## Object Scope
There are two kinds of objects: cluster-wide and tenant-wide.  
Cluster-wide objects are global to the cluster, while tenant-wide objects are specific to each tenant. 
Some examples of cluster-wide objects are `Cluster`, `Node` and `AuthenticationPolicy`. 
Tenant-wide objects include `Network` and `SecurityGroup`.  
See the API reference for more details on individual objects.

## Response Messages
Each CRUD call receives a response message indicating the return status of the call.  
The corresponding HTTPS response code should be used as the primary indicator of success or failure for the operation. 
The JSON payload response contains return status and details. 
Below are the response status-codes that the PSM will use to indicate the operation result:

| Status Code | Description |
|-------------|-------------|
| 200 | OK |
| 400 | Bad request parameters |
| 401 | Unauthorized request |
| 409 | Conflict while processing request |
| 412 | Pre-condition failed |
| 500 | Internal Server Error |
| 501 | Request not implemented |
| 503 | Service Unavailable |



NOTE: The PSM API Gateway returns a JSON-structured payload which includes the details of the response.  
Best practice is to first check the HTTPS response code, and then parse the JSON data to get the details

## Policy Propagation
To confirm that policy propagation has completed as intended for a given managed object, 
the programmer must follow any `add/update` operation with a corresponding `get/list` of the object to verify both of the following:
* The propagation status has been marked `Propagation Complete`
* The `generation-id` field in `propagation-status` has the same value as the `generation-id` in the object’s `meta` section.

Below is an example of ensuring that propagation is complete:

![](img/propagation.png)

## Sessions
Username and Password credentials are referenced at runtime through the `PSM_USER` and `PSM_PASSWORD` environment variables.

In cases where PSM is running without SSL certificates, developers can set `configuration.verify_ssl = False` 
to avoid `Unauthorized request` responses.    

Login is implicit within the `configuration.Configuration` method, as shown below:


```
import os
from pensando_cloud.psm.apis import ClusterV1Api
from pensando_cloud.psm import configuration, api_client

import warnings
warnings.simplefilter("ignore")

configuration = configuration.Configuration(
    psm_config_path = os.environ['HOME'] + "/.psm/config.json",
    interactive_mode = True
)
configuration.verify_ssl = False

client = api_client.ApiClient(configuration)
api_instance = ClusterV1Api(client)
response = api_instance.get_cluster()
[...]

```

Following successful login, the PSM IP-addr and login token will be stored for the user in `$HOME/.psm/config.json`
There is no need to perform a token refresh.  A token is valid for six days. 
There is no need to perform a logout.  When a client no longer needs access it can simply discard the current token.  
However, deleting a user or changing RBAC privileges for a user will immediately affect any existing valid token the user might have.  

## Staging Buffer
A staging buffer allows for multiple operations to be consolidated into one single function call.  
When staging multiple calls, each individual call is authorized and validated and accumulated in the staging buffer.  
A commit operation on the staging buffer then applies and persists the contents of the staging buffer in a single function call.
Buffer commit operations have “all-or-nothing” semantics, meaning that either all changes accumulated in the buffer are applied together, or none is.  
The following shows the flow when using configuration staging. 

![](img/staging.png)

The staging buffer is represented as an object, identified by an ID which can be either user-provided (a “named buffer”), or automatically generated by the system.
All staging operations will then use this identifier. 
The buffer ID becomes part of the URL for the CRUD operations on the buffer contents.
There are two categories of actions related to the staging buffer:
* Operations on the staging buffer itself
* Staged operations in the staging buffer

### Operations on the Staging Buffer Object
All actions on the staging buffer go through RBAC authorization.  
In addition to privileges for CRUD operations for  objects that are staged, 
the following privileges are associated with the staging buffer object itself :

* Create 
* Update 
* List Buffer Contents
* Commit
* Delete
* List Staging Buffers

Only operations for which the user has privileges will be allowed on the staging buffer. 
The Update, List and Commit Operations have additional considerations for the staging buffer. 

#### Create
Creates a new staging buffer. The identifier can be user-specified or will be a system-generated ID. This identifier is used for all subsequent operations on the staging buffer. 
#### Update
Updating the staging buffer involves adding API Object CRUD operations to the staging buffer. The CRUD operations themselves are authorized separately.  To update the staging buffer with an API operation, the user needs to have both update privilege for the staging buffer, and privilege for the CRUD operation being staged. 
#### List Buffer Contents
Verifies and shows the contents of the staging buffer. This involves both semantic and syntactic validation at the API server. 
Each object in the buffer is validated, considering all the other objects in the staging buffer, plus the current state of the KV store. 
The Validation result specifies “success” or “failure”, and lists any objects that failed validation along with the associated failure messages.
#### Commit
The commit operation applies the changes in the staging buffer to the system. 
The user performing the commit must have both commit privileges on the staging buffer, and privileges for the object operations stored in the staging buffer. 
#### Delete
Deletes the staging buffer and its contents.  Has no effect on the actual objects within the staging buffer
#### List Staging Buffers
List active staging buffers.  Requires Read privileges on the staging buffer itself.

### Operations on Objects Staged in the Staging Buffer
The REST API will allow the following operations on entries within the staging buffer:
* Create
* Update
* Delete

#### Create
Creates a new staging buffer entry. The identifier can be user-specified or will be a system-generated ID. This identifier is used for all subsequent operations on the staging buffer entry. 
#### Update
Modify an existing entry in the buffer; elements to be updated are identified in the request using an URI.
#### Delete
Clears one or more entries in the staging buffer. The “clear” could be for any operation that is staged (Create/Update/Delete). Elements to be cleared are identified in the request using a URI. 
Each operation goes through the same RBAC authorization process as non-staged operations. If the operation passes RBAC, the object is validated and added to the staging buffer.  Only one operation is supported per API object referenced in the staging buffer; for example, “delete” and “modify” on the same object is not permitted.  If there is a conflicting operation on the same object then the latest operation will overwrite.  A create and a subsequent modify would modify the initial create request.


### Bulk Configuration Edits Using a Staging Buffer
PSM clients can use the staging buffer “bulk edit” feature to create, update, or delete multiple objects in one  call, 
simplifying the task of staging large numbers of configuration changes.
A typical sequence would be:
* Create a staging buffer
* Stage a single bulk edit, containing multiple operations
* Get the buffer to review its content
* Commit the buffer, executing all staged changes
* Delete the buffer

Bulk edit operations are currently supported only on config objects. 
Bulk edit operations are not supported on archive logs, configuration snapshots, rollout images or fwlogs.
