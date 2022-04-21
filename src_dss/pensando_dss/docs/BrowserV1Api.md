# psm.BrowserV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_query1**](BrowserV1Api.md#get_query1) | **GET** /configs/browser/v1/query | 
[**get_references**](BrowserV1Api.md#get_references) | **GET** /configs/browser/v1/dependencies/** | 
[**get_referrers**](BrowserV1Api.md#get_referrers) | **GET** /configs/browser/v1/dependedby/** | 
[**post_query**](BrowserV1Api.md#post_query) | **POST** /configs/browser/v1/query | 


# **get_query1**
> BrowserBrowseResponseList get_query1()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import browser_v1_api
from pensando_dss.psm.models.browser import *
from pensando_dss.psm.model.browser_browse_response_list import BrowserBrowseResponseList
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
    api_instance = browser_v1_api.BrowserV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_query1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling BrowserV1Api->get_query1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**BrowserBrowseResponseList**](BrowserBrowseResponseList.md)

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

# **get_references**
> BrowserBrowseResponse get_references()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import browser_v1_api
from pensando_dss.psm.models.browser import *
from pensando_dss.psm.model.browser_browse_response import BrowserBrowseResponse
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
    api_instance = browser_v1_api.BrowserV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    b_kind_filters = [
        "B.kind-filters_example",
    ] # [str] | KindFilters Specify the kind types to match/filter (for links only) on when returning the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_references()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling BrowserV1Api->get_references: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **b_kind_filters** | **[str]**| KindFilters Specify the kind types to match/filter (for links only) on when returning the response. | [optional]

### Return type

[**BrowserBrowseResponse**](BrowserBrowseResponse.md)

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

# **get_referrers**
> BrowserBrowseResponse get_referrers()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import browser_v1_api
from pensando_dss.psm.models.browser import *
from pensando_dss.psm.model.browser_browse_response import BrowserBrowseResponse
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
    api_instance = browser_v1_api.BrowserV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    b_kind_filters = [
        "B.kind-filters_example",
    ] # [str] | KindFilters Specify the kind types to match/filter (for links only) on when returning the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_referrers()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling BrowserV1Api->get_referrers: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **b_kind_filters** | **[str]**| KindFilters Specify the kind types to match/filter (for links only) on when returning the response. | [optional]

### Return type

[**BrowserBrowseResponse**](BrowserBrowseResponse.md)

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

# **post_query**
> BrowserBrowseResponseList post_query(body)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import browser_v1_api
from pensando_dss.psm.models.browser import *
from pensando_dss.psm.model.browser_browse_response_list import BrowserBrowseResponseList
from pensando_dss.psm.model.browser_browse_request_list import BrowserBrowseRequestList
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
    api_instance = browser_v1_api.BrowserV1Api(api_client)
    body = BrowserBrowseRequestList(
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
        requestlist=[
            BrowserBrowseRequestObject(
                count_only=True,
                kind_filters=[
                    "kind_filters_example",
                ],
                max_depth=1,
                query_type="dependencies",
                uri="uri_example",
            ),
        ],
    ) # BrowserBrowseRequestList | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_query(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling BrowserV1Api->post_query: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BrowserBrowseRequestList**](BrowserBrowseRequestList.md)|  |

### Return type

[**BrowserBrowseResponseList**](BrowserBrowseResponseList.md)

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

