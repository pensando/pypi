# AuthAuthenticationPolicySpec

spec part of authentication policy object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticators** | [**AuthAuthenticators**](AuthAuthenticators.md) |  | [optional] 
**secret** | **str** | Secret used to sign JWT token. | [optional] 
**token_expiry** | **str** | TokenExpiry is time duration after which JWT token expires. Default is 6 days. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Should be a valid time duration. | [optional]  if omitted the server will use the default value of "144h"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


