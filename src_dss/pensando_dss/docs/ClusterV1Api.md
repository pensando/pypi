# psm.ClusterV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_configuration_snapshot**](ClusterV1Api.md#add_configuration_snapshot) | **POST** /configs/cluster/v1/config-snapshot | Create ConfigurationSnapshot object
[**add_dsc_profile**](ClusterV1Api.md#add_dsc_profile) | **POST** /configs/cluster/v1/dscprofiles | Create DSCProfile object
[**add_host**](ClusterV1Api.md#add_host) | **POST** /configs/cluster/v1/hosts | Create Host object
[**add_license**](ClusterV1Api.md#add_license) | **POST** /configs/cluster/v1/licenses | Create License object
[**add_node**](ClusterV1Api.md#add_node) | **POST** /configs/cluster/v1/nodes | Create Node object
[**add_tenant**](ClusterV1Api.md#add_tenant) | **POST** /configs/cluster/v1/tenants | Create Tenant object
[**auth_bootstrap_complete**](ClusterV1Api.md#auth_bootstrap_complete) | **POST** /configs/cluster/v1/cluster/AuthBootstrapComplete | Mark bootstrapping as complete for the cluster
[**delete_configuration_snapshot**](ClusterV1Api.md#delete_configuration_snapshot) | **DELETE** /configs/cluster/v1/config-snapshot | Delete ConfigurationSnapshot object
[**delete_distributed_service_card**](ClusterV1Api.md#delete_distributed_service_card) | **DELETE** /configs/cluster/v1/distributedservicecards/{O.Name} | Delete DistributedServiceCard object
[**delete_dsc_profile**](ClusterV1Api.md#delete_dsc_profile) | **DELETE** /configs/cluster/v1/dscprofiles/{O.Name} | Delete DSCProfile object
[**delete_host**](ClusterV1Api.md#delete_host) | **DELETE** /configs/cluster/v1/hosts/{O.Name} | Delete Host object
[**delete_node**](ClusterV1Api.md#delete_node) | **DELETE** /configs/cluster/v1/nodes/{O.Name} | Delete Node object
[**delete_tenant**](ClusterV1Api.md#delete_tenant) | **DELETE** /configs/cluster/v1/tenants/{O.Name} | Delete Tenant object
[**get_cluster**](ClusterV1Api.md#get_cluster) | **GET** /configs/cluster/v1/cluster | Get Cluster object
[**get_cluster_profile**](ClusterV1Api.md#get_cluster_profile) | **GET** /configs/cluster/v1/clusterprofile | Get ClusterProfile object
[**get_configuration_snapshot**](ClusterV1Api.md#get_configuration_snapshot) | **GET** /configs/cluster/v1/config-snapshot | Get ConfigurationSnapshot object
[**get_distributed_service_card**](ClusterV1Api.md#get_distributed_service_card) | **GET** /configs/cluster/v1/distributedservicecards/{O.Name} | Get DistributedServiceCard object
[**get_dsc_profile**](ClusterV1Api.md#get_dsc_profile) | **GET** /configs/cluster/v1/dscprofiles/{O.Name} | Get DSCProfile object
[**get_host**](ClusterV1Api.md#get_host) | **GET** /configs/cluster/v1/hosts/{O.Name} | Get Host object
[**get_license**](ClusterV1Api.md#get_license) | **GET** /configs/cluster/v1/licenses | Get License object
[**get_node**](ClusterV1Api.md#get_node) | **GET** /configs/cluster/v1/nodes/{O.Name} | Get Node object
[**get_snapshot_restore**](ClusterV1Api.md#get_snapshot_restore) | **GET** /configs/cluster/v1/config-restore | Get SnapshotRestore object
[**get_tenant**](ClusterV1Api.md#get_tenant) | **GET** /configs/cluster/v1/tenants/{O.Name} | Get Tenant object
[**get_version**](ClusterV1Api.md#get_version) | **GET** /configs/cluster/v1/version | Get Version object
[**label_cluster**](ClusterV1Api.md#label_cluster) | **POST** /configs/cluster/v1/cluster/label | Label Cluster object
[**label_cluster_profile**](ClusterV1Api.md#label_cluster_profile) | **POST** /configs/cluster/v1/clusterprofile/label | Label ClusterProfile object
[**label_configuration_snapshot**](ClusterV1Api.md#label_configuration_snapshot) | **POST** /configs/cluster/v1/config-snapshot/label | Label ConfigurationSnapshot object
[**label_distributed_service_card**](ClusterV1Api.md#label_distributed_service_card) | **POST** /configs/cluster/v1/distributedservicecards/{O.Name}/label | Label DistributedServiceCard object
[**label_dsc_profile**](ClusterV1Api.md#label_dsc_profile) | **POST** /configs/cluster/v1/dscprofiles/{O.Name}/label | Label DSCProfile object
[**label_host**](ClusterV1Api.md#label_host) | **POST** /configs/cluster/v1/hosts/{O.Name}/label | Label Host object
[**label_license**](ClusterV1Api.md#label_license) | **POST** /configs/cluster/v1/licenses/label | Label License object
[**label_node**](ClusterV1Api.md#label_node) | **POST** /configs/cluster/v1/nodes/{O.Name}/label | Label Node object
[**label_tenant**](ClusterV1Api.md#label_tenant) | **POST** /configs/cluster/v1/tenants/{O.Name}/label | Label Tenant object
[**list_distributed_service_card**](ClusterV1Api.md#list_distributed_service_card) | **GET** /configs/cluster/v1/distributedservicecards | List DistributedServiceCard objects
[**list_dsc_profile**](ClusterV1Api.md#list_dsc_profile) | **GET** /configs/cluster/v1/dscprofiles | List DSCProfile objects
[**list_host**](ClusterV1Api.md#list_host) | **GET** /configs/cluster/v1/hosts | List Host objects
[**list_node**](ClusterV1Api.md#list_node) | **GET** /configs/cluster/v1/nodes | List Node objects
[**list_tenant**](ClusterV1Api.md#list_tenant) | **GET** /configs/cluster/v1/tenants | List Tenant objects
[**restore**](ClusterV1Api.md#restore) | **POST** /configs/cluster/v1/config-restore/restore | Restore Configuration
[**save**](ClusterV1Api.md#save) | **POST** /configs/cluster/v1/config-snapshot/save | Perform a Configuation Snapshot
[**update_cluster**](ClusterV1Api.md#update_cluster) | **PUT** /configs/cluster/v1/cluster | Update Cluster object
[**update_cluster_profile**](ClusterV1Api.md#update_cluster_profile) | **PUT** /configs/cluster/v1/clusterprofile | Update ClusterProfile object
[**update_configuration_snapshot**](ClusterV1Api.md#update_configuration_snapshot) | **PUT** /configs/cluster/v1/config-snapshot | Update ConfigurationSnapshot object
[**update_distributed_service_card**](ClusterV1Api.md#update_distributed_service_card) | **PUT** /configs/cluster/v1/distributedservicecards/{O.Name} | Update DistributedServiceCard object
[**update_dsc_profile**](ClusterV1Api.md#update_dsc_profile) | **PUT** /configs/cluster/v1/dscprofiles/{O.Name} | Update DSCProfile object
[**update_host**](ClusterV1Api.md#update_host) | **PUT** /configs/cluster/v1/hosts/{O.Name} | Update Host object
[**update_license**](ClusterV1Api.md#update_license) | **PUT** /configs/cluster/v1/licenses | Update License object
[**update_node**](ClusterV1Api.md#update_node) | **PUT** /configs/cluster/v1/nodes/{O.Name} | Update Node object
[**update_tenant**](ClusterV1Api.md#update_tenant) | **PUT** /configs/cluster/v1/tenants/{O.Name} | Update Tenant object
[**update_tls_config**](ClusterV1Api.md#update_tls_config) | **POST** /configs/cluster/v1/cluster/UpdateTLSConfig | Update TLS Configuration for cluster
[**update_version**](ClusterV1Api.md#update_version) | **PUT** /configs/cluster/v1/version | Update Version object
[**watch_cluster**](ClusterV1Api.md#watch_cluster) | **GET** /configs/cluster/v1/watch/cluster | Watch Cluster objects. Supports WebSockets or HTTP long poll
[**watch_cluster_profile**](ClusterV1Api.md#watch_cluster_profile) | **GET** /configs/cluster/v1/watch/clusterprofile | Watch ClusterProfile objects. Supports WebSockets or HTTP long poll
[**watch_configuration_snapshot**](ClusterV1Api.md#watch_configuration_snapshot) | **GET** /configs/cluster/v1/watch/config-snapshot | Watch ConfigurationSnapshot objects. Supports WebSockets or HTTP long poll
[**watch_distributed_service_card**](ClusterV1Api.md#watch_distributed_service_card) | **GET** /configs/cluster/v1/watch/distributedservicecards | Watch DistributedServiceCard objects. Supports WebSockets or HTTP long poll
[**watch_dsc_profile**](ClusterV1Api.md#watch_dsc_profile) | **GET** /configs/cluster/v1/watch/dscprofiles | Watch DSCProfile objects. Supports WebSockets or HTTP long poll
[**watch_host**](ClusterV1Api.md#watch_host) | **GET** /configs/cluster/v1/watch/hosts | Watch Host objects. Supports WebSockets or HTTP long poll
[**watch_node**](ClusterV1Api.md#watch_node) | **GET** /configs/cluster/v1/watch/nodes | Watch Node objects. Supports WebSockets or HTTP long poll
[**watch_tenant**](ClusterV1Api.md#watch_tenant) | **GET** /configs/cluster/v1/watch/tenants | Watch Tenant objects. Supports WebSockets or HTTP long poll
[**watch_version**](ClusterV1Api.md#watch_version) | **GET** /configs/cluster/v1/watch/version | Watch Version objects. Supports WebSockets or HTTP long poll


# **add_configuration_snapshot**
> ClusterConfigurationSnapshot add_configuration_snapshot(body)

Create ConfigurationSnapshot object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterConfigurationSnapshot(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterConfigurationSnapshotSpec(
            destination=ClusterSnapshotDestination(
                type="objectstore",
            ),
        ),
        status=ClusterConfigurationSnapshotStatus(
            last_snapshot=ConfigurationSnapshotStatusConfigSaveStatus(
                dest_type="objectstore",
                uri="uri_example",
            ),
        ),
    ) # ClusterConfigurationSnapshot | 

    # example passing only required values which don't have defaults set
    try:
        # Create ConfigurationSnapshot object
        api_response = api_instance.add_configuration_snapshot(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_configuration_snapshot: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)|  |

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dsc_profile**
> ClusterDSCProfile add_dsc_profile(body)

Create DSCProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_dsc_profile import ClusterDSCProfile
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterDSCProfile(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterDSCProfileSpec(
            apply_policies_to_encapsulated_traffic="disabled",
            deployment_target="host",
            feature_set="smartnic",
            interface_profile=DSCProfileSpecInterfaces(
                num_pfs=1,
                num_vfs=1,
            ),
        ),
        status=ClusterDSCProfileStatus(
            propagation_status=ClusterPropagationStatus(
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
        ),
    ) # ClusterDSCProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Create DSCProfile object
        api_response = api_instance.add_dsc_profile(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterDSCProfile**](ClusterDSCProfile.md)|  |

### Return type

[**ClusterDSCProfile**](ClusterDSCProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_host**
> ClusterHost add_host(body)

Create Host object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_host import ClusterHost
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterHost(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterHostSpec(
            dscs=[
                ClusterDistributedServiceCardID(
                    id="id_example",
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                ),
            ],
        ),
        status=ClusterHostStatus(
            admitted_dscs=[
                "admitted_dscs_example",
            ],
            mirror_sessions=[
                "mirror_sessions_example",
            ],
        ),
    ) # ClusterHost | 

    # example passing only required values which don't have defaults set
    try:
        # Create Host object
        api_response = api_instance.add_host(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterHost**](ClusterHost.md)|  |

### Return type

[**ClusterHost**](ClusterHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_license**
> ClusterLicense add_license(body)

Create License object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_license import ClusterLicense
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterLicense(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterLicenseSpec(
            features=[
                ClusterFeature(
                    feature_key="feature_key_example",
                    licence="licence_example",
                ),
            ],
        ),
        status=ClusterLicenseStatus(
            features=[
                ClusterFeatureStatus(
                    expiry="expiry_example",
                    feature_key="feature_key_example",
                    value="value_example",
                ),
            ],
            unknown=[
                "unknown_example",
            ],
        ),
    ) # ClusterLicense | 

    # example passing only required values which don't have defaults set
    try:
        # Create License object
        api_response = api_instance.add_license(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_license: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterLicense**](ClusterLicense.md)|  |

### Return type

[**ClusterLicense**](ClusterLicense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_node**
> ClusterNode add_node(body)

Create Node object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node import ClusterNode
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterNode(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterNodeSpec(
            routing_config="routing_config_example",
        ),
        status=ClusterNodeStatus(
            conditions=[
                ClusterNodeCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    reason="reason_example",
                    status="unknown",
                    type="leader",
                ),
            ],
            phase="unknown",
            quorum=True,
        ),
    ) # ClusterNode | 

    # example passing only required values which don't have defaults set
    try:
        # Create Node object
        api_response = api_instance.add_node(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterNode**](ClusterNode.md)|  |

### Return type

[**ClusterNode**](ClusterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tenant**
> ClusterTenant add_tenant(body)

Create Tenant object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_tenant import ClusterTenant
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterTenant(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterTenantSpec(
            admin_user="admin_user_example",
        ),
        status={},
    ) # ClusterTenant | 

    # example passing only required values which don't have defaults set
    try:
        # Create Tenant object
        api_response = api_instance.add_tenant(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->add_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterTenant**](ClusterTenant.md)|  |

### Return type

[**ClusterTenant**](ClusterTenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_bootstrap_complete**
> ClusterCluster auth_bootstrap_complete(body)

Mark bootstrapping as complete for the cluster

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_cluster_auth_bootstrap_request import ClusterClusterAuthBootstrapRequest
from pensando_dss.psm.model.cluster_cluster import ClusterCluster
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterClusterAuthBootstrapRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # ClusterClusterAuthBootstrapRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Mark bootstrapping as complete for the cluster
        api_response = api_instance.auth_bootstrap_complete(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->auth_bootstrap_complete: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterClusterAuthBootstrapRequest**](ClusterClusterAuthBootstrapRequest.md)|  |

### Return type

[**ClusterCluster**](ClusterCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration_snapshot**
> ClusterConfigurationSnapshot delete_configuration_snapshot()

Delete ConfigurationSnapshot object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete ConfigurationSnapshot object
        api_response = api_instance.delete_configuration_snapshot()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_configuration_snapshot: %s\n" % e)

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_distributed_service_card**
> ClusterDistributedServiceCard delete_distributed_service_card(o_name)

Delete DistributedServiceCard object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_distributed_service_card import ClusterDistributedServiceCard
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete DistributedServiceCard object
        api_response = api_instance.delete_distributed_service_card(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**ClusterDistributedServiceCard**](ClusterDistributedServiceCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dsc_profile**
> ClusterDSCProfile delete_dsc_profile(o_name)

Delete DSCProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_dsc_profile import ClusterDSCProfile
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete DSCProfile object
        api_response = api_instance.delete_dsc_profile(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**ClusterDSCProfile**](ClusterDSCProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host**
> ClusterHost delete_host(o_name)

Delete Host object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_host import ClusterHost
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Host object
        api_response = api_instance.delete_host(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**ClusterHost**](ClusterHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> ClusterNode delete_node(o_name)

Delete Node object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node import ClusterNode
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Node object
        api_response = api_instance.delete_node(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**ClusterNode**](ClusterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> ClusterTenant delete_tenant(o_name)

Delete Tenant object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_tenant import ClusterTenant
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Tenant object
        api_response = api_instance.delete_tenant(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->delete_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**ClusterTenant**](ClusterTenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ClusterCluster get_cluster()

Get Cluster object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_cluster import ClusterCluster
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_quorum_nodes = [
        "spec.quorum-nodes_example",
    ] # [str] | QuorumNodes contains the list of hostnames for nodes configured to be quorum nodes in the cluster. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Cluster object
        api_response = api_instance.get_cluster()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_cluster: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_quorum_nodes** | **[str]**| QuorumNodes contains the list of hostnames for nodes configured to be quorum nodes in the cluster. | [optional]

### Return type

[**ClusterCluster**](ClusterCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_profile**
> ClusterClusterProfile get_cluster_profile()

Get ClusterProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_cluster_profile import ClusterClusterProfile
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ClusterProfile object
        api_response = api_instance.get_cluster_profile()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_cluster_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**ClusterClusterProfile**](ClusterClusterProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_snapshot**
> ClusterConfigurationSnapshot get_configuration_snapshot()

Get ConfigurationSnapshot object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    destination_type = "destination.Type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ConfigurationSnapshot object
        api_response = api_instance.get_configuration_snapshot()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_configuration_snapshot: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **destination_type** | **str**|  | [optional]

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distributed_service_card**
> ClusterDistributedServiceCard get_distributed_service_card(o_name)

Get DistributedServiceCard object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_distributed_service_card import ClusterDistributedServiceCard
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    ip_config_dns_servers = [
        "ip-config.dns-servers_example",
    ] # [str] | DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. (optional)
    spec_dscprofile = "spec.dscprofile_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get DistributedServiceCard object
        api_response = api_instance.get_distributed_service_card(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **ip_config_dns_servers** | **[str]**| DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. | [optional]
 **spec_dscprofile** | **str**|  | [optional]

### Return type

[**ClusterDistributedServiceCard**](ClusterDistributedServiceCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dsc_profile**
> ClusterDSCProfile get_dsc_profile(o_name)

Get DSCProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_dsc_profile import ClusterDSCProfile
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_deployment_target = "spec.deployment-target_example" # str |  (optional)
    interface_profile_num_pfs = 1 # int |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get DSCProfile object
        api_response = api_instance.get_dsc_profile(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_deployment_target** | **str**|  | [optional]
 **interface_profile_num_pfs** | **int**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**ClusterDSCProfile**](ClusterDSCProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host**
> ClusterHost get_host(o_name)

Get Host object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_host import ClusterHost
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    status_admitted_dscs = [
        "status.admitted-dscs_example",
    ] # [str] | AdmittedDSCs contains a list of admitted DistributedServiceCards that are on this host. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Host object
        api_response = api_instance.get_host(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **status_admitted_dscs** | **[str]**| AdmittedDSCs contains a list of admitted DistributedServiceCards that are on this host. | [optional]

### Return type

[**ClusterHost**](ClusterHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> ClusterLicense get_license()

Get License object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_license import ClusterLicense
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    status_unknown = [
        "status.unknown_example",
    ] # [str] | Licenses that are not understood by the current running version of software. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get License object
        api_response = api_instance.get_license()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_license: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **status_unknown** | **[str]**| Licenses that are not understood by the current running version of software. | [optional]

### Return type

[**ClusterLicense**](ClusterLicense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> ClusterNode get_node(o_name)

Get Node object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node import ClusterNode
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Node object
        api_response = api_instance.get_node(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**ClusterNode**](ClusterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_restore**
> ClusterSnapshotRestore get_snapshot_restore()

Get SnapshotRestore object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_snapshot_restore import ClusterSnapshotRestore
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_path = "spec.path_example" # str |  (optional)
    status_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SnapshotRestore object
        api_response = api_instance.get_snapshot_restore()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_snapshot_restore: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_path** | **str**|  | [optional]
 **status_start_time** | **datetime**|  | [optional]

### Return type

[**ClusterSnapshotRestore**](ClusterSnapshotRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> ClusterTenant get_tenant(o_name)

Get Tenant object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_tenant import ClusterTenant
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Tenant object
        api_response = api_instance.get_tenant(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**ClusterTenant**](ClusterTenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> ClusterVersion get_version()

Get Version object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_version import ClusterVersion
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Version object
        api_response = api_instance.get_version()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->get_version: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_cluster**
> ClusterCluster label_cluster(body)

Label Cluster object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.cluster_cluster import ClusterCluster
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Cluster object
        api_response = api_instance.label_cluster(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_cluster: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterCluster**](ClusterCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_cluster_profile**
> ClusterClusterProfile label_cluster_profile(body)

Label ClusterProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_cluster_profile import ClusterClusterProfile
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label ClusterProfile object
        api_response = api_instance.label_cluster_profile(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_cluster_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterClusterProfile**](ClusterClusterProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_configuration_snapshot**
> ClusterConfigurationSnapshot label_configuration_snapshot(body)

Label ConfigurationSnapshot object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label ConfigurationSnapshot object
        api_response = api_instance.label_configuration_snapshot(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_configuration_snapshot: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_distributed_service_card**
> ClusterDistributedServiceCard label_distributed_service_card(o_name, body)

Label DistributedServiceCard object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_distributed_service_card import ClusterDistributedServiceCard
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label DistributedServiceCard object
        api_response = api_instance.label_distributed_service_card(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterDistributedServiceCard**](ClusterDistributedServiceCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_dsc_profile**
> ClusterDSCProfile label_dsc_profile(o_name, body)

Label DSCProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.cluster_dsc_profile import ClusterDSCProfile
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label DSCProfile object
        api_response = api_instance.label_dsc_profile(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterDSCProfile**](ClusterDSCProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_host**
> ClusterHost label_host(o_name, body)

Label Host object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_host import ClusterHost
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Host object
        api_response = api_instance.label_host(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterHost**](ClusterHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_license**
> ClusterLicense label_license(body)

Label License object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_license import ClusterLicense
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label License object
        api_response = api_instance.label_license(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_license: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterLicense**](ClusterLicense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_node**
> ClusterNode label_node(o_name, body)

Label Node object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node import ClusterNode
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Node object
        api_response = api_instance.label_node(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterNode**](ClusterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_tenant**
> ClusterTenant label_tenant(o_name, body)

Label Tenant object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.cluster_tenant import ClusterTenant
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Tenant object
        api_response = api_instance.label_tenant(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->label_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**ClusterTenant**](ClusterTenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_distributed_service_card**
> ClusterDistributedServiceCardList list_distributed_service_card()

List DistributedServiceCard objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_distributed_service_card_list import ClusterDistributedServiceCardList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List DistributedServiceCard objects
        api_response = api_instance.list_distributed_service_card()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->list_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterDistributedServiceCardList**](ClusterDistributedServiceCardList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dsc_profile**
> ClusterDSCProfileList list_dsc_profile()

List DSCProfile objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_dsc_profile_list import ClusterDSCProfileList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List DSCProfile objects
        api_response = api_instance.list_dsc_profile()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->list_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterDSCProfileList**](ClusterDSCProfileList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_host**
> ClusterHostList list_host()

List Host objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_host_list import ClusterHostList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Host objects
        api_response = api_instance.list_host()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->list_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterHostList**](ClusterHostList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node**
> ClusterNodeList list_node()

List Node objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node_list import ClusterNodeList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Node objects
        api_response = api_instance.list_node()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->list_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterNodeList**](ClusterNodeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenant**
> ClusterTenantList list_tenant()

List Tenant objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_tenant_list import ClusterTenantList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Tenant objects
        api_response = api_instance.list_tenant()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->list_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterTenantList**](ClusterTenantList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore**
> ClusterSnapshotRestore restore(body)

Restore Configuration

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_snapshot_restore import ClusterSnapshotRestore
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterSnapshotRestore(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterSnapshotRestoreSpec(
            path="path_example",
        ),
        status=ClusterSnapshotRestoreStatus(
            backup_snapshot_path="backup_snapshot_path_example",
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            status="unknown",
        ),
    ) # ClusterSnapshotRestore | 

    # example passing only required values which don't have defaults set
    try:
        # Restore Configuration
        api_response = api_instance.restore(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->restore: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterSnapshotRestore**](ClusterSnapshotRestore.md)|  |

### Return type

[**ClusterSnapshotRestore**](ClusterSnapshotRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> ClusterConfigurationSnapshot save(body)

Perform a Configuation Snapshot

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.cluster_configuration_snapshot_request import ClusterConfigurationSnapshotRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterConfigurationSnapshotRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # ClusterConfigurationSnapshotRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Perform a Configuation Snapshot
        api_response = api_instance.save(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->save: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterConfigurationSnapshotRequest**](ClusterConfigurationSnapshotRequest.md)|  |

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> ClusterCluster update_cluster(body)

Update Cluster object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_cluster import ClusterCluster
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterCluster(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterClusterSpec(
            auto_admit_dscs=True,
            certs="certs_example",
            key="key_example",
            ntp_servers=[
                "ntp_servers_example",
            ],
            quorum_nodes=[
                "quorum_nodes_example",
            ],
            recovery_keys=RecoverykeysRecoveryKeys(
                private_key="private_key_example",
                psm_version="psm_version_example",
                trust_chain=[
                    "trust_chain_example",
                ],
                trust_roots=[
                    "trust_roots_example",
                ],
            ),
            virtual_ip="virtual_ip_example",
        ),
        status=ClusterClusterStatus(
            auth_bootstrapped=True,
            conditions=[
                ClusterClusterCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    reason="reason_example",
                    status="unknown",
                    type="healthy",
                ),
            ],
            current_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_leader_transition_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            leader="leader_example",
            quorum_status=ClusterQuorumStatus(
                members=[
                    ClusterQuorumMemberStatus(
                        conditions=[
                            ClusterQuorumMemberCondition(
                                last_transition_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                status="unknown",
                                type="healthy",
                            ),
                        ],
                        id="id_example",
                        name="name_example",
                        status="status_example",
                        term="term_example",
                    ),
                ],
            ),
            recovery_keys_downloaded=True,
        ),
    ) # ClusterCluster | 

    # example passing only required values which don't have defaults set
    try:
        # Update Cluster object
        api_response = api_instance.update_cluster(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_cluster: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterCluster**](ClusterCluster.md)|  |

### Return type

[**ClusterCluster**](ClusterCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_profile**
> ClusterClusterProfile update_cluster_profile(body)

Update ClusterProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_cluster_profile import ClusterClusterProfile
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterClusterProfile(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterClusterProfileSpec(
            search_options=ClusterSearchOptions(
                enable_fwlog_search=True,
            ),
        ),
        status={},
    ) # ClusterClusterProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update ClusterProfile object
        api_response = api_instance.update_cluster_profile(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_cluster_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterClusterProfile**](ClusterClusterProfile.md)|  |

### Return type

[**ClusterClusterProfile**](ClusterClusterProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_snapshot**
> ClusterConfigurationSnapshot update_configuration_snapshot(body)

Update ConfigurationSnapshot object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_configuration_snapshot import ClusterConfigurationSnapshot
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterConfigurationSnapshot(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterConfigurationSnapshotSpec(
            destination=ClusterSnapshotDestination(
                type="objectstore",
            ),
        ),
        status=ClusterConfigurationSnapshotStatus(
            last_snapshot=ConfigurationSnapshotStatusConfigSaveStatus(
                dest_type="objectstore",
                uri="uri_example",
            ),
        ),
    ) # ClusterConfigurationSnapshot | 

    # example passing only required values which don't have defaults set
    try:
        # Update ConfigurationSnapshot object
        api_response = api_instance.update_configuration_snapshot(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_configuration_snapshot: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)|  |

### Return type

[**ClusterConfigurationSnapshot**](ClusterConfigurationSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_distributed_service_card**
> ClusterDistributedServiceCard update_distributed_service_card(o_name, body)

Update DistributedServiceCard object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_distributed_service_card import ClusterDistributedServiceCard
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ClusterDistributedServiceCard(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterDistributedServiceCardSpec(
            admit=True,
            controllers=[
                "controllers_example",
            ],
            dscprofile="dscprofile_example",
            enable_secure_boot=False,
            fwlog_policy=ClusterFwlogPolicyRef(
                name="name_example",
                tenant="default",
            ),
            id="id_example",
            ip_config=ClusterIPConfig(
                default_gw="10.1.1.1, ff02::5 ",
                dns_servers=[
                    "dns_servers_example",
                ],
                ip_address="10.1.1.1/24, ff02::5/32 ",
            ),
            mgmt_mode="host",
            mgmt_vlan=0,
            network_mode="oob",
            policer=ClusterPolicerRef(
                tenant="default",
                tx_policer="tx_policer_example",
            ),
            routing_config="routing_config_example",
        ),
        status=ClusterDistributedServiceCardStatus(
            dsc_sku="dsc_sku_example",
            dsc_version="dsc_version_example",
            adm_phase_reason="adm_phase_reason_example",
            admission_phase="unknown",
            alom_present=True,
            conditions=[
                ClusterDSCCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    reason="reason_example",
                    status="unknown",
                    type="healthy",
                ),
            ],
            control_plane_status=ClusterDSCControlPlaneStatus(
                bgp_status=[
                    ClusterPeerStatus(
                        address_families=[
                            "address_families_example",
                        ],
                        peer_address="peer_address_example",
                        remote_asn=1,
                        state="state_example",
                    ),
                ],
                last_updated_time="last_updated_time_example",
                message="message_example",
            ),
            dss_info=ClusterDSSInfo(
                dsms=[
                    ClusterDSM(
                        mac_address="mac_address_example",
                        unit_id=1,
                    ),
                ],
                fault_info=ClusterFault(
                    description="description_example",
                    last_occured_time="last_occured_time_example",
                    mitigation="system-reboot",
                    severity="info",
                ),
                host_name="host_name_example",
                version="version_example",
            ),
            host="host_example",
            inband_ip_config=ClusterIPConfig(
                default_gw="10.1.1.1, ff02::5 ",
                dns_servers=[],
                ip_address="10.1.1.1/24, ff02::5/32 ",
            ),
            interfaces=[
                "interfaces_example",
            ],
            ip_config=ClusterIPConfig(
                default_gw="10.1.1.1, ff02::5 ",
                dns_servers=[],
                ip_address="10.1.1.1/24, ff02::5/32 ",
            ),
            is_connected_to_psm=True,
            num_mac_address=24,
            package_type="dsc",
            primary_mac="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            secure_booted=True,
            serial_num="serial_num_example",
            system_info=ClusterDSCInfo(
                bios_info=ClusterBiosInfo(
                    fw_major_ver="fw_major_ver_example",
                    fw_minor_ver="fw_minor_ver_example",
                    vendor="vendor_example",
                    version="version_example",
                ),
                cpu_info=ClusterCPUInfo(
                    num_cores=1,
                    num_sockets=1,
                    num_threads=1,
                    speed="speed_example",
                ),
                memory_info=ClusterMemInfo(
                    size="size_example",
                    type="unknown",
                ),
                os_info=ClusterOsInfo(
                    kernel_release="kernel_release_example",
                    kernel_version="kernel_version_example",
                    processor="processor_example",
                    type="type_example",
                ),
                storage_info=ClusterStorageInfo(
                    devices=[
                        ClusterStorageDeviceInfo(
                            capacity="capacity_example",
                            percent_life_used_a=1,
                            percent_life_used_b=1,
                            serial_num="serial_num_example",
                            type="type_example",
                            vendor="vendor_example",
                        ),
                    ],
                ),
            ),
            unhealthy_services=[
                "unhealthy_services_example",
            ],
            version_mismatch=True,
        ),
    ) # ClusterDistributedServiceCard | 

    # example passing only required values which don't have defaults set
    try:
        # Update DistributedServiceCard object
        api_response = api_instance.update_distributed_service_card(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ClusterDistributedServiceCard**](ClusterDistributedServiceCard.md)|  |

### Return type

[**ClusterDistributedServiceCard**](ClusterDistributedServiceCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dsc_profile**
> ClusterDSCProfile update_dsc_profile(o_name, body)

Update DSCProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_dsc_profile import ClusterDSCProfile
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ClusterDSCProfile(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterDSCProfileSpec(
            apply_policies_to_encapsulated_traffic="disabled",
            deployment_target="host",
            feature_set="smartnic",
            interface_profile=DSCProfileSpecInterfaces(
                num_pfs=1,
                num_vfs=1,
            ),
        ),
        status=ClusterDSCProfileStatus(
            propagation_status=ClusterPropagationStatus(
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
        ),
    ) # ClusterDSCProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update DSCProfile object
        api_response = api_instance.update_dsc_profile(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ClusterDSCProfile**](ClusterDSCProfile.md)|  |

### Return type

[**ClusterDSCProfile**](ClusterDSCProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host**
> ClusterHost update_host(o_name, body)

Update Host object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_host import ClusterHost
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ClusterHost(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterHostSpec(
            dscs=[
                ClusterDistributedServiceCardID(
                    id="id_example",
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                ),
            ],
        ),
        status=ClusterHostStatus(
            admitted_dscs=[
                "admitted_dscs_example",
            ],
            mirror_sessions=[
                "mirror_sessions_example",
            ],
        ),
    ) # ClusterHost | 

    # example passing only required values which don't have defaults set
    try:
        # Update Host object
        api_response = api_instance.update_host(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ClusterHost**](ClusterHost.md)|  |

### Return type

[**ClusterHost**](ClusterHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> ClusterLicense update_license(body)

Update License object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_license import ClusterLicense
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterLicense(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterLicenseSpec(
            features=[
                ClusterFeature(
                    feature_key="feature_key_example",
                    licence="licence_example",
                ),
            ],
        ),
        status=ClusterLicenseStatus(
            features=[
                ClusterFeatureStatus(
                    expiry="expiry_example",
                    feature_key="feature_key_example",
                    value="value_example",
                ),
            ],
            unknown=[
                "unknown_example",
            ],
        ),
    ) # ClusterLicense | 

    # example passing only required values which don't have defaults set
    try:
        # Update License object
        api_response = api_instance.update_license(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_license: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterLicense**](ClusterLicense.md)|  |

### Return type

[**ClusterLicense**](ClusterLicense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node**
> ClusterNode update_node(o_name, body)

Update Node object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_node import ClusterNode
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ClusterNode(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterNodeSpec(
            routing_config="routing_config_example",
        ),
        status=ClusterNodeStatus(
            conditions=[
                ClusterNodeCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    reason="reason_example",
                    status="unknown",
                    type="leader",
                ),
            ],
            phase="unknown",
            quorum=True,
        ),
    ) # ClusterNode | 

    # example passing only required values which don't have defaults set
    try:
        # Update Node object
        api_response = api_instance.update_node(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ClusterNode**](ClusterNode.md)|  |

### Return type

[**ClusterNode**](ClusterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant**
> ClusterTenant update_tenant(o_name, body)

Update Tenant object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_tenant import ClusterTenant
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ClusterTenant(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterTenantSpec(
            admin_user="admin_user_example",
        ),
        status={},
    ) # ClusterTenant | 

    # example passing only required values which don't have defaults set
    try:
        # Update Tenant object
        api_response = api_instance.update_tenant(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ClusterTenant**](ClusterTenant.md)|  |

### Return type

[**ClusterTenant**](ClusterTenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tls_config**
> ClusterCluster update_tls_config(body)

Update TLS Configuration for cluster

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_update_tls_config_request import ClusterUpdateTLSConfigRequest
from pensando_dss.psm.model.cluster_cluster import ClusterCluster
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterUpdateTLSConfigRequest(
        api_version="api_version_example",
        certs="certs_example",
        key="key_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # ClusterUpdateTLSConfigRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update TLS Configuration for cluster
        api_response = api_instance.update_tls_config(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_tls_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpdateTLSConfigRequest**](ClusterUpdateTLSConfigRequest.md)|  |

### Return type

[**ClusterCluster**](ClusterCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> ClusterVersion update_version(body)

Update Version object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_version import ClusterVersion
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    body = ClusterVersion(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=ClusterVersionSpec(
            auto_rollout_dsc_version="auto_rollout_dsc_version_example",
        ),
        status=ClusterVersionStatus(
            build_date="build_date_example",
            build_version="build_version_example",
            rollout_build_version="rollout_build_version_example",
            vcs_commit="vcs_commit_example",
        ),
    ) # ClusterVersion | 

    # example passing only required values which don't have defaults set
    try:
        # Update Version object
        api_response = api_instance.update_version(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->update_version: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterVersion**](ClusterVersion.md)|  |

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_cluster**
> ClusterAutoMsgClusterWatchHelper watch_cluster()

Watch Cluster objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_cluster_watch_helper import ClusterAutoMsgClusterWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Cluster objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_cluster()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_cluster: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgClusterWatchHelper**](ClusterAutoMsgClusterWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_cluster_profile**
> ClusterAutoMsgClusterProfileWatchHelper watch_cluster_profile()

Watch ClusterProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_cluster_profile_watch_helper import ClusterAutoMsgClusterProfileWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch ClusterProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_cluster_profile()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_cluster_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgClusterProfileWatchHelper**](ClusterAutoMsgClusterProfileWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_configuration_snapshot**
> ClusterAutoMsgConfigurationSnapshotWatchHelper watch_configuration_snapshot()

Watch ConfigurationSnapshot objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_configuration_snapshot_watch_helper import ClusterAutoMsgConfigurationSnapshotWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch ConfigurationSnapshot objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_configuration_snapshot()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_configuration_snapshot: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgConfigurationSnapshotWatchHelper**](ClusterAutoMsgConfigurationSnapshotWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_distributed_service_card**
> ClusterAutoMsgDistributedServiceCardWatchHelper watch_distributed_service_card()

Watch DistributedServiceCard objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.cluster_auto_msg_distributed_service_card_watch_helper import ClusterAutoMsgDistributedServiceCardWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch DistributedServiceCard objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_distributed_service_card()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_distributed_service_card: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgDistributedServiceCardWatchHelper**](ClusterAutoMsgDistributedServiceCardWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_dsc_profile**
> ClusterAutoMsgDSCProfileWatchHelper watch_dsc_profile()

Watch DSCProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_dsc_profile_watch_helper import ClusterAutoMsgDSCProfileWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch DSCProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_dsc_profile()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_dsc_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgDSCProfileWatchHelper**](ClusterAutoMsgDSCProfileWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_host**
> ClusterAutoMsgHostWatchHelper watch_host()

Watch Host objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_host_watch_helper import ClusterAutoMsgHostWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Host objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_host()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_host: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgHostWatchHelper**](ClusterAutoMsgHostWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_node**
> ClusterAutoMsgNodeWatchHelper watch_node()

Watch Node objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_node_watch_helper import ClusterAutoMsgNodeWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Node objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_node()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_node: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgNodeWatchHelper**](ClusterAutoMsgNodeWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_tenant**
> ClusterAutoMsgTenantWatchHelper watch_tenant()

Watch Tenant objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_tenant_watch_helper import ClusterAutoMsgTenantWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Tenant objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_tenant()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_tenant: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgTenantWatchHelper**](ClusterAutoMsgTenantWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_version**
> ClusterAutoMsgVersionWatchHelper watch_version()

Watch Version objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import cluster_v1_api
from pensando_dss.psm.models.cluster import *
from pensando_dss.psm.model.cluster_auto_msg_version_watch_helper import ClusterAutoMsgVersionWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_v1_api.ClusterV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Version objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_version()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling ClusterV1Api->watch_version: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**ClusterAutoMsgVersionWatchHelper**](ClusterAutoMsgVersionWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

