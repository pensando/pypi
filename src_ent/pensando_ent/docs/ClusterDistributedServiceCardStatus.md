# ClusterDistributedServiceCardStatus

DistributedServiceCardStatus contains current status of a DistributedServiceCard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_sku** | **str** | DSC SKU. | [optional] 
**dsc_version** | **str** | DSC Version. | [optional] 
**adm_phase_reason** | **str** | The reason why the DistributedServiceCard is not in ADMITTED state. | [optional] 
**admission_phase** | **str** | Current admission phase of the DistributedServiceCard. When auto-admission is enabled, AdmissionPhase will be set to NIC_ADMITTED by CMD for validated NICs. When auto-admission is not enabled, AdmissionPhase will be set to NIC_PENDING by CMD for validated NICs since it requires manual approval. To admit the NIC as a part of manual admission, user is expected to set Spec.Admit to true for the NICs that are in NIC_PENDING state. Note : Whitelist mode is not supported yet. | [optional]  if omitted the server will use the default value of "unknown"
**alom_present** | **bool** | ALOMPresent true value indicates ALOM cable is present. | [optional] 
**conditions** | [**[ClusterDSCCondition]**](ClusterDSCCondition.md) | List of current NIC conditions. | [optional] 
**control_plane_status** | [**ClusterDSCControlPlaneStatus**](ClusterDSCControlPlaneStatus.md) |  | [optional] 
**host** | **str** | The name of the host this DistributedServiceCard is plugged into. | [optional] 
**inband_ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**interfaces** | **[str]** | Network Interfaces. | [optional] 
**ip_config** | [**ClusterIPConfig**](ClusterIPConfig.md) |  | [optional] 
**is_connected_to_psm** | **bool** | IsConnectedToPSM is set to true if connected to PSM. | [optional] 
**num_mac_address** | **int** | NumMacAddress has the number of mac addresses that is available on this DSC. Value should be between 0 and 256. | [optional]  if omitted the server will use the default value of 24
**package_type** | **str** | Type of DSC. | [optional]  if omitted the server will use the default value of "dsc"
**primary_mac** | **str** | PrimaryMAC is the MAC address of the primary PF exposed by DistributedServiceCard. Should be a valid MAC address. | [optional] 
**secure_booted** | **bool** | SecureBooted a true value indicates, secure boot is enabled. | [optional] 
**serial_num** | **str** | Serial number. | [optional] 
**system_info** | [**ClusterDSCInfo**](ClusterDSCInfo.md) |  | [optional] 
**unhealthy_services** | **[str]** | Lists the unhealthy services of a distributed service card. | [optional] 
**version_mismatch** | **bool** | Set to true if venice and dsc versions are incompatible. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


