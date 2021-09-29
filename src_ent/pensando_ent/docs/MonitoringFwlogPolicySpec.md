# MonitoringFwlogPolicySpec

Venice collects fwlog irrespective of the export config.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**MonitoringSyslogExportConfig**](MonitoringSyslogExportConfig.md) |  | [optional] 
**filter** | **[str]** | filter firewall logs, FWLOG_ALL default. | [optional] 
**format** | **str** | fwlog format, SYSLOG_BSD default. | [optional]  if omitted the server will use the default value of "syslog-bsd"
**psm_target** | [**MonitoringPSMExportTarget**](MonitoringPSMExportTarget.md) |  | [optional] 
**targets** | [**[MonitoringExportConfig]**](MonitoringExportConfig.md) | Target contains ip/port/protocol. | [optional] 
**vrf_name** | **str** | VrfName specifies the name of the VRF that the current Firewall Log Policy belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


