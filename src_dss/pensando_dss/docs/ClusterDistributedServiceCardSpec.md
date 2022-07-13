# ClusterDistributedServiceCardSpec

DistributedServiceCardSpec contains configuration of the DistributedServiceCard (Naples I/O subsystem).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admit** | **bool** | Admit allows a DistributedServiceCard to join the cluster. | [optional] 
**controllers** | **[str]** | Controllers contains the list of remote controllers IP addresses or hostnames. | [optional] 
**dscprofile** | **str** |  | [optional] 
**enable_secure_boot** | **bool** | EnableSecureBoot a true value indicates, set lifecycle fuse to enable secure boot. | [optional]  if omitted the server will use the default value of False
**flow_export_policy** | [**[ClusterFlowExportPolicyRef]**](ClusterFlowExportPolicyRef.md) | FlowExportPolicy is the configuration for flow export policy. | [optional] 
**fwlog_policy** | [**ClusterFwlogPolicyRef**](ClusterFwlogPolicyRef.md) |  | [optional] 
**id** | **str** | ID is used as a user friendly identifier in logs/events. | [optional] 
**ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**mgmt_mode** | **str** | MgmtMode defines the management mode of the DistributedServiceCard. | [optional]  if omitted the server will use the default value of "host"
**mgmt_vlan** | **int** | MgmtVlan defines the vlan to be used in network managed mode. The default of 0 means we use untagged-vlan for doing inband management. Value should be between 0 and 4095. | [optional] 
**network_mode** | **str** | MgmtMode defines the management mode of the DistributedServiceCard. | [optional]  if omitted the server will use the default value of "oob"
**policer** | [**ClusterPolicerRef**](ClusterPolicerRef.md) |  | [optional] 
**routing_config** | **str** | RoutingConfig is the routing configuration for the underlay routed network that this DSC participates in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


