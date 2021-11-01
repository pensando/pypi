# psm.RecoverykeysV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_recovery_keys**](RecoverykeysV1Api.md#get_download_recovery_keys) | **GET** /sysruntime/v1/cluster/recoverykeys | 


# **get_download_recovery_keys**
> RecoverykeysRecoveryKeys get_download_recovery_keys()



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import recoverykeys_v1_api
from pensando_dss.psm.models.recoverykeys import *
from pensando_dss.psm.model.recoverykeys_recovery_keys import RecoverykeysRecoveryKeys
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
    api_instance = recoverykeys_v1_api.RecoverykeysV1Api(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_download_recovery_keys()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

