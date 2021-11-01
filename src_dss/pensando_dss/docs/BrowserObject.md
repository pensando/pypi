# BrowserObject

Object is a node in the dependency tree representing a config object with links to related objects.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**links** | [**{str: (ObjectURIs,)}**](ObjectURIs.md) | Links points to the relations of the object. The key for the map is the path to the filed which is causing the relation. | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**query_type** | **str** | QueryType specifies the direction of the relations in Links. | [optional]  if omitted the server will use the default value of "dependencies"
**reverse** | **str** | Reverse is the view from the object looking back in the reverse direction of the dependency tree. | [optional] 
**uri** | **str** | URI is the Browser URI for this object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


