# StagingCommitAction

CommitAction commits the changes in the staging buffer. All staged entries are verified and if verification is successful they are commited.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**spec** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**status** | [**StagingCommitActionStatus**](StagingCommitActionStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


