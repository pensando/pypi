# OrchestrationNamespaceSpec

NamespaceSpec contains the namespace specification.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_spec** | [**OrchestrationManagedNamespaceSpec**](OrchestrationManagedNamespaceSpec.md) |  | [optional] 
**mode** | **str** |  | [optional]  if omitted the server will use the default value of "managed"
**monitored_spec** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | MonitoredNamespaceSpec contains namespace specific configuration. | [optional] 
**name** | **str** | Length of string should be at least 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


