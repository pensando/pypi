# WorkloadWorkloadMigrationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** | migration completion time. | [optional] 
**flow_migration_status** | [**[WorkloadInterfaceMigrationStatus]**](WorkloadInterfaceMigrationStatus.md) | Interface migration status. | [optional] 
**migration_id** | **str** | ID of the endpoints migration object. | [optional] 
**stage** | **str** | Controller&#39;s migration stage. | [optional]  if omitted the server will use the default value of "migration-none"
**started_at** | **datetime** | migration start time. | [optional] 
**status** | **str** | The status from the dataplane performing migration. | [optional]  if omitted the server will use the default value of "none"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


