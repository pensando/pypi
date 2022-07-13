# NetworkVirtualRouterSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ipam_policy** | **str** | Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. | [optional] 
**egress_security_policy** | **[str]** | Security Policy to apply in the egress direction. | [optional] 
**flow_export_policy** | **[str]** | FlowExportPolicy is the flow export policy associated to this virtual router. | [optional] 
**ingress_security_policy** | **[str]** | Security Policy to apply in the ingress direction. | [optional] 
**maximum_cps_per_network_per_distributed_services_entity** | **int** | Maximum Connections Per Second supported for any Network belonging to the Virtual Router within a Distributed Services Entity. Valid values 0 no limit and 1000 &lt;&#x3D; maxcps  &lt;&#x3D; 1000000 The value configured here is the CPS limit enforced per Network within a Distributed Services Entity and is the same for all Networks within the Virtual Router. However the value can be overriden at Network level. Value 0 means the CPS limit is not enforced and the CPS is limited only by the system capacity. All new connections exceeding the CPS limit are dropped. Value should be between 0 and 1000000. | [optional] 
**maximum_sessions_per_network_per_distributed_services_entity** | **int** | Maximum sessions supported in any Network belonging to the Virtual Router within a Distributed Services Entity. Valid values 0 (no limit) and 10000  &lt;&#x3D; maxsessions &lt;&#x3D; 5000000 The value configured here is the sessions limit enforced per Network within a Distributed Services Entity and is the same for all Networks within the Virtual Router. However the value can be overriden at Network level. Value 0 means the sessions limit is not enforced and the number of sessions is limited only by the system capacity. Sessions exceeding the sessions limit are dropped. NOTE: no active sessions will be pruned if the value changes, but until the session count comes down to a value below this limit, new sessions won&#39;t be installed in h/w (packet will be dropped) 1 session &#x3D; forward flow + reverse flow. Value should be between 0 and 5000000. | [optional] 
**route_import_export** | [**NetworkRDSpec**](NetworkRDSpec.md) |  | [optional] 
**router_mac_address** | **str** | Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. | [optional] 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "unknown"
**vxlan_vni** | **int** | VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


