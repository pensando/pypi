# psm.SearchV1Api

All URIs are relative to *https://PSM-IP-addr*

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import search_v1_api
from pensando_dss.psm.models.search import *
from pensando_dss.psm.model.search_policy_search_response import SearchPolicySearchResponse
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
    api_instance = search_v1_api.SearchV1Api(api_client)
    tenant = "tenant_example" # str | Tenant Name, to perform query within a Tenant's scope. The default tenant is \"default\". In the backend this field gets auto-filled & validated by apigw-hook based on user login context. (optional)
    kinds = [
        "kinds_example",
    ] # [str] | Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy, IPSecPolicy or NATPolicy. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Security Policy Query
        api_response = api_instance.get_policy_query1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SearchV1Api->get_policy_query1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant Name, to perform query within a Tenant&#39;s scope. The default tenant is \&quot;default\&quot;. In the backend this field gets auto-filled &amp; validated by apigw-hook based on user login context. | [optional]
 **kinds** | **[str]**| Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy, IPSecPolicy or NATPolicy. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query1**
> SearchSearchResponse get_query1()

Structured or free-form search

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import search_v1_api
from pensando_dss.psm.models.search import *
from pensando_dss.psm.model.search_search_response import SearchSearchResponse
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
    api_instance = search_v1_api.SearchV1Api(api_client)
    query_string = "query-string_example" # str | Simple query string This can be specified as URI parameter. For advanced query cases, Users should use specify SearchQuery and pass the SearchRequest in a GET/POST Body The max query-string length is 256 bytes. Length of string should be between 0 and 256. (optional)
    _from = 1 # int | From represents the start offset (zero based), used in paginated search requests The results returned would be in the range [From ... From+MaxResults-1] This can be specified as URI parameter. Default value is 0 and valid range is 0..8192. Value should be between 0 and 8192. (optional)
    query_categories = [
        "query.categories_example",
    ] # [str] | OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Structured or free-form search
        api_response = api_instance.get_query1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SearchV1Api->get_query1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| Simple query string This can be specified as URI parameter. For advanced query cases, Users should use specify SearchQuery and pass the SearchRequest in a GET/POST Body The max query-string length is 256 bytes. Length of string should be between 0 and 256. | [optional]
 **_from** | **int**| From represents the start offset (zero based), used in paginated search requests The results returned would be in the range [From ... From+MaxResults-1] This can be specified as URI parameter. Default value is 0 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]
 **query_categories** | **[str]**| OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_policy_query**
> SearchPolicySearchResponse post_policy_query(body)

Security Policy Query

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import search_v1_api
from pensando_dss.psm.models.search import *
from pensando_dss.psm.model.search_policy_search_response import SearchPolicySearchResponse
from pensando_dss.psm.model.search_policy_search_request import SearchPolicySearchRequest
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
    api_instance = search_v1_api.SearchV1Api(api_client)
    body = SearchPolicySearchRequest(
        action="action_example",
        app="app_example",
        destination_address="destination_address_example",
        from_ip_address="from_ip_address_example",
        from_workload_group="from_workload_group_example",
        kinds=[
            "kinds_example",
        ],
        name="name_example",
        namespace="default",
        port="port_example",
        protocol="protocol_example",
        source_address="source_address_example",
        tenant="default",
        to_ip_address="to_ip_address_example",
        to_workload_group="to_workload_group_example",
        translated_destination_address="translated_destination_address_example",
        translated_destination_port="translated_destination_port_example",
        translated_source_address="translated_source_address_example",
        virtual_routers=[
            "virtual_routers_example",
        ],
    ) # SearchPolicySearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Security Policy Query
        api_response = api_instance.post_policy_query(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_query**
> SearchSearchResponse post_query(body)

Structured or free-form search

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import search_v1_api
from pensando_dss.psm.models.search import *
from pensando_dss.psm.model.search_search_request import SearchSearchRequest
from pensando_dss.psm.model.search_search_response import SearchSearchResponse
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
    except pensando_dss.psm.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

