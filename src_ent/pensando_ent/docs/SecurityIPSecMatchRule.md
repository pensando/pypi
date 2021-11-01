# SecurityIPSecMatchRule

IPSecMatchRule : This is used to select packets to match the IPSec Rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | **[str]** | list of apps objects to which the rule applies to. | [optional] 
**dst_ip_addresses** | **[str]** | outbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;to-ip. | [optional] 
**proto_ports** | [**[SecurityProtoPort]**](SecurityProtoPort.md) | list of (protocol, ports) pairs to which the rule applies to, in addition to apps. | [optional] 
**src_ip_addresses** | **[str]** | inbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;from-ip. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


