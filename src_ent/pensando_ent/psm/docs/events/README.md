```python

import time
import psm
from pprint import pprint
from api import events_v1_api
from pensando_ent.psm.model.events_event import EventsEvent
from pensando_ent.psm.model.events_event_list import EventsEventList
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_v1_api.EventsV1Api(api_client)
    uuid = "UUID_example" # str | 

    try:
        # Get specific event
        api_response = api_instance.get_get_event(uuid)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling EventsV1Api->get_get_event: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsV1Api* | [**get_get_event**](docs/EventsV1Api.md#get_get_event) | **GET** /events/v1/events/{UUID} | Get specific event
*EventsV1Api* | [**get_get_events1**](docs/EventsV1Api.md#get_get_events1) | **GET** /events/v1/events | 
*EventsV1Api* | [**post_get_events**](docs/EventsV1Api.md#post_get_events) | **POST** /events/v1/events | 


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
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
 - [EventsEvent](docs/EventsEvent.md)
 - [EventsEventAttributes](docs/EventsEventAttributes.md)
 - [EventsEventList](docs/EventsEventList.md)
 - [EventsEventSource](docs/EventsEventSource.md)
 - [EventsGetEventRequest](docs/EventsGetEventRequest.md)
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
