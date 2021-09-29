# MonitoringMatchedRequirement

One of the requirement from the expression that was met.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**observed_value** | **str** | The value at which the requirement was met. same as Requirement.value for operator &#x60;Equals&#x60; but could vary for other operators e.g. requirement - CPU;Gt;90 could have a matching value 96. | [optional] 
**operator** | **str** |  | [optional]  if omitted the server will use the default value of "equals"
**values** | **[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


