# SecurityIPSecPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**SecurityIPSecConfig**](SecurityIPSecConfig.md) |  | [optional] 
**ha_mode** | **str** | Applies to North-South Traffic only. | [optional]  if omitted the server will use the default value of "no_ha"
**policy_distribution_targets** | **[str]** | PolicyDistributionTargets on which this policy should get deployed. | [optional] 
**rules** | [**[SecurityIPSecPolicyRule]**](SecurityIPSecPolicyRule.md) | list of rules; Applies to East-West Traffic only. | [optional] 
**tunnel_endpoints** | [**[SecurityTunnelEndpoint]**](SecurityTunnelEndpoint.md) | TunnelEndpoints applies to North-South Traffic only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


