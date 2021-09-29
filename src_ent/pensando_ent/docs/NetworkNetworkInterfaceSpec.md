# NetworkNetworkInterfaceSpec

NetworkInterfaceSpec.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **str** | desired Admin state of the port. | [optional]  if omitted the server will use the default value of "up"
**attach_network** | **str** | AttachNetwork associates the interface with a Network. This is only valid for HOST_PF type. | [optional] 
**attach_tenant** | **str** |  | [optional] 
**connection_tracking** | **bool** | ConnectionTracking enables connection tracking on the interface. This is valid only for HOST_PF type. | [optional]  if omitted the server will use the default value of False
**enable_fw_logging** | **bool** | EnableFwLogging enables flow logging on the interface. This is valid only for HOST_PF type. | [optional] 
**ip_alloc_type** | **str** |  | [optional]  if omitted the server will use the default value of "none"
**ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**mac_address** | **str** | Override system allocated MAC address. Should be a valid MAC address. | [optional] 
**mtu** | **int** | Mtu of the interface. | [optional] 
**pause** | [**NetworkPauseSpec**](NetworkPauseSpec.md) |  | [optional] 
**speed** | **str** | Intefaae speed. | [optional] 
**tx_policer** | **str** |  | [optional] 
**type** | **str** | Type specifies the type of interface. | [optional]  if omitted the server will use the default value of "none"
**vnf_attached** | **bool** | VNFAttached knob on the interface. This is valid only for HOST_PF type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


