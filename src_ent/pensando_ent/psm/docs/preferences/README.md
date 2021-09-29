```python

import time
import psm
from pprint import pprint
from api import preferences_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.preferences_auto_msg_ui_global_settings_watch_helper import PreferencesAutoMsgUIGlobalSettingsWatchHelper
from pensando_ent.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = preferences_v1_api.PreferencesV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
meta_name = "meta.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
spec_style_options = "spec.style-options_example" # str | Can contain any UI style preferences. Provide typing through UI code. (optional)
idle_timeout_duration = "idle-timeout.duration_example" # str | Time of inactivity after which user logout countdown warning pops up. Should be a valid time duration. (optional)
idle_timeout_warning_time = "idle-timeout.warning-time_example" # str | Warning duration before logout and after system idle time. Should be a valid time duration of at most 5m0s. (optional)

    try:
        # Get UIGlobalSettings object
        api_response = api_instance.get_ui_global_settings(o_tenant, t_kind=t_kind, t_api_version=t_api_version, meta_name=meta_name, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_style_options=spec_style_options, idle_timeout_duration=idle_timeout_duration, idle_timeout_warning_time=idle_timeout_warning_time)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling PreferencesV1Api->get_ui_global_settings: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PreferencesV1Api* | [**get_ui_global_settings**](pensando_ent/docs/PreferencesV1Api.md#get_ui_global_settings) | **GET** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Get UIGlobalSettings object
*PreferencesV1Api* | [**get_ui_global_settings1**](pensando_ent/docs/PreferencesV1Api.md#get_ui_global_settings1) | **GET** /configs/preferences/v1/uiglobalsettings | Get UIGlobalSettings object
*PreferencesV1Api* | [**label_ui_global_settings**](pensando_ent/docs/PreferencesV1Api.md#label_ui_global_settings) | **POST** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings/label | Label UIGlobalSettings object
*PreferencesV1Api* | [**label_ui_global_settings1**](pensando_ent/docs/PreferencesV1Api.md#label_ui_global_settings1) | **POST** /configs/preferences/v1/uiglobalsettings/label | Label UIGlobalSettings object
*PreferencesV1Api* | [**update_ui_global_settings**](pensando_ent/docs/PreferencesV1Api.md#update_ui_global_settings) | **PUT** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Update UIGlobalSettings object
*PreferencesV1Api* | [**update_ui_global_settings1**](pensando_ent/docs/PreferencesV1Api.md#update_ui_global_settings1) | **PUT** /configs/preferences/v1/uiglobalsettings | Update UIGlobalSettings object
*PreferencesV1Api* | [**watch_ui_global_settings**](pensando_ent/docs/PreferencesV1Api.md#watch_ui_global_settings) | **GET** /configs/preferences/v1/watch/tenant/{O.Tenant}/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll
*PreferencesV1Api* | [**watch_ui_global_settings1**](pensando_ent/docs/PreferencesV1Api.md#watch_ui_global_settings1) | **GET** /configs/preferences/v1/watch/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll


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
 - [PreferencesAutoMsgUIGlobalSettingsWatchHelper](docs/PreferencesAutoMsgUIGlobalSettingsWatchHelper.md)
 - [PreferencesAutoMsgUIGlobalSettingsWatchHelperWatchEvent](docs/PreferencesAutoMsgUIGlobalSettingsWatchHelperWatchEvent.md)
 - [PreferencesIdleTimeout](docs/PreferencesIdleTimeout.md)
 - [PreferencesUIGlobalSettings](docs/PreferencesUIGlobalSettings.md)
 - [PreferencesUIGlobalSettingsList](docs/PreferencesUIGlobalSettingsList.md)
 - [PreferencesUIGlobalSettingsSpec](docs/PreferencesUIGlobalSettingsSpec.md)


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
