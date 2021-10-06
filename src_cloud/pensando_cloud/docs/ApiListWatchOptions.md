# ApiListWatchOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **datetime** |  | [optional] 
**field_change_selector** | **[str]** | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional] 
**field_selector** | **str** | FieldSelector to select on field values in list or watch results. | [optional] 
**_from** | **int** | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional] 
**generation_id** | **str** |  | [optional] 
**label_selector** | **str** | LabelSelector to select on labels in list or watch results. | [optional] 
**labels** | **{str: (str,)}** |  | [optional] 
**max_results** | **int** | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional] 
**mod_time** | **datetime** |  | [optional] 
**name** | **str** | Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional] 
**namespace** | **str** | Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional] 
**resource_version** | **str** |  | [optional] 
**self_link** | **str** |  | [optional] 
**sort_order** | **str** | order to sort List results in. | [optional]  if omitted the server will use the default value of "none"
**tenant** | **str** | Must be alpha-numerics. Length of string should be between 1 and 48. | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


