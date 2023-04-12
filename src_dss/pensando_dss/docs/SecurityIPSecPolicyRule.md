# SecurityIPSecPolicyRule

Applies to East-West Traffic only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | IPSec action Type for  all traffic that matches the MatchRule. This policy rule, either CLEAR or PROTECT. | [optional]  if omitted the server will use the default value of "clear"
**description** | **str** | Describes rule. Length of string should be between 0 and 256. | [optional] 
**match_rule** | [**SecurityIPSecMatchRule**](SecurityIPSecMatchRule.md) |  | [optional] 
**name** | **str** | rule name. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 0 and 64. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


