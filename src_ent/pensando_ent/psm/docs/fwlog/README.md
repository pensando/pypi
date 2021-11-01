
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FwlogV1Api* | [**get_download_fw_log_file_content**](../../../../pensando_ent/docs/FwlogV1Api.md#get_download_fw_log_file_content) | **GET** /fwlog/v1/tenants/{O.Tenant}/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
*FwlogV1Api* | [**get_download_fw_log_file_content1**](../../../../pensando_ent/docs/FwlogV1Api.md#get_download_fw_log_file_content1) | **GET** /fwlog/v1/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
*FwlogV1Api* | [**get_get_logs1**](../../../../pensando_ent/docs/FwlogV1Api.md#get_get_logs1) | **GET** /fwlog/v1/query | Queries firewall logs
*FwlogV1Api* | [**get_watch_logs**](../../../../pensando_ent/docs/FwlogV1Api.md#get_watch_logs) | **GET** /fwlog/v1/watch/query | 
*FwlogV1Api* | [**post_get_logs**](../../../../pensando_ent/docs/FwlogV1Api.md#post_get_logs) | **POST** /fwlog/v1/query | Queries firewall logs


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
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
 - [FwlogFwLog](../../../docs/FwlogFwLog.md)
 - [FwlogFwLogList](../../../docs/FwlogFwLogList.md)
 - [FwlogFwLogQuery](../../../docs/FwlogFwLogQuery.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)


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
