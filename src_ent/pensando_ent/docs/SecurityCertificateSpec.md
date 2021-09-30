# SecurityCertificateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body of the certificate in PEM encoding. | [optional] 
**description** | **str** | Description of the purpose of this certificate. | [optional] 
**trust_chain** | **str** | Trust chain of the certificate in PEM encoding. These certificates are treated opaquely. We do not process them in any way other than decoding them for informational purposes. | [optional] 
**usages** | **[str]** | Usage can be \&quot;client\&quot;, \&quot;server\&quot; or \&quot;trust-root\&quot; in any combination. A \&quot;server\&quot; certificate is used by a server to authenticate itself to the client A \&quot;client\&quot; certificate is used by a client to authenticate itself to a server A \&quot;trust-root\&quot; certificate is self-signed and is only used to validate certificates presented by peers. \&quot;client\&quot; and \&quot;server\&quot; certificates are always accompanied by a private key, whereas \&quot;trust-root\&quot;-only certificates are not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


