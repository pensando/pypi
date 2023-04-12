# SecurityTunnelEndpointStatus

Applies to North-South Traffic only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dse_id** | **str** | DSE ID for which the agent error or warning is issued. | [optional] 
**extended_seq_num_enabled** | **bool** |  | [optional] 
**ike_sa** | [**SecurityIKESAStatus**](SecurityIKESAStatus.md) |  | [optional] 
**ike_version** | **str** |  | [optional]  if omitted the server will use the default value of "prefer_ikev2_support_ikev1"
**interface_name** | **str** |  | [optional] 
**ipsec_sa** | [**SecurityIPsecSAStatus**](SecurityIPsecSAStatus.md) |  | [optional] 
**local_address** | **str** |  | [optional] 
**oper_state** | **str** |  | [optional]  if omitted the server will use the default value of "up"
**oper_state_info** | **[str]** |  | [optional] 
**remote_address** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


