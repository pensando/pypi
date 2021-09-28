# psm.FwlogV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_fw_log_file_content**](FwlogV1Api.md#get_download_fw_log_file_content) | **GET** /fwlog/v1/tenants/{O.Tenant}/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
[**get_download_fw_log_file_content1**](FwlogV1Api.md#get_download_fw_log_file_content1) | **GET** /fwlog/v1/objects/{O.Name} | fwlog/v1/tenants/default/objects/&lt;objectName&gt;
[**get_get_logs1**](FwlogV1Api.md#get_get_logs1) | **GET** /fwlog/v1/query | Queries firewall logs
[**get_watch_logs**](FwlogV1Api.md#get_watch_logs) | **GET** /fwlog/v1/watch/query | 
[**post_get_logs**](FwlogV1Api.md#post_get_logs) | **POST** /fwlog/v1/query | Queries firewall logs


# **get_download_fw_log_file_content**
> FwlogFwLogList get_download_fw_log_file_content(o_tenant, o_name)

fwlog/v1/tenants/default/objects/<objectName>

### Example

```python
import time
import psm
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content(o_tenant, o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

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

```python
import time
import psm
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    o_name = "O.Name_example" # str | 
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # fwlog/v1/tenants/default/objects/<objectName>
        api_response = api_instance.get_download_fw_log_file_content1(o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_download_fw_log_file_content1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

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

```python
import time
import psm
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    source_ips = [
        "source-ips_example",
    ] # [str] | OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    destination_ips = [
        "destination-ips_example",
    ] # [str] | OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    source_ports = [
        1,
    ] # [int] | OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535. (optional)
    destination_ports = [
        1,
    ] # [int] | OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535. (optional)
    protocols = [
        "protocols_example",
    ] # [str] | OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present. (optional)
    actions = [
        "actions_example",
    ] # [str] | OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present. (optional)
    reporter_ids = [
        "reporter-ids_example",
    ] # [str] | OR of reporter names to be matched. Only one reporter ID can be specified. (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. (optional)
    sort_order = "sort-order_example" # str | SortOrder specifies time ordering of results. (optional)
    max_results = 1 # int | MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. (optional)
    tenants = [
        "tenants_example",
    ] # [str] | OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only. (optional)
    scroll_id = "scroll-id_example" # str | ScrollID to scroll through results fetched by an earlier query. (optional)
    scroll_expiry = "scroll-expiry_example" # str | ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \"300ms\" or \"2h45m\". Valid time units are \"ns\", \"us\" (or \"µs\"), \"ms\", \"s\", \"m\", \"h\". Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration. (optional)
    batch_size = 1 # int | BatchSize is the number of results returned in one batch while scrolling. (optional)
    scroll_action = "scroll-action_example" # str | ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted. (optional)
    count_only = True # bool | if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta. (optional)
    encryption_status = "encryption-status_example" # str | if set, search logs that match the specified encryption status. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Queries firewall logs
        api_response = api_instance.get_get_logs1(source_ips=source_ips, destination_ips=destination_ips, source_ports=source_ports, destination_ports=destination_ports, protocols=protocols, actions=actions, reporter_ids=reporter_ids, start_time=start_time, end_time=end_time, sort_order=sort_order, max_results=max_results, tenants=tenants, scroll_id=scroll_id, scroll_expiry=scroll_expiry, batch_size=batch_size, scroll_action=scroll_action, count_only=count_only, encryption_status=encryption_status)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_get_logs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_ips** | **[str]**| OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **destination_ips** | **[str]**| OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **source_ports** | **[int]**| OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535. | [optional]
 **destination_ports** | **[int]**| OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535. | [optional]
 **protocols** | **[str]**| OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present. | [optional]
 **actions** | **[str]**| OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present. | [optional]
 **reporter_ids** | **[str]**| OR of reporter names to be matched. Only one reporter ID can be specified. | [optional]
 **start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **end_time** | **datetime**| EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional]
 **sort_order** | **str**| SortOrder specifies time ordering of results. | [optional]
 **max_results** | **int**| MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]
 **tenants** | **[str]**| OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only. | [optional]
 **scroll_id** | **str**| ScrollID to scroll through results fetched by an earlier query. | [optional]
 **scroll_expiry** | **str**| ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration. | [optional]
 **batch_size** | **int**| BatchSize is the number of results returned in one batch while scrolling. | [optional]
 **scroll_action** | **str**| ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted. | [optional]
 **count_only** | **bool**| if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta. | [optional]
 **encryption_status** | **str**| if set, search logs that match the specified encryption status. | [optional]

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

```python
import time
import psm
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fwlog_v1_api.FwlogV1Api(api_client)
    source_ips = [
        "source-ips_example",
    ] # [str] | OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    destination_ips = [
        "destination-ips_example",
    ] # [str] | OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address. (optional)
    source_ports = [
        1,
    ] # [int] | OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535. (optional)
    destination_ports = [
        1,
    ] # [int] | OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535. (optional)
    protocols = [
        "protocols_example",
    ] # [str] | OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present. (optional)
    actions = [
        "actions_example",
    ] # [str] | OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present. (optional)
    reporter_ids = [
        "reporter-ids_example",
    ] # [str] | OR of reporter names to be matched. Only one reporter ID can be specified. (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. (optional)
    sort_order = "sort-order_example" # str | SortOrder specifies time ordering of results. (optional)
    max_results = 1 # int | MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. (optional)
    tenants = [
        "tenants_example",
    ] # [str] | OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only. (optional)
    scroll_id = "scroll-id_example" # str | ScrollID to scroll through results fetched by an earlier query. (optional)
    scroll_expiry = "scroll-expiry_example" # str | ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \"300ms\" or \"2h45m\". Valid time units are \"ns\", \"us\" (or \"µs\"), \"ms\", \"s\", \"m\", \"h\". Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration. (optional)
    batch_size = 1 # int | BatchSize is the number of results returned in one batch while scrolling. (optional)
    scroll_action = "scroll-action_example" # str | ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted. (optional)
    count_only = True # bool | if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta. (optional)
    encryption_status = "encryption-status_example" # str | if set, search logs that match the specified encryption status. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_watch_logs(source_ips=source_ips, destination_ips=destination_ips, source_ports=source_ports, destination_ports=destination_ports, protocols=protocols, actions=actions, reporter_ids=reporter_ids, start_time=start_time, end_time=end_time, sort_order=sort_order, max_results=max_results, tenants=tenants, scroll_id=scroll_id, scroll_expiry=scroll_expiry, batch_size=batch_size, scroll_action=scroll_action, count_only=count_only, encryption_status=encryption_status)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling FwlogV1Api->get_watch_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_ips** | **[str]**| OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **destination_ips** | **[str]**| OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address. | [optional]
 **source_ports** | **[int]**| OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535. | [optional]
 **destination_ports** | **[int]**| OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535. | [optional]
 **protocols** | **[str]**| OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present. | [optional]
 **actions** | **[str]**| OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present. | [optional]
 **reporter_ids** | **[str]**| OR of reporter names to be matched. Only one reporter ID can be specified. | [optional]
 **start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **end_time** | **datetime**| EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional]
 **sort_order** | **str**| SortOrder specifies time ordering of results. | [optional]
 **max_results** | **int**| MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]
 **tenants** | **[str]**| OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only. | [optional]
 **scroll_id** | **str**| ScrollID to scroll through results fetched by an earlier query. | [optional]
 **scroll_expiry** | **str**| ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration. | [optional]
 **batch_size** | **int**| BatchSize is the number of results returned in one batch while scrolling. | [optional]
 **scroll_action** | **str**| ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted. | [optional]
 **count_only** | **bool**| if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta. | [optional]
 **encryption_status** | **str**| if set, search logs that match the specified encryption status. | [optional]

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

```python
import time
import psm
from api import fwlog_v1_api
from pensando_ent.psm.model.fwlog_fw_log_query import FwlogFwLogQuery
from pensando_ent.psm.model.fwlog_fw_log_list import FwlogFwLogList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
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
    ) # FwlogFwLogQuery | 

    # example passing only required values which don't have defaults set
    try:
        # Queries firewall logs
        api_response = api_instance.post_get_logs(body)
        pprint(api_response)
    except psm.ApiException as e:
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

