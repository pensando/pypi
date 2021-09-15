# psm_ent.AuditV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_event**](AuditV1Api.md#get_get_event) | **GET** /audit/v1/events/{UUID} | Fetches an audit event given its uuid


# **get_get_event**
> AuditAuditEvent get_get_event(uuid)

Fetches an audit event given its uuid

### Example

```python
#!/usr/bin/env python3
import time
import .psm_ent
from pensando_ent.psm_ent.api import audit_v1_api
from pensando_ent.psm_ent.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm_ent.models.audit import *
from pensando_ent.psm_ent  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm_ent.model.audit_audit_event import AuditAuditEvent
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm_ent.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = audit_v1_api.AuditV1Api(api_client)
    uuid = "UUID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetches an audit event given its uuid
        api_response = api_instance.get_get_event(uuid)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_ent.AuditV1Api top]](#psm_ent.AuditV1Api) [[Back to audit README]](../psm_ent/docs/audit/README.md) [[Back to pensando_ent README]](../README.md)

