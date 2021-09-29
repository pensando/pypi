# psm.RecoverykeysV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_recovery_keys**](RecoverykeysV1Api.md#get_download_recovery_keys) | **GET** /sysruntime/v1/cluster/recoverykeys | 


# **get_download_recovery_keys**
> RecoverykeysRecoveryKeys get_download_recovery_keys()



### Example

```python
import time
import pensando_ent.psm
from pensando_ent.psm.api import recoverykeys_v1_api
from pensando_ent.psm.model.recoverykeys_recovery_keys import RecoverykeysRecoveryKeys
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recoverykeys_v1_api.RecoverykeysV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_download_recovery_keys()
        pprint(api_response)
    except psm.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

