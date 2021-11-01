
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuditV1Api* | [**get_get_event**](../../../../pensando_cloud/docs/AuditV1Api.md#get_get_event) | **GET** /audit/v1/events/{UUID} | Fetches an audit event given its uuid


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
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
 - [AuditAuditEvent](../../../docs/AuditAuditEvent.md)
 - [AuditAuditEventRequest](../../../docs/AuditAuditEventRequest.md)
 - [AuditEventAttributes](../../../docs/AuditEventAttributes.md)
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
