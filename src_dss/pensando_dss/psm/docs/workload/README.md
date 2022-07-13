
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WorkloadV1Api* | [**abort_migration**](../../../../pensando_dss/docs/WorkloadV1Api.md#abort_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
*WorkloadV1Api* | [**abort_migration1**](../../../../pensando_dss/docs/WorkloadV1Api.md#abort_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
*WorkloadV1Api* | [**add_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#add_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads | Create Workload object
*WorkloadV1Api* | [**add_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#add_workload1) | **POST** /configs/workload/v1/workloads | Create Workload object
*WorkloadV1Api* | [**add_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#add_workload_group) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups | Create WorkloadGroup object
*WorkloadV1Api* | [**add_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#add_workload_group1) | **POST** /configs/workload/v1/workloadgroups | Create WorkloadGroup object
*WorkloadV1Api* | [**delete_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#delete_workload) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Delete Workload object
*WorkloadV1Api* | [**delete_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#delete_workload1) | **DELETE** /configs/workload/v1/workloads/{O.Name} | Delete Workload object
*WorkloadV1Api* | [**delete_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#delete_workload_group) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Delete WorkloadGroup object
*WorkloadV1Api* | [**delete_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#delete_workload_group1) | **DELETE** /configs/workload/v1/workloadgroups/{O.Name} | Delete WorkloadGroup object
*WorkloadV1Api* | [**final_sync_migration**](../../../../pensando_dss/docs/WorkloadV1Api.md#final_sync_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
*WorkloadV1Api* | [**final_sync_migration1**](../../../../pensando_dss/docs/WorkloadV1Api.md#final_sync_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
*WorkloadV1Api* | [**finish_migration**](../../../../pensando_dss/docs/WorkloadV1Api.md#finish_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
*WorkloadV1Api* | [**finish_migration1**](../../../../pensando_dss/docs/WorkloadV1Api.md#finish_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
*WorkloadV1Api* | [**get_endpoint**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints/{O.Name} | Get Endpoint object
*WorkloadV1Api* | [**get_endpoint1**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_endpoint1) | **GET** /configs/workload/v1/endpoints/{O.Name} | Get Endpoint object
*WorkloadV1Api* | [**get_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Get Workload object
*WorkloadV1Api* | [**get_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_workload1) | **GET** /configs/workload/v1/workloads/{O.Name} | Get Workload object
*WorkloadV1Api* | [**get_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_workload_group) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Get WorkloadGroup object
*WorkloadV1Api* | [**get_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#get_workload_group1) | **GET** /configs/workload/v1/workloadgroups/{O.Name} | Get WorkloadGroup object
*WorkloadV1Api* | [**label_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#label_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/label | Label Workload object
*WorkloadV1Api* | [**label_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#label_workload1) | **POST** /configs/workload/v1/workloads/{O.Name}/label | Label Workload object
*WorkloadV1Api* | [**label_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#label_workload_group) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name}/label | Label WorkloadGroup object
*WorkloadV1Api* | [**label_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#label_workload_group1) | **POST** /configs/workload/v1/workloadgroups/{O.Name}/label | Label WorkloadGroup object
*WorkloadV1Api* | [**list_endpoint**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints | List Endpoint objects
*WorkloadV1Api* | [**list_endpoint1**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_endpoint1) | **GET** /configs/workload/v1/endpoints | List Endpoint objects
*WorkloadV1Api* | [**list_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads | List Workload objects
*WorkloadV1Api* | [**list_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_workload1) | **GET** /configs/workload/v1/workloads | List Workload objects
*WorkloadV1Api* | [**list_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_workload_group) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups | List WorkloadGroup objects
*WorkloadV1Api* | [**list_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#list_workload_group1) | **GET** /configs/workload/v1/workloadgroups | List WorkloadGroup objects
*WorkloadV1Api* | [**start_migration**](../../../../pensando_dss/docs/WorkloadV1Api.md#start_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/StartMigration | Start Workload Migration operation
*WorkloadV1Api* | [**start_migration1**](../../../../pensando_dss/docs/WorkloadV1Api.md#start_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/StartMigration | Start Workload Migration operation
*WorkloadV1Api* | [**update_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#update_workload) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Update Workload object
*WorkloadV1Api* | [**update_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#update_workload1) | **PUT** /configs/workload/v1/workloads/{O.Name} | Update Workload object
*WorkloadV1Api* | [**update_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#update_workload_group) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Update WorkloadGroup object
*WorkloadV1Api* | [**update_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#update_workload_group1) | **PUT** /configs/workload/v1/workloadgroups/{O.Name} | Update WorkloadGroup object
*WorkloadV1Api* | [**watch_endpoint**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_endpoint) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_endpoint1**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_endpoint1) | **GET** /configs/workload/v1/watch/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_workload) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload1**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_workload1) | **GET** /configs/workload/v1/watch/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload_group**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_workload_group) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloadgroups | Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll
*WorkloadV1Api* | [**watch_workload_group1**](../../../../pensando_dss/docs/WorkloadV1Api.md#watch_workload_group1) | **GET** /configs/workload/v1/watch/workloadgroups | Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll


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
 - [ClusterIPConfig](../../../docs/ClusterIPConfig.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [LabelsRequirement](../../../docs/LabelsRequirement.md)
 - [LabelsSelector](../../../docs/LabelsSelector.md)
 - [SecurityDSCStatus](../../../docs/SecurityDSCStatus.md)
 - [SecurityPropagationStatus](../../../docs/SecurityPropagationStatus.md)
 - [WorkloadAutoMsgEndpointWatchHelper](../../../docs/WorkloadAutoMsgEndpointWatchHelper.md)
 - [WorkloadAutoMsgEndpointWatchHelperWatchEvent](../../../docs/WorkloadAutoMsgEndpointWatchHelperWatchEvent.md)
 - [WorkloadAutoMsgWorkloadGroupWatchHelper](../../../docs/WorkloadAutoMsgWorkloadGroupWatchHelper.md)
 - [WorkloadAutoMsgWorkloadGroupWatchHelperWatchEvent](../../../docs/WorkloadAutoMsgWorkloadGroupWatchHelperWatchEvent.md)
 - [WorkloadAutoMsgWorkloadWatchHelper](../../../docs/WorkloadAutoMsgWorkloadWatchHelper.md)
 - [WorkloadAutoMsgWorkloadWatchHelperWatchEvent](../../../docs/WorkloadAutoMsgWorkloadWatchHelperWatchEvent.md)
 - [WorkloadEndpoint](../../../docs/WorkloadEndpoint.md)
 - [WorkloadEndpointList](../../../docs/WorkloadEndpointList.md)
 - [WorkloadEndpointMigrationStatus](../../../docs/WorkloadEndpointMigrationStatus.md)
 - [WorkloadEndpointSpec](../../../docs/WorkloadEndpointSpec.md)
 - [WorkloadEndpointStatus](../../../docs/WorkloadEndpointStatus.md)
 - [WorkloadIPBlock](../../../docs/WorkloadIPBlock.md)
 - [WorkloadInterfaceMigrationStatus](../../../docs/WorkloadInterfaceMigrationStatus.md)
 - [WorkloadMigrationSource](../../../docs/WorkloadMigrationSource.md)
 - [WorkloadWorkload](../../../docs/WorkloadWorkload.md)
 - [WorkloadWorkloadGroup](../../../docs/WorkloadWorkloadGroup.md)
 - [WorkloadWorkloadGroupList](../../../docs/WorkloadWorkloadGroupList.md)
 - [WorkloadWorkloadGroupSpec](../../../docs/WorkloadWorkloadGroupSpec.md)
 - [WorkloadWorkloadGroupStatus](../../../docs/WorkloadWorkloadGroupStatus.md)
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
