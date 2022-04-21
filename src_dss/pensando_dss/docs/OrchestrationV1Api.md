# psm.OrchestrationV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_orchestrator**](OrchestrationV1Api.md#add_orchestrator) | **POST** /configs/orchestration/v1/orchestrator | Create Orchestrator object
[**delete_orchestrator**](OrchestrationV1Api.md#delete_orchestrator) | **DELETE** /configs/orchestration/v1/orchestrator/{O.Name} | Delete Orchestrator object
[**get_orchestrator**](OrchestrationV1Api.md#get_orchestrator) | **GET** /configs/orchestration/v1/orchestrator/{O.Name} | Get Orchestrator object
[**label_orchestrator**](OrchestrationV1Api.md#label_orchestrator) | **POST** /configs/orchestration/v1/orchestrator/{O.Name}/label | Label Orchestrator object
[**list_orchestrator**](OrchestrationV1Api.md#list_orchestrator) | **GET** /configs/orchestration/v1/orchestrator | List Orchestrator objects
[**update_orchestrator**](OrchestrationV1Api.md#update_orchestrator) | **PUT** /configs/orchestration/v1/orchestrator/{O.Name} | Update Orchestrator object
[**watch_orchestrator**](OrchestrationV1Api.md#watch_orchestrator) | **GET** /configs/orchestration/v1/watch/orchestrator | Watch Orchestrator objects. Supports WebSockets or HTTP long poll


# **add_orchestrator**
> OrchestrationOrchestrator add_orchestrator(body)

Create Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
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

    # example passing only required values which don't have defaults set
    try:
        # Create Orchestrator object
        api_response = api_instance.add_orchestrator(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->add_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **delete_orchestrator**
> OrchestrationOrchestrator delete_orchestrator(o_name)

Delete Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Orchestrator object
        api_response = api_instance.delete_orchestrator(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->delete_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **get_orchestrator**
> OrchestrationOrchestrator get_orchestrator(o_name)

Get Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    status_connection_status = "status.connection-status_example" # str |  (optional)
    status_last_transition_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    status_discovered_namespaces = [
        "status.discovered-namespaces_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Orchestrator object
        api_response = api_instance.get_orchestrator(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->get_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **status_connection_status** | **str**|  | [optional]
 **status_last_transition_time** | **datetime**|  | [optional]
 **status_discovered_namespaces** | **[str]**|  | [optional]

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **label_orchestrator**
> OrchestrationOrchestrator label_orchestrator(o_name, body)

Label Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pensando_dss.psm.model.api_label import ApiLabel
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Orchestrator object
        api_response = api_instance.label_orchestrator(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->label_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **list_orchestrator**
> OrchestrationOrchestratorList list_orchestrator()

List Orchestrator objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator_list import OrchestrationOrchestratorList
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Orchestrator objects
        api_response = api_instance.list_orchestrator()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->list_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**OrchestrationOrchestratorList**](OrchestrationOrchestratorList.md)

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

# **update_orchestrator**
> OrchestrationOrchestrator update_orchestrator(o_name, body)

Update Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 
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

    # example passing only required values which don't have defaults set
    try:
        # Update Orchestrator object
        api_response = api_instance.update_orchestrator(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->update_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **watch_orchestrator**
> OrchestrationAutoMsgOrchestratorWatchHelper watch_orchestrator()

Watch Orchestrator objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import orchestration_v1_api
from pensando_dss.psm.models.orchestration import *
from pensando_dss.psm.model.orchestration_auto_msg_orchestrator_watch_helper import OrchestrationAutoMsgOrchestratorWatchHelper
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
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Orchestrator objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_orchestrator()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->watch_orchestrator: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**OrchestrationAutoMsgOrchestratorWatchHelper**](OrchestrationAutoMsgOrchestratorWatchHelper.md)

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

