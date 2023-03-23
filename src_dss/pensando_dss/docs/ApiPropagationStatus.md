# ApiPropagationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dse_status** | [**[ApiDSEStatus]**](ApiDSEStatus.md) | list of DSEs status. | [optional] 
**generation_id** | **str** | The Generation ID this status is for. | [optional] 
**pending** | **int** | Number of DSEs pending. If this is 0 it can be assumed that everything is up to date. | [optional] 
**pending_dses** | **[str]** | list of DSEs where propagation did not complete. | [optional] 
**status** | **str** | Textual description of propagation status. | [optional] 
**updated** | **int** | The number of DSEs that this version has already been pushed to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


