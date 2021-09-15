# SearchPolicySearchResponse

PolicySearchResponse is response to the security/firewall policy search request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**{str: (SearchPolicyMatchEntries,)}**](SearchPolicyMatchEntries.md) | Result is Map of &lt;NetworkSecurityPolicy object name, PolicyMatch Entry&gt;. | [optional] 
**status** | **str** | Status of firewall policy search. | [optional]  if omitted the server will use the default value of "match"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


