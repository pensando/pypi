# LabelsRequirement

Requirement defines a single matching condition for a selector.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key that the condition applies to. | [optional] 
**operator** | **str** | Condition checked for the key. | [optional]  if omitted the server will use the default value of "equals"
**values** | **[str]** | Values contains one or more values corresponding to the label key. \&quot;equals\&quot; and \&quot;notEquals\&quot; operators need a single Value. \&quot;in\&quot; and \&quot;notIn\&quot; operators can have one or more values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


