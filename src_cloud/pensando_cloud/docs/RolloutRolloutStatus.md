# RolloutRolloutStatus

Rollout Status gives the status of the rollout at the top level as well as details of individual components.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_percent** | **int** | Heuristic value of percentage completion of the rollout. | [optional] 
**controller_nodes_status** | [**[RolloutRolloutPhase]**](RolloutRolloutPhase.md) | Rollout status of Controller Node. | [optional] 
**controller_services_status** | [**[RolloutRolloutPhase]**](RolloutRolloutPhase.md) | Rollout status of Various Controller Services. | [optional] 
**dscs_status** | [**[RolloutRolloutPhase]**](RolloutRolloutPhase.md) | Rollout status of DistributedServiceCards in the cluster. Has entries for DistributedServiceCards on Controller nodes as well as workload nodes The entries are group by parallelism based on the order-constraints and max-parallel specified by the user. | [optional] 
**end_time** | **datetime** | End time of Rollout. | [optional] 
**prev_version** | **str** | Version of the cluster before the start of rollout. | [optional] 
**reason** | **str** | details the reason for overall Failure or Suspend. | [optional] 
**start_time** | **datetime** | Start time of Rollout. | [optional] 
**state** | **str** |  | [optional]  if omitted the server will use the default value of "progressing"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


