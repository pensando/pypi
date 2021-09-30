# SearchSearchResponse

SearchResponse is the output provided by the search API Based on the search request, search results would be part of one of the entities : Entries or NestedAggregation. In case of failures, Error would indicate the error status and description.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_hits** | **str** | ActualHits indicates the actual hits returned in this response. | [optional] 
**aggregated_entries** | [**SearchTenantAggregation**](SearchTenantAggregation.md) |  | [optional] 
**entries** | [**[SearchEntry]**](SearchEntry.md) | EntryList is list of all search results with no grouping. This attribute is populated and valid only in Full request-mode. | [optional] 
**error** | [**SearchError**](SearchError.md) |  | [optional] 
**preview_entries** | [**SearchTenantPreview**](SearchTenantPreview.md) |  | [optional] 
**time_taken_msecs** | **str** | TimeTakenMsecs is the time taken for search response in millisecs. | [optional] 
**total_hits** | **str** | TotalHits indicates total number of hits matched. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


