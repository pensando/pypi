# MonitoringStatsAlertPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **[str]** | name of the alert destinations to be used to send out notification when an alert gets generated. | [optional] 
**enable** | **bool** | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]  if omitted the server will use the default value of True
**instance_selector** | [**MonitoringInstanceSelector**](MonitoringInstanceSelector.md) |  | [optional] 
**measurement_criteria** | [**MonitoringMeasurementCriteria**](MonitoringMeasurementCriteria.md) |  | [optional] 
**message_template** | **str** | Template that is used for constructing the alert message template can refer fields form the policy like {{.Spec.Metric.Kind}}, {{.Spec.Metric.FieldName}} or from the metric table like {{.reporterID}}, {{.name}} only scalar fields from the policy can be referred, repeated fields, or maps cannot be referred on the template. | [optional] 
**metric** | [**MonitoringMetricIdentifier**](MonitoringMetricIdentifier.md) |  | [optional] 
**thresholds** | [**MonitoringThresholds**](MonitoringThresholds.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


