# SysruntimeConnectionFilter

ConnectionFilter filter to be applied for the query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**SysruntimeWorkloadSelector**](SysruntimeWorkloadSelector.md) |  | [optional] 
**destination_port** | **int** | destination port to be matched. Value should be between 1 and 65535. | [optional] 
**protocol** | **str** | protocol to be matched. | [optional]  if omitted the server will use the default value of "none"
**source** | [**SysruntimeWorkloadSelector**](SysruntimeWorkloadSelector.md) |  | [optional] 
**source_port** | **int** | source port to be matched. Value should be between 1 and 65535. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


