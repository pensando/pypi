```python

import time
import psm
from pprint import pprint
from api import staging_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.staging_buffer import StagingBuffer
from pensando_ent.psm.model.staging_buffer_list import StagingBufferList
from pensando_ent.psm.model.staging_bulk_edit_action import StagingBulkEditAction
from pensando_ent.psm.model.staging_clear_action import StagingClearAction
from pensando_ent.psm.model.staging_commit_action import StagingCommitAction
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
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

    try:
        # Create Buffer object
        api_response = api_instance.add_buffer(o_tenant, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling StagingV1Api->add_buffer: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StagingV1Api* | [**add_buffer**](pensando_ent/docs/StagingV1Api.md#add_buffer) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers | Create Buffer object
*StagingV1Api* | [**add_buffer1**](pensando_ent/docs/StagingV1Api.md#add_buffer1) | **POST** /configs/staging/v1/buffers | Create Buffer object
*StagingV1Api* | [**bulkedit**](pensando_ent/docs/StagingV1Api.md#bulkedit) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/bulkedit | Create/Update/Delete multiple objects as part of a single request
*StagingV1Api* | [**bulkedit1**](pensando_ent/docs/StagingV1Api.md#bulkedit1) | **POST** /configs/staging/v1/buffers/{O.Name}/bulkedit | Create/Update/Delete multiple objects as part of a single request
*StagingV1Api* | [**clear**](pensando_ent/docs/StagingV1Api.md#clear) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/clear | Clear operations from a configuration buffer
*StagingV1Api* | [**clear1**](pensando_ent/docs/StagingV1Api.md#clear1) | **POST** /configs/staging/v1/buffers/{O.Name}/clear | Clear operations from a configuration buffer
*StagingV1Api* | [**commit**](pensando_ent/docs/StagingV1Api.md#commit) | **POST** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name}/commit | Commit a staged configuration buffer
*StagingV1Api* | [**commit1**](pensando_ent/docs/StagingV1Api.md#commit1) | **POST** /configs/staging/v1/buffers/{O.Name}/commit | Commit a staged configuration buffer
*StagingV1Api* | [**delete_buffer**](pensando_ent/docs/StagingV1Api.md#delete_buffer) | **DELETE** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name} | Delete Buffer object
*StagingV1Api* | [**delete_buffer1**](pensando_ent/docs/StagingV1Api.md#delete_buffer1) | **DELETE** /configs/staging/v1/buffers/{O.Name} | Delete Buffer object
*StagingV1Api* | [**get_buffer**](pensando_ent/docs/StagingV1Api.md#get_buffer) | **GET** /configs/staging/v1/tenant/{O.Tenant}/buffers/{O.Name} | Get Buffer object
*StagingV1Api* | [**get_buffer1**](pensando_ent/docs/StagingV1Api.md#get_buffer1) | **GET** /configs/staging/v1/buffers/{O.Name} | Get Buffer object
*StagingV1Api* | [**list_buffer**](pensando_ent/docs/StagingV1Api.md#list_buffer) | **GET** /configs/staging/v1/tenant/{O.Tenant}/buffers | List Buffer objects
*StagingV1Api* | [**list_buffer1**](pensando_ent/docs/StagingV1Api.md#list_buffer1) | **GET** /configs/staging/v1/buffers | List Buffer objects


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiAny](docs/ApiAny.md)
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
 - [BulkeditBulkEditActionSpec](docs/BulkeditBulkEditActionSpec.md)
 - [BulkeditBulkEditItem](docs/BulkeditBulkEditItem.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [StagingAutoMsgBufferWatchHelper](docs/StagingAutoMsgBufferWatchHelper.md)
 - [StagingAutoMsgBufferWatchHelperWatchEvent](docs/StagingAutoMsgBufferWatchHelperWatchEvent.md)
 - [StagingBuffer](docs/StagingBuffer.md)
 - [StagingBufferList](docs/StagingBufferList.md)
 - [StagingBufferSpec](docs/StagingBufferSpec.md)
 - [StagingBufferStatus](docs/StagingBufferStatus.md)
 - [StagingBulkEditAction](docs/StagingBulkEditAction.md)
 - [StagingBulkEditActionStatus](docs/StagingBulkEditActionStatus.md)
 - [StagingClearAction](docs/StagingClearAction.md)
 - [StagingClearActionSpec](docs/StagingClearActionSpec.md)
 - [StagingClearActionStatus](docs/StagingClearActionStatus.md)
 - [StagingCommitAction](docs/StagingCommitAction.md)
 - [StagingCommitActionStatus](docs/StagingCommitActionStatus.md)
 - [StagingItem](docs/StagingItem.md)
 - [StagingItemId](docs/StagingItemId.md)
 - [StagingValidationError](docs/StagingValidationError.md)


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
