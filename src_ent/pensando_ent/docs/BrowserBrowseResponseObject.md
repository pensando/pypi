# BrowserBrowseResponseObject

BrowseResponse is the response to a query request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_depth** | **int** | MaxDepth that the response explored. Reflects the value specified in the query. | [optional] 
**objects** | [**{str: (BrowserObject,)}**](BrowserObject.md) | map of results. Key to the map is the URI of the  Object. | [optional] 
**query_type** | **str** | QueryType is the direction of the query. | [optional] 
**root_uri** | **str** | RootURI is the root node for the response. | [optional] 
**total_count** | **int** | TotalCount of objects in the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


