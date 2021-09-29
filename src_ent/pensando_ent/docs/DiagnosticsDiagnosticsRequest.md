# DiagnosticsDiagnosticsRequest

DiagnosticsRequest sends a diagnostics request to the service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**parameters** | **{str: (str,)}** | Parameters to be passed for a diagnostic query. | [optional] 
**query** | **str** | Query is type of diagnostic information requested like Profile, Log. This string is service specific and meaning is assigned by the service. | [optional] 
**service_port** | [**DiagnosticsServicePort**](DiagnosticsServicePort.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


