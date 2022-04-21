# psm.RoutingV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_z**](RoutingV1Api.md#get_health_z) | **GET** /routing/v1/{Instance}/health | 
[**get_list_neighbors**](RoutingV1Api.md#get_list_neighbors) | **GET** /routing/v1/{Instance}/neighbors | 
[**get_list_routes1**](RoutingV1Api.md#get_list_routes1) | **GET** /routing/v1/{Instance}/routes | 
[**post_list_routes**](RoutingV1Api.md#post_list_routes) | **POST** /routing/v1/{Instance}/routes | 


# **get_health_z**
> RoutingHealth get_health_z(instance)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import routing_v1_api
from pensando_dss.psm.models.routing import *
from pensando_dss.psm.model.routing_health import RoutingHealth
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
    api_instance = routing_v1_api.RoutingV1Api(api_client)
    instance = "Instance_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_health_z(instance)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RoutingV1Api->get_health_z: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**|  |

### Return type

[**RoutingHealth**](RoutingHealth.md)

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

# **get_list_neighbors**
> RoutingNeighborList get_list_neighbors(instance)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import routing_v1_api
from pensando_dss.psm.models.routing import *
from pensando_dss.psm.model.routing_neighbor_list import RoutingNeighborList
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
    api_instance = routing_v1_api.RoutingV1Api(api_client)
    instance = "Instance_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    neighbor = "neighbor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_list_neighbors(instance)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RoutingV1Api->get_list_neighbors: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **neighbor** | **str**|  | [optional]

### Return type

[**RoutingNeighborList**](RoutingNeighborList.md)

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

# **get_list_routes1**
> RoutingRouteList get_list_routes1(instance)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import routing_v1_api
from pensando_dss.psm.models.routing import *
from pensando_dss.psm.model.routing_route_list import RoutingRouteList
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
    api_instance = routing_v1_api.RoutingV1Api(api_client)
    instance = "Instance_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    ipaddress = "ipaddress_example" # str |  (optional)
    page_number = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_list_routes1(instance)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RoutingV1Api->get_list_routes1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **ipaddress** | **str**|  | [optional]
 **page_number** | **int**|  | [optional]

### Return type

[**RoutingRouteList**](RoutingRouteList.md)

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

# **post_list_routes**
> RoutingRouteList post_list_routes(instance, body)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import routing_v1_api
from pensando_dss.psm.models.routing import *
from pensando_dss.psm.model.routing_route_list import RoutingRouteList
from pensando_dss.psm.model.routing_route_filter import RoutingRouteFilter
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
    api_instance = routing_v1_api.RoutingV1Api(api_client)
    instance = "Instance_example" # str | 
    body = RoutingRouteFilter(
        all_routes=True,
        api_version="api_version_example",
        extcomm="extcomm_example",
        instance="instance_example",
        ipaddress="ipaddress_example",
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
        nhop="nhop_example",
        page_number=1,
        rtype="rtype_example",
        type="type_example",
        vnid="vnid_example",
    ) # RoutingRouteFilter | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_list_routes(instance, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling RoutingV1Api->post_list_routes: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**|  |
 **body** | [**RoutingRouteFilter**](RoutingRouteFilter.md)|  |

### Return type

[**RoutingRouteList**](RoutingRouteList.md)

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

