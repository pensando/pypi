
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiagnosticsV1Api* | [**debug**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#debug) | **POST** /configs/diagnostics/v1/modules/{O.Name}/Debug | Request Diagnostics information for a module
*DiagnosticsV1Api* | [**get_module**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#get_module) | **GET** /configs/diagnostics/v1/modules/{O.Name} | Get Module object
*DiagnosticsV1Api* | [**label_module**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#label_module) | **POST** /configs/diagnostics/v1/modules/{O.Name}/label | Label Module object
*DiagnosticsV1Api* | [**list_module**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#list_module) | **GET** /configs/diagnostics/v1/modules | List Module objects
*DiagnosticsV1Api* | [**update_module**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#update_module) | **PUT** /configs/diagnostics/v1/modules/{O.Name} | Update Module object
*DiagnosticsV1Api* | [**watch_module**](../../../../pensando_ent/apiDocPath}}DiagnosticsV1Api.md#watch_module) | **GET** /configs/diagnostics/v1/watch/modules | Watch Module objects. Supports WebSockets or HTTP long poll


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
