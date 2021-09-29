# MonitoringMirrorCollector

Mirror collector - can be an external device (via ERSPAN) or Venice (internal packet capture).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_config** | [**MonitoringMirrorExportConfig**](MonitoringMirrorExportConfig.md) |  | [optional] 
**strip_vlan_hdr** | **bool** | remove vlan from mirror packet. | [optional] 
**type** | **str** | Type of Collector. | [optional]  if omitted the server will use the default value of "erspan_type_3"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


