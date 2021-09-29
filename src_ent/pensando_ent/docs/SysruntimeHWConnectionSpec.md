# SysruntimeHWConnectionSpec

HWConnectionSpec represents a full session with forward and reverse flow It is possible to have a session with just one flow (for L2 mcast/bcast).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_flow** | [**SysruntimeFlowSpec**](SysruntimeFlowSpec.md) |  | [optional] 
**peer_initiator_flow** | [**SysruntimeFlowSpec**](SysruntimeFlowSpec.md) |  | [optional] 
**peer_responder_flow** | [**SysruntimeFlowSpec**](SysruntimeFlowSpec.md) |  | [optional] 
**responder_flow** | [**SysruntimeFlowSpec**](SysruntimeFlowSpec.md) |  | [optional] 
**session_id** | **str** | sessionId is unique session identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


