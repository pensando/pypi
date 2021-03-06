# psm.AuditV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_event**](AuditV1Api.md#get_get_event) | **GET** /audit/v1/events/{UUID} | Fetches an audit event given its uuid


# **get_get_event**
> AuditAuditEvent get_get_event(uuid)

Fetches an audit event given its uuid

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import audit_v1_api
from pensando_ent.psm.models.audit import *
from pensando_ent.psm.model.audit_audit_event import AuditAuditEvent
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_v1_api.AuditV1Api(api_client)
    uuid = "UUID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetches an audit event given its uuid
        api_response = api_instance.get_get_event(uuid)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling AuditV1Api->get_get_event: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

### Return type

[**AuditAuditEvent**](AuditAuditEvent.md)

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

