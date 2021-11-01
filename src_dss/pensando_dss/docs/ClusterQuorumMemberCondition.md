# ClusterQuorumMemberCondition

QuorumMemberCondition represents conditions that can affect quorum members.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | The last time the condition transitioned. | [optional] 
**status** | **str** | Condition Status. | [optional]  if omitted the server will use the default value of "unknown"
**type** | **str** | Type indicates a certain node condition. | [optional]  if omitted the server will use the default value of "healthy"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


