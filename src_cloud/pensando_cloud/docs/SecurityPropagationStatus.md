# SecurityPropagationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_status** | [**[SecurityDSCStatus]**](SecurityDSCStatus.md) | list of DSCs status. | [optional] 
**generation_id** | **str** | The Generation ID this status is for. | [optional] 
**min_version** | **str** | The Version running on the slowest Naples. | [optional] 
**pending** | **int** | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional] 
**pending_dscs** | **[str]** | list of DSCs where propagation did not complete. | [optional] 
**status** | **str** | Textual description of propagation status. | [optional] 
**updated** | **int** | The number of Naples that this version has already been pushed to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


