# ClusterQuorumMemberStatus

QuorumMemberStatus represents the overall status of a quorum member.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[ClusterQuorumMemberCondition]**](ClusterQuorumMemberCondition.md) | Conditions reported by the quorum member. | [optional] 
**id** | **str** | A unique identifier for this quorum member. | [optional] 
**name** | **str** | The name of the quorum member, matching the node name. | [optional] 
**status** | **str** | \&quot;Started\&quot; if the member succesfully joined the quorum, \&quot;Unstarted\&quot; otherwise. | [optional] 
**term** | **str** | The last election term this member has participated in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


