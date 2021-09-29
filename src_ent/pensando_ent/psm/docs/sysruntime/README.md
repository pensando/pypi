```python

import time
import psm
from pprint import pprint
from api import distributedservicecards_v1_api
from pensando_ent.psm.model.sysruntime_connection_request import SysruntimeConnectionRequest
from pensando_ent.psm.model.sysruntime_connection_status import SysruntimeConnectionStatus
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = distributedservicecards_v1_api.DistributedservicecardsV1Api(api_client)
    dsc_name = "DSCName_example" # str | 
body = SysruntimeConnectionRequest(
        api_version="api_version_example",
        dsc_name="dsc_name_example",
        filters=[
            SysruntimeConnectionFilter(
                destination=SysruntimeWorkloadSelector(
                    ip_address="10.1.1.1 ",
                ),
                destination_port=1,
                protocol="none",
                source=SysruntimeWorkloadSelector(
                    ip_address="10.1.1.1 ",
                ),
                source_port=1,
            ),
        ],
        kind="kind_example",
        list=ApiListWatchOptions(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            field_change_selector=[
                "field_change_selector_example",
            ],
            field_selector="field_selector_example",
            _from=1,
            generation_id="generation_id_example",
            label_selector="label_selector_example",
            labels={
                "key": "key_example",
            },
            max_results=1,
            meta_only=False,
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            sort_order="none",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # SysruntimeConnectionRequest | 

    try:
        # Active Connection Query
        api_response = api_instance.post_query_connection(dsc_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling DistributedservicecardsV1Api->post_query_connection: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DistributedservicecardsV1Api* | [**post_query_connection**](pensando_ent/docs/DistributedservicecardsV1Api.md#post_query_connection) | **POST** /sysruntime/distributedservicecards/v1/{DSCName}/connections | Active Connection Query


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
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [SysruntimeConnTrackInfo](docs/SysruntimeConnTrackInfo.md)
 - [SysruntimeConnectionFilter](docs/SysruntimeConnectionFilter.md)
 - [SysruntimeConnectionRequest](docs/SysruntimeConnectionRequest.md)
 - [SysruntimeConnectionStatus](docs/SysruntimeConnectionStatus.md)
 - [SysruntimeFlowData](docs/SysruntimeFlowData.md)
 - [SysruntimeFlowInfo](docs/SysruntimeFlowInfo.md)
 - [SysruntimeFlowKey](docs/SysruntimeFlowKey.md)
 - [SysruntimeFlowKeyESPInfo](docs/SysruntimeFlowKeyESPInfo.md)
 - [SysruntimeFlowKeyICMPInfo](docs/SysruntimeFlowKeyICMPInfo.md)
 - [SysruntimeFlowKeyL2](docs/SysruntimeFlowKeyL2.md)
 - [SysruntimeFlowKeyTcpUdpInfo](docs/SysruntimeFlowKeyTcpUdpInfo.md)
 - [SysruntimeFlowKeyV4](docs/SysruntimeFlowKeyV4.md)
 - [SysruntimeFlowSpec](docs/SysruntimeFlowSpec.md)
 - [SysruntimeFlowStatus](docs/SysruntimeFlowStatus.md)
 - [SysruntimeFwStatus](docs/SysruntimeFwStatus.md)
 - [SysruntimeHWConnectionGetResponse](docs/SysruntimeHWConnectionGetResponse.md)
 - [SysruntimeHWConnectionSpec](docs/SysruntimeHWConnectionSpec.md)
 - [SysruntimeHWConnectionStats](docs/SysruntimeHWConnectionStats.md)
 - [SysruntimeHWConnectionStatus](docs/SysruntimeHWConnectionStatus.md)
 - [SysruntimeHWFlowStats](docs/SysruntimeHWFlowStats.md)
 - [SysruntimeIPSecStatus](docs/SysruntimeIPSecStatus.md)
 - [SysruntimeTelemetryInfo](docs/SysruntimeTelemetryInfo.md)
 - [SysruntimeWorkloadSelector](docs/SysruntimeWorkloadSelector.md)


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
