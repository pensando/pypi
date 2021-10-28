# MonitoringArchiveQuery

ArchiveQuery is to archive audit logs and events based on time window, field values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional] 
**fields** | [**FieldsSelector**](FieldsSelector.md) |  | [optional] 
**labels** | [**LabelsSelector**](LabelsSelector.md) |  | [optional] 
**start_time** | **datetime** | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional] 
**tenants** | **[str]** | OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. | [optional] 
**texts** | [**[SearchTextRequirement]**](SearchTextRequirement.md) | OR of Text-requirements to be matched, Exclude is not supported for Text search. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


