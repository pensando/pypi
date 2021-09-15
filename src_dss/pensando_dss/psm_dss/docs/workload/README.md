# workload

This page provides working code examples for the **workload** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WorkloadV1Api* | [**abort_migration**](../../../docs/WorkloadV1Api.md#abort_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
*WorkloadV1Api* | [**abort_migration1**](../../../docs/WorkloadV1Api.md#abort_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
*WorkloadV1Api* | [**add_workload**](../../../docs/WorkloadV1Api.md#add_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads | Create Workload object
*WorkloadV1Api* | [**add_workload1**](../../../docs/WorkloadV1Api.md#add_workload1) | **POST** /configs/workload/v1/workloads | Create Workload object
*WorkloadV1Api* | [**delete_workload**](../../../docs/WorkloadV1Api.md#delete_workload) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Delete Workload object
*WorkloadV1Api* | [**delete_workload1**](../../../docs/WorkloadV1Api.md#delete_workload1) | **DELETE** /configs/workload/v1/workloads/{O.Name} | Delete Workload object
*WorkloadV1Api* | [**final_sync_migration**](../../../docs/WorkloadV1Api.md#final_sync_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
*WorkloadV1Api* | [**final_sync_migration1**](../../../docs/WorkloadV1Api.md#final_sync_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
*WorkloadV1Api* | [**finish_migration**](../../../docs/WorkloadV1Api.md#finish_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
*WorkloadV1Api* | [**finish_migration1**](../../../docs/WorkloadV1Api.md#finish_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
*WorkloadV1Api* | [**get_endpoint**](../../../docs/WorkloadV1Api.md#get_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints/{O.Name} | Get Endpoint object
*WorkloadV1Api* | [**get_endpoint1**](../../../docs/WorkloadV1Api.md#get_endpoint1) | **GET** /configs/workload/v1/endpoints/{O.Name} | Get Endpoint object
*WorkloadV1Api* | [**get_workload**](../../../docs/WorkloadV1Api.md#get_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Get Workload object
*WorkloadV1Api* | [**get_workload1**](../../../docs/WorkloadV1Api.md#get_workload1) | **GET** /configs/workload/v1/workloads/{O.Name} | Get Workload object
*WorkloadV1Api* | [**label_workload**](../../../docs/WorkloadV1Api.md#label_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/label | Label Workload object
*WorkloadV1Api* | [**label_workload1**](../../../docs/WorkloadV1Api.md#label_workload1) | **POST** /configs/workload/v1/workloads/{O.Name}/label | Label Workload object
*WorkloadV1Api* | [**list_endpoint**](../../../docs/WorkloadV1Api.md#list_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints | List Endpoint objects
*WorkloadV1Api* | [**list_endpoint1**](../../../docs/WorkloadV1Api.md#list_endpoint1) | **GET** /configs/workload/v1/endpoints | List Endpoint objects
*WorkloadV1Api* | [**list_workload**](../../../docs/WorkloadV1Api.md#list_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads | List Workload objects
*WorkloadV1Api* | [**list_workload1**](../../../docs/WorkloadV1Api.md#list_workload1) | **GET** /configs/workload/v1/workloads | List Workload objects
*WorkloadV1Api* | [**start_migration**](../../../docs/WorkloadV1Api.md#start_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/StartMigration | Start Workload Migration operation
*WorkloadV1Api* | [**start_migration1**](../../../docs/WorkloadV1Api.md#start_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/StartMigration | Start Workload Migration operation
*WorkloadV1Api* | [**update_workload**](../../../docs/WorkloadV1Api.md#update_workload) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Update Workload object
*WorkloadV1Api* | [**update_workload1**](../../../docs/WorkloadV1Api.md#update_workload1) | **PUT** /configs/workload/v1/workloads/{O.Name} | Update Workload object
*WorkloadV1Api* | [**watch_endpoint**](../../../docs/WorkloadV1Api.md#watch_endpoint) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_endpoint1**](../../../docs/WorkloadV1Api.md#watch_endpoint1) | **GET** /configs/workload/v1/watch/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload**](../../../docs/WorkloadV1Api.md#watch_workload) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload1**](../../../docs/WorkloadV1Api.md#watch_workload1) | **GET** /configs/workload/v1/watch/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll


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
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [SecurityDSCStatus](../../../docs/SecurityDSCStatus.md)
 - [SecurityPropagationStatus](../../../docs/SecurityPropagationStatus.md)
 - [WorkloadAutoMsgEndpointWatchHelper](../../../docs/WorkloadAutoMsgEndpointWatchHelper.md)
 - [WorkloadAutoMsgEndpointWatchHelperWatchEvent](../../../docs/WorkloadAutoMsgEndpointWatchHelperWatchEvent.md)
 - [WorkloadAutoMsgWorkloadWatchHelper](../../../docs/WorkloadAutoMsgWorkloadWatchHelper.md)
 - [WorkloadAutoMsgWorkloadWatchHelperWatchEvent](../../../docs/WorkloadAutoMsgWorkloadWatchHelperWatchEvent.md)
 - [WorkloadEndpoint](../../../docs/WorkloadEndpoint.md)
 - [WorkloadEndpointList](../../../docs/WorkloadEndpointList.md)
 - [WorkloadEndpointMigrationStatus](../../../docs/WorkloadEndpointMigrationStatus.md)
 - [WorkloadEndpointSpec](../../../docs/WorkloadEndpointSpec.md)
 - [WorkloadEndpointStatus](../../../docs/WorkloadEndpointStatus.md)
 - [WorkloadWorkload](../../../docs/WorkloadWorkload.md)
 - [WorkloadWorkloadIntfSpec](../../../docs/WorkloadWorkloadIntfSpec.md)
 - [WorkloadWorkloadIntfStatus](../../../docs/WorkloadWorkloadIntfStatus.md)
 - [WorkloadWorkloadList](../../../docs/WorkloadWorkloadList.md)
 - [WorkloadWorkloadMigrationStatus](../../../docs/WorkloadWorkloadMigrationStatus.md)
 - [WorkloadWorkloadSpec](../../../docs/WorkloadWorkloadSpec.md)
 - [WorkloadWorkloadStatus](../../../docs/WorkloadWorkloadStatus.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_dss.apis and psm_dss.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_dss.api.default_api import DefaultApi`
- `from psm_dss.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_dss
from psm_dss.apis import *
from psm_dss.models import *
```
