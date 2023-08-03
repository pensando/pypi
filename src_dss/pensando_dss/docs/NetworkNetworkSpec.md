# NetworkNetworkSpec

spec part of network object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_session_reuse** | **str** | AllowSessionReuse helps to handle TCP half open state connections. When there is mismatch in TCP connection state between client, server and DSE, and client tries to establish a new connection with same 5 tuple with source port reuse, typically DSE would drop the new connection attempts without AllowSessionReuse being enabled. With AllowSessionReuse turned ON, DSE will relax the TCP state/sequence number checks to allow the new connection to go through. AllowSessionReuseMode can be INHERIT_FROM_VRF, DISABLE or ENABLE. INHERIT_FROM_VRF is the default value. | [optional]  if omitted the server will use the default value of "inherit_from_vrf"
**egress_security_policy** | **[str]** | Security Policy to apply in the egress direction. | [optional] 
**firewall_profile** | [**NetworkNetworkFirewallProfile**](NetworkNetworkFirewallProfile.md) |  | [optional] 
**ingress_security_policy** | **[str]** | Security Policy to apply in the ingress direction. | [optional] 
**ipam_policy** | **str** | Relay Configuration if any. | [optional] 
**ipv4_gateway** | **str** | IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address. | [optional] 
**ipv4_subnet** | **str** | IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block. | [optional] 
**ipv6_gateway** | **str** | IPv6 gateway. | [optional] 
**ipv6_subnet** | **str** | IPv6 subnet CIDR. | [optional] 
**orchestrators** | [**[NetworkOrchestratorInfo]**](NetworkOrchestratorInfo.md) | If supplied, this network will only be applied to the orchestrators specified. | [optional] 
**route_import_export** | [**NetworkRDSpec**](NetworkRDSpec.md) |  | [optional] 
**type** | **str** | type of network. (vlan/vxlan/routed etc). | [optional]  if omitted the server will use the default value of "bridged"
**virtual_router** | **str** | VirtualRouter specifies the VRF this network belongs to. | [optional] 
**vlan_id** | **int** | Vlan ID for the network. Value should be between 0 and 4095. | [optional] 
**vxlan_vni** | **int** | Vxlan VNI for the network. Value should be between 0 and 16777215. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


