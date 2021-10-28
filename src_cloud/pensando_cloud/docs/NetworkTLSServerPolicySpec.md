# NetworkTLSServerPolicySpec

The Service TLS configuration for inbound connections. It is used on all ports specified in the Service spec. Multiple Service objects can select the same workload and provide different server TLS configurations for disjoint sets of ports.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_authentication** | **str** | Client authentication \&quot;None\&quot; means that server does not request and will not validate a client certificate. \&quot;Mandatory\&quot; means that server requests and validates client certificate. \&quot;Optional\&quot; means that server requests client certificate but proceeds even if client does not present it. Default is \&quot;Mandatory\&quot;. | [optional]  if omitted the server will use the default value of "mandatory"
**tls_server_allowed_peer_id** | **[str]** | Valid DNS names or IP addresses that must appear in the client certificate SubjAltName or Common Name (if SAN is not specified). If client auth is enabled and AllowedPeerId is not specified, server accepts any client certificate as long as it is valid  (not expired and with a valid trust chain). | [optional] 
**tls_server_certificates** | **[str]** | List of names of certificates to present to clients. The certificates \&quot;usage\&quot; field must contain \&quot;server\&quot;. If multiple certificates names are provided, system tries to choose the correct one using SNI, otherwise it picks the first one in the list. | [optional] 
**tls_server_trust_roots** | **[str]** | The list of root certificates used to validate a trust chain presented by client. If the list is empty, all roots certificates in the tenant scope are considered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


