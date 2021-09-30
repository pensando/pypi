# SearchSearchQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **[str]** | OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64. | [optional] 
**fields** | [**FieldsSelector**](FieldsSelector.md) |  | [optional] 
**kinds** | **[str]** | OR of Kinds to be matched, AND and Exclude are not supported for this type. Should be a valid object Kind. | [optional] 
**labels** | [**LabelsSelector**](LabelsSelector.md) |  | [optional] 
**texts** | [**[SearchTextRequirement]**](SearchTextRequirement.md) | OR of Text-requirements to be matched, Exclude is not supported for Text search. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


