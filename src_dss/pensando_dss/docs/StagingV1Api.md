# psm.StagingV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_buffer**](StagingV1Api.md#add_buffer) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers | Create Buffer object
[**add_buffer1**](StagingV1Api.md#add_buffer1) | **POST** /configs/staging/v1/buffers | Create Buffer object
[**bulkedit**](StagingV1Api.md#bulkedit) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/bulkedit | Create/Update/Delete multiple objects as part of a single request
[**bulkedit1**](StagingV1Api.md#bulkedit1) | **POST** /configs/staging/v1/buffers/{O.Name}/bulkedit | Create/Update/Delete multiple objects as part of a single request
[**clear**](StagingV1Api.md#clear) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/clear | Clear operations from a configuration buffer
[**clear1**](StagingV1Api.md#clear1) | **POST** /configs/staging/v1/buffers/{O.Name}/clear | Clear operations from a configuration buffer
[**commit**](StagingV1Api.md#commit) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/commit | Commit a staged configuration buffer
[**commit1**](StagingV1Api.md#commit1) | **POST** /configs/staging/v1/buffers/{O.Name}/commit | Commit a staged configuration buffer
[**delete_buffer**](StagingV1Api.md#delete_buffer) | **DELETE** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name} | Delete Buffer object
[**delete_buffer1**](StagingV1Api.md#delete_buffer1) | **DELETE** /configs/staging/v1/buffers/{O.Name} | Delete Buffer object
[**get_buffer**](StagingV1Api.md#get_buffer) | **GET** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name} | Get Buffer object
[**get_buffer1**](StagingV1Api.md#get_buffer1) | **GET** /configs/staging/v1/buffers/{O.Name} | Get Buffer object
[**list_buffer**](StagingV1Api.md#list_buffer) | **GET** /configs/staging/v1/tenant/{O.Tenant}/buffers | List Buffer objects
[**list_buffer1**](StagingV1Api.md#list_buffer1) | **GET** /configs/staging/v1/buffers | List Buffer objects


# **add_buffer**
> StagingBuffer add_buffer(o_tenant, body)

Create Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = StagingBuffer(
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
        spec=StagingBufferSpec(
            contact="contact_example",
        ),
        status=StagingBufferStatus(
            errors=[
                StagingValidationError(
                    error=[
                        "error_example",
                    ],
                    method="method_example",
                    uri="uri_example",
                ),
            ],
            items=[
                StagingItem(
                    method="method_example",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
            validation_result="success",
        ),
    ) # StagingBuffer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Buffer object
        api_response = api_instance.add_buffer(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->add_buffer: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**StagingBuffer**](StagingBuffer.md)|  |

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **add_buffer1**
> StagingBuffer add_buffer1(body)

Create Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    body = StagingBuffer(
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
        spec=StagingBufferSpec(
            contact="contact_example",
        ),
        status=StagingBufferStatus(
            errors=[
                StagingValidationError(
                    error=[
                        "error_example",
                    ],
                    method="method_example",
                    uri="uri_example",
                ),
            ],
            items=[
                StagingItem(
                    method="method_example",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
            validation_result="success",
        ),
    ) # StagingBuffer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Buffer object
        api_response = api_instance.add_buffer1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->add_buffer1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StagingBuffer**](StagingBuffer.md)|  |

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **bulkedit**
> StagingBulkEditAction bulkedit(o_tenant, body)

Create/Update/Delete multiple objects as part of a single request

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_bulk_edit_action import StagingBulkEditAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = StagingBulkEditAction(
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
        spec=BulkeditBulkEditActionSpec(
            items=[
                BulkeditBulkEditItem(
                    method="create",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
        ),
        status=StagingBulkEditActionStatus(
            errors=[
                StagingValidationError(
                    error=[
                        "error_example",
                    ],
                    method="method_example",
                    uri="uri_example",
                ),
            ],
            items=[
                StagingItem(
                    method="method_example",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
            validation_result="success",
        ),
    ) # StagingBulkEditAction | 

    # example passing only required values which don't have defaults set
    try:
        # Create/Update/Delete multiple objects as part of a single request
        api_response = api_instance.bulkedit(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->bulkedit: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**StagingBulkEditAction**](StagingBulkEditAction.md)|  |

### Return type

[**StagingBulkEditAction**](StagingBulkEditAction.md)

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

# **bulkedit1**
> StagingBulkEditAction bulkedit1(o_name, body)

Create/Update/Delete multiple objects as part of a single request

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_bulk_edit_action import StagingBulkEditAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = StagingBulkEditAction(
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
        spec=BulkeditBulkEditActionSpec(
            items=[
                BulkeditBulkEditItem(
                    method="create",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
        ),
        status=StagingBulkEditActionStatus(
            errors=[
                StagingValidationError(
                    error=[
                        "error_example",
                    ],
                    method="method_example",
                    uri="uri_example",
                ),
            ],
            items=[
                StagingItem(
                    method="method_example",
                    object=ApiAny(
                        type_url="type_url_example",
                        value='YQ==',
                    ),
                    uri="uri_example",
                ),
            ],
            validation_result="success",
        ),
    ) # StagingBulkEditAction | 

    # example passing only required values which don't have defaults set
    try:
        # Create/Update/Delete multiple objects as part of a single request
        api_response = api_instance.bulkedit1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->bulkedit1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**StagingBulkEditAction**](StagingBulkEditAction.md)|  |

### Return type

[**StagingBulkEditAction**](StagingBulkEditAction.md)

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

# **clear**
> StagingClearAction clear(o_tenant, body)

Clear operations from a configuration buffer

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.staging_clear_action import StagingClearAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = StagingClearAction(
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
        spec=StagingClearActionSpec(
            items=[
                StagingItemId(
                    method="method_example",
                    uri="uri_example",
                ),
            ],
        ),
        status=StagingClearActionStatus(
            reason="reason_example",
            status="success",
        ),
    ) # StagingClearAction | 

    # example passing only required values which don't have defaults set
    try:
        # Clear operations from a configuration buffer
        api_response = api_instance.clear(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->clear: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**StagingClearAction**](StagingClearAction.md)|  |

### Return type

[**StagingClearAction**](StagingClearAction.md)

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

# **clear1**
> StagingClearAction clear1(o_name, body)

Clear operations from a configuration buffer

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.staging_clear_action import StagingClearAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = StagingClearAction(
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
        spec=StagingClearActionSpec(
            items=[
                StagingItemId(
                    method="method_example",
                    uri="uri_example",
                ),
            ],
        ),
        status=StagingClearActionStatus(
            reason="reason_example",
            status="success",
        ),
    ) # StagingClearAction | 

    # example passing only required values which don't have defaults set
    try:
        # Clear operations from a configuration buffer
        api_response = api_instance.clear1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->clear1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**StagingClearAction**](StagingClearAction.md)|  |

### Return type

[**StagingClearAction**](StagingClearAction.md)

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

# **commit**
> StagingCommitAction commit(o_tenant, body)

Commit a staged configuration buffer

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_commit_action import StagingCommitAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = StagingCommitAction(
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
        spec={},
        status=StagingCommitActionStatus(
            reason="reason_example",
            status="success",
        ),
    ) # StagingCommitAction | 

    # example passing only required values which don't have defaults set
    try:
        # Commit a staged configuration buffer
        api_response = api_instance.commit(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->commit: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**StagingCommitAction**](StagingCommitAction.md)|  |

### Return type

[**StagingCommitAction**](StagingCommitAction.md)

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

# **commit1**
> StagingCommitAction commit1(o_name, body)

Commit a staged configuration buffer

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_commit_action import StagingCommitAction
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = StagingCommitAction(
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
        spec={},
        status=StagingCommitActionStatus(
            reason="reason_example",
            status="success",
        ),
    ) # StagingCommitAction | 

    # example passing only required values which don't have defaults set
    try:
        # Commit a staged configuration buffer
        api_response = api_instance.commit1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->commit1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**StagingCommitAction**](StagingCommitAction.md)|  |

### Return type

[**StagingCommitAction**](StagingCommitAction.md)

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

# **delete_buffer**
> StagingBuffer delete_buffer(o_tenant)

Delete Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Buffer object
        api_response = api_instance.delete_buffer(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->delete_buffer: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **delete_buffer1**
> StagingBuffer delete_buffer1(o_name)

Delete Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Buffer object
        api_response = api_instance.delete_buffer1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->delete_buffer1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **get_buffer**
> StagingBuffer get_buffer(o_tenant)

Get Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_contact = "spec.Contact_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Buffer object
        api_response = api_instance.get_buffer(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->get_buffer: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_contact** | **str**|  | [optional]

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **get_buffer1**
> StagingBuffer get_buffer1(o_name)

Get Buffer object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer import StagingBuffer
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_contact = "spec.Contact_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Buffer object
        api_response = api_instance.get_buffer1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->get_buffer1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_contact** | **str**|  | [optional]

### Return type

[**StagingBuffer**](StagingBuffer.md)

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

# **list_buffer**
> StagingBufferList list_buffer(o_tenant)

List Buffer objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer_list import StagingBufferList
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Buffer objects
        api_response = api_instance.list_buffer(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->list_buffer: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**StagingBufferList**](StagingBufferList.md)

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

# **list_buffer1**
> StagingBufferList list_buffer1()

List Buffer objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import staging_v1_api
from pensando_dss.psm.models.staging import *
from pensando_dss.psm.model.staging_buffer_list import StagingBufferList
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
    api_instance = staging_v1_api.StagingV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Buffer objects
        api_response = api_instance.list_buffer1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling StagingV1Api->list_buffer1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**StagingBufferList**](StagingBufferList.md)

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

