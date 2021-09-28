```python

import time
import psm
from pprint import pprint
from api import objstore_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.objstore_auto_msg_object_watch_helper import ObjstoreAutoMsgObjectWatchHelper
from pensando_ent.psm.model.objstore_object import ObjstoreObject
from pensando_ent.psm.model.objstore_object_list import ObjstoreObjectList
from pensando_ent.psm.model.objstore_stream_chunk import ObjstoreStreamChunk
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
o_namespace = "O.Namespace_example" # str | 
body = ObjstoreObject(
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
        spec=ObjstoreObjectSpec(
            content_type="content_type_example",
        ),
        status=ObjstoreObjectStatus(
            digest="digest_example",
            size="size_example",
        ),
    ) # ObjstoreObject | 

    try:
        # Create Object object
        api_response = api_instance.add_object(o_tenant, o_namespace, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->add_object: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ObjstoreV1Api* | [**add_object**](docs/ObjstoreV1Api.md#add_object) | **POST** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**add_object1**](docs/ObjstoreV1Api.md#add_object1) | **POST** /objstore/v1/{O.Namespace}/objects | Create Object object
*ObjstoreV1Api* | [**delete_object**](docs/ObjstoreV1Api.md#delete_object) | **DELETE** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**delete_object1**](docs/ObjstoreV1Api.md#delete_object1) | **DELETE** /objstore/v1/{O.Namespace}/objects/{O.Name} | Delete Object object
*ObjstoreV1Api* | [**get_download_file**](docs/ObjstoreV1Api.md#get_download_file) | **GET** /objstore/v1/downloads/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file1**](docs/ObjstoreV1Api.md#get_download_file1) | **GET** /objstore/v1/downloads/{O.Namespace}/{O.Name} | Download file
*ObjstoreV1Api* | [**get_download_file_by_prefix**](docs/ObjstoreV1Api.md#get_download_file_by_prefix) | **GET** /objstore/v1/downloads/all/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file by prefix
*ObjstoreV1Api* | [**get_object**](docs/ObjstoreV1Api.md#get_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**get_object1**](docs/ObjstoreV1Api.md#get_object1) | **GET** /objstore/v1/{O.Namespace}/objects/{O.Name} | Get Object object
*ObjstoreV1Api* | [**list_object**](docs/ObjstoreV1Api.md#list_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**list_object1**](docs/ObjstoreV1Api.md#list_object1) | **GET** /objstore/v1/{O.Namespace}/objects | List Object objects
*ObjstoreV1Api* | [**watch_object**](docs/ObjstoreV1Api.md#watch_object) | **GET** /objstore/v1/watch/tenant/{O.Tenant}/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll
*ObjstoreV1Api* | [**watch_object1**](docs/ObjstoreV1Api.md#watch_object1) | **GET** /objstore/v1/watch/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll


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
