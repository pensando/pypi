# psm_dss.SearchV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_policy_query1**](SearchV1Api.md#get_policy_query1) | **GET** /search/v1/policy-query | Security Policy Query
[**get_query1**](SearchV1Api.md#get_query1) | **GET** /search/v1/query | Structured or free-form search
[**post_policy_query**](SearchV1Api.md#post_policy_query) | **POST** /search/v1/policy-query | Security Policy Query
[**post_query**](SearchV1Api.md#post_query) | **POST** /search/v1/query | Structured or free-form search


# **get_policy_query1**
> SearchPolicySearchResponse get_policy_query1()

Security Policy Query

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import search_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.search import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.search_policy_search_response import SearchPolicySearchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_v1_api.SearchV1Api(api_client)
    tenant = "tenant_example" # str | Tenant Name, to perform query within a Tenant's scope. The default tenant is \"default\". In the backend this field gets auto-filled & validated by apigw-hook based on user login context. (optional)
    namespace = "namespace_example" # str | Namespace is optional. If provided policy-search will be limited to the specified namespace. (optional)
    app = "app_example" # str | App specification,  predefined apps and alg config. (optional)
    protocol = "protocol_example" # str | Protocol eg: tcp, udp, icmp. (optional)
    port = "port_example" # str | TCP or UDP Port number. (optional)
    from_ip_address = "from-ip-address_example" # str | Inbound ip-address, use any to refer to all ipaddresses eg: 10.1.1.1, any. (optional)
    to_ip_address = "to-ip-address_example" # str | Outbound ip-address, use any to refer to all ipaddresses eg: 20.1.1.1, any. (optional)
    from_security_group = "from-security-group_example" # str | Inbound security group. (optional)
    to_security_group = "to-security-group_example" # str | Outbound security group. (optional)
    kinds = [
        "kinds_example",
    ] # [str] | Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy or IPSecPolicy. (optional)
    name = "name_example" # str | Name is optional. If provided policy-search will be limited to the specified policy of the given name on the given kind. If empty, then all the policies of the given kind will be searched. (optional)
    action = "action_example" # str | Action, e.g. PERMIT, DENY or REJECT/CLEAR, PROTECT_PERMISSIVE or PROTECT_STRICT. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Security Policy Query
        api_response = api_instance.get_policy_query1(tenant=tenant, namespace=namespace, app=app, protocol=protocol, port=port, from_ip_address=from_ip_address, to_ip_address=to_ip_address, from_security_group=from_security_group, to_security_group=to_security_group, kinds=kinds, name=name, action=action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchV1Api->get_policy_query1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant Name, to perform query within a Tenant&#39;s scope. The default tenant is \&quot;default\&quot;. In the backend this field gets auto-filled &amp; validated by apigw-hook based on user login context. | [optional]
 **namespace** | **str**| Namespace is optional. If provided policy-search will be limited to the specified namespace. | [optional]
 **app** | **str**| App specification,  predefined apps and alg config. | [optional]
 **protocol** | **str**| Protocol eg: tcp, udp, icmp. | [optional]
 **port** | **str**| TCP or UDP Port number. | [optional]
 **from_ip_address** | **str**| Inbound ip-address, use any to refer to all ipaddresses eg: 10.1.1.1, any. | [optional]
 **to_ip_address** | **str**| Outbound ip-address, use any to refer to all ipaddresses eg: 20.1.1.1, any. | [optional]
 **from_security_group** | **str**| Inbound security group. | [optional]
 **to_security_group** | **str**| Outbound security group. | [optional]
 **kinds** | **[str]**| Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy or IPSecPolicy. | [optional]
 **name** | **str**| Name is optional. If provided policy-search will be limited to the specified policy of the given name on the given kind. If empty, then all the policies of the given kind will be searched. | [optional]
 **action** | **str**| Action, e.g. PERMIT, DENY or REJECT/CLEAR, PROTECT_PERMISSIVE or PROTECT_STRICT. | [optional]

### Return type

[**SearchPolicySearchResponse**](SearchPolicySearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm_dss.SearchV1Api top]](#psm_dss.SearchV1Api) [[Back to search README]](../psm_dss/docs/search/README.md) [[Back to pensando_dss README]](../README.md)

# **get_query1**
> SearchSearchResponse get_query1()

Structured or free-form search

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import search_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.search import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.search_search_response import SearchSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_v1_api.SearchV1Api(api_client)
    query_string = "query-string_example" # str | Simple query string This can be specified as URI parameter. For advanced query cases, Users should use specify SearchQuery and pass the SearchRequest in a GET/POST Body The max query-string length is 256 bytes. Length of string should be between 0 and 256. (optional)
    _from = 1 # int | From represents the start offset (zero based), used in paginated search requests The results returned would be in the range [From ... From+MaxResults-1] This can be specified as URI parameter. Default value is 0 and valid range is 0..8192. Value should be between 0 and 8192. (optional)
    max_results = 1 # int | MaxResults is the max-count of search results This can be specified as URI parameter. Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. (optional)
    sort_by = "sort-by_example" # str | SortyBy is an optional parameter and contains the field name to be sorted by, For eg: \"meta.name\" This can be specified as URI parameter. Length of string should be between 0 and 256. (optional)
    sort_order = "sort-order_example" # str | SortOrder is an optional parameter and contains whether to sort ascending or descending This can be specified as URI parameter. (optional)
    mode = "mode_example" # str | Query Mode. (optional)
    query_categories = [
        "query.categories_example",
    ] # [str] | OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64. (optional)
    query_kinds = [
        "query.kinds_example",
    ] # [str] | OR of Kinds to be matched, AND and Exclude are not supported for this type. Should be a valid object Kind. (optional)
    tenants = [
        "tenants_example",
    ] # [str] | OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. (optional)
    aggregate = True # bool | Indicates whether to perform aggregation on the search results or not. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Structured or free-form search
        api_response = api_instance.get_query1(query_string=query_string, _from=_from, max_results=max_results, sort_by=sort_by, sort_order=sort_order, mode=mode, query_categories=query_categories, query_kinds=query_kinds, tenants=tenants, aggregate=aggregate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchV1Api->get_query1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| Simple query string This can be specified as URI parameter. For advanced query cases, Users should use specify SearchQuery and pass the SearchRequest in a GET/POST Body The max query-string length is 256 bytes. Length of string should be between 0 and 256. | [optional]
 **_from** | **int**| From represents the start offset (zero based), used in paginated search requests The results returned would be in the range [From ... From+MaxResults-1] This can be specified as URI parameter. Default value is 0 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]
 **max_results** | **int**| MaxResults is the max-count of search results This can be specified as URI parameter. Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]
 **sort_by** | **str**| SortyBy is an optional parameter and contains the field name to be sorted by, For eg: \&quot;meta.name\&quot; This can be specified as URI parameter. Length of string should be between 0 and 256. | [optional]
 **sort_order** | **str**| SortOrder is an optional parameter and contains whether to sort ascending or descending This can be specified as URI parameter. | [optional]
 **mode** | **str**| Query Mode. | [optional]
 **query_categories** | **[str]**| OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64. | [optional]
 **query_kinds** | **[str]**| OR of Kinds to be matched, AND and Exclude are not supported for this type. Should be a valid object Kind. | [optional]
 **tenants** | **[str]**| OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. | [optional]
 **aggregate** | **bool**| Indicates whether to perform aggregation on the search results or not. | [optional]

### Return type

[**SearchSearchResponse**](SearchSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm_dss.SearchV1Api top]](#psm_dss.SearchV1Api) [[Back to search README]](../psm_dss/docs/search/README.md) [[Back to pensando_dss README]](../README.md)

# **post_policy_query**
> SearchPolicySearchResponse post_policy_query(body)

Security Policy Query

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import search_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.search import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.search_policy_search_response import SearchPolicySearchResponse
from pensando_dss.psm_dss.model.search_policy_search_request import SearchPolicySearchRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_v1_api.SearchV1Api(api_client)
    body = SearchPolicySearchRequest(
        action="action_example",
        app="app_example",
        from_ip_address="from_ip_address_example",
        from_security_group="from_security_group_example",
        kinds=[
            "kinds_example",
        ],
        name="name_example",
        namespace="default",
        port="port_example",
        protocol="protocol_example",
        tenant="default",
        to_ip_address="to_ip_address_example",
        to_security_group="to_security_group_example",
    ) # SearchPolicySearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Security Policy Query
        api_response = api_instance.post_policy_query(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchV1Api->post_policy_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchPolicySearchRequest**](SearchPolicySearchRequest.md)|  |

### Return type

[**SearchPolicySearchResponse**](SearchPolicySearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm_dss.SearchV1Api top]](#psm_dss.SearchV1Api) [[Back to search README]](../psm_dss/docs/search/README.md) [[Back to pensando_dss README]](../README.md)

# **post_query**
> SearchSearchResponse post_query(body)

Structured or free-form search

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import search_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.search import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.search_search_response import SearchSearchResponse
from pensando_dss.psm_dss.model.search_search_request import SearchSearchRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_v1_api.SearchV1Api(api_client)
    body = SearchSearchRequest(
        aggregate=True,
        _from=0,
        max_results=50,
        mode="full",
        query=SearchSearchQuery(
            categories=[
                "categories_example",
            ],
            fields=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            kinds=[
                "Network",
            ],
            labels=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[],
                    ),
                ],
            ),
            texts=[
                SearchTextRequirement(
                    text=[
                        "text_example",
                    ],
                ),
            ],
        ),
        query_string="query_string_example",
        sort_by="sort_by_example",
        sort_order="ascending",
        tenants=[
            "tenants_example",
        ],
    ) # SearchSearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Structured or free-form search
        api_response = api_instance.post_query(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchV1Api->post_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchSearchRequest**](SearchSearchRequest.md)|  |

### Return type

[**SearchSearchResponse**](SearchSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm_dss.SearchV1Api top]](#psm_dss.SearchV1Api) [[Back to search README]](../psm_dss/docs/search/README.md) [[Back to pensando_dss README]](../README.md)

