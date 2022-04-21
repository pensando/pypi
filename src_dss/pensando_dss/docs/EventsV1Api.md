# psm.EventsV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_event**](EventsV1Api.md#get_get_event) | **GET** /events/v1/events/{UUID} | Get specific event
[**get_get_events1**](EventsV1Api.md#get_get_events1) | **GET** /events/v1/events | 
[**post_get_events**](EventsV1Api.md#post_get_events) | **POST** /events/v1/events | 


# **get_get_event**
> EventsEvent get_get_event(uuid)

Get specific event

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import events_v1_api
from pensando_dss.psm.models.events import *
from pensando_dss.psm.model.events_event import EventsEvent
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
    api_instance = events_v1_api.EventsV1Api(api_client)
    uuid = "UUID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get specific event
        api_response = api_instance.get_get_event(uuid)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling EventsV1Api->get_get_event: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

### Return type

[**EventsEvent**](EventsEvent.md)

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

# **get_get_events1**
> EventsEventList get_get_events1()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import events_v1_api
from pensando_dss.psm.models.events import *
from pensando_dss.psm.model.events_event_list import EventsEventList
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
    api_instance = events_v1_api.EventsV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_get_events1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling EventsV1Api->get_get_events1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**EventsEventList**](EventsEventList.md)

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

# **post_get_events**
> EventsEventList post_get_events()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import events_v1_api
from pensando_dss.psm.models.events import *
from pensando_dss.psm.model.events_event_list import EventsEventList
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
    api_instance = events_v1_api.EventsV1Api(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_get_events()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling EventsV1Api->post_get_events: %s\n" % e)

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventsEventList**](EventsEventList.md)

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

