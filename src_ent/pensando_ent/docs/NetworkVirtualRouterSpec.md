# NetworkVirtualRouterSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ipam_policy** | **str** | Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. | [optional] 
**route_import_export** | [**NetworkRDSpec**](NetworkRDSpec.md) |  | [optional] 
**router_mac_address** | **str** | Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. | [optional] 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "unknown"
**vxlan_vni** | **int** | VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


