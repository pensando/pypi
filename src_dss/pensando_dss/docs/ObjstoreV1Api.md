# psm_dss.ObjstoreV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_object**](ObjstoreV1Api.md#add_object) | **POST** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | Create Object object
[**add_object1**](ObjstoreV1Api.md#add_object1) | **POST** /objstore/v1/{O.Namespace}/objects | Create Object object
[**delete_object**](ObjstoreV1Api.md#delete_object) | **DELETE** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Delete Object object
[**delete_object1**](ObjstoreV1Api.md#delete_object1) | **DELETE** /objstore/v1/{O.Namespace}/objects/{O.Name} | Delete Object object
[**get_download_file**](ObjstoreV1Api.md#get_download_file) | **GET** /objstore/v1/downloads/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file
[**get_download_file1**](ObjstoreV1Api.md#get_download_file1) | **GET** /objstore/v1/downloads/{O.Namespace}/{O.Name} | Download file
[**get_download_file_by_prefix**](ObjstoreV1Api.md#get_download_file_by_prefix) | **GET** /objstore/v1/downloads/all/tenant/{O.Tenant}/{O.Namespace}/{O.Name} | Download file by prefix
[**get_object**](ObjstoreV1Api.md#get_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects/{O.Name} | Get Object object
[**get_object1**](ObjstoreV1Api.md#get_object1) | **GET** /objstore/v1/{O.Namespace}/objects/{O.Name} | Get Object object
[**list_object**](ObjstoreV1Api.md#list_object) | **GET** /objstore/v1/tenant/{O.Tenant}/{O.Namespace}/objects | List Object objects
[**list_object1**](ObjstoreV1Api.md#list_object1) | **GET** /objstore/v1/{O.Namespace}/objects | List Object objects
[**watch_object**](ObjstoreV1Api.md#watch_object) | **GET** /objstore/v1/watch/tenant/{O.Tenant}/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll
[**watch_object1**](ObjstoreV1Api.md#watch_object1) | **GET** /objstore/v1/watch/{O.Namespace}/objects | Watch Object objects. Supports WebSockets or HTTP long poll


# **add_object**
> ObjstoreObject add_object(o_tenant, o_namespace, body)

Create Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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

    # example passing only required values which don't have defaults set
    try:
        # Create Object object
        api_response = api_instance.add_object(o_tenant, o_namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->add_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **body** | [**ObjstoreObject**](ObjstoreObject.md)|  |

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **add_object1**
> ObjstoreObject add_object1(o_namespace, body)

Create Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Create Object object
        api_response = api_instance.add_object1(o_namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->add_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **body** | [**ObjstoreObject**](ObjstoreObject.md)|  |

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_object**
> ObjstoreObject delete_object(o_tenant, o_namespace, o_name)

Delete Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Object object
        api_response = api_instance.delete_object(o_tenant, o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->delete_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_object1**
> ObjstoreObject delete_object1(o_namespace, o_name)

Delete Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Object object
        api_response = api_instance.delete_object1(o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->delete_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **get_download_file**
> ObjstoreStreamChunk get_download_file(o_tenant, o_namespace, o_name)

Download file

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_content_type = "spec.content-type_example" # str | Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. (optional)
    status_size = "status.size_example" # str | Size is the total size of the object. (optional)
    status_digest = "status.digest_example" # str | Digest is a hash digest of the object content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file
        api_response = api_instance.get_download_file(o_tenant, o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download file
        api_response = api_instance.get_download_file(o_tenant, o_namespace, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_content_type=spec_content_type, status_size=status_size, status_digest=status_digest)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_content_type** | **str**| Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. | [optional]
 **status_size** | **str**| Size is the total size of the object. | [optional]
 **status_digest** | **str**| Digest is a hash digest of the object content. | [optional]

### Return type

[**ObjstoreStreamChunk**](ObjstoreStreamChunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **get_download_file1**
> ObjstoreStreamChunk get_download_file1(o_namespace, o_name)

Download file

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_content_type = "spec.content-type_example" # str | Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. (optional)
    status_size = "status.size_example" # str | Size is the total size of the object. (optional)
    status_digest = "status.digest_example" # str | Digest is a hash digest of the object content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file
        api_response = api_instance.get_download_file1(o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download file
        api_response = api_instance.get_download_file1(o_namespace, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_content_type=spec_content_type, status_size=status_size, status_digest=status_digest)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_content_type** | **str**| Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. | [optional]
 **status_size** | **str**| Size is the total size of the object. | [optional]
 **status_digest** | **str**| Digest is a hash digest of the object content. | [optional]

### Return type

[**ObjstoreStreamChunk**](ObjstoreStreamChunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **get_download_file_by_prefix**
> ObjstoreStreamChunk get_download_file_by_prefix(o_tenant, o_namespace, o_name)

Download file by prefix

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_content_type = "spec.content-type_example" # str | Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. (optional)
    status_size = "status.size_example" # str | Size is the total size of the object. (optional)
    status_digest = "status.digest_example" # str | Digest is a hash digest of the object content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file by prefix
        api_response = api_instance.get_download_file_by_prefix(o_tenant, o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file_by_prefix: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download file by prefix
        api_response = api_instance.get_download_file_by_prefix(o_tenant, o_namespace, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_content_type=spec_content_type, status_size=status_size, status_digest=status_digest)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file_by_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_content_type** | **str**| Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. | [optional]
 **status_size** | **str**| Size is the total size of the object. | [optional]
 **status_digest** | **str**| Digest is a hash digest of the object content. | [optional]

### Return type

[**ObjstoreStreamChunk**](ObjstoreStreamChunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **get_object**
> ObjstoreObject get_object(o_tenant, o_namespace, o_name)

Get Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_content_type = "spec.content-type_example" # str | Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. (optional)
    status_size = "status.size_example" # str | Size is the total size of the object. (optional)
    status_digest = "status.digest_example" # str | Digest is a hash digest of the object content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Object object
        api_response = api_instance.get_object(o_tenant, o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Object object
        api_response = api_instance.get_object(o_tenant, o_namespace, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_content_type=spec_content_type, status_size=status_size, status_digest=status_digest)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_content_type** | **str**| Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. | [optional]
 **status_size** | **str**| Size is the total size of the object. | [optional]
 **status_digest** | **str**| Digest is a hash digest of the object content. | [optional]

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **get_object1**
> ObjstoreObject get_object1(o_namespace, o_name)

Get Object object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_object import ObjstoreObject
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_content_type = "spec.content-type_example" # str | Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. (optional)
    status_size = "status.size_example" # str | Size is the total size of the object. (optional)
    status_digest = "status.digest_example" # str | Digest is a hash digest of the object content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Object object
        api_response = api_instance.get_object1(o_namespace, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Object object
        api_response = api_instance.get_object1(o_namespace, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_content_type=spec_content_type, status_size=status_size, status_digest=status_digest)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_content_type** | **str**| Content-Type for the stored object. Can either be specified when uploading. or the backend guesses one if possible. | [optional]
 **status_size** | **str**| Size is the total size of the object. | [optional]
 **status_digest** | **str**| Digest is a hash digest of the object content. | [optional]

### Return type

[**ObjstoreObject**](ObjstoreObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **list_object**
> ObjstoreObjectList list_object(o_tenant, o_namespace)

List Object objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.objstore_object_list import ObjstoreObjectList
from pensando_dss.psm_dss.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Object objects
        api_response = api_instance.list_object(o_tenant, o_namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Object objects
        api_response = api_instance.list_object(o_tenant, o_namespace, o_name=o_name, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**ObjstoreObjectList**](ObjstoreObjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **list_object1**
> ObjstoreObjectList list_object1(o_namespace)

List Object objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.objstore_object_list import ObjstoreObjectList
from pensando_dss.psm_dss.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Object objects
        api_response = api_instance.list_object1(o_namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Object objects
        api_response = api_instance.list_object1(o_namespace, o_name=o_name, o_tenant=o_tenant, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**ObjstoreObjectList**](ObjstoreObjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_object**
> ObjstoreAutoMsgObjectWatchHelper watch_object(o_tenant, o_namespace)

Watch Object objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_auto_msg_object_watch_helper import ObjstoreAutoMsgObjectWatchHelper
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object(o_tenant, o_namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object(o_tenant, o_namespace, o_name=o_name, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**ObjstoreAutoMsgObjectWatchHelper**](ObjstoreAutoMsgObjectWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_object1**
> ObjstoreAutoMsgObjectWatchHelper watch_object1(o_namespace)

Watch Object objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import objstore_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.objstore import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.objstore_auto_msg_object_watch_helper import ObjstoreAutoMsgObjectWatchHelper
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object1(o_namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object1(o_namespace, o_name=o_name, o_tenant=o_tenant, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**ObjstoreAutoMsgObjectWatchHelper**](ObjstoreAutoMsgObjectWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.ObjstoreV1Api top]](#psm_dss.ObjstoreV1Api) [[Back to objstore README]](../psm_dss/docs/objstore/README.md) [[Back to pensando_dss README]](../README.md)

