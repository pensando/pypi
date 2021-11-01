# NetworkTLSClientPolicySpec

Service TLS configuration for connections initiated by the workload towards destinations inside or outside the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls_client_allowed_peer_id** | **[str]** | Valid DNS names or IP addresses that must appear in the server certificate SubjAltName or Common Name (if SAN is not specified). If not specified, client validates the IP address of the server. | [optional] 
**tls_client_certificates_selector** | **{str: (str,)}** | A map containing the certificate to use for a set of destinations. The key is a selector for workloads that exist either inside or outside the cluster. It can be based on labels, hostnames or \&quot;IP:port\&quot; pairs. The value is the name of the certificate to use for the selected destinations. The certificates \&quot;usage\&quot; field must contain \&quot;client\&quot;. TODO: replace the first \&quot;string\&quot; type with proper selector type when available. A single \&quot;default\&quot; certificate which matches all destinations is allowed. If a destination matches multiple non-default map keys, an error is returned. If a destination does not match any map key (and there is no default), the outbound connection is initiated without TLS. | [optional] 
**tls_client_trust_roots** | **[str]** | The list of root certificates used to validate a trust chain presented by a server. If the list is empty, all roots certificates in the tenant scope are considered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


