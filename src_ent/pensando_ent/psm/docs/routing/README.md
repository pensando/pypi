```python

import time
import psm
from pprint import pprint
from api import routing_v1_api
from pensando_ent.psm.model.routing_health import RoutingHealth
from pensando_ent.psm.model.routing_neighbor_list import RoutingNeighborList
from pensando_ent.psm.model.routing_route_filter import RoutingRouteFilter
from pensando_ent.psm.model.routing_route_list import RoutingRouteList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_v1_api.RoutingV1Api(api_client)
    instance = "Instance_example" # str | 

    try:
        api_response = api_instance.get_health_z(instance)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling RoutingV1Api->get_health_z: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RoutingV1Api* | [**get_health_z**](docs/RoutingV1Api.md#get_health_z) | **GET** /routing/v1/{Instance}/health | 
*RoutingV1Api* | [**get_list_neighbors**](docs/RoutingV1Api.md#get_list_neighbors) | **GET** /routing/v1/{Instance}/neighbors | 
*RoutingV1Api* | [**get_list_routes1**](docs/RoutingV1Api.md#get_list_routes1) | **GET** /routing/v1/{Instance}/routes | 
*RoutingV1Api* | [**post_list_routes**](docs/RoutingV1Api.md#post_list_routes) | **POST** /routing/v1/{Instance}/routes | 


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiBgpAsn](docs/ApiBgpAsn.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiListMeta](docs/ApiListMeta.md)
 - [ApiListWatchOptions](docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](docs/ApiObjectMeta.md)
 - [ApiObjectRef](docs/ApiObjectRef.md)
 - [ApiStatus](docs/ApiStatus.md)
 - [ApiStatusResult](docs/ApiStatusResult.md)
 - [ApiTimestamp](docs/ApiTimestamp.md)
 - [ApiTypeMeta](docs/ApiTypeMeta.md)
 - [ApiWatchControl](docs/ApiWatchControl.md)
 - [ApiWatchEvent](docs/ApiWatchEvent.md)
 - [ApiWatchEventList](docs/ApiWatchEventList.md)
 - [EVPNRouteEVPNType2Route](docs/EVPNRouteEVPNType2Route.md)
 - [EVPNRouteEVPNType5Route](docs/EVPNRouteEVPNType5Route.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [HealthStatusPeeringStatus](docs/HealthStatusPeeringStatus.md)
 - [NetworkBGPNeighbor](docs/NetworkBGPNeighbor.md)
 - [RoutingEVPNRoute](docs/RoutingEVPNRoute.md)
 - [RoutingEmptyReq](docs/RoutingEmptyReq.md)
 - [RoutingHealth](docs/RoutingHealth.md)
 - [RoutingHealthStatus](docs/RoutingHealthStatus.md)
 - [RoutingNeighbor](docs/RoutingNeighbor.md)
 - [RoutingNeighborFilter](docs/RoutingNeighborFilter.md)
 - [RoutingNeighborList](docs/RoutingNeighborList.md)
 - [RoutingNeighborStatus](docs/RoutingNeighborStatus.md)
 - [RoutingRoute](docs/RoutingRoute.md)
 - [RoutingRouteFilter](docs/RoutingRouteFilter.md)
 - [RoutingRouteList](docs/RoutingRouteList.md)
 - [RoutingRouteStatus](docs/RoutingRouteStatus.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm.apis and psm.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm.api.default_api import DefaultApi`
- `from psm.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm
from psm.apis import *
from psm.models import *
```
