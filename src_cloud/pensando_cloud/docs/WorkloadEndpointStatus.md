# WorkloadEndpointStatus

status part of Endpoint object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_state** | **str** | endpoint FSM state. | [optional] 
**security_groups** | **[str]** | security groups. | [optional] 
**homing_host_addr** | **str** | host address of the host where this endpoint exists. | [optional] 
**homing_host_name** | **str** | host name of the host where this endpoint exists. | [optional] 
**ipv4_address** | **str** | IPv4 address of the endpoint. | [optional] 
**ipv4_addresses** | **[str]** | IPv4 addresses of the endpoint. | [optional] 
**ipv4_gateway** | **str** | IPv4 gateway for the endpoint. | [optional] 
**ipv4_gateways** | **[str]** | IPv4 gateways for the endpoint. | [optional] 
**ipv6_address** | **str** | IPv6 address for the endpoint. | [optional] 
**ipv6_addresses** | **[str]** | IPv6 addresses for the endpoint. | [optional] 
**ipv6_gateway** | **str** | IPv6 gateway. | [optional] 
**ipv6_gateways** | **[str]** | IPv6 gateways. | [optional] 
**mac_address** | **str** | Mac address of the endpoint. Should be a valid MAC address. | [optional] 
**micro_segment_vlan** | **int** | micro-segment VLAN. | [optional] 
**migration** | [**WorkloadEndpointMigrationStatus**](WorkloadEndpointMigrationStatus.md) |  | [optional] 
**mirror_sessions** | **[str]** | MirrorSessions list of mirror sessions enabled on this endpoint. | [optional] 
**network** | **str** | network this endpoint belogs to. | [optional] 
**node_uuid** | **str** | homing host&#39;s UUID. | [optional] 
**node_uuid_list** | **[str]** | NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional] 
**workload_attributes** | **{str: (str,)}** | VM or container attribute/labels. | [optional] 
**workload_name** | **str** | VM or container name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


