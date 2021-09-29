# NetworkNetworkInterfaceStatus

NetworkInterfaceStatus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_node** | **str** | Set only if interface is on Venice Node. | [optional] 
**dsc** | **str** |  | [optional] 
**dsc_id** | **str** |  | [optional] 
**if_host_status** | [**NetworkNetworkInterfaceHostStatus**](NetworkNetworkInterfaceHostStatus.md) |  | [optional] 
**if_uplink_status** | [**NetworkNetworkInterfaceUplinkStatus**](NetworkNetworkInterfaceUplinkStatus.md) |  | [optional] 
**mirror_sessions** | **[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**oper_status** | **str** |  | [optional]  if omitted the server will use the default value of "up"
**primary_mac** | **str** | Should be a valid MAC address. | [optional] 
**propagation_status** | [**SecurityPropagationStatus**](SecurityPropagationStatus.md) |  | [optional] 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "none"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


