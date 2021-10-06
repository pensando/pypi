# MonitoringAlertPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_resolve** | **bool** | If set, the underlying alert will be auto-resolved if the rule that triggered the alert is cleared. | [optional] 
**clear_duration** | **str** | Met rule (requirements) needs to be cleared for the given duration to resolve an alert. | [optional] 
**destinations** | **[str]** | name of the alert destinations to be used to send out notification when an alert gets generated. | [optional] 
**enable** | **bool** | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]  if omitted the server will use the default value of True
**message** | **str** | Message to be used while generating the alert XXX: Event based alerts should not carry a message. It will be derived from the event. | [optional] 
**persistence_duration** | **str** | Met rule (requirements) needs to sustain for the given duration to qualify to be an alert. | [optional] 
**requirements** | [**[FieldsRequirement]**](FieldsRequirement.md) | List of requirements that needs to be met to trigger an alert. | [optional] 
**resource** | **str** | Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. | [optional] 
**severity** | **str** | Severity to be set for an alert that gets triggered from this rule. | [optional]  if omitted the server will use the default value of "info"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


