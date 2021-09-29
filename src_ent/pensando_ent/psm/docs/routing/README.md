
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RoutingV1Api* | [**get_health_z**](../../../../pensando_ent/docs/RoutingV1Api.md#get_health_z) | **GET** /routing/v1/{Instance}/health | 
*RoutingV1Api* | [**get_list_neighbors**](../../../../pensando_ent/docs/RoutingV1Api.md#get_list_neighbors) | **GET** /routing/v1/{Instance}/neighbors | 
*RoutingV1Api* | [**get_list_routes1**](../../../../pensando_ent/docs/RoutingV1Api.md#get_list_routes1) | **GET** /routing/v1/{Instance}/routes | 
*RoutingV1Api* | [**post_list_routes**](../../../../pensando_ent/docs/RoutingV1Api.md#post_list_routes) | **POST** /routing/v1/{Instance}/routes | 


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
