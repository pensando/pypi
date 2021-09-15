# objstore

This page provides working code examples for the **objstore** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ObjstoreV1Api* | [**add_object**](../../../docs/ObjstoreV1Api.md#add_object) | **POST** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**add_object1**](../../../docs/ObjstoreV1Api.md#add_object1) | **POST** /objstore/v1/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**delete_object**](../../../docs/ObjstoreV1Api.md#delete_object) | **DELETE** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**delete_object1**](../../../docs/ObjstoreV1Api.md#delete_object1) | **DELETE** /objstore/v1/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**get_download_file**](../../../docs/ObjstoreV1Api.md#get_download_file) | **GET** /objstore/v1/downloads/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file1**](../../../docs/ObjstoreV1Api.md#get_download_file1) | **GET** /objstore/v1/downloads/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file_by_prefix**](../../../docs/ObjstoreV1Api.md#get_download_file_by_prefix) | **GET** /objstore/v1/downloads/all/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file by prefix
*ObjstoreV1Api* | [**get_object**](../../../docs/ObjstoreV1Api.md#get_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**get_object1**](../../../docs/ObjstoreV1Api.md#get_object1) | **GET** /objstore/v1/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**list_object**](../../../docs/ObjstoreV1Api.md#list_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**list_object1**](../../../docs/ObjstoreV1Api.md#list_object1) | **GET** /objstore/v1/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**watch_object**](../../../docs/ObjstoreV1Api.md#watch_object) | **GET** /objstore/v1/watch/tenant/{O.Tenant}/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll
*ObjstoreV1Api* | [**watch_object1**](../../../docs/ObjstoreV1Api.md#watch_object1) | **GET** /objstore/v1/watch/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll


## README links for Model Groups

[aggwatch README.md](..//aggwatch/README.md)

[audit README.md](..//audit/README.md)

[auth README.md](..//auth/README.md)

[browser README.md](..//browser/README.md)

[cluster README.md](..//cluster/README.md)

[diagnostics README.md](..//diagnostics/README.md)

[events README.md](..//events/README.md)

[fwlog README.md](..//fwlog/README.md)

[monitoring README.md](..//monitoring/README.md)

[network README.md](..//network/README.md)

[objstore README.md](..//objstore/README.md)

[orchestration README.md](..//orchestration/README.md)

[preferences README.md](..//preferences/README.md)

[recoverykeys README.md](..//recoverykeys/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[sysruntime README.md](..//sysruntime/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiLabel](../../../docs/ApiLabel.md)
 - [ApiListMeta](../../../docs/ApiListMeta.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [ObjstoreAutoMsgBucketWatchHelper](../../../docs/ObjstoreAutoMsgBucketWatchHelper.md)
 - [ObjstoreAutoMsgBucketWatchHelperWatchEvent](../../../docs/ObjstoreAutoMsgBucketWatchHelperWatchEvent.md)
 - [ObjstoreAutoMsgObjectWatchHelper](../../../docs/ObjstoreAutoMsgObjectWatchHelper.md)
 - [ObjstoreAutoMsgObjectWatchHelperWatchEvent](../../../docs/ObjstoreAutoMsgObjectWatchHelperWatchEvent.md)
 - [ObjstoreBucket](../../../docs/ObjstoreBucket.md)
 - [ObjstoreBucketList](../../../docs/ObjstoreBucketList.md)
 - [ObjstoreBucketSpec](../../../docs/ObjstoreBucketSpec.md)
 - [ObjstoreBucketStatus](../../../docs/ObjstoreBucketStatus.md)
 - [ObjstoreObject](../../../docs/ObjstoreObject.md)
 - [ObjstoreObjectList](../../../docs/ObjstoreObjectList.md)
 - [ObjstoreObjectSpec](../../../docs/ObjstoreObjectSpec.md)
 - [ObjstoreObjectStatus](../../../docs/ObjstoreObjectStatus.md)
 - [ObjstoreStreamChunk](../../../docs/ObjstoreStreamChunk.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_ent.apis and psm_ent.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_ent.api.default_api import DefaultApi`
- `from psm_ent.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_ent
from psm_ent.apis import *
from psm_ent.models import *
```
