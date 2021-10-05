# Pensando Python Bindings
This repo contains the code-generated language bindings for the Pensando Policy and Services Manager (PSM).
For the Cloud pipeline bindings, please start [here](src_cloud/pensando_cloud/README.md)
For the Enterprise pipeline bindings, please start [here](src_end/pensando_ent/README.md)

Language bindings reflect the PSM REST API and are code-generated from the PSM schema, presented in Swagger format.
The authoritative REST API and the Swagger schema references for any PSM pipeline is available dynamically through any PSM instance at **https://PSM-IPaddr/docs**
and **https://PSM-IPaddr/generated/swaggeruri.html** respectively.

## Using the PSM GUI to See API Examples
REST developers can take advantage of the fact that the PSM GUI itself uses the REST API. 
REST API calls sent from the GUI to the PSM as it implements the configurations created by the user can be displayed using the API Capture feature.  
API Capture is accessible from the “Admin” menu item on the PSM GUI screen.    
On the API Capture screen, click the “Enable Live Capture” button in the upper right, to enable Live Capture.  

## Pensando PSM Overview
The Pensando PSM is the central management component of the Pensando Distributed Services Platform. 
It provides a programmable, secure microservice-based infrastructure to control global policies and distributed services in a data center, such as Network, Security and  Storage services.
The PSM platform consists of an odd number of quorum controller nodes (e.g. 3, 5, 7) that provide consistent services to thousands of physical devices utilizing Pensando Distributed Services Cards (DSCs).  
The following figure is an architectural diagram of the PSM platform. 
![](PSM_Architecture)

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
![]((schema_example1)


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
![](propagation)





