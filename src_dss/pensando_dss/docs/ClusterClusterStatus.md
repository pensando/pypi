# ClusterClusterStatus

ClusterStatus contains the current state of the Cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_bootstrapped** | **bool** | AuthBootstrapped indicates whether the Cluster has Completed BootStrap of Auth. | [optional] 
**conditions** | [**[ClusterClusterCondition]**](ClusterClusterCondition.md) | List of current cluster conditions. | [optional] 
**current_time** | **datetime** | CurrentTime is current time of a cluster. | [optional] 
**last_leader_transition_time** | **datetime** | LastLeaderTransitionTime is when the leadership changed last time. | [optional] 
**leader** | **str** | Leader contains the node name of the cluster leader. | [optional] 
**public_key** | **str** | PublicKey is the pem encoded public key created by CMD during cluster creation. | [optional] 
**quorum_status** | [**ClusterQuorumStatus**](ClusterQuorumStatus.md) |  | [optional] 
**recovery_keys_downloaded** | **bool** | RecoveryKeysDownloaded indicates whether keys have been downloaded since the cluster has been bootstrapped. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


