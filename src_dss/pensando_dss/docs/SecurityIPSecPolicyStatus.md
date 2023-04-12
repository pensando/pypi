# SecurityIPSecPolicyStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_issues** | [**ApiConfigurationIssues**](ApiConfigurationIssues.md) |  | [optional] 
**esp_params** | **str** | Encryption and Algorithm details used for encrypting data traffic (ESP). | [optional] 
**ike_params** | **str** | Encryption and Algorithm details used for IKEv2 key exchange. | [optional] 
**propagation_status** | [**SecurityPropagationStatus**](SecurityPropagationStatus.md) |  | [optional] 
**rule_status** | [**[SecurityIPSecRuleStatus]**](SecurityIPSecRuleStatus.md) |  | [optional] 
**tunnel_endpoint_status** | [**[SecurityTunnelEndpointStatus]**](SecurityTunnelEndpointStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


