# MonitoringAlertStatus

Status part of the alert object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | [**MonitoringAuditInfo**](MonitoringAuditInfo.md) |  | [optional] 
**event_uri** | **str** | Event that triggered the alert. | [optional] 
**message** | **str** | Message from the alert rule that triggered the alert. | [optional] 
**object_ref** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 
**reason** | [**MonitoringAlertReason**](MonitoringAlertReason.md) |  | [optional] 
**resolved** | [**MonitoringAuditInfo**](MonitoringAuditInfo.md) |  | [optional] 
**severity** | **str** | Severity of an alert. | [optional]  if omitted the server will use the default value of "info"
**source** | [**MonitoringAlertSource**](MonitoringAlertSource.md) |  | [optional] 
**total_hits** | **int** | TotalHits on this alert, If there is an exisiting alert for the condition, we do not re-create the alert instead we update this counter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


