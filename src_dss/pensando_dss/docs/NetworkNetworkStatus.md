# NetworkNetworkStatus

status part of network object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_ipv4_addrs** | **str** | allocated IPv4 addresses (bitmap). | [optional] 
**id** | **str** | Handle is the internal Handle allocated to this network. | [optional] 
**oper_state** | **str** |  | [optional]  if omitted the server will use the default value of "active"
**propagation_status** | [**SecurityPropagationStatus**](SecurityPropagationStatus.md) |  | [optional] 
**security_policy_status** | [**NetworkSecurityPolicyStatus**](NetworkSecurityPolicyStatus.md) |  | [optional] 
**workloads** | **[str]** | list of all workloads in this network. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


