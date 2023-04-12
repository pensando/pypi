
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TelemetryQueryV1Api* | [**get_metrics1**](../../../../pensando_dss/docs/TelemetryQueryV1Api.md#get_metrics1) | **GET** /telemetry/v1/metrics | telemetry metrics query
*TelemetryQueryV1Api* | [**get_sql_query1**](../../../../pensando_dss/docs/TelemetryQueryV1Api.md#get_sql_query1) | **GET** /telemetry/v1/sqlmetrics | 
*TelemetryQueryV1Api* | [**post_metrics**](../../../../pensando_dss/docs/TelemetryQueryV1Api.md#post_metrics) | **POST** /telemetry/v1/metrics | telemetry metrics query
*TelemetryQueryV1Api* | [**post_sql_query**](../../../../pensando_dss/docs/TelemetryQueryV1Api.md#post_sql_query) | **POST** /telemetry/v1/sqlmetrics | 


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
 - [TelemetryQueryBottomSpec](../../../docs/TelemetryQueryBottomSpec.md)
 - [TelemetryQueryMetricsQueryList](../../../docs/TelemetryQueryMetricsQueryList.md)
 - [TelemetryQueryMetricsQueryResponse](../../../docs/TelemetryQueryMetricsQueryResponse.md)
 - [TelemetryQueryMetricsQueryResult](../../../docs/TelemetryQueryMetricsQueryResult.md)
 - [TelemetryQueryMetricsQuerySpec](../../../docs/TelemetryQueryMetricsQuerySpec.md)
 - [TelemetryQueryMetricsSQLQuery](../../../docs/TelemetryQueryMetricsSQLQuery.md)
 - [TelemetryQueryPaginationSpec](../../../docs/TelemetryQueryPaginationSpec.md)
 - [TelemetryQueryResultSeries](../../../docs/TelemetryQueryResultSeries.md)
 - [TelemetryQueryTopSpec](../../../docs/TelemetryQueryTopSpec.md)


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
