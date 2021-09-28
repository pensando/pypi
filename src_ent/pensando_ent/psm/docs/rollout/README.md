# rollout

This page provides working code examples for the **rollout** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RolloutV1Api* | [**create_rollout**](../../../docs/RolloutV1Api.md#create_rollout) | **POST** /configs/rollout/v1/rollout/CreateRollout | Start Rollout operation
*RolloutV1Api* | [**get_rollout**](../../../docs/RolloutV1Api.md#get_rollout) | **GET** /configs/rollout/v1/rollout/{O.Name} | Get Rollout object
*RolloutV1Api* | [**list_rollout**](../../../docs/RolloutV1Api.md#list_rollout) | **GET** /configs/rollout/v1/rollout | List Rollout objects
*RolloutV1Api* | [**remove_rollout**](../../../docs/RolloutV1Api.md#remove_rollout) | **POST** /configs/rollout/v1/rollout/RemoveRollout | Remove a Rollout
*RolloutV1Api* | [**stop_rollout**](../../../docs/RolloutV1Api.md#stop_rollout) | **POST** /configs/rollout/v1/rollout/StopRollout | Stop a Rollout operation
*RolloutV1Api* | [**update_rollout**](../../../docs/RolloutV1Api.md#update_rollout) | **POST** /configs/rollout/v1/rollout/UpdateRollout | Update Rollout configuration
*RolloutV1Api* | [**watch_rollout**](../../../docs/RolloutV1Api.md#watch_rollout) | **GET** /configs/rollout/v1/watch/rollout | Watch Rollout objects. Supports WebSockets or HTTP long poll


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
 - [LabelsRequirement](../../../docs/LabelsRequirement.md)
 - [LabelsSelector](../../../docs/LabelsSelector.md)
 - [RolloutAutoMsgRolloutActionWatchHelper](../../../docs/RolloutAutoMsgRolloutActionWatchHelper.md)
 - [RolloutAutoMsgRolloutActionWatchHelperWatchEvent](../../../docs/RolloutAutoMsgRolloutActionWatchHelperWatchEvent.md)
 - [RolloutAutoMsgRolloutWatchHelper](../../../docs/RolloutAutoMsgRolloutWatchHelper.md)
 - [RolloutAutoMsgRolloutWatchHelperWatchEvent](../../../docs/RolloutAutoMsgRolloutWatchHelperWatchEvent.md)
 - [RolloutRollout](../../../docs/RolloutRollout.md)
 - [RolloutRolloutAction](../../../docs/RolloutRolloutAction.md)
 - [RolloutRolloutActionList](../../../docs/RolloutRolloutActionList.md)
 - [RolloutRolloutActionStatus](../../../docs/RolloutRolloutActionStatus.md)
 - [RolloutRolloutList](../../../docs/RolloutRolloutList.md)
 - [RolloutRolloutPhase](../../../docs/RolloutRolloutPhase.md)
 - [RolloutRolloutSpec](../../../docs/RolloutRolloutSpec.md)
 - [RolloutRolloutStatus](../../../docs/RolloutRolloutStatus.md)


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
