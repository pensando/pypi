# MonitoringInstanceSelector

Helps to select/filter instances of a kind. If instance selector is not given, then the policy will be applied across all DSCs or Nodes based on the metric identifier. If kind was given, then either names or label or both have to be specified. If the user specified both names and label, policies will be applied on the union of both. Allowed list of kinds: Node, DistributedServiceCard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind of the instances to be selected using names/label. | [optional] 
**labels** | [**LabelsSelector**](LabelsSelector.md) |  | [optional] 
**names** | **[str]** | List of names/reporter IDs. | [optional] 
**rule_names** | **[str]** | List of rule-names that the policy applies to when given. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


