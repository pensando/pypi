# BrowserBrowseRequest

BrowseRequest is the query request for the dependency tree.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**count_only** | **bool** |  | [optional] 
**kind** | **str** |  | [optional] 
**max_depth** | **int** |  | [optional]  if omitted the server will use the default value of 1
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**query_type** | **str** |  | [optional]  if omitted the server will use the default value of "dependencies"
**uri** | **str** | Length of string should be between 2 and 512. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


