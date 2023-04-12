# FwlogFwLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action. | [optional]  if omitted the server will use the default value of "allow"
**alg** | **str** | Appliction Layer Gateway. | [optional] 
**api_version** | **str** |  | [optional] 
**app_id** | **str** | Application ID. | [optional] 
**bytes_received** | **str** | Bytes received represents the number of bytes received at the source from the destination. | [optional] 
**bytes_sent** | **str** | Bytes sent represents the number of bytes sent from the source to the destination. | [optional] 
**create_reason** | **str** | CreateReason represents the specific reason of flow&#39;s creation. | [optional] 
**destination_ip** | **str** | Destination IP. | [optional] 
**destination_port** | **int** | Destination Port. | [optional] 
**destination_vrf** | **str** | Destination VRF,. | [optional] 
**direction** | **str** | Flow Direction. | [optional]  if omitted the server will use the default value of "from-host"
**flow_action** | **str** | Flow action. | [optional] 
**icmp_code** | **int** | icmp code. | [optional] 
**icmp_id** | **int** | icmp ID. | [optional] 
**icmp_type** | **int** | icmp type. | [optional] 
**ipsec_protected** | **bool** | If IPsec protected. | [optional] 
**ipsec_rule_id** | **str** | IPsec policy rule ID. | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**nat_translated_destination_ip** | **str** | NATTranslatedDestIP represents the destination ip post NAT translation. | [optional] 
**nat_translated_destination_port** | **int** | NATTranslatedDestPort represents the destination port post NAT translation. | [optional] 
**nat_translated_source_ip** | **str** | NATTranslatedSrcIP represents the source ip post NAT translation. | [optional] 
**packets_received** | **str** | Packets received represents the number of packets received at the source from the destination. | [optional] 
**packets_sent** | **str** | Packets sent represents the number of packets sent from the source to the destination. | [optional] 
**policy_display_name** | **str** | PolicyDisplayName represents the display name of the security policy. | [optional] 
**policy_name** | **str** | policy name. | [optional] 
**protocol** | **str** | Protocol,. | [optional] 
**reporter_id** | **str** | Reporter ID. | [optional] 
**reporter_name** | **str** | ReporterName represents the name or hostname of the DSM that generated the log. | [optional] 
**rule_id** | **str** | Rule ID. | [optional] 
**rule_name** | **str** | Rule Name represents the name of the firewall rule that was hit by this session. | [optional] 
**security_policy_id** | **str** | SecurityPolicyID represents the UUID of the security policy. | [optional] 
**session_id** | **str** | Session ID. | [optional] 
**source_ip** | **str** | Source IP,. | [optional] 
**source_port** | **int** | Source Port. | [optional] 
**source_vrf** | **str** | Source VRF,. | [optional] 
**src_vlan** | **int** | Src VLAN represents the packet&#39;s VLAN tag. | [optional] 
**vnid** | **str** | VXLAN ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


