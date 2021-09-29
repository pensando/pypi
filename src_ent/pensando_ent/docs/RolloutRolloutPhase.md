# RolloutRolloutPhase

RolloutPhase gives details of status of Rollout on each Node/Service/DistributedServiceCard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** | Time at which rollout completed for this node/service. | [optional] 
**message** | **str** | A detailed message indicating details about the transition. | [optional] 
**name** | **str** | Name of the Node, Service or DistributedServiceCard. | [optional] 
**num_retries** | **int** | Number of retries rollout performed. | [optional]  if omitted the server will use the default value of 0
**phase** | **str** | Phase indicates a certain rollout phase/condition. | [optional]  if omitted the server will use the default value of "pre-check"
**reason** | **str** | The reason for the Phase last transition, if any. | [optional] 
**start_time** | **datetime** | The time of starting the rollout for this node/service. This does not include the pre-check which can happen way before the actual rollout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


