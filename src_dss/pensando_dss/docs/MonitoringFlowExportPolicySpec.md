# MonitoringFlowExportPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Enable/disable flow export. Not supported for DSS. | [optional] 
**exports** | [**[MonitoringExportConfig]**](MonitoringExportConfig.md) | Export contains export parameters. | [optional] 
**format** | **str** |  | [optional]  if omitted the server will use the default value of "ipfix"
**interval** | **str** | Interval defines how often to push the records to an external collector The value is specified as a string format, &#39;10s&#39;, &#39;20m&#39;. Should be a valid time duration between 1s and 24h0m0s. | [optional]  if omitted the server will use the default value of "10s"
**match_rules** | [**[MonitoringMatchRule]**](MonitoringMatchRule.md) |  | [optional] 
**template_interval** | **str** | TemplateInterval defines how often to send ipfix templates to an external collector The value is specified as a string format, &#39;1m&#39;, &#39;10m&#39;. Should be a valid time duration between 1m0s and 30m0s. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


