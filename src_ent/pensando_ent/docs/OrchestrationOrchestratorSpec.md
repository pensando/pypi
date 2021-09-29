# OrchestrationOrchestratorSpec

OrchestratorSpec contains the configuration of the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**MonitoringExternalCred**](MonitoringExternalCred.md) |  | [optional] 
**namespaces** | [**[OrchestrationNamespaceSpec]**](OrchestrationNamespaceSpec.md) | Namespaces are used to provide namespace specific information. From Rel-C this will be the only means to pass namespace information \&quot;all_namespaces\&quot; will be treated as a special namespace, which will apply the same configuration for all the namespaces discovered by the orchestrator. | [optional] 
**type** | **str** | Type of orchestrator. | [optional]  if omitted the server will use the default value of "vcenter"
**uri** | **str** | URI of the orchestrator. Length of string should be at least 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


