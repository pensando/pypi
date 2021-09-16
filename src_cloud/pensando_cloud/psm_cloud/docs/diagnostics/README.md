# diagnostics

This page provides working code examples for the **diagnostics** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiagnosticsV1Api* | [**debug**](../../../docs/DiagnosticsV1Api.md#debug) | **POST** /configs/diagnostics/v1/modules/{O.Name}/Debug | Request Diagnostics information for a module
*DiagnosticsV1Api* | [**get_module**](../../../docs/DiagnosticsV1Api.md#get_module) | **GET** /configs/diagnostics/v1/modules/{O.Name} | Get Module object
*DiagnosticsV1Api* | [**label_module**](../../../docs/DiagnosticsV1Api.md#label_module) | **POST** /configs/diagnostics/v1/modules/{O.Name}/label | Label Module object
*DiagnosticsV1Api* | [**list_module**](../../../docs/DiagnosticsV1Api.md#list_module) | **GET** /configs/diagnostics/v1/modules | List Module objects
*DiagnosticsV1Api* | [**update_module**](../../../docs/DiagnosticsV1Api.md#update_module) | **PUT** /configs/diagnostics/v1/modules/{O.Name} | Update Module object
*DiagnosticsV1Api* | [**watch_module**](../../../docs/DiagnosticsV1Api.md#watch_module) | **GET** /configs/diagnostics/v1/watch/modules | Watch Module objects. Supports WebSockets or HTTP long poll


## README links for Model Groups

[aggwatch README.md](..//aggwatch/README.md)

[audit README.md](..//audit/README.md)

[auth README.md](..//auth/README.md)

[browser README.md](..//browser/README.md)

[cluster README.md](..//cluster/README.md)

[diagnostics README.md](..//diagnostics/README.md)

[events README.md](..//events/README.md)

[fwlog README.md](..//fwlog/README.md)

[monitoring README.md](..//monitoring/README.md)

[network README.md](..//network/README.md)

[objstore README.md](..//objstore/README.md)

[orchestration README.md](..//orchestration/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiAny](../../../docs/ApiAny.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiLabel](../../../docs/ApiLabel.md)
 - [ApiListMeta](../../../docs/ApiListMeta.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [DiagnosticsAutoMsgModuleWatchHelper](../../../docs/DiagnosticsAutoMsgModuleWatchHelper.md)
 - [DiagnosticsAutoMsgModuleWatchHelperWatchEvent](../../../docs/DiagnosticsAutoMsgModuleWatchHelperWatchEvent.md)
 - [DiagnosticsDiagnosticsRequest](../../../docs/DiagnosticsDiagnosticsRequest.md)
 - [DiagnosticsDiagnosticsResponse](../../../docs/DiagnosticsDiagnosticsResponse.md)
 - [DiagnosticsModule](../../../docs/DiagnosticsModule.md)
 - [DiagnosticsModuleList](../../../docs/DiagnosticsModuleList.md)
 - [DiagnosticsModuleSpec](../../../docs/DiagnosticsModuleSpec.md)
 - [DiagnosticsModuleStatus](../../../docs/DiagnosticsModuleStatus.md)
 - [DiagnosticsServicePort](../../../docs/DiagnosticsServicePort.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_cloud.apis and psm_cloud.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_cloud.api.default_api import DefaultApi`
- `from psm_cloud.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_cloud
from psm_cloud.apis import *
from psm_cloud.models import *
```
