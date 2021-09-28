```python

import time
import psm
from pprint import pprint
from api import telemetry_query_v1_api
from pensando_ent.psm.model.telemetry_query_metrics_query_list import TelemetryQueryMetricsQueryList
from pensando_ent.psm.model.telemetry_query_metrics_query_response import TelemetryQueryMetricsQueryResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telemetry_query_v1_api.TelemetryQueryV1Api(api_client)
    tenant = "tenant_example" # str | Tenant for the request. (optional)
namespace = "namespace_example" # str | Namespace for the request. (optional)

    try:
        # telemetry metrics query
        api_response = api_instance.get_metrics1(tenant=tenant, namespace=namespace)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling TelemetryQueryV1Api->get_metrics1: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TelemetryQueryV1Api* | [**get_metrics1**](docs/TelemetryQueryV1Api.md#get_metrics1) | **GET** /telemetry/v1/metrics | telemetry metrics query
*TelemetryQueryV1Api* | [**post_metrics**](docs/TelemetryQueryV1Api.md#post_metrics) | **POST** /telemetry/v1/metrics | telemetry metrics query


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiInterface](docs/ApiInterface.md)
 - [ApiInterfaceSlice](docs/ApiInterfaceSlice.md)
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
 - [FieldsRequirement](docs/FieldsRequirement.md)
 - [FieldsSelector](docs/FieldsSelector.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [TelemetryQueryBottomSpec](docs/TelemetryQueryBottomSpec.md)
 - [TelemetryQueryMetricsQueryList](docs/TelemetryQueryMetricsQueryList.md)
 - [TelemetryQueryMetricsQueryResponse](docs/TelemetryQueryMetricsQueryResponse.md)
 - [TelemetryQueryMetricsQueryResult](docs/TelemetryQueryMetricsQueryResult.md)
 - [TelemetryQueryMetricsQuerySpec](docs/TelemetryQueryMetricsQuerySpec.md)
 - [TelemetryQueryMetricsSQLQuery](docs/TelemetryQueryMetricsSQLQuery.md)
 - [TelemetryQueryPaginationSpec](docs/TelemetryQueryPaginationSpec.md)
 - [TelemetryQueryResultSeries](docs/TelemetryQueryResultSeries.md)
 - [TelemetryQueryTopSpec](docs/TelemetryQueryTopSpec.md)


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
