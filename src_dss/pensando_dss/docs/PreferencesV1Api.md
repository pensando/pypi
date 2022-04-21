# psm.PreferencesV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ui_global_settings**](PreferencesV1Api.md#get_ui_global_settings) | **GET** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Get UIGlobalSettings object
[**get_ui_global_settings1**](PreferencesV1Api.md#get_ui_global_settings1) | **GET** /configs/preferences/v1/uiglobalsettings | Get UIGlobalSettings object
[**label_ui_global_settings**](PreferencesV1Api.md#label_ui_global_settings) | **POST** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings/label | Label UIGlobalSettings object
[**label_ui_global_settings1**](PreferencesV1Api.md#label_ui_global_settings1) | **POST** /configs/preferences/v1/uiglobalsettings/label | Label UIGlobalSettings object
[**update_ui_global_settings**](PreferencesV1Api.md#update_ui_global_settings) | **PUT** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Update UIGlobalSettings object
[**update_ui_global_settings1**](PreferencesV1Api.md#update_ui_global_settings1) | **PUT** /configs/preferences/v1/uiglobalsettings | Update UIGlobalSettings object
[**watch_ui_global_settings**](PreferencesV1Api.md#watch_ui_global_settings) | **GET** /configs/preferences/v1/watch/tenant/{O.Tenant}/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll
[**watch_ui_global_settings1**](PreferencesV1Api.md#watch_ui_global_settings1) | **GET** /configs/preferences/v1/watch/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll


# **get_ui_global_settings**
> PreferencesUIGlobalSettings get_ui_global_settings(o_tenant)

Get UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UIGlobalSettings object
        api_response = api_instance.get_ui_global_settings(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->get_ui_global_settings: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **get_ui_global_settings1**
> PreferencesUIGlobalSettings get_ui_global_settings1()

Get UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UIGlobalSettings object
        api_response = api_instance.get_ui_global_settings1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->get_ui_global_settings1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **label_ui_global_settings**
> PreferencesUIGlobalSettings label_ui_global_settings(o_tenant, body)

Label UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label UIGlobalSettings object
        api_response = api_instance.label_ui_global_settings(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->label_ui_global_settings: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **label_ui_global_settings1**
> PreferencesUIGlobalSettings label_ui_global_settings1(body)

Label UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
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
        # Label UIGlobalSettings object
        api_response = api_instance.label_ui_global_settings1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->label_ui_global_settings1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **update_ui_global_settings**
> PreferencesUIGlobalSettings update_ui_global_settings(o_tenant, body)

Update UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = PreferencesUIGlobalSettings(
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
        spec=PreferencesUIGlobalSettingsSpec(
            idle_timeout=PreferencesIdleTimeout(
                duration="60s",
                warning_time="60s",
            ),
            style_options="style_options_example",
        ),
        status={},
    ) # PreferencesUIGlobalSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Update UIGlobalSettings object
        api_response = api_instance.update_ui_global_settings(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->update_ui_global_settings: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)|  |

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **update_ui_global_settings1**
> PreferencesUIGlobalSettings update_ui_global_settings1(body)

Update UIGlobalSettings object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    body = PreferencesUIGlobalSettings(
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
        spec=PreferencesUIGlobalSettingsSpec(
            idle_timeout=PreferencesIdleTimeout(
                duration="60s",
                warning_time="60s",
            ),
            style_options="style_options_example",
        ),
        status={},
    ) # PreferencesUIGlobalSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Update UIGlobalSettings object
        api_response = api_instance.update_ui_global_settings1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->update_ui_global_settings1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)|  |

### Return type

[**PreferencesUIGlobalSettings**](PreferencesUIGlobalSettings.md)

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

# **watch_ui_global_settings**
> PreferencesAutoMsgUIGlobalSettingsWatchHelper watch_ui_global_settings(o_tenant)

Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.preferences_auto_msg_ui_global_settings_watch_helper import PreferencesAutoMsgUIGlobalSettingsWatchHelper
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ui_global_settings(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->watch_ui_global_settings: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**PreferencesAutoMsgUIGlobalSettingsWatchHelper**](PreferencesAutoMsgUIGlobalSettingsWatchHelper.md)

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

# **watch_ui_global_settings1**
> PreferencesAutoMsgUIGlobalSettingsWatchHelper watch_ui_global_settings1()

Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import preferences_v1_api
from pensando_dss.psm.models.preferences import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.preferences_auto_msg_ui_global_settings_watch_helper import PreferencesAutoMsgUIGlobalSettingsWatchHelper
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
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ui_global_settings1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->watch_ui_global_settings1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**PreferencesAutoMsgUIGlobalSettingsWatchHelper**](PreferencesAutoMsgUIGlobalSettingsWatchHelper.md)

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

