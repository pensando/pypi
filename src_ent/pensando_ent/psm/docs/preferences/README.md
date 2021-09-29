
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PreferencesV1Api* | [**get_ui_global_settings**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#get_ui_global_settings) | **GET** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Get UIGlobalSettings object
*PreferencesV1Api* | [**get_ui_global_settings1**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#get_ui_global_settings1) | **GET** /configs/preferences/v1/uiglobalsettings | Get UIGlobalSettings object
*PreferencesV1Api* | [**label_ui_global_settings**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#label_ui_global_settings) | **POST** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings/label | Label UIGlobalSettings object
*PreferencesV1Api* | [**label_ui_global_settings1**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#label_ui_global_settings1) | **POST** /configs/preferences/v1/uiglobalsettings/label | Label UIGlobalSettings object
*PreferencesV1Api* | [**update_ui_global_settings**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#update_ui_global_settings) | **PUT** /configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings | Update UIGlobalSettings object
*PreferencesV1Api* | [**update_ui_global_settings1**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#update_ui_global_settings1) | **PUT** /configs/preferences/v1/uiglobalsettings | Update UIGlobalSettings object
*PreferencesV1Api* | [**watch_ui_global_settings**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#watch_ui_global_settings) | **GET** /configs/preferences/v1/watch/tenant/{O.Tenant}/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll
*PreferencesV1Api* | [**watch_ui_global_settings1**](../../../../pensando_ent/apiDocPath}}PreferencesV1Api.md#watch_ui_global_settings1) | **GET** /configs/preferences/v1/watch/uiglobalsettings | Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll


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
