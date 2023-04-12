# SearchPolicySearchRequest

PolicySearchRequest is input to the security/firewall policy search request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action, e.g. PERMIT, DENY or REJECT/CLEAR, PROTECT_PERMISSIVE or PROTECT_STRICT. | [optional] 
**app** | **str** | App specification,  predefined apps and alg config. | [optional] 
**destination_address** | **str** | Destination Address to be used for NAT policy search, can be either an IP address or IP collection name. | [optional] 
**from_ip_address** | **str** | Inbound ip-address, use any to refer to all ipaddresses eg: 10.1.1.1, any. | [optional] 
**from_workload_group** | **str** | Inbound workload group. | [optional] 
**kinds** | **[str]** | Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy, IPSecPolicy or NATPolicy. | [optional] 
**name** | **str** | Name is optional. If provided policy-search will be limited to the specified policy of the given name on the given kind. If empty, then all the policies of the given kind will be searched. | [optional] 
**namespace** | **str** | Namespace is optional. If provided policy-search will be limited to the specified namespace. | [optional]  if omitted the server will use the default value of "default"
**port** | **str** | TCP or UDP Port number. | [optional] 
**protocol** | **str** | Protocol eg: tcp, udp, icmp. | [optional] 
**source_address** | **str** | NAT policy related fields Source Address to be used for NAT policy search, can be either an IP address or IP collection name. | [optional] 
**tenant** | **str** | Tenant Name, to perform query within a Tenant&#39;s scope. The default tenant is \&quot;default\&quot;. In the backend this field gets auto-filled &amp; validated by apigw-hook based on user login context. | [optional]  if omitted the server will use the default value of "default"
**to_ip_address** | **str** | Outbound ip-address, use any to refer to all ipaddresses eg: 20.1.1.1, any. | [optional] 
**to_workload_group** | **str** | Outbound workload group. | [optional] 
**translated_destination_address** | **str** | Translated Destination Address to be used for NAT policy search, can be either an IP address or IP collection name. | [optional] 
**translated_destination_port** | **str** | Translated Destination Port to be use for NAT policy search. | [optional] 
**translated_source_address** | **str** | Translated Source Address to be used for NAT policy search, can be either an IP address or IP collection name. | [optional] 
**virtual_routers** | **[str]** | VirtualRouters to be use for searching Security Policy / IPSec Policy / NAT Policy based on VRF association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


