# AuthTLSOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | ServerName is used to verify the hostname on the returned certificates unless SkipServerCertVerification is true. | [optional] 
**skip_server_cert_verification** | **bool** | SkipServerCertVerification controls whether a client verifies the server&#39;s certificate chain and host name. If SkipServerCertVerification is true, TLS accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. This should be used only for testing. | [optional] 
**start_tls** | **bool** | StartTLS determines if ldap connection uses TLS. | [optional] 
**trusted_certs** | **str** | TrustedCerts defines the set of PEM encoded root certificate authorities that will be used when verifying server certificates. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


