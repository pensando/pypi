# MonitoringMirrorSessionSpec

MirrorSessionSpec.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectors** | [**[MonitoringMirrorCollector]**](MonitoringMirrorCollector.md) | Mirrored packet collectors. | [optional] 
**disabled** | **bool** | Enable/disable mirroring. | [optional] 
**interfaces** | [**MonitoringInterfaceMirror**](MonitoringInterfaceMirror.md) |  | [optional] 
**match_rules** | [**[MonitoringMatchRule]**](MonitoringMatchRule.md) | Traffic Selection Rules - Matching pakcets are mirrored, based on packet filters and start/stop conditions. | [optional] 
**packet_filters** | **[str]** |  | [optional] 
**packet_size** | **int** | PacketSize: Max size of a mirrored packet, packet size is not checked by default. Value should be between 64 and 2048. | [optional] 
**source** | [**MonitoringMirrorSource**](MonitoringMirrorSource.md) |  | [optional] 
**span_id** | **int** | Value should be between 1 and 1023. | [optional]  if omitted the server will use the default value of 1
**start_condition** | [**MonitoringMirrorStartConditions**](MonitoringMirrorStartConditions.md) |  | [optional] 
**workloads** | [**MonitoringWorkloadMirror**](MonitoringWorkloadMirror.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


