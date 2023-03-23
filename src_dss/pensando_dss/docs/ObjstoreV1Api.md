# psm.ObjstoreV1Api

All URIs are relative to *https://PSM-IP-addr*

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
> ObjstoreObject add_object(o_tenant, body)

Create Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ObjstoreObject(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.add_object(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->add_object: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_object1**
> ObjstoreObject add_object1(o_namespace, body)

Create Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    body = ObjstoreObject(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> ObjstoreObject delete_object(o_tenant)

Delete Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Object object
        api_response = api_instance.delete_object(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->delete_object: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object1**
> ObjstoreObject delete_object1(o_namespace)

Delete Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Object object
        api_response = api_instance.delete_object1(o_namespace)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->delete_object1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_file**
> ObjstoreStreamChunk get_download_file(o_tenant)

Download file

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file
        api_response = api_instance.get_download_file(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_file1**
> ObjstoreStreamChunk get_download_file1(o_namespace)

Download file

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file
        api_response = api_instance.get_download_file1(o_namespace)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_file_by_prefix**
> ObjstoreStreamChunk get_download_file_by_prefix(o_tenant)

Download file by prefix

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_stream_chunk import ObjstoreStreamChunk
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download file by prefix
        api_response = api_instance.get_download_file_by_prefix(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_download_file_by_prefix: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object**
> ObjstoreObject get_object(o_tenant)

Get Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Object object
        api_response = api_instance.get_object(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object1**
> ObjstoreObject get_object1(o_namespace)

Get Object object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object import ObjstoreObject
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Object object
        api_response = api_instance.get_object1(o_namespace)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->get_object1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object**
> ObjstoreObjectList list_object(o_tenant)

List Object objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object_list import ObjstoreObjectList
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Object objects
        api_response = api_instance.list_object(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object1**
> ObjstoreObjectList list_object1(o_namespace)

List Object objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_object_list import ObjstoreObjectList
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Object objects
        api_response = api_instance.list_object1(o_namespace)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->list_object1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_object**
> ObjstoreAutoMsgObjectWatchHelper watch_object(o_tenant)

Watch Object objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_auto_msg_object_watch_helper import ObjstoreAutoMsgObjectWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_object1**
> ObjstoreAutoMsgObjectWatchHelper watch_object1(o_namespace)

Watch Object objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import objstore_v1_api
from pensando_dss.psm.models.objstore import *
from pensando_dss.psm.model.objstore_auto_msg_object_watch_helper import ObjstoreAutoMsgObjectWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
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
    api_instance = objstore_v1_api.ObjstoreV1Api(api_client)
    o_namespace = "O.Namespace_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Object objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_object1(o_namespace)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ObjstoreV1Api->watch_object1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_namespace** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

