# ClusterDistributedServiceEntitySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admit** | **bool** |  | [optional] 
**controllers** | **[str]** |  | [optional] 
**dscprofile** | **str** |  | [optional] 
**enable_secure_boot** | **bool** |  | [optional]  if omitted the server will use the default value of False
**flow_export_policy** | [**[ClusterFlowExportPolicyRef]**](ClusterFlowExportPolicyRef.md) |  | [optional] 
**fwlog_policy** | [**ClusterFwlogPolicyRef**](ClusterFwlogPolicyRef.md) |  | [optional] 
**id** | **str** |  | [optional] 
**ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**mgmt_mode** | **str** |  | [optional]  if omitted the server will use the default value of "host"
**mgmt_vlan** | **int** | Value should be between 0 and 4095. | [optional] 
**network_mode** | **str** |  | [optional]  if omitted the server will use the default value of "oob"
**policer** | [**ClusterPolicerRef**](ClusterPolicerRef.md) |  | [optional] 
**routing_config** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


