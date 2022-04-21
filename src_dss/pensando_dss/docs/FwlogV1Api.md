# psm.FwlogV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_fw_log_file_content**](FwlogV1Api.md#get_download_fw_log_file_content) | **GET** /fwlog/v1/tenants/{O.Tenant}/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
[**get_download_fw_log_file_content1**](FwlogV1Api.md#get_download_fw_log_file_content1) | **GET** /fwlog/v1/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
[**get_get_logs1**](FwlogV1Api.md#get_get_logs1) | **GET** /fwlog/v1/query | Queries firewall logs
[**get_watch_logs**](FwlogV1Api.md#get_watch_logs) | **GET** /fwlog/v1/watch/query | 
[**post_get_logs**](FwlogV1Api.md#post_get_logs) | **POST** /fwlog/v1/query | Queries firewall logs


# **get_download_fw_log_file_content**
> FwlogFwLogList get_download_fw_log_file_content(o_tenant)

fwlog/v1/tenants/default/objects/<objectName>

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import fwlog_v1_api
from pensando_dss.psm.models.fwlog import *
from pensando_dss.psm.model.fwlog_fw_log_list import FwlogFwLogList
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
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**FwlogFwLogList**](FwlogFwLogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_fw_log_file_content1**
> FwlogFwLogList get_download_fw_log_file_content1(o_name)

fwlog/v1/tenants/default/objects/<objectName>

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import fwlog_v1_api
from pensando_dss.psm.models.fwlog import *
from pensando_dss.psm.model.fwlog_fw_log_list import FwlogFwLogList
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
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    o_name = "O.Name_example" # str | 
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**FwlogFwLogList**](FwlogFwLogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_logs1**
> FwlogFwLogList get_get_logs1()

Queries firewall logs

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import fwlog_v1_api
from pensando_dss.psm.models.fwlog import *
from pensando_dss.psm.model.fwlog_fw_log_list import FwlogFwLogList
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
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    source_ips = [
        "source-ips_example",
    ] # [str] | OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    sort_order = "sort-order_example" # str | SortOrder specifies time ordering of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Queries firewall logs
        api_response = api_instance.get_get_logs1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_get_logs1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_ips** | **[str]**| OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **sort_order** | **str**| SortOrder specifies time ordering of results. | [optional]

### Return type

[**FwlogFwLogList**](FwlogFwLogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watch_logs**
> FwlogFwLogList get_watch_logs()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import fwlog_v1_api
from pensando_dss.psm.models.fwlog import *
from pensando_dss.psm.model.fwlog_fw_log_list import FwlogFwLogList
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
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    source_ips = [
        "source-ips_example",
    ] # [str] | OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    sort_order = "sort-order_example" # str | SortOrder specifies time ordering of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_watch_logs()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_watch_logs: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_ips** | **[str]**| OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **sort_order** | **str**| SortOrder specifies time ordering of results. | [optional]

### Return type

[**FwlogFwLogList**](FwlogFwLogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_logs**
> FwlogFwLogList post_get_logs(body)

Queries firewall logs

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import fwlog_v1_api
from pensando_dss.psm.models.fwlog import *
from pensando_dss.psm.model.fwlog_fw_log_query import FwlogFwLogQuery
from pensando_dss.psm.model.fwlog_fw_log_list import FwlogFwLogList
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
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    body = FwlogFwLogQuery(
        actions=[
            "actions_example",
        ],
        batch_size=25,
        count_only=True,
        destination_ips=[
            "10.1.1.1, ff02::5 ",
        ],
        destination_ports=[
            1,
        ],
        encryption_status="all",
        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        max_results=50,
        protocols=[
            "protocols_example",
        ],
        reporter_ids=[
            "reporter_ids_example",
        ],
        scroll_action="none",
        scroll_expiry="60s",
        scroll_id="scroll_id_example",
        sort_order="descending",
        source_ips=[
            "10.1.1.1, ff02::5 ",
        ],
        source_ports=[
            1,
        ],
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        tenants=[
            "tenants_example",
        ],
        vpc_names=[
            "vpc_names_example",
        ],
    ) # FwlogFwLogQuery | 

    # example passing only required values which don't have defaults set
    try:
        # Queries firewall logs
        api_response = api_instance.post_get_logs(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling FwlogV1Api->post_get_logs: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FwlogFwLogQuery**](FwlogFwLogQuery.md)|  |

### Return type

[**FwlogFwLogList**](FwlogFwLogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

