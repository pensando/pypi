# SecurityIPsecSAParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dh_groups** | **[str]** |  | [optional] 
**encryption_algorithms** | **[str]** | Currently, only AES-GCM-128 and AES-GCM-256 are supported. | [optional] 
**rekey_lifetime** | **str** | RekeyLifetime is time duration after which fresh cryptographic keys are created for IPsec SA. Default is 1 hour. Empty value disables re-keying. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;1h\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Should be a valid time duration between 15m0s and 24h0m0s. | [optional]  if omitted the server will use the default value of "1h"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


