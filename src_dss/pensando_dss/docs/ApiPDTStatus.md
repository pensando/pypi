# ApiPDTStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of PDT. | [optional] 
**pending** | **int** | Number of DSEs in PDT pending. If this is 0 it can be assumed that everything is up to date. | [optional] 
**pending_dses** | **[str]** | list of DSEs in PDT where propagation did not complete. | [optional] 
**status** | **str** | Textual description of pdt-propagation status. | [optional] 
**updated** | **int** | The number of DSEs in PDT that this version has already been pushed to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


