
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ObjstoreV1Api* | [**add_object**](../../../../pensando_ent/docs/ObjstoreV1Api.md#add_object) | **POST** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**add_object1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#add_object1) | **POST** /objstore/v1/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**delete_object**](../../../../pensando_ent/docs/ObjstoreV1Api.md#delete_object) | **DELETE** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**delete_object1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#delete_object1) | **DELETE** /objstore/v1/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**get_download_file**](../../../../pensando_ent/docs/ObjstoreV1Api.md#get_download_file) | **GET** /objstore/v1/downloads/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#get_download_file1) | **GET** /objstore/v1/downloads/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file_by_prefix**](../../../../pensando_ent/docs/ObjstoreV1Api.md#get_download_file_by_prefix) | **GET** /objstore/v1/downloads/all/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file by prefix
*ObjstoreV1Api* | [**get_object**](../../../../pensando_ent/docs/ObjstoreV1Api.md#get_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**get_object1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#get_object1) | **GET** /objstore/v1/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**list_object**](../../../../pensando_ent/docs/ObjstoreV1Api.md#list_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**list_object1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#list_object1) | **GET** /objstore/v1/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**watch_object**](../../../../pensando_ent/docs/ObjstoreV1Api.md#watch_object) | **GET** /objstore/v1/watch/tenant/{O.Tenant}/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll
*ObjstoreV1Api* | [**watch_object1**](../../../../pensando_ent/docs/ObjstoreV1Api.md#watch_object1) | **GET** /objstore/v1/watch/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiLabel](docs/ApiLabel.md)
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
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [ObjstoreAutoMsgBucketWatchHelper](docs/ObjstoreAutoMsgBucketWatchHelper.md)
 - [ObjstoreAutoMsgBucketWatchHelperWatchEvent](docs/ObjstoreAutoMsgBucketWatchHelperWatchEvent.md)
 - [ObjstoreAutoMsgObjectWatchHelper](docs/ObjstoreAutoMsgObjectWatchHelper.md)
 - [ObjstoreAutoMsgObjectWatchHelperWatchEvent](docs/ObjstoreAutoMsgObjectWatchHelperWatchEvent.md)
 - [ObjstoreBucket](docs/ObjstoreBucket.md)
 - [ObjstoreBucketList](docs/ObjstoreBucketList.md)
 - [ObjstoreBucketSpec](docs/ObjstoreBucketSpec.md)
 - [ObjstoreBucketStatus](docs/ObjstoreBucketStatus.md)
 - [ObjstoreObject](docs/ObjstoreObject.md)
 - [ObjstoreObjectList](docs/ObjstoreObjectList.md)
 - [ObjstoreObjectSpec](docs/ObjstoreObjectSpec.md)
 - [ObjstoreObjectStatus](docs/ObjstoreObjectStatus.md)
 - [ObjstoreStreamChunk](docs/ObjstoreStreamChunk.md)


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
