# orchestration

This page provides working code examples for the **orchestration** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrchestrationV1Api* | [**add_orchestrator**](../../../docs/OrchestrationV1Api.md#add_orchestrator) | **POST** /configs/orchestration/v1/orchestrator | Create Orchestrator object
*OrchestrationV1Api* | [**delete_orchestrator**](../../../docs/OrchestrationV1Api.md#delete_orchestrator) | **DELETE** /configs/orchestration/v1/orchestrator/{O.Name} | Delete Orchestrator object
*OrchestrationV1Api* | [**get_orchestrator**](../../../docs/OrchestrationV1Api.md#get_orchestrator) | **GET** /configs/orchestration/v1/orchestrator/{O.Name} | Get Orchestrator object
*OrchestrationV1Api* | [**label_orchestrator**](../../../docs/OrchestrationV1Api.md#label_orchestrator) | **POST** /configs/orchestration/v1/orchestrator/{O.Name}/label | Label Orchestrator object
*OrchestrationV1Api* | [**list_orchestrator**](../../../docs/OrchestrationV1Api.md#list_orchestrator) | **GET** /configs/orchestration/v1/orchestrator | List Orchestrator objects
*OrchestrationV1Api* | [**update_orchestrator**](../../../docs/OrchestrationV1Api.md#update_orchestrator) | **PUT** /configs/orchestration/v1/orchestrator/{O.Name} | Update Orchestrator object
*OrchestrationV1Api* | [**watch_orchestrator**](../../../docs/OrchestrationV1Api.md#watch_orchestrator) | **GET** /configs/orchestration/v1/watch/orchestrator | Watch Orchestrator objects. Supports WebSockets or HTTP long poll


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
 - [MonitoringExternalCred](../../../docs/MonitoringExternalCred.md)
 - [OrchestrationAutoMsgOrchestratorWatchHelper](../../../docs/OrchestrationAutoMsgOrchestratorWatchHelper.md)
 - [OrchestrationAutoMsgOrchestratorWatchHelperWatchEvent](../../../docs/OrchestrationAutoMsgOrchestratorWatchHelperWatchEvent.md)
 - [OrchestrationManagedNamespaceSpec](../../../docs/OrchestrationManagedNamespaceSpec.md)
 - [OrchestrationNamespaceSpec](../../../docs/OrchestrationNamespaceSpec.md)
 - [OrchestrationOrchestrator](../../../docs/OrchestrationOrchestrator.md)
 - [OrchestrationOrchestratorList](../../../docs/OrchestrationOrchestratorList.md)
 - [OrchestrationOrchestratorSpec](../../../docs/OrchestrationOrchestratorSpec.md)
 - [OrchestrationOrchestratorStatus](../../../docs/OrchestrationOrchestratorStatus.md)


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
