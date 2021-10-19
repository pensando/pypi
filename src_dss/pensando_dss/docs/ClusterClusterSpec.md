# ClusterClusterSpec

ClusterSpec contains the configuration of the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_admit_dscs** | **bool** | AutoAdmitDSCs when enabled auto-admits DSCs that are validated into Venice Cluster. When it is disabled, DSCs validated by CMD are set to Pending state and it requires Manual approval to be admitted into the cluster. | [optional] 
**certs** | **str** | Certs is the pem encoded certificate bundle used for API Gateway TLS. | [optional] 
**key** | **str** | Key is the pem encoded private key used for API Gateway TLS. We support RSA or ECDSA. | [optional] 
**ntp_servers** | **[str]** | NTPServers contains the list of NTP servers for the cluster. | [optional] 
**quorum_nodes** | **[str]** | QuorumNodes contains the list of hostnames for nodes configured to be quorum nodes in the cluster. | [optional] 
**recovery_keys** | [**RecoverykeysRecoveryKeys**](RecoverykeysRecoveryKeys.md) |  | [optional] 
**virtual_ip** | **str** | VirtualIP is the IP address for managing the cluster. It will be hosted by the winner of election between quorum nodes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


