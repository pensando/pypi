# sysruntime

This page provides working code examples for the **sysruntime** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DistributedservicecardsV1Api* | [**post_query_connection**](../../../docs/DistributedservicecardsV1Api.md#post_query_connection) | **POST** /sysruntime/distributedservicecards/v1/{DSCName}/connections | Active Connection Query


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

[preferences README.md](..//preferences/README.md)

[recoverykeys README.md](..//recoverykeys/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[sysruntime README.md](..//sysruntime/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


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
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [SysruntimeConnTrackInfo](../../../docs/SysruntimeConnTrackInfo.md)
 - [SysruntimeConnectionFilter](../../../docs/SysruntimeConnectionFilter.md)
 - [SysruntimeConnectionRequest](../../../docs/SysruntimeConnectionRequest.md)
 - [SysruntimeConnectionStatus](../../../docs/SysruntimeConnectionStatus.md)
 - [SysruntimeFlowData](../../../docs/SysruntimeFlowData.md)
 - [SysruntimeFlowInfo](../../../docs/SysruntimeFlowInfo.md)
 - [SysruntimeFlowKey](../../../docs/SysruntimeFlowKey.md)
 - [SysruntimeFlowKeyESPInfo](../../../docs/SysruntimeFlowKeyESPInfo.md)
 - [SysruntimeFlowKeyICMPInfo](../../../docs/SysruntimeFlowKeyICMPInfo.md)
 - [SysruntimeFlowKeyL2](../../../docs/SysruntimeFlowKeyL2.md)
 - [SysruntimeFlowKeyTcpUdpInfo](../../../docs/SysruntimeFlowKeyTcpUdpInfo.md)
 - [SysruntimeFlowKeyV4](../../../docs/SysruntimeFlowKeyV4.md)
 - [SysruntimeFlowSpec](../../../docs/SysruntimeFlowSpec.md)
 - [SysruntimeFlowStatus](../../../docs/SysruntimeFlowStatus.md)
 - [SysruntimeFwStatus](../../../docs/SysruntimeFwStatus.md)
 - [SysruntimeHWConnectionGetResponse](../../../docs/SysruntimeHWConnectionGetResponse.md)
 - [SysruntimeHWConnectionSpec](../../../docs/SysruntimeHWConnectionSpec.md)
 - [SysruntimeHWConnectionStats](../../../docs/SysruntimeHWConnectionStats.md)
 - [SysruntimeHWConnectionStatus](../../../docs/SysruntimeHWConnectionStatus.md)
 - [SysruntimeHWFlowStats](../../../docs/SysruntimeHWFlowStats.md)
 - [SysruntimeIPSecStatus](../../../docs/SysruntimeIPSecStatus.md)
 - [SysruntimeTelemetryInfo](../../../docs/SysruntimeTelemetryInfo.md)
 - [SysruntimeWorkloadSelector](../../../docs/SysruntimeWorkloadSelector.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_ent.apis and psm_ent.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_ent.api.default_api import DefaultApi`
- `from psm_ent.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_ent
from psm_ent.apis import *
from psm_ent.models import *
```
