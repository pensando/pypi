# EventsEvent

Event is a system notification of a fault, condition or configuration that should be user visible. These objects are created internally by Event client and persisted in EventDB.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**category** | **str** |  | [optional]  if omitted the server will use the default value of "cluster"
**count** | **int** |  | [optional] 
**kind** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**object_ref** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 
**severity** | **str** |  | [optional]  if omitted the server will use the default value of "info"
**source** | [**EventsEventSource**](EventsEventSource.md) |  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


