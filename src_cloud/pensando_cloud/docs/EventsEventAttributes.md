# EventsEventAttributes

EventAttributes contains all the event attributes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category represents the category of an event. e.g. Cluster/Network/Datapath. | [optional]  if omitted the server will use the default value of "cluster"
**count** | **int** | Number of occurrence of this event in the active interval. | [optional] 
**message** | **str** | Message represents the human readable description of an event. | [optional] 
**object_ref** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 
**severity** | **str** | Severity represents the criticality level of an event. | [optional]  if omitted the server will use the default value of "info"
**source** | [**EventsEventSource**](EventsEventSource.md) |  | [optional] 
**type** | **str** | Type represents the type of an event. e.g. NICAdmittedEvent, NodeJoined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


