# WorkloadWorkloadSpec

Spec part of Workload object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Hostname of the server where the workload should be running. | [optional] 
**interfaces** | [**[WorkloadWorkloadIntfSpec]**](WorkloadWorkloadIntfSpec.md) | Spec of all interfaces in the Workload identified by Primary MAC. | [optional] 
**migration_timeout** | **str** | Should be a valid time duration. | [optional]  if omitted the server will use the default value of "3m"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


