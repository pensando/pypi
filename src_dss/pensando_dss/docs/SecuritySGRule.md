# SecuritySGRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | SGRule action, either PERMIT, DENY or REJECT. | [optional]  if omitted the server will use the default value of "permit"
**apps** | **[str]** | list of apps objects to which the rule applies to. | [optional] 
**description** | **str** | describes rule. Length of string should be between 0 and 256. | [optional] 
**disable** | **bool** | is rule disabled. | [optional] 
**from_ip_addresses** | **[str]** | inbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;from-ip. | [optional] 
**from_ipcollections** | **[str]** | inbound rule from a given ipcollection. | [optional] 
**from_workload_groups** | **[str]** | inbound rule from a given workload group. | [optional] 
**name** | **str** | rule name. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 0 and 128. | [optional] 
**proto_ports** | [**[SecurityProtoPort]**](SecurityProtoPort.md) | list of (protocol, ports) pairs to which the rule applies to, in addition to apps. | [optional] 
**to_ip_addresses** | **[str]** | outbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;to-ip. | [optional] 
**to_ipcollections** | **[str]** | outbound rule from a given ipcollection. | [optional] 
**to_workload_groups** | **[str]** | outbound rule from a given workload group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


