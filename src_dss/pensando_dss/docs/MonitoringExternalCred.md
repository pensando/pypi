# MonitoringExternalCred

ExternalCred defines credentials required to access an external entity, such as a stats collector, compute orchestration entity, or a syslog server. External entity may support a variety of methods, like username/password, TLS Client authentication, or Bearer Token based authentication. User is expected to configure one of the methods.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | AuthType is the authentication type used in this config. | [optional]  if omitted the server will use the default value of "none"
**bearer_token** | **str** | External entity supports bearer tokens for authentication and authorization Token refresh is not supported using OAuth2. | [optional] 
**ca_data** | **str** | CaData holds PEM-encoded bytes (typically read from a root certificates bundle). CaData is used by client to autheticate external server. This is applicable to all authentication methods. | [optional] 
**cert_data** | **str** | CertData holds PEM-encoded bytes (typically read from a client certificate file). | [optional] 
**disable_server_authentication** | **bool** | DisableServerAuthentication flag can be used when a client does not want to authenticate a server. | [optional] 
**key_data** | **str** | KeyData holds PEM-encoded bytes (typically read from a client certificate key file). | [optional] 
**password** | **str** | Password is one time specified, not visibile on read operations Only valid when UserName is defined. | [optional] 
**username** | **str** | UserName is the login id to be used towards the external entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


