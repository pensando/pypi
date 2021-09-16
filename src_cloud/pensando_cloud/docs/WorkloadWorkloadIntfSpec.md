# WorkloadWorkloadIntfSpec

Spec of a Workload interface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_interfaces** | **[str]** | List of all DSC interfaces that can be used. The DSC interface is identified using the MAC address assigned to the DSC port. If not specified, DSCs from workload&#39;s host object are used. | [optional] 
**external_vlan** | **int** | External vlan assigned for this interface. Value should be between 0 and 4095. | [optional] 
**ip_addresses** | **[str]** | List of all IP addresses configured on a Workload Interface. | [optional] 
**mac_address** | **str** | MACAddress contains the MAC address of the interface as seen by the workload. Should be a valid MAC address. | [optional] 
**micro_seg_vlan** | **int** | Micro-segmentation vlan assigned for this interface. Value should be between 0 and 4095. | [optional] 
**network** | **str** | Network this interface will belong to. | [optional] 
**vni** | **int** | vni is network identifier when the interface uses tunneling protocols, 0 &#x3D; not used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


