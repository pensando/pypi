# psm.RolloutV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rollout**](RolloutV1Api.md#create_rollout) | **POST** /configs/rollout/v1/rollout/CreateRollout | Start Rollout operation
[**get_rollout**](RolloutV1Api.md#get_rollout) | **GET** /configs/rollout/v1/rollout/{O.Name} | Get Rollout object
[**list_rollout**](RolloutV1Api.md#list_rollout) | **GET** /configs/rollout/v1/rollout | List Rollout objects
[**remove_rollout**](RolloutV1Api.md#remove_rollout) | **POST** /configs/rollout/v1/rollout/RemoveRollout | Remove a Rollout
[**stop_rollout**](RolloutV1Api.md#stop_rollout) | **POST** /configs/rollout/v1/rollout/StopRollout | Stop a Rollout operation
[**update_rollout**](RolloutV1Api.md#update_rollout) | **POST** /configs/rollout/v1/rollout/UpdateRollout | Update Rollout configuration
[**watch_rollout**](RolloutV1Api.md#watch_rollout) | **GET** /configs/rollout/v1/watch/rollout | Watch Rollout objects. Supports WebSockets or HTTP long poll


# **create_rollout**
> RolloutRollout create_rollout(body)

Start Rollout operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout import RolloutRollout
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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

    # example passing only required values which don't have defaults set
    try:
        # Start Rollout operation
        api_response = api_instance.create_rollout(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->create_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollout**
> RolloutRollout get_rollout(o_name)

Get Rollout object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout import RolloutRollout
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_strategy = "spec.strategy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Rollout object
        api_response = api_instance.get_rollout(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->get_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_strategy** | **str**|  | [optional]

### Return type

[**RolloutRollout**](RolloutRollout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rollout**
> RolloutRolloutList list_rollout()

List Rollout objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout_list import RolloutRolloutList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Rollout objects
        api_response = api_instance.list_rollout()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->list_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**RolloutRolloutList**](RolloutRolloutList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rollout**
> RolloutRollout remove_rollout(body)

Remove a Rollout

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout import RolloutRollout
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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

    # example passing only required values which don't have defaults set
    try:
        # Remove a Rollout
        api_response = api_instance.remove_rollout(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->remove_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_rollout**
> RolloutRollout stop_rollout(body)

Stop a Rollout operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout import RolloutRollout
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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

    # example passing only required values which don't have defaults set
    try:
        # Stop a Rollout operation
        api_response = api_instance.stop_rollout(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->stop_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rollout**
> RolloutRollout update_rollout(body)

Update Rollout configuration

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_rollout import RolloutRollout
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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

    # example passing only required values which don't have defaults set
    try:
        # Update Rollout configuration
        api_response = api_instance.update_rollout(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->update_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_rollout**
> RolloutAutoMsgRolloutWatchHelper watch_rollout()

Watch Rollout objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import rollout_v1_api
from pensando_dss.psm.models.rollout import *
from pensando_dss.psm.model.rollout_auto_msg_rollout_watch_helper import RolloutAutoMsgRolloutWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Rollout objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_rollout()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RolloutV1Api->watch_rollout: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**RolloutAutoMsgRolloutWatchHelper**](RolloutAutoMsgRolloutWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

