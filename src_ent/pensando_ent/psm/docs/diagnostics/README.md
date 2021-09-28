```python

import time
import psm
from pprint import pprint
from api import diagnostics_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.diagnostics_auto_msg_module_watch_helper import DiagnosticsAutoMsgModuleWatchHelper
from pensando_ent.psm.model.diagnostics_diagnostics_request import DiagnosticsDiagnosticsRequest
from pensando_ent.psm.model.diagnostics_diagnostics_response import DiagnosticsDiagnosticsResponse
from pensando_ent.psm.model.diagnostics_module import DiagnosticsModule
from pensando_ent.psm.model.diagnostics_module_list import DiagnosticsModuleList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.Name_example" # str | 
body = DiagnosticsDiagnosticsRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        parameters={
            "key": "key_example",
        },
        query="query_example",
        service_port=DiagnosticsServicePort(
            name="name_example",
            port=1,
        ),
    ) # DiagnosticsDiagnosticsRequest | 

    try:
        # Request Diagnostics information for a module
        api_response = api_instance.debug(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->debug: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiagnosticsV1Api* | [**debug**](docs/DiagnosticsV1Api.md#debug) | **POST** /configs/diagnostics/v1/modules/{O.Name}/Debug | Request Diagnostics information for a module
*DiagnosticsV1Api* | [**get_module**](docs/DiagnosticsV1Api.md#get_module) | **GET** /configs/diagnostics/v1/modules/{O.Name} | Get Module object
*DiagnosticsV1Api* | [**label_module**](docs/DiagnosticsV1Api.md#label_module) | **POST** /configs/diagnostics/v1/modules/{O.Name}/label | Label Module object
*DiagnosticsV1Api* | [**list_module**](docs/DiagnosticsV1Api.md#list_module) | **GET** /configs/diagnostics/v1/modules | List Module objects
*DiagnosticsV1Api* | [**update_module**](docs/DiagnosticsV1Api.md#update_module) | **PUT** /configs/diagnostics/v1/modules/{O.Name} | Update Module object
*DiagnosticsV1Api* | [**watch_module**](docs/DiagnosticsV1Api.md#watch_module) | **GET** /configs/diagnostics/v1/watch/modules | Watch Module objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiAny](docs/ApiAny.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiLabel](docs/ApiLabel.md)
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
 - [DiagnosticsAutoMsgModuleWatchHelper](docs/DiagnosticsAutoMsgModuleWatchHelper.md)
 - [DiagnosticsAutoMsgModuleWatchHelperWatchEvent](docs/DiagnosticsAutoMsgModuleWatchHelperWatchEvent.md)
 - [DiagnosticsDiagnosticsRequest](docs/DiagnosticsDiagnosticsRequest.md)
 - [DiagnosticsDiagnosticsResponse](docs/DiagnosticsDiagnosticsResponse.md)
 - [DiagnosticsModule](docs/DiagnosticsModule.md)
 - [DiagnosticsModuleList](docs/DiagnosticsModuleList.md)
 - [DiagnosticsModuleSpec](docs/DiagnosticsModuleSpec.md)
 - [DiagnosticsModuleStatus](docs/DiagnosticsModuleStatus.md)
 - [DiagnosticsServicePort](docs/DiagnosticsServicePort.md)
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
