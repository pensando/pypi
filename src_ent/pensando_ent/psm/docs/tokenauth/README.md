```python

import time
import psm
from pprint import pprint
from api import tokenauth_v1_api
from pensando_ent.psm.model.tokenauth_node_token_response import TokenauthNodeTokenResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokenauth_v1_api.TokenauthV1Api(api_client)
    audience = [
        "audience_example",
    ] # [str] | Audience represents a list of nodes the token is valid for. \"*\" indicates all nodes. (optional)
validity_start = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ValidityStart indicates the time at which the token becomes valid. (optional)
validity_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ValidityEnd indicates the time at which the token becomes invalid. (optional)

    try:
        api_response = api_instance.get_generate_node_token(audience=audience, validity_start=validity_start, validity_end=validity_end)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling TokenauthV1Api->get_generate_node_token: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TokenauthV1Api* | [**get_generate_node_token**](pensando_ent/docs/TokenauthV1Api.md#get_generate_node_token) | **GET** /tokenauth/v1/node | 


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](docs/ApiObjectMeta.md)
 - [ApiObjectRef](docs/ApiObjectRef.md)
 - [ApiStatus](docs/ApiStatus.md)
 - [ApiStatusResult](docs/ApiStatusResult.md)
 - [ApiTimestamp](docs/ApiTimestamp.md)
 - [ApiWatchControl](docs/ApiWatchControl.md)
 - [ApiWatchEvent](docs/ApiWatchEvent.md)
 - [ApiWatchEventList](docs/ApiWatchEventList.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [TokenauthNodeTokenRequest](docs/TokenauthNodeTokenRequest.md)
 - [TokenauthNodeTokenResponse](docs/TokenauthNodeTokenResponse.md)


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
