
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClusterV1Api* | [**add_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#add_configuration_snapshot) | **POST** /configs/cluster/v1/config-snapshot | Create ConfigurationSnapshot object
*ClusterV1Api* | [**add_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#add_dsc_profile) | **POST** /configs/cluster/v1/dscprofiles | Create DSCProfile object
*ClusterV1Api* | [**add_host**](../../../../pensando_ent/docs/ClusterV1Api.md#add_host) | **POST** /configs/cluster/v1/hosts | Create Host object
*ClusterV1Api* | [**add_license**](../../../../pensando_ent/docs/ClusterV1Api.md#add_license) | **POST** /configs/cluster/v1/licenses | Create License object
*ClusterV1Api* | [**add_node**](../../../../pensando_ent/docs/ClusterV1Api.md#add_node) | **POST** /configs/cluster/v1/nodes | Create Node object
*ClusterV1Api* | [**add_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#add_tenant) | **POST** /configs/cluster/v1/tenants | Create Tenant object
*ClusterV1Api* | [**auth_bootstrap_complete**](../../../../pensando_ent/docs/ClusterV1Api.md#auth_bootstrap_complete) | **POST** /configs/cluster/v1/cluster/AuthBootstrapComplete | Mark bootstrapping as complete for the cluster
*ClusterV1Api* | [**delete_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_configuration_snapshot) | **DELETE** /configs/cluster/v1/config-snapshot | Delete ConfigurationSnapshot object
*ClusterV1Api* | [**delete_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_distributed_service_card) | **DELETE** /configs/cluster/v1/distributedservicecards/{O.Name} | Delete DistributedServiceCard object
*ClusterV1Api* | [**delete_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_dsc_profile) | **DELETE** /configs/cluster/v1/dscprofiles/{O.Name} | Delete DSCProfile object
*ClusterV1Api* | [**delete_host**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_host) | **DELETE** /configs/cluster/v1/hosts/{O.Name} | Delete Host object
*ClusterV1Api* | [**delete_node**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_node) | **DELETE** /configs/cluster/v1/nodes/{O.Name} | Delete Node object
*ClusterV1Api* | [**delete_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#delete_tenant) | **DELETE** /configs/cluster/v1/tenants/{O.Name} | Delete Tenant object
*ClusterV1Api* | [**get_cluster**](../../../../pensando_ent/docs/ClusterV1Api.md#get_cluster) | **GET** /configs/cluster/v1/cluster | Get Cluster object
*ClusterV1Api* | [**get_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#get_configuration_snapshot) | **GET** /configs/cluster/v1/config-snapshot | Get ConfigurationSnapshot object
*ClusterV1Api* | [**get_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#get_distributed_service_card) | **GET** /configs/cluster/v1/distributedservicecards/{O.Name} | Get DistributedServiceCard object
*ClusterV1Api* | [**get_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#get_dsc_profile) | **GET** /configs/cluster/v1/dscprofiles/{O.Name} | Get DSCProfile object
*ClusterV1Api* | [**get_host**](../../../../pensando_ent/docs/ClusterV1Api.md#get_host) | **GET** /configs/cluster/v1/hosts/{O.Name} | Get Host object
*ClusterV1Api* | [**get_license**](../../../../pensando_ent/docs/ClusterV1Api.md#get_license) | **GET** /configs/cluster/v1/licenses | Get License object
*ClusterV1Api* | [**get_node**](../../../../pensando_ent/docs/ClusterV1Api.md#get_node) | **GET** /configs/cluster/v1/nodes/{O.Name} | Get Node object
*ClusterV1Api* | [**get_snapshot_restore**](../../../../pensando_ent/docs/ClusterV1Api.md#get_snapshot_restore) | **GET** /configs/cluster/v1/config-restore | Get SnapshotRestore object
*ClusterV1Api* | [**get_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#get_tenant) | **GET** /configs/cluster/v1/tenants/{O.Name} | Get Tenant object
*ClusterV1Api* | [**get_version**](../../../../pensando_ent/docs/ClusterV1Api.md#get_version) | **GET** /configs/cluster/v1/version | Get Version object
*ClusterV1Api* | [**label_cluster**](../../../../pensando_ent/docs/ClusterV1Api.md#label_cluster) | **POST** /configs/cluster/v1/cluster/label | Label Cluster object
*ClusterV1Api* | [**label_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#label_configuration_snapshot) | **POST** /configs/cluster/v1/config-snapshot/label | Label ConfigurationSnapshot object
*ClusterV1Api* | [**label_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#label_distributed_service_card) | **POST** /configs/cluster/v1/distributedservicecards/{O.Name}/label | Label DistributedServiceCard object
*ClusterV1Api* | [**label_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#label_dsc_profile) | **POST** /configs/cluster/v1/dscprofiles/{O.Name}/label | Label DSCProfile object
*ClusterV1Api* | [**label_host**](../../../../pensando_ent/docs/ClusterV1Api.md#label_host) | **POST** /configs/cluster/v1/hosts/{O.Name}/label | Label Host object
*ClusterV1Api* | [**label_license**](../../../../pensando_ent/docs/ClusterV1Api.md#label_license) | **POST** /configs/cluster/v1/licenses/label | Label License object
*ClusterV1Api* | [**label_node**](../../../../pensando_ent/docs/ClusterV1Api.md#label_node) | **POST** /configs/cluster/v1/nodes/{O.Name}/label | Label Node object
*ClusterV1Api* | [**label_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#label_tenant) | **POST** /configs/cluster/v1/tenants/{O.Name}/label | Label Tenant object
*ClusterV1Api* | [**list_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#list_distributed_service_card) | **GET** /configs/cluster/v1/distributedservicecards | List DistributedServiceCard objects
*ClusterV1Api* | [**list_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#list_dsc_profile) | **GET** /configs/cluster/v1/dscprofiles | List DSCProfile objects
*ClusterV1Api* | [**list_host**](../../../../pensando_ent/docs/ClusterV1Api.md#list_host) | **GET** /configs/cluster/v1/hosts | List Host objects
*ClusterV1Api* | [**list_node**](../../../../pensando_ent/docs/ClusterV1Api.md#list_node) | **GET** /configs/cluster/v1/nodes | List Node objects
*ClusterV1Api* | [**list_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#list_tenant) | **GET** /configs/cluster/v1/tenants | List Tenant objects
*ClusterV1Api* | [**restore**](../../../../pensando_ent/docs/ClusterV1Api.md#restore) | **POST** /configs/cluster/v1/config-restore/restore | Restore Configuration
*ClusterV1Api* | [**save**](../../../../pensando_ent/docs/ClusterV1Api.md#save) | **POST** /configs/cluster/v1/config-snapshot/save | Perform a Configuation Snapshot
*ClusterV1Api* | [**update_cluster**](../../../../pensando_ent/docs/ClusterV1Api.md#update_cluster) | **PUT** /configs/cluster/v1/cluster | Update Cluster object
*ClusterV1Api* | [**update_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#update_configuration_snapshot) | **PUT** /configs/cluster/v1/config-snapshot | Update ConfigurationSnapshot object
*ClusterV1Api* | [**update_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#update_distributed_service_card) | **PUT** /configs/cluster/v1/distributedservicecards/{O.Name} | Update DistributedServiceCard object
*ClusterV1Api* | [**update_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#update_dsc_profile) | **PUT** /configs/cluster/v1/dscprofiles/{O.Name} | Update DSCProfile object
*ClusterV1Api* | [**update_host**](../../../../pensando_ent/docs/ClusterV1Api.md#update_host) | **PUT** /configs/cluster/v1/hosts/{O.Name} | Update Host object
*ClusterV1Api* | [**update_license**](../../../../pensando_ent/docs/ClusterV1Api.md#update_license) | **PUT** /configs/cluster/v1/licenses | Update License object
*ClusterV1Api* | [**update_node**](../../../../pensando_ent/docs/ClusterV1Api.md#update_node) | **PUT** /configs/cluster/v1/nodes/{O.Name} | Update Node object
*ClusterV1Api* | [**update_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#update_tenant) | **PUT** /configs/cluster/v1/tenants/{O.Name} | Update Tenant object
*ClusterV1Api* | [**update_tls_config**](../../../../pensando_ent/docs/ClusterV1Api.md#update_tls_config) | **POST** /configs/cluster/v1/cluster/UpdateTLSConfig | Update TLS Configuration for cluster
*ClusterV1Api* | [**update_version**](../../../../pensando_ent/docs/ClusterV1Api.md#update_version) | **PUT** /configs/cluster/v1/version | Update Version object
*ClusterV1Api* | [**watch_cluster**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_cluster) | **GET** /configs/cluster/v1/watch/cluster | Watch Cluster objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_configuration_snapshot**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_configuration_snapshot) | **GET** /configs/cluster/v1/watch/config-snapshot | Watch ConfigurationSnapshot objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_distributed_service_card**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_distributed_service_card) | **GET** /configs/cluster/v1/watch/distributedservicecards | Watch DistributedServiceCard objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_dsc_profile**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_dsc_profile) | **GET** /configs/cluster/v1/watch/dscprofiles | Watch DSCProfile objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_host**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_host) | **GET** /configs/cluster/v1/watch/hosts | Watch Host objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_node**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_node) | **GET** /configs/cluster/v1/watch/nodes | Watch Node objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_tenant**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_tenant) | **GET** /configs/cluster/v1/watch/tenants | Watch Tenant objects. Supports WebSockets or HTTP long poll
*ClusterV1Api* | [**watch_version**](../../../../pensando_ent/docs/ClusterV1Api.md#watch_version) | **GET** /configs/cluster/v1/watch/version | Watch Version objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiLabel](../../../docs/ApiLabel.md)
 - [ApiListMeta](../../../docs/ApiListMeta.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [ClusterAutoMsgClusterWatchHelper](../../../docs/ClusterAutoMsgClusterWatchHelper.md)
 - [ClusterAutoMsgClusterWatchHelperWatchEvent](../../../docs/ClusterAutoMsgClusterWatchHelperWatchEvent.md)
 - [ClusterAutoMsgConfigurationSnapshotWatchHelper](../../../docs/ClusterAutoMsgConfigurationSnapshotWatchHelper.md)
 - [ClusterAutoMsgConfigurationSnapshotWatchHelperWatchEvent](../../../docs/ClusterAutoMsgConfigurationSnapshotWatchHelperWatchEvent.md)
 - [ClusterAutoMsgCredentialsWatchHelper](../../../docs/ClusterAutoMsgCredentialsWatchHelper.md)
 - [ClusterAutoMsgCredentialsWatchHelperWatchEvent](../../../docs/ClusterAutoMsgCredentialsWatchHelperWatchEvent.md)
 - [ClusterAutoMsgDSCProfileWatchHelper](../../../docs/ClusterAutoMsgDSCProfileWatchHelper.md)
 - [ClusterAutoMsgDSCProfileWatchHelperWatchEvent](../../../docs/ClusterAutoMsgDSCProfileWatchHelperWatchEvent.md)
 - [ClusterAutoMsgDistributedServiceCardWatchHelper](../../../docs/ClusterAutoMsgDistributedServiceCardWatchHelper.md)
 - [ClusterAutoMsgDistributedServiceCardWatchHelperWatchEvent](../../../docs/ClusterAutoMsgDistributedServiceCardWatchHelperWatchEvent.md)
 - [ClusterAutoMsgHostWatchHelper](../../../docs/ClusterAutoMsgHostWatchHelper.md)
 - [ClusterAutoMsgHostWatchHelperWatchEvent](../../../docs/ClusterAutoMsgHostWatchHelperWatchEvent.md)
 - [ClusterAutoMsgLicenseWatchHelper](../../../docs/ClusterAutoMsgLicenseWatchHelper.md)
 - [ClusterAutoMsgLicenseWatchHelperWatchEvent](../../../docs/ClusterAutoMsgLicenseWatchHelperWatchEvent.md)
 - [ClusterAutoMsgNodeWatchHelper](../../../docs/ClusterAutoMsgNodeWatchHelper.md)
 - [ClusterAutoMsgNodeWatchHelperWatchEvent](../../../docs/ClusterAutoMsgNodeWatchHelperWatchEvent.md)
 - [ClusterAutoMsgSnapshotRestoreWatchHelper](../../../docs/ClusterAutoMsgSnapshotRestoreWatchHelper.md)
 - [ClusterAutoMsgSnapshotRestoreWatchHelperWatchEvent](../../../docs/ClusterAutoMsgSnapshotRestoreWatchHelperWatchEvent.md)
 - [ClusterAutoMsgTenantWatchHelper](../../../docs/ClusterAutoMsgTenantWatchHelper.md)
 - [ClusterAutoMsgTenantWatchHelperWatchEvent](../../../docs/ClusterAutoMsgTenantWatchHelperWatchEvent.md)
 - [ClusterAutoMsgVersionWatchHelper](../../../docs/ClusterAutoMsgVersionWatchHelper.md)
 - [ClusterAutoMsgVersionWatchHelperWatchEvent](../../../docs/ClusterAutoMsgVersionWatchHelperWatchEvent.md)
 - [ClusterBiosInfo](../../../docs/ClusterBiosInfo.md)
 - [ClusterCPUInfo](../../../docs/ClusterCPUInfo.md)
 - [ClusterCluster](../../../docs/ClusterCluster.md)
 - [ClusterClusterAuthBootstrapRequest](../../../docs/ClusterClusterAuthBootstrapRequest.md)
 - [ClusterClusterCondition](../../../docs/ClusterClusterCondition.md)
 - [ClusterClusterList](../../../docs/ClusterClusterList.md)
 - [ClusterClusterSpec](../../../docs/ClusterClusterSpec.md)
 - [ClusterClusterStatus](../../../docs/ClusterClusterStatus.md)
 - [ClusterConfigurationSnapshot](../../../docs/ClusterConfigurationSnapshot.md)
 - [ClusterConfigurationSnapshotList](../../../docs/ClusterConfigurationSnapshotList.md)
 - [ClusterConfigurationSnapshotRequest](../../../docs/ClusterConfigurationSnapshotRequest.md)
 - [ClusterConfigurationSnapshotSpec](../../../docs/ClusterConfigurationSnapshotSpec.md)
 - [ClusterConfigurationSnapshotStatus](../../../docs/ClusterConfigurationSnapshotStatus.md)
 - [ClusterCredentials](../../../docs/ClusterCredentials.md)
 - [ClusterCredentialsList](../../../docs/ClusterCredentialsList.md)
 - [ClusterCredentialsSpec](../../../docs/ClusterCredentialsSpec.md)
 - [ClusterDSCCondition](../../../docs/ClusterDSCCondition.md)
 - [ClusterDSCControlPlaneStatus](../../../docs/ClusterDSCControlPlaneStatus.md)
 - [ClusterDSCInfo](../../../docs/ClusterDSCInfo.md)
 - [ClusterDSCProfile](../../../docs/ClusterDSCProfile.md)
 - [ClusterDSCProfileList](../../../docs/ClusterDSCProfileList.md)
 - [ClusterDSCProfileSpec](../../../docs/ClusterDSCProfileSpec.md)
 - [ClusterDSCProfileStatus](../../../docs/ClusterDSCProfileStatus.md)
 - [ClusterDistributedServiceCard](../../../docs/ClusterDistributedServiceCard.md)
 - [ClusterDistributedServiceCardID](../../../docs/ClusterDistributedServiceCardID.md)
 - [ClusterDistributedServiceCardList](../../../docs/ClusterDistributedServiceCardList.md)
 - [ClusterDistributedServiceCardSpec](../../../docs/ClusterDistributedServiceCardSpec.md)
 - [ClusterDistributedServiceCardStatus](../../../docs/ClusterDistributedServiceCardStatus.md)
 - [ClusterFeature](../../../docs/ClusterFeature.md)
 - [ClusterFeatureStatus](../../../docs/ClusterFeatureStatus.md)
 - [ClusterFwlogPolicyRef](../../../docs/ClusterFwlogPolicyRef.md)
 - [ClusterHost](../../../docs/ClusterHost.md)
 - [ClusterHostList](../../../docs/ClusterHostList.md)
 - [ClusterHostSpec](../../../docs/ClusterHostSpec.md)
 - [ClusterHostStatus](../../../docs/ClusterHostStatus.md)
 - [ClusterIPConfig](../../../docs/ClusterIPConfig.md)
 - [ClusterKeyValue](../../../docs/ClusterKeyValue.md)
 - [ClusterLicense](../../../docs/ClusterLicense.md)
 - [ClusterLicenseList](../../../docs/ClusterLicenseList.md)
 - [ClusterLicenseSpec](../../../docs/ClusterLicenseSpec.md)
 - [ClusterLicenseStatus](../../../docs/ClusterLicenseStatus.md)
 - [ClusterMemInfo](../../../docs/ClusterMemInfo.md)
 - [ClusterNode](../../../docs/ClusterNode.md)
 - [ClusterNodeCondition](../../../docs/ClusterNodeCondition.md)
 - [ClusterNodeList](../../../docs/ClusterNodeList.md)
 - [ClusterNodeSpec](../../../docs/ClusterNodeSpec.md)
 - [ClusterNodeStatus](../../../docs/ClusterNodeStatus.md)
 - [ClusterOsInfo](../../../docs/ClusterOsInfo.md)
 - [ClusterPeerStatus](../../../docs/ClusterPeerStatus.md)
 - [ClusterPolicerRef](../../../docs/ClusterPolicerRef.md)
 - [ClusterPropagationStatus](../../../docs/ClusterPropagationStatus.md)
 - [ClusterQuorumMemberCondition](../../../docs/ClusterQuorumMemberCondition.md)
 - [ClusterQuorumMemberStatus](../../../docs/ClusterQuorumMemberStatus.md)
 - [ClusterQuorumStatus](../../../docs/ClusterQuorumStatus.md)
 - [ClusterSnapshotDestination](../../../docs/ClusterSnapshotDestination.md)
 - [ClusterSnapshotRestore](../../../docs/ClusterSnapshotRestore.md)
 - [ClusterSnapshotRestoreList](../../../docs/ClusterSnapshotRestoreList.md)
 - [ClusterSnapshotRestoreSpec](../../../docs/ClusterSnapshotRestoreSpec.md)
 - [ClusterSnapshotRestoreStatus](../../../docs/ClusterSnapshotRestoreStatus.md)
 - [ClusterStorageDeviceInfo](../../../docs/ClusterStorageDeviceInfo.md)
 - [ClusterStorageInfo](../../../docs/ClusterStorageInfo.md)
 - [ClusterTenant](../../../docs/ClusterTenant.md)
 - [ClusterTenantList](../../../docs/ClusterTenantList.md)
 - [ClusterTenantSpec](../../../docs/ClusterTenantSpec.md)
 - [ClusterUpdateTLSConfigRequest](../../../docs/ClusterUpdateTLSConfigRequest.md)
 - [ClusterVersion](../../../docs/ClusterVersion.md)
 - [ClusterVersionList](../../../docs/ClusterVersionList.md)
 - [ClusterVersionSpec](../../../docs/ClusterVersionSpec.md)
 - [ClusterVersionStatus](../../../docs/ClusterVersionStatus.md)
 - [ConfigurationSnapshotStatusConfigSaveStatus](../../../docs/ConfigurationSnapshotStatusConfigSaveStatus.md)
 - [DSCProfileSpecInterfaces](../../../docs/DSCProfileSpecInterfaces.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [RecoverykeysRecoveryKeys](../../../docs/RecoverykeysRecoveryKeys.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm.apis and psm.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm.api.default_api import DefaultApi`
- `from psm.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm
from psm.apis import *
from psm.models import *
```
