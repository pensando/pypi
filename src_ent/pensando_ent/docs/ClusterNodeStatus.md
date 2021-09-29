# ClusterNodeStatus

NodeStatus contains the current state of the node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[ClusterNodeCondition]**](ClusterNodeCondition.md) | List of current node conditions. | [optional] 
**phase** | **str** | Current lifecycle phase of the node. | [optional]  if omitted the server will use the default value of "unknown"
**quorum** | **bool** | Quorum node or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


