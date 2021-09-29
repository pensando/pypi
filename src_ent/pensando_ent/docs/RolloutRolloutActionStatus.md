# RolloutRolloutActionStatus

RolloutAction Status gives the status of the rollout at the top level as well as details of individual components.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_percent** | **int** | Heuristic value of percentage completion of the rollout. | [optional] 
**end_time** | **datetime** | End time of Rollout. | [optional] 
**prev_version** | **str** | Version of the cluster before the start of rollout. | [optional] 
**start_time** | **datetime** | Start time of Rollout. | [optional] 
**state** | **str** |  | [optional]  if omitted the server will use the default value of "progressing"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


