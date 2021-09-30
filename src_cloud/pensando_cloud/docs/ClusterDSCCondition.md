# ClusterDSCCondition

DSCCondition describes the state of a DistributedServiceCard at a certain point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **str** | The last time the condition transitioned. | [optional] 
**message** | **str** | A detailed message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Condition Status. | [optional]  if omitted the server will use the default value of "unknown"
**type** | **str** | Type indicates a certain NIC condition. | [optional]  if omitted the server will use the default value of "healthy"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


