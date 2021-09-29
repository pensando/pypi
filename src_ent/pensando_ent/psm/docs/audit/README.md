```python

import time
import psm
from pprint import pprint
from api import audit_v1_api
from pensando_ent.psm.model.audit_audit_event import AuditAuditEvent
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_v1_api.AuditV1Api(api_client)
    uuid = "UUID_example" # str | 

    try:
        # Fetches an audit event given its uuid
        api_response = api_instance.get_get_event(uuid)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuditV1Api->get_get_event: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuditV1Api* | [**get_get_event**](pensando_ent/docs/AuditV1Api.md#get_get_event) | **GET** /audit/v1/events/{UUID} | Fetches an audit event given its uuid


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
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
 - [AuditAuditEvent](docs/AuditAuditEvent.md)
 - [AuditAuditEventRequest](docs/AuditAuditEventRequest.md)
 - [AuditEventAttributes](docs/AuditEventAttributes.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)


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
