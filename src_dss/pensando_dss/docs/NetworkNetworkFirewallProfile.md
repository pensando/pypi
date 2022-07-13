# NetworkNetworkFirewallProfile

Firewall features that can be enabled on the network.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_cps_per_distributed_services_entity** | **int** | Maximum Connections Per Second supported for the Network within a Distributed Services Entity. Valid values -1 (inherit VPC config)  0 no limit and 1000 &lt;&#x3D; maxcps &lt;&#x3D; 1000000 Value 0 means the CPS limit is not enforced at network level and overrides any setting at VPC level. Value -1 means the CPS limit is not set (no config) and the network will inherit whatever is set at VPC level will be inherited. All new connections exceeding the CPS limit are dropped. Value should be between -1 and 1000000. | [optional]  if omitted the server will use the default value of -1
**maximum_sessions_per_distributed_services_entity** | **int** | Maximum sessions supported in the Network within a Distributed Services Entity. Valid values -1 (inherit VPC config)  0 (no limit) and 10000 &lt;&#x3D; maxsessions &lt;&#x3D; 5000000 Value 0 means the Sessions limit is not enforced at network level and overrides any setting at VPC level. Value -1 means the Sessions limit is not set (no config) and the network will inherit whatever is set at VPC level will be inherited. Sessions exceeding the sessions limit are dropped. NOTE: no active sessions will be pruned if the value changes, but until the session count comes down to a value below this limit, new sessions won&#39;t be installed in h/w (packet will be dropped) 1 session &#x3D; forward flow + reverse flow. Value should be between -1 and 5000000. | [optional]  if omitted the server will use the default value of -1

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


