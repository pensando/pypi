```python

import time
import psm
from pprint import pprint
from api import orchestration_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_auto_msg_orchestrator_watch_helper import OrchestrationAutoMsgOrchestratorWatchHelper
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pensando_ent.psm.model.orchestration_orchestrator_list import OrchestrationOrchestratorList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    body = OrchestrationOrchestrator(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=OrchestrationOrchestratorSpec(
            credentials=MonitoringExternalCred(
                auth_type="none",
                bearer_token="bearer_token_example",
                ca_data="ca_data_example",
                cert_data="cert_data_example",
                disable_server_authentication=True,
                key_data="key_data_example",
                password="password_example",
                username="username_example",
            ),
            namespaces=[
                OrchestrationNamespaceSpec(
                    managed_spec=OrchestrationManagedNamespaceSpec(
                        discovery_operation="disc-op-default",
                        discovery_protocol="disc-proto-default",
                        mtu=0,
                        multicast_filter="mcast-filter-default",
                        override_vlan_end=4087,
                        override_vlan_start=3832,
                    ),
                    mode="managed",
                    monitored_spec={},
                    name="name_example",
                ),
            ],
            type="vcenter",
            uri="uri_example",
        ),
        status=OrchestrationOrchestratorStatus(
            connection_status="unknown",
            discovered_namespaces=[
                "discovered_namespaces_example",
            ],
            incompatible_dscs=[
                "incompatible_dscs_example",
            ],
            last_transition_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            message="message_example",
            orch_id=1,
        ),
    ) # OrchestrationOrchestrator | 

    try:
        # Create Orchestrator object
        api_response = api_instance.add_orchestrator(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->add_orchestrator: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrchestrationV1Api* | [**add_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#add_orchestrator) | **POST** /configs/orchestration/v1/orchestrator | Create Orchestrator object
*OrchestrationV1Api* | [**delete_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#delete_orchestrator) | **DELETE** /configs/orchestration/v1/orchestrator/{O.Name} | Delete Orchestrator object
*OrchestrationV1Api* | [**get_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#get_orchestrator) | **GET** /configs/orchestration/v1/orchestrator/{O.Name} | Get Orchestrator object
*OrchestrationV1Api* | [**label_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#label_orchestrator) | **POST** /configs/orchestration/v1/orchestrator/{O.Name}/label | Label Orchestrator object
*OrchestrationV1Api* | [**list_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#list_orchestrator) | **GET** /configs/orchestration/v1/orchestrator | List Orchestrator objects
*OrchestrationV1Api* | [**update_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#update_orchestrator) | **PUT** /configs/orchestration/v1/orchestrator/{O.Name} | Update Orchestrator object
*OrchestrationV1Api* | [**watch_orchestrator**](pensando_ent/docs/OrchestrationV1Api.md#watch_orchestrator) | **GET** /configs/orchestration/v1/watch/orchestrator | Watch Orchestrator objects. Supports WebSockets or HTTP long poll


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
