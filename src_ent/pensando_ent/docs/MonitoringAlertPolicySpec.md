# MonitoringAlertPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **[str]** | name of the alert destinations to be used to send out notification when an alert gets generated. | [optional] 
**enable** | **bool** | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]  if omitted the server will use the default value of True
**message** | **str** | Message to be used while generating the alert. | [optional] 
**requirements** | [**[FieldsRequirement]**](FieldsRequirement.md) | List of requirements that needs to be met to trigger an alert. | [optional] 
**resource** | **str** | Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. | [optional] 
**severity** | **str** | Severity to be set for an alert that gets triggered from this rule. | [optional]  if omitted the server will use the default value of "info"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


