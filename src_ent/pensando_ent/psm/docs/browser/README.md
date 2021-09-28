```python

import time
import psm
from pprint import pprint
from api import browser_v1_api
from pensando_ent.psm.model.browser_browse_request_list import BrowserBrowseRequestList
from pensando_ent.psm.model.browser_browse_response import BrowserBrowseResponse
from pensando_ent.psm.model.browser_browse_response_list import BrowserBrowseResponseList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = browser_v1_api.BrowserV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
meta_name = "meta.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)

    try:
        api_response = api_instance.get_query1(t_kind=t_kind, t_api_version=t_api_version, meta_name=meta_name, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling BrowserV1Api->get_query1: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrowserV1Api* | [**get_query1**](docs/BrowserV1Api.md#get_query1) | **GET** /configs/browser/v1/query | 
*BrowserV1Api* | [**get_references**](docs/BrowserV1Api.md#get_references) | **GET** /configs/browser/v1/dependencies/** | 
*BrowserV1Api* | [**get_referrers**](docs/BrowserV1Api.md#get_referrers) | **GET** /configs/browser/v1/dependedby/** | 
*BrowserV1Api* | [**post_query**](docs/BrowserV1Api.md#post_query) | **POST** /configs/browser/v1/query | 


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](docs/ApiObjectMeta.md)
 - [ApiObjectRef](docs/ApiObjectRef.md)
 - [ApiStatus](docs/ApiStatus.md)
 - [ApiStatusResult](docs/ApiStatusResult.md)
 - [ApiTimestamp](docs/ApiTimestamp.md)
 - [ApiTypeMeta](docs/ApiTypeMeta.md)
 - [ApiWatchControl](docs/ApiWatchControl.md)
 - [ApiWatchEvent](docs/ApiWatchEvent.md)
 - [ApiWatchEventList](docs/ApiWatchEventList.md)
 - [BrowserBrowseRequest](docs/BrowserBrowseRequest.md)
 - [BrowserBrowseRequestList](docs/BrowserBrowseRequestList.md)
 - [BrowserBrowseRequestObject](docs/BrowserBrowseRequestObject.md)
 - [BrowserBrowseResponse](docs/BrowserBrowseResponse.md)
 - [BrowserBrowseResponseList](docs/BrowserBrowseResponseList.md)
 - [BrowserBrowseResponseObject](docs/BrowserBrowseResponseObject.md)
 - [BrowserObject](docs/BrowserObject.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [ObjectURIs](docs/ObjectURIs.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm.apis and psm.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm.api.default_api import DefaultApi`
- `from psm.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm
from psm.apis import *
from psm.models import *
```
