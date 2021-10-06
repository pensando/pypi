
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrchestrationV1Api* | [**add_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#add_orchestrator) | **POST** /configs/orchestration/v1/orchestrator | Create Orchestrator object
*OrchestrationV1Api* | [**delete_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#delete_orchestrator) | **DELETE** /configs/orchestration/v1/orchestrator/{O.Name} | Delete Orchestrator object
*OrchestrationV1Api* | [**get_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#get_orchestrator) | **GET** /configs/orchestration/v1/orchestrator/{O.Name} | Get Orchestrator object
*OrchestrationV1Api* | [**label_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#label_orchestrator) | **POST** /configs/orchestration/v1/orchestrator/{O.Name}/label | Label Orchestrator object
*OrchestrationV1Api* | [**list_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#list_orchestrator) | **GET** /configs/orchestration/v1/orchestrator | List Orchestrator objects
*OrchestrationV1Api* | [**update_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#update_orchestrator) | **PUT** /configs/orchestration/v1/orchestrator/{O.Name} | Update Orchestrator object
*OrchestrationV1Api* | [**watch_orchestrator**](../../../../pensando_ent/docs/OrchestrationV1Api.md#watch_orchestrator) | **GET** /configs/orchestration/v1/watch/orchestrator | Watch Orchestrator objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
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
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [MonitoringExternalCred](docs/MonitoringExternalCred.md)
 - [OrchestrationAutoMsgOrchestratorWatchHelper](docs/OrchestrationAutoMsgOrchestratorWatchHelper.md)
 - [OrchestrationAutoMsgOrchestratorWatchHelperWatchEvent](docs/OrchestrationAutoMsgOrchestratorWatchHelperWatchEvent.md)
 - [OrchestrationManagedNamespaceSpec](docs/OrchestrationManagedNamespaceSpec.md)
 - [OrchestrationNamespaceSpec](docs/OrchestrationNamespaceSpec.md)
 - [OrchestrationOrchestrator](docs/OrchestrationOrchestrator.md)
 - [OrchestrationOrchestratorList](docs/OrchestrationOrchestratorList.md)
 - [OrchestrationOrchestratorSpec](docs/OrchestrationOrchestratorSpec.md)
 - [OrchestrationOrchestratorStatus](docs/OrchestrationOrchestratorStatus.md)


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
