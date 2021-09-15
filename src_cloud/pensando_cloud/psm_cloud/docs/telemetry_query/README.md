# telemetry_query

This page provides working code examples for the **telemetry_query** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TelemetryQueryV1Api* | [**get_metrics1**](../../../docs/TelemetryQueryV1Api.md#get_metrics1) | **GET** /telemetry/v1/metrics | telemetry metrics query
*TelemetryQueryV1Api* | [**post_metrics**](../../../docs/TelemetryQueryV1Api.md#post_metrics) | **POST** /telemetry/v1/metrics | telemetry metrics query


## README links for Model Groups

[aggwatch README.md](..//aggwatch/README.md)

[audit README.md](..//audit/README.md)

[auth README.md](..//auth/README.md)

[browser README.md](..//browser/README.md)

[cluster README.md](..//cluster/README.md)

[diagnostics README.md](..//diagnostics/README.md)

[events README.md](..//events/README.md)

[fwlog README.md](..//fwlog/README.md)

[monitoring README.md](..//monitoring/README.md)

[network README.md](..//network/README.md)

[objstore README.md](..//objstore/README.md)

[orchestration README.md](..//orchestration/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiInterface](../../../docs/ApiInterface.md)
 - [ApiInterfaceSlice](../../../docs/ApiInterfaceSlice.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [FieldsRequirement](../../../docs/FieldsRequirement.md)
 - [FieldsSelector](../../../docs/FieldsSelector.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [TelemetryQueryMetricsQueryList](../../../docs/TelemetryQueryMetricsQueryList.md)
 - [TelemetryQueryMetricsQueryResponse](../../../docs/TelemetryQueryMetricsQueryResponse.md)
 - [TelemetryQueryMetricsQueryResult](../../../docs/TelemetryQueryMetricsQueryResult.md)
 - [TelemetryQueryMetricsQuerySpec](../../../docs/TelemetryQueryMetricsQuerySpec.md)
 - [TelemetryQueryMetricsSQLQuery](../../../docs/TelemetryQueryMetricsSQLQuery.md)
 - [TelemetryQueryPaginationSpec](../../../docs/TelemetryQueryPaginationSpec.md)
 - [TelemetryQueryResultSeries](../../../docs/TelemetryQueryResultSeries.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_cloud.apis and psm_cloud.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_cloud.api.default_api import DefaultApi`
- `from psm_cloud.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_cloud
from psm_cloud.apis import *
from psm_cloud.models import *
```
