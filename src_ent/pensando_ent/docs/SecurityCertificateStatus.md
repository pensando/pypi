# SecurityCertificateStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validity** | **str** | Status of the certificate: \&quot;valid\&quot;, \&quot;invalid\&quot;, \&quot;expired\&quot; \&quot;invalid\&quot; means that the signature of the certificate does not match or there are inconsistencies in the trust chain. | [optional]  if omitted the server will use the default value of "unknown"
**workloads** | **[str]** | The workloads where this certificate has been deployed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


