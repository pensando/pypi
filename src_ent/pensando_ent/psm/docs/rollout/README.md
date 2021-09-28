```python

import time
import psm
from pprint import pprint
from api import rollout_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.rollout_auto_msg_rollout_watch_helper import RolloutAutoMsgRolloutWatchHelper
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.rollout_rollout_list import RolloutRolloutList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
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
        spec=RolloutRolloutSpec(
            dsc_must_match_constraint=True,
            dscs_only=True,
            max_nic_failures_before_abort=1,
            max_parallel=2,
            order_constraints=[
                LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
            ],
            retry=True,
            scheduled_end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            scheduled_start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            strategy="linear",
            suspend=True,
            upgrade_type="graceful",
            version="version_example",
        ),
        status=RolloutRolloutStatus(
            completion_percent=1,
            controller_nodes_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            controller_services_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            dscs_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            prev_version="prev_version_example",
            reason="reason_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            state="progressing",
        ),
    ) # RolloutRollout | 

    try:
        # Start Rollout operation
        api_response = api_instance.create_rollout(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling RolloutV1Api->create_rollout: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RolloutV1Api* | [**create_rollout**](docs/RolloutV1Api.md#create_rollout) | **POST** /configs/rollout/v1/rollout/CreateRollout | Start Rollout operation
*RolloutV1Api* | [**get_rollout**](docs/RolloutV1Api.md#get_rollout) | **GET** /configs/rollout/v1/rollout/{O.Name} | Get Rollout object
*RolloutV1Api* | [**list_rollout**](docs/RolloutV1Api.md#list_rollout) | **GET** /configs/rollout/v1/rollout | List Rollout objects
*RolloutV1Api* | [**remove_rollout**](docs/RolloutV1Api.md#remove_rollout) | **POST** /configs/rollout/v1/rollout/RemoveRollout | Remove a Rollout
*RolloutV1Api* | [**stop_rollout**](docs/RolloutV1Api.md#stop_rollout) | **POST** /configs/rollout/v1/rollout/StopRollout | Stop a Rollout operation
*RolloutV1Api* | [**update_rollout**](docs/RolloutV1Api.md#update_rollout) | **POST** /configs/rollout/v1/rollout/UpdateRollout | Update Rollout configuration
*RolloutV1Api* | [**watch_rollout**](docs/RolloutV1Api.md#watch_rollout) | **GET** /configs/rollout/v1/watch/rollout | Watch Rollout objects. Supports WebSockets or HTTP long poll


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
 - [LabelsRequirement](docs/LabelsRequirement.md)
 - [LabelsSelector](docs/LabelsSelector.md)
 - [RolloutAutoMsgRolloutActionWatchHelper](docs/RolloutAutoMsgRolloutActionWatchHelper.md)
 - [RolloutAutoMsgRolloutActionWatchHelperWatchEvent](docs/RolloutAutoMsgRolloutActionWatchHelperWatchEvent.md)
 - [RolloutAutoMsgRolloutWatchHelper](docs/RolloutAutoMsgRolloutWatchHelper.md)
 - [RolloutAutoMsgRolloutWatchHelperWatchEvent](docs/RolloutAutoMsgRolloutWatchHelperWatchEvent.md)
 - [RolloutRollout](docs/RolloutRollout.md)
 - [RolloutRolloutAction](docs/RolloutRolloutAction.md)
 - [RolloutRolloutActionList](docs/RolloutRolloutActionList.md)
 - [RolloutRolloutActionStatus](docs/RolloutRolloutActionStatus.md)
 - [RolloutRolloutList](docs/RolloutRolloutList.md)
 - [RolloutRolloutPhase](docs/RolloutRolloutPhase.md)
 - [RolloutRolloutSpec](docs/RolloutRolloutSpec.md)
 - [RolloutRolloutStatus](docs/RolloutRolloutStatus.md)


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
