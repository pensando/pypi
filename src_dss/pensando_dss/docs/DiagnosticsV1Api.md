# psm.DiagnosticsV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug**](DiagnosticsV1Api.md#debug) | **POST** /configs/diagnostics/v1/modules/{O.Name}/Debug | Request Diagnostics information for a module
[**get_module**](DiagnosticsV1Api.md#get_module) | **GET** /configs/diagnostics/v1/modules/{O.Name} | Get Module object
[**label_module**](DiagnosticsV1Api.md#label_module) | **POST** /configs/diagnostics/v1/modules/{O.Name}/label | Label Module object
[**list_module**](DiagnosticsV1Api.md#list_module) | **GET** /configs/diagnostics/v1/modules | List Module objects
[**update_module**](DiagnosticsV1Api.md#update_module) | **PUT** /configs/diagnostics/v1/modules/{O.Name} | Update Module object
[**watch_module**](DiagnosticsV1Api.md#watch_module) | **GET** /configs/diagnostics/v1/watch/modules | Watch Module objects. Supports WebSockets or HTTP long poll


# **debug**
> DiagnosticsDiagnosticsResponse debug(o_name, body)

Request Diagnostics information for a module

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_diagnostics_response import DiagnosticsDiagnosticsResponse
from pensando_dss.psm.model.diagnostics_diagnostics_request import DiagnosticsDiagnosticsRequest
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = DiagnosticsDiagnosticsRequest(
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
        parameters={
            "key": "key_example",
        },
        query="query_example",
        service_port=DiagnosticsServicePort(
            name="name_example",
            port=1,
        ),
    ) # DiagnosticsDiagnosticsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Request Diagnostics information for a module
        api_response = api_instance.debug(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->debug: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**DiagnosticsDiagnosticsRequest**](DiagnosticsDiagnosticsRequest.md)|  |

### Return type

[**DiagnosticsDiagnosticsResponse**](DiagnosticsDiagnosticsResponse.md)

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

# **get_module**
> DiagnosticsModule get_module(o_name)

Get Module object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_module import DiagnosticsModule
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_args = [
        "spec.args_example",
    ] # [str] | Args are command line arguments passed to the module. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Module object
        api_response = api_instance.get_module(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->get_module: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_args** | **[str]**| Args are command line arguments passed to the module. | [optional]

### Return type

[**DiagnosticsModule**](DiagnosticsModule.md)

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

# **label_module**
> DiagnosticsModule label_module(o_name, body)

Label Module object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_module import DiagnosticsModule
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        # Label Module object
        api_response = api_instance.label_module(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->label_module: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**DiagnosticsModule**](DiagnosticsModule.md)

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

# **list_module**
> DiagnosticsModuleList list_module()

List Module objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_module_list import DiagnosticsModuleList
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Module objects
        api_response = api_instance.list_module()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->list_module: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**DiagnosticsModuleList**](DiagnosticsModuleList.md)

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

# **update_module**
> DiagnosticsModule update_module(o_name, body)

Update Module object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_module import DiagnosticsModule
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = DiagnosticsModule(
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
        spec=DiagnosticsModuleSpec(
            args=[
                "args_example",
            ],
            enable_trace=True,
            log_level="info",
        ),
        status=DiagnosticsModuleStatus(
            category="venice",
            last_restart_reason="last_restart_reason_example",
            last_start=dateutil_parser('1970-01-01T00:00:00.00Z'),
            mac_address="mac_address_example",
            module="module_example",
            node="node_example",
            restart_count=1,
            service="service_example",
            service_ports=[
                DiagnosticsServicePort(
                    name="name_example",
                    port=1,
                ),
            ],
        ),
    ) # DiagnosticsModule | 

    # example passing only required values which don't have defaults set
    try:
        # Update Module object
        api_response = api_instance.update_module(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->update_module: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**DiagnosticsModule**](DiagnosticsModule.md)|  |

### Return type

[**DiagnosticsModule**](DiagnosticsModule.md)

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

# **watch_module**
> DiagnosticsAutoMsgModuleWatchHelper watch_module()

Watch Module objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import diagnostics_v1_api
from pensando_dss.psm.models.diagnostics import *
from pensando_dss.psm.model.diagnostics_auto_msg_module_watch_helper import DiagnosticsAutoMsgModuleWatchHelper
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
    api_instance = diagnostics_v1_api.DiagnosticsV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Module objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_module()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling DiagnosticsV1Api->watch_module: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**DiagnosticsAutoMsgModuleWatchHelper**](DiagnosticsAutoMsgModuleWatchHelper.md)

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

