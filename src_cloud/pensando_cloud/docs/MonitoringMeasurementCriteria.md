# MonitoringMeasurementCriteria

Measurement window and function to be used for monitoring the metric. nil `measurement` indicates that the policy will act on the instantaneous value of the metric that gets reported every 30s.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | **str** | Aggregate function to be applied on the metric values that were monitored over a window/interval. | [optional]  if omitted the server will use the default value of "none_function"
**window** | **str** | The length of time the metric will be monitored/observed before running the values against thresholds for alert creation/resolution. ui-hint: Allowed values - 5m, 10m, 30m, 1h. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


