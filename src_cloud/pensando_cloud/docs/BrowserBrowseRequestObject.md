# BrowserBrowseRequestObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_only** | **bool** | When CountOnly is set the response only contains counts and not the actual objects. | [optional] 
**max_depth** | **int** | Max-Depth specifies how deep the query should explore. By default depth is set to 1 which means immediate relations 0 means to maximum depth. | [optional]  if omitted the server will use the default value of 1
**query_type** | **str** | QueryType is the direction of the query. | [optional]  if omitted the server will use the default value of "dependencies"
**uri** | **str** | URI is the root node from where to query. Length of string should be between 2 and 512. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


