# WorkloadWorkloadGroupSpec

Spec part of WorkloadGroup object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_block** | [**[WorkloadIPBlock]**](WorkloadIPBlock.md) | IP Block selector for entities outside of cluster if used alone When used in conjuction with WorkloadSelector, The Workload selected based on LabelSelector or if IPAddress is part of the IPBlock entries Each IPBlock are ORed. | [optional] 
**workload_selector** | [**[LabelsSelector]**](LabelsSelector.md) | Workload selector is a list of label selectors. Each WorkloadSelector are ORed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


