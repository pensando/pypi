# MonitoringStatsAlertPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **[str]** | name of the alert destinations to be used to send out notification when an alert gets generated. | [optional] 
**enable** | **bool** | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]  if omitted the server will use the default value of True
**measurement_criteria** | [**MonitoringMeasurementCriteria**](MonitoringMeasurementCriteria.md) |  | [optional] 
**metric** | [**MonitoringMetricIdentifier**](MonitoringMetricIdentifier.md) |  | [optional] 
**thresholds** | [**MonitoringThresholds**](MonitoringThresholds.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


