# WorkloadWorkloadIntfStatus

Status of a Workload interface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_interfaces** | **[str]** | List of all DSC interfaces that can be used. The DSC interface is identified using the MAC address assigned to the DSC port. | [optional] 
**endpoint** | **str** | Endpoint associated with this Workload interface. | [optional] 
**external_vlan** | **int** | External vlan assigned for this interface. | [optional] 
**ip_addresses** | **[str]** | List of all IP addresses configured and discovered on a Workload Interface. | [optional] 
**mac_address** | **str** | MACAddress contains the MAC address of the interface as seen by the workload. | [optional] 
**micro_seg_vlan** | **int** | Micro-segmentation vlan used by this interface. | [optional] 
**network** | **str** | Network this interface belongs to. | [optional] 
**pending_workload_groups** | **[str]** | WorkloadGroups list of workload groups unassociated with this workload. | [optional] 
**vni** | **int** | vni is network identifier when the interface uses tunneling protocols, 0 &#x3D; not used. | [optional] 
**workload_groups** | **[str]** | WorkloadGroups list of workload groups associated with this workload. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


