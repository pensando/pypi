# TelemetryQueryMetricsQuerySpec

MetricsQuerySpec requires a structured body consisting of: -  Object Selector (selects one more more objects of same Kind) -  Time Range (for the time series) -  A set of Metric Specs -  A pagination spec.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**bottom_param** | [**TelemetryQueryBottomSpec**](TelemetryQueryBottomSpec.md) |  | [optional] 
**end_time** | **datetime** | EndTime selects all metrics with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional] 
**fields** | **[str]** | Fields select the metric fields to be included in the result Empty will include all fields, must contain at least one non-tag field. Must start and end with alpha numeric and can have alphanumeric, -, _, . | [optional] 
**function** | **str** | Functions specify an operation function to be applied, example mean()/max(). | [optional]  if omitted the server will use the default value of "none"
**group_by_field** | **str** | GroupbyField groups series based on the field specified. Must start and end with alpha numeric and can have alphanumeric, -, _, . and ,. | [optional] 
**group_by_time** | **str** | GroupbyTime groups series based on the interval specified. Should be a valid time duration. | [optional] 
**kind** | **str** |  | [optional] 
**name** | **str** | Name is the name of the API object. Must start and end with alpha numeric and can have alphanumeric, -, _, . | [optional] 
**pagination** | [**TelemetryQueryPaginationSpec**](TelemetryQueryPaginationSpec.md) |  | [optional] 
**selector** | [**FieldsSelector**](FieldsSelector.md) |  | [optional] 
**sort_order** | **str** | SortOrder specifies time ordering of results. | [optional]  if omitted the server will use the default value of "ascending"
**start_time** | **datetime** | StartTime selects all metrics with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional] 
**subquery** | [**TelemetryQueryMetricsQuerySpec**](TelemetryQueryMetricsQuerySpec.md) |  | [optional] 
**top_param** | [**TelemetryQueryTopSpec**](TelemetryQueryTopSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


