# SecurityNetworkSecurityPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_tenant** | **bool** | specifies if the set of rules need to be attached globally to a tenant. | [optional]  if omitted the server will use the default value of True
**policy_distribution_targets** | **[str]** | PolicyDistributionTargets on which this policy should get deployed. | [optional] 
**priority** | **int** | Policy priority. If not specified, it will be assigned automatically in increments of 1000. | [optional] 
**rules** | [**[SecuritySGRule]**](SecuritySGRule.md) | list of rules. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


