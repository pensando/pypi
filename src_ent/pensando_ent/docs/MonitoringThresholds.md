# MonitoringThresholds

List of threshold values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Operator to be applied when comparing metric values against the threshold values. | [optional]  if omitted the server will use the default value of "less_or_equal_than"
**values** | [**[MonitoringThreshold]**](MonitoringThreshold.md) | List of threshold values to be acted against. Key should be one of the alert severity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


