# MonitoringEventPolicySpec

EventPolicySpec is the specification of an Event Policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**MonitoringSyslogExportConfig**](MonitoringSyslogExportConfig.md) |  | [optional] 
**format** | **str** | event export format, SYSLOG_BSD default. | [optional]  if omitted the server will use the default value of "syslog-bsd"
**selector** | [**FieldsSelector**](FieldsSelector.md) |  | [optional] 
**targets** | [**[MonitoringExportConfig]**](MonitoringExportConfig.md) | export target ip/port/protocol. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


