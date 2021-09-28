```python

import time
import psm
from pprint import pprint
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pensando_ent.psm.model.fwlog_fw_log_query import FwlogFwLogQuery
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
o_name = "O.Name_example" # str | 
o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
_from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
sort_order = "sort-order_example" # str | order to sort List results in. (optional)
meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content(o_tenant, o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FwlogV1Api* | [**get_download_fw_log_file_content**](docs/FwlogV1Api.md#get_download_fw_log_file_content) | **GET** /fwlog/v1/tenants/{O.Tenant}/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
*FwlogV1Api* | [**get_download_fw_log_file_content1**](docs/FwlogV1Api.md#get_download_fw_log_file_content1) | **GET** /fwlog/v1/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
*FwlogV1Api* | [**get_get_logs1**](docs/FwlogV1Api.md#get_get_logs1) | **GET** /fwlog/v1/query | Queries firewall logs
*FwlogV1Api* | [**get_watch_logs**](docs/FwlogV1Api.md#get_watch_logs) | **GET** /fwlog/v1/watch/query | 
*FwlogV1Api* | [**post_get_logs**](docs/FwlogV1Api.md#post_get_logs) | **POST** /fwlog/v1/query | Queries firewall logs


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiListMeta](docs/ApiListMeta.md)
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
 - [FwlogFwLog](docs/FwlogFwLog.md)
 - [FwlogFwLogList](docs/FwlogFwLogList.md)
 - [FwlogFwLogQuery](docs/FwlogFwLogQuery.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)


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
