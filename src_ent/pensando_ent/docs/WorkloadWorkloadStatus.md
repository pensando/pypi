# WorkloadWorkloadStatus

Status part of Workload object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Hostname of the server where the workload is currently running. | [optional] 
**interfaces** | [**[WorkloadWorkloadIntfStatus]**](WorkloadWorkloadIntfStatus.md) | Status of all interfaces in the Workload identified by Primary MAC. | [optional] 
**migration_status** | [**WorkloadWorkloadMigrationStatus**](WorkloadWorkloadMigrationStatus.md) |  | [optional] 
**mirror_sessions** | **[str]** | MirrorSessions list of mirror sessions enabled on this workload. | [optional] 
**propagation_status** | [**SecurityPropagationStatus**](SecurityPropagationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


