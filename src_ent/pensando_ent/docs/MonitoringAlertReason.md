# MonitoringAlertReason

AlertReason captures all the requirements with matched value from the alert policy rule at the time of creating an alert. e.g. \"matched-requirements\": [{\"field\": \"cpu\", \"operator\": \"Gt\", \"values\": [90], \"observed-value\": 95}].
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_policy_id** | **str** | Alert Policy ID that matched. | [optional] 
**matched_requirements** | [**[MonitoringMatchedRequirement]**](MonitoringMatchedRequirement.md) | List of requirements from the alert policy with it&#39;s matched value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


