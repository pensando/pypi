# RolloutRollout

Rollout object captures the admin's intent and status of the software version running on the cluster It is incorrect to have two different Rollouts active at the same time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**spec** | [**RolloutRolloutSpec**](RolloutRolloutSpec.md) |  | [optional] 
**status** | [**RolloutRolloutStatus**](RolloutRolloutStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


