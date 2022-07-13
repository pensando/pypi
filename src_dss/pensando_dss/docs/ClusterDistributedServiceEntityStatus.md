# ClusterDistributedServiceEntityStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_sku** | **str** |  | [optional] 
**dsc_version** | **str** |  | [optional] 
**adm_phase_reason** | **str** |  | [optional] 
**admission_phase** | **str** |  | [optional]  if omitted the server will use the default value of "unknown"
**alom_present** | **bool** |  | [optional] 
**conditions** | [**[ClusterDSCCondition]**](ClusterDSCCondition.md) |  | [optional] 
**control_plane_status** | [**ClusterDSCControlPlaneStatus**](ClusterDSCControlPlaneStatus.md) |  | [optional] 
**dss_info** | [**ClusterDSSInfo**](ClusterDSSInfo.md) |  | [optional] 
**host** | **str** |  | [optional] 
**inband_ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**interfaces** | **[str]** |  | [optional] 
**ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**is_connected_to_psm** | **bool** |  | [optional] 
**num_mac_address** | **int** | Value should be between 0 and 256. | [optional]  if omitted the server will use the default value of 24
**package_type** | **str** |  | [optional]  if omitted the server will use the default value of "dsc"
**primary_mac** | **str** | Should be a valid MAC address. | [optional] 
**secure_booted** | **bool** |  | [optional] 
**security_policy_rule_scale_profile** | **str** |  | [optional] 
**serial_num** | **str** |  | [optional] 
**system_info** | [**ClusterDSCInfo**](ClusterDSCInfo.md) |  | [optional] 
**unhealthy_services** | **[str]** |  | [optional] 
**version_mismatch** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


