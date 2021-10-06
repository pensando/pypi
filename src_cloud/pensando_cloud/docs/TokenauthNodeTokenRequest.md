# TokenauthNodeTokenRequest

NodeTokenRequest is a message that allows user to retrieve an auth token to connect to a cluster node and perform privileged operations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **[str]** | Audience represents a list of nodes the token is valid for. \&quot;*\&quot; indicates all nodes. | [optional] 
**validity_end** | **datetime** | ValidityEnd indicates the time at which the token becomes invalid. | [optional] 
**validity_start** | **datetime** | ValidityStart indicates the time at which the token becomes valid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


