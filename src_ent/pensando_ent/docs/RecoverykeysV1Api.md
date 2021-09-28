# psm.RecoverykeysV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_recovery_keys**](RecoverykeysV1Api.md#get_download_recovery_keys) | **GET** /sysruntime/v1/cluster/recoverykeys | 


# **get_download_recovery_keys**
> RecoverykeysRecoveryKeys get_download_recovery_keys()



### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import recoverykeys_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.recoverykeys import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.recoverykeys_recovery_keys import RecoverykeysRecoveryKeys
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recoverykeys_v1_api.RecoverykeysV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_download_recovery_keys()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecoverykeysV1Api->get_download_recovery_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RecoverykeysRecoveryKeys**](RecoverykeysRecoveryKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm.RecoverykeysV1Api top]](#psm.RecoverykeysV1Api) [[Back to recoverykeys README]](../psm/docs/recoverykeys/README.md) [[Back to pensando_ent README]](../README.md)

