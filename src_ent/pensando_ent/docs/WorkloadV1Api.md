# psm.WorkloadV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_migration**](WorkloadV1Api.md#abort_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
[**abort_migration1**](WorkloadV1Api.md#abort_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
[**add_workload**](WorkloadV1Api.md#add_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads | Create Workload object
[**add_workload1**](WorkloadV1Api.md#add_workload1) | **POST** /configs/workload/v1/workloads | Create Workload object
[**delete_workload**](WorkloadV1Api.md#delete_workload) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Delete Workload object
[**delete_workload1**](WorkloadV1Api.md#delete_workload1) | **DELETE** /configs/workload/v1/workloads/{O.Name} | Delete Workload object
[**final_sync_migration**](WorkloadV1Api.md#final_sync_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
[**final_sync_migration1**](WorkloadV1Api.md#final_sync_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
[**finish_migration**](WorkloadV1Api.md#finish_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
[**finish_migration1**](WorkloadV1Api.md#finish_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
[**get_endpoint**](WorkloadV1Api.md#get_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints/{O.Name} | Get Endpoint object
[**get_endpoint1**](WorkloadV1Api.md#get_endpoint1) | **GET** /configs/workload/v1/endpoints/{O.Name} | Get Endpoint object
[**get_workload**](WorkloadV1Api.md#get_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Get Workload object
[**get_workload1**](WorkloadV1Api.md#get_workload1) | **GET** /configs/workload/v1/workloads/{O.Name} | Get Workload object
[**label_workload**](WorkloadV1Api.md#label_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/label | Label Workload object
[**label_workload1**](WorkloadV1Api.md#label_workload1) | **POST** /configs/workload/v1/workloads/{O.Name}/label | Label Workload object
[**list_endpoint**](WorkloadV1Api.md#list_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints | List Endpoint objects
[**list_endpoint1**](WorkloadV1Api.md#list_endpoint1) | **GET** /configs/workload/v1/endpoints | List Endpoint objects
[**list_workload**](WorkloadV1Api.md#list_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads | List Workload objects
[**list_workload1**](WorkloadV1Api.md#list_workload1) | **GET** /configs/workload/v1/workloads | List Workload objects
[**start_migration**](WorkloadV1Api.md#start_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/StartMigration | Start Workload Migration operation
[**start_migration1**](WorkloadV1Api.md#start_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/StartMigration | Start Workload Migration operation
[**update_workload**](WorkloadV1Api.md#update_workload) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Update Workload object
[**update_workload1**](WorkloadV1Api.md#update_workload1) | **PUT** /configs/workload/v1/workloads/{O.Name} | Update Workload object
[**watch_endpoint**](WorkloadV1Api.md#watch_endpoint) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
[**watch_endpoint1**](WorkloadV1Api.md#watch_endpoint1) | **GET** /configs/workload/v1/watch/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
[**watch_workload**](WorkloadV1Api.md#watch_workload) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
[**watch_workload1**](WorkloadV1Api.md#watch_workload1) | **GET** /configs/workload/v1/watch/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll


# **abort_migration**
> WorkloadWorkload abort_migration(o_tenant, o_name, body)

Abort Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Abort Workload Migration operation
        api_response = api_instance.abort_migration(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->abort_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **abort_migration1**
> WorkloadWorkload abort_migration1(o_name, body)

Abort Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Abort Workload Migration operation
        api_response = api_instance.abort_migration1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->abort_migration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **add_workload**
> WorkloadWorkload add_workload(o_tenant, body)

Create Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workload object
        api_response = api_instance.add_workload(o_tenant, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->add_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **add_workload1**
> WorkloadWorkload add_workload1(body)

Create Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workload object
        api_response = api_instance.add_workload1(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->add_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **delete_workload**
> WorkloadWorkload delete_workload(o_tenant, o_name)

Delete Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Workload object
        api_response = api_instance.delete_workload(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->delete_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **delete_workload1**
> WorkloadWorkload delete_workload1(o_name)

Delete Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Workload object
        api_response = api_instance.delete_workload1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->delete_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **final_sync_migration**
> WorkloadWorkload final_sync_migration(o_tenant, o_name, body)

Initiates the final sync for the Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the final sync for the Workload Migration operation
        api_response = api_instance.final_sync_migration(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->final_sync_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **final_sync_migration1**
> WorkloadWorkload final_sync_migration1(o_name, body)

Initiates the final sync for the Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the final sync for the Workload Migration operation
        api_response = api_instance.final_sync_migration1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->final_sync_migration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **finish_migration**
> WorkloadWorkload finish_migration(o_tenant, o_name, body)

Finish Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Finish Workload Migration operation
        api_response = api_instance.finish_migration(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->finish_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **finish_migration1**
> WorkloadWorkload finish_migration1(o_name, body)

Finish Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Finish Workload Migration operation
        api_response = api_instance.finish_migration1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->finish_migration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **get_endpoint**
> WorkloadEndpoint get_endpoint(o_tenant, o_name)

Get Endpoint object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_endpoint import WorkloadEndpoint
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_node_uuid = "spec.node-uuid_example" # str | The DSC Name or MAC where the endpoint should reside. (optional)
    spec_homing_host_addr = "spec.homing-host-addr_example" # str | IP of the DSC where this endpoint exists. (optional)
    spec_micro_segment_vlan = 1 # int | MicroSegmentVlan to be assigned to the endpoint. (optional)
    spec_node_uuid_list = [
        "spec.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)
    spec_type = "spec.type_example" # str | Type is the type of Endpoint that is being created - L2 or L3. (optional)
    status_workload_name = "status.workload-name_example" # str | VM or container name. (optional)
    status_network = "status.network_example" # str | network this endpoint belogs to. (optional)
    status_homing_host_addr = "status.homing-host-addr_example" # str | host address of the host where this endpoint exists. (optional)
    status_homing_host_name = "status.homing-host-name_example" # str | host name of the host where this endpoint exists. (optional)
    status_ipv4_address = "status.ipv4-address_example" # str | IPv4 address of the endpoint. (optional)
    status_ipv4_gateway = "status.ipv4-gateway_example" # str | IPv4 gateway for the endpoint. (optional)
    status_ipv6_address = "status.ipv6-address_example" # str | IPv6 address for the endpoint. (optional)
    status_ipv6_gateway = "status.ipv6-gateway_example" # str | IPv6 gateway. (optional)
    status_mac_address = "status.mac-address_example" # str | Mac address of the endpoint. Should be a valid MAC address. (optional)
    status_node_uuid = "status.node-uuid_example" # str | homing host's UUID. (optional)
    status_endpoint_state = "status.EndpointState_example" # str | endpoint FSM state. (optional)
    status_security_groups = [
        "status.SecurityGroups_example",
    ] # [str] | security groups. (optional)
    status_micro_segment_vlan = 1 # int | micro-segment VLAN. (optional)
    migration_status = "migration.status_example" # str | Status of migration. (optional)
    status_ipv4_addresses = [
        "status.ipv4-addresses_example",
    ] # [str] | IPv4 addresses of the endpoint. (optional)
    status_ipv4_gateways = [
        "status.ipv4-gateways_example",
    ] # [str] | IPv4 gateways for the endpoint. (optional)
    status_ipv6_addresses = [
        "status.ipv6-addresses_example",
    ] # [str] | IPv6 addresses for the endpoint. (optional)
    status_ipv6_gateways = [
        "status.ipv6-gateways_example",
    ] # [str] | IPv6 gateways. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this endpoint. (optional)
    status_node_uuid_list = [
        "status.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)
    status_workload_names = [
        "status.workload-names_example",
    ] # [str] | WorkloadNames associated with endpoint. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_node_uuid=spec_node_uuid, spec_homing_host_addr=spec_homing_host_addr, spec_micro_segment_vlan=spec_micro_segment_vlan, spec_node_uuid_list=spec_node_uuid_list, spec_type=spec_type, status_workload_name=status_workload_name, status_network=status_network, status_homing_host_addr=status_homing_host_addr, status_homing_host_name=status_homing_host_name, status_ipv4_address=status_ipv4_address, status_ipv4_gateway=status_ipv4_gateway, status_ipv6_address=status_ipv6_address, status_ipv6_gateway=status_ipv6_gateway, status_mac_address=status_mac_address, status_node_uuid=status_node_uuid, status_endpoint_state=status_endpoint_state, status_security_groups=status_security_groups, status_micro_segment_vlan=status_micro_segment_vlan, migration_status=migration_status, status_ipv4_addresses=status_ipv4_addresses, status_ipv4_gateways=status_ipv4_gateways, status_ipv6_addresses=status_ipv6_addresses, status_ipv6_gateways=status_ipv6_gateways, status_mirror_sessions=status_mirror_sessions, status_node_uuid_list=status_node_uuid_list, status_workload_names=status_workload_names)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_node_uuid** | **str**| The DSC Name or MAC where the endpoint should reside. | [optional]
 **spec_homing_host_addr** | **str**| IP of the DSC where this endpoint exists. | [optional]
 **spec_micro_segment_vlan** | **int**| MicroSegmentVlan to be assigned to the endpoint. | [optional]
 **spec_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]
 **spec_type** | **str**| Type is the type of Endpoint that is being created - L2 or L3. | [optional]
 **status_workload_name** | **str**| VM or container name. | [optional]
 **status_network** | **str**| network this endpoint belogs to. | [optional]
 **status_homing_host_addr** | **str**| host address of the host where this endpoint exists. | [optional]
 **status_homing_host_name** | **str**| host name of the host where this endpoint exists. | [optional]
 **status_ipv4_address** | **str**| IPv4 address of the endpoint. | [optional]
 **status_ipv4_gateway** | **str**| IPv4 gateway for the endpoint. | [optional]
 **status_ipv6_address** | **str**| IPv6 address for the endpoint. | [optional]
 **status_ipv6_gateway** | **str**| IPv6 gateway. | [optional]
 **status_mac_address** | **str**| Mac address of the endpoint. Should be a valid MAC address. | [optional]
 **status_node_uuid** | **str**| homing host&#39;s UUID. | [optional]
 **status_endpoint_state** | **str**| endpoint FSM state. | [optional]
 **status_security_groups** | **[str]**| security groups. | [optional]
 **status_micro_segment_vlan** | **int**| micro-segment VLAN. | [optional]
 **migration_status** | **str**| Status of migration. | [optional]
 **status_ipv4_addresses** | **[str]**| IPv4 addresses of the endpoint. | [optional]
 **status_ipv4_gateways** | **[str]**| IPv4 gateways for the endpoint. | [optional]
 **status_ipv6_addresses** | **[str]**| IPv6 addresses for the endpoint. | [optional]
 **status_ipv6_gateways** | **[str]**| IPv6 gateways. | [optional]
 **status_mirror_sessions** | **[str]**| MirrorSessions list of mirror sessions enabled on this endpoint. | [optional]
 **status_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]
 **status_workload_names** | **[str]**| WorkloadNames associated with endpoint. | [optional]

### Return type

[**WorkloadEndpoint**](WorkloadEndpoint.md)

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

# **get_endpoint1**
> WorkloadEndpoint get_endpoint1(o_name)

Get Endpoint object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_endpoint import WorkloadEndpoint
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_node_uuid = "spec.node-uuid_example" # str | The DSC Name or MAC where the endpoint should reside. (optional)
    spec_homing_host_addr = "spec.homing-host-addr_example" # str | IP of the DSC where this endpoint exists. (optional)
    spec_micro_segment_vlan = 1 # int | MicroSegmentVlan to be assigned to the endpoint. (optional)
    spec_node_uuid_list = [
        "spec.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)
    spec_type = "spec.type_example" # str | Type is the type of Endpoint that is being created - L2 or L3. (optional)
    status_workload_name = "status.workload-name_example" # str | VM or container name. (optional)
    status_network = "status.network_example" # str | network this endpoint belogs to. (optional)
    status_homing_host_addr = "status.homing-host-addr_example" # str | host address of the host where this endpoint exists. (optional)
    status_homing_host_name = "status.homing-host-name_example" # str | host name of the host where this endpoint exists. (optional)
    status_ipv4_address = "status.ipv4-address_example" # str | IPv4 address of the endpoint. (optional)
    status_ipv4_gateway = "status.ipv4-gateway_example" # str | IPv4 gateway for the endpoint. (optional)
    status_ipv6_address = "status.ipv6-address_example" # str | IPv6 address for the endpoint. (optional)
    status_ipv6_gateway = "status.ipv6-gateway_example" # str | IPv6 gateway. (optional)
    status_mac_address = "status.mac-address_example" # str | Mac address of the endpoint. Should be a valid MAC address. (optional)
    status_node_uuid = "status.node-uuid_example" # str | homing host's UUID. (optional)
    status_endpoint_state = "status.EndpointState_example" # str | endpoint FSM state. (optional)
    status_security_groups = [
        "status.SecurityGroups_example",
    ] # [str] | security groups. (optional)
    status_micro_segment_vlan = 1 # int | micro-segment VLAN. (optional)
    migration_status = "migration.status_example" # str | Status of migration. (optional)
    status_ipv4_addresses = [
        "status.ipv4-addresses_example",
    ] # [str] | IPv4 addresses of the endpoint. (optional)
    status_ipv4_gateways = [
        "status.ipv4-gateways_example",
    ] # [str] | IPv4 gateways for the endpoint. (optional)
    status_ipv6_addresses = [
        "status.ipv6-addresses_example",
    ] # [str] | IPv6 addresses for the endpoint. (optional)
    status_ipv6_gateways = [
        "status.ipv6-gateways_example",
    ] # [str] | IPv6 gateways. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this endpoint. (optional)
    status_node_uuid_list = [
        "status.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)
    status_workload_names = [
        "status.workload-names_example",
    ] # [str] | WorkloadNames associated with endpoint. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_node_uuid=spec_node_uuid, spec_homing_host_addr=spec_homing_host_addr, spec_micro_segment_vlan=spec_micro_segment_vlan, spec_node_uuid_list=spec_node_uuid_list, spec_type=spec_type, status_workload_name=status_workload_name, status_network=status_network, status_homing_host_addr=status_homing_host_addr, status_homing_host_name=status_homing_host_name, status_ipv4_address=status_ipv4_address, status_ipv4_gateway=status_ipv4_gateway, status_ipv6_address=status_ipv6_address, status_ipv6_gateway=status_ipv6_gateway, status_mac_address=status_mac_address, status_node_uuid=status_node_uuid, status_endpoint_state=status_endpoint_state, status_security_groups=status_security_groups, status_micro_segment_vlan=status_micro_segment_vlan, migration_status=migration_status, status_ipv4_addresses=status_ipv4_addresses, status_ipv4_gateways=status_ipv4_gateways, status_ipv6_addresses=status_ipv6_addresses, status_ipv6_gateways=status_ipv6_gateways, status_mirror_sessions=status_mirror_sessions, status_node_uuid_list=status_node_uuid_list, status_workload_names=status_workload_names)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_node_uuid** | **str**| The DSC Name or MAC where the endpoint should reside. | [optional]
 **spec_homing_host_addr** | **str**| IP of the DSC where this endpoint exists. | [optional]
 **spec_micro_segment_vlan** | **int**| MicroSegmentVlan to be assigned to the endpoint. | [optional]
 **spec_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]
 **spec_type** | **str**| Type is the type of Endpoint that is being created - L2 or L3. | [optional]
 **status_workload_name** | **str**| VM or container name. | [optional]
 **status_network** | **str**| network this endpoint belogs to. | [optional]
 **status_homing_host_addr** | **str**| host address of the host where this endpoint exists. | [optional]
 **status_homing_host_name** | **str**| host name of the host where this endpoint exists. | [optional]
 **status_ipv4_address** | **str**| IPv4 address of the endpoint. | [optional]
 **status_ipv4_gateway** | **str**| IPv4 gateway for the endpoint. | [optional]
 **status_ipv6_address** | **str**| IPv6 address for the endpoint. | [optional]
 **status_ipv6_gateway** | **str**| IPv6 gateway. | [optional]
 **status_mac_address** | **str**| Mac address of the endpoint. Should be a valid MAC address. | [optional]
 **status_node_uuid** | **str**| homing host&#39;s UUID. | [optional]
 **status_endpoint_state** | **str**| endpoint FSM state. | [optional]
 **status_security_groups** | **[str]**| security groups. | [optional]
 **status_micro_segment_vlan** | **int**| micro-segment VLAN. | [optional]
 **migration_status** | **str**| Status of migration. | [optional]
 **status_ipv4_addresses** | **[str]**| IPv4 addresses of the endpoint. | [optional]
 **status_ipv4_gateways** | **[str]**| IPv4 gateways for the endpoint. | [optional]
 **status_ipv6_addresses** | **[str]**| IPv6 addresses for the endpoint. | [optional]
 **status_ipv6_gateways** | **[str]**| IPv6 gateways. | [optional]
 **status_mirror_sessions** | **[str]**| MirrorSessions list of mirror sessions enabled on this endpoint. | [optional]
 **status_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]
 **status_workload_names** | **[str]**| WorkloadNames associated with endpoint. | [optional]

### Return type

[**WorkloadEndpoint**](WorkloadEndpoint.md)

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

# **get_workload**
> WorkloadWorkload get_workload(o_tenant, o_name)

Get Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_host_name = "spec.host-name_example" # str | Hostname of the server where the workload should be running. (optional)
    spec_migration_timeout = "spec.migration-timeout_example" # str | Should be a valid time duration. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_host_name = "status.host-name_example" # str | Hostname of the server where the workload is currently running. (optional)
    migration_status_stage = "migration-status.stage_example" # str | Controller's migration stage. (optional)
    migration_status_started_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | migration start time. (optional)
    migration_status_status = "migration-status.status_example" # str | The status from the dataplane performing migration. (optional)
    migration_status_completed_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | migration completion time. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this workload. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Workload object
        api_response = api_instance.get_workload(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Workload object
        api_response = api_instance.get_workload(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_host_name=spec_host_name, spec_migration_timeout=spec_migration_timeout, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs, status_host_name=status_host_name, migration_status_stage=migration_status_stage, migration_status_started_at=migration_status_started_at, migration_status_status=migration_status_status, migration_status_completed_at=migration_status_completed_at, status_mirror_sessions=status_mirror_sessions)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_host_name** | **str**| Hostname of the server where the workload should be running. | [optional]
 **spec_migration_timeout** | **str**| Should be a valid time duration. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_host_name** | **str**| Hostname of the server where the workload is currently running. | [optional]
 **migration_status_stage** | **str**| Controller&#39;s migration stage. | [optional]
 **migration_status_started_at** | **datetime**| migration start time. | [optional]
 **migration_status_status** | **str**| The status from the dataplane performing migration. | [optional]
 **migration_status_completed_at** | **datetime**| migration completion time. | [optional]
 **status_mirror_sessions** | **[str]**| MirrorSessions list of mirror sessions enabled on this workload. | [optional]

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **get_workload1**
> WorkloadWorkload get_workload1(o_name)

Get Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_host_name = "spec.host-name_example" # str | Hostname of the server where the workload should be running. (optional)
    spec_migration_timeout = "spec.migration-timeout_example" # str | Should be a valid time duration. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_host_name = "status.host-name_example" # str | Hostname of the server where the workload is currently running. (optional)
    migration_status_stage = "migration-status.stage_example" # str | Controller's migration stage. (optional)
    migration_status_started_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | migration start time. (optional)
    migration_status_status = "migration-status.status_example" # str | The status from the dataplane performing migration. (optional)
    migration_status_completed_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | migration completion time. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this workload. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Workload object
        api_response = api_instance.get_workload1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Workload object
        api_response = api_instance.get_workload1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_host_name=spec_host_name, spec_migration_timeout=spec_migration_timeout, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs, status_host_name=status_host_name, migration_status_stage=migration_status_stage, migration_status_started_at=migration_status_started_at, migration_status_status=migration_status_status, migration_status_completed_at=migration_status_completed_at, status_mirror_sessions=status_mirror_sessions)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_host_name** | **str**| Hostname of the server where the workload should be running. | [optional]
 **spec_migration_timeout** | **str**| Should be a valid time duration. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_host_name** | **str**| Hostname of the server where the workload is currently running. | [optional]
 **migration_status_stage** | **str**| Controller&#39;s migration stage. | [optional]
 **migration_status_started_at** | **datetime**| migration start time. | [optional]
 **migration_status_status** | **str**| The status from the dataplane performing migration. | [optional]
 **migration_status_completed_at** | **datetime**| migration completion time. | [optional]
 **status_mirror_sessions** | **[str]**| MirrorSessions list of mirror sessions enabled on this workload. | [optional]

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **label_workload**
> WorkloadWorkload label_workload(o_tenant, o_name, body)

Label Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label Workload object
        api_response = api_instance.label_workload(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->label_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **label_workload1**
> WorkloadWorkload label_workload1(o_name, body)

Label Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
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
        # Label Workload object
        api_response = api_instance.label_workload1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->label_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **list_endpoint**
> WorkloadEndpointList list_endpoint(o_tenant)

List Endpoint objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_endpoint_list import WorkloadEndpointList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Endpoint objects
        api_response = api_instance.list_endpoint(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_endpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Endpoint objects
        api_response = api_instance.list_endpoint(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadEndpointList**](WorkloadEndpointList.md)

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

# **list_endpoint1**
> WorkloadEndpointList list_endpoint1()

List Endpoint objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_endpoint_list import WorkloadEndpointList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Endpoint objects
        api_response = api_instance.list_endpoint1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_endpoint1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadEndpointList**](WorkloadEndpointList.md)

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

# **list_workload**
> WorkloadWorkloadList list_workload(o_tenant)

List Workload objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload_list import WorkloadWorkloadList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Workload objects
        api_response = api_instance.list_workload(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Workload objects
        api_response = api_instance.list_workload(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadWorkloadList**](WorkloadWorkloadList.md)

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

# **list_workload1**
> WorkloadWorkloadList list_workload1()

List Workload objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload_list import WorkloadWorkloadList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Workload objects
        api_response = api_instance.list_workload1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadWorkloadList**](WorkloadWorkloadList.md)

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

# **start_migration**
> WorkloadWorkload start_migration(o_tenant, o_name, body)

Start Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Start Workload Migration operation
        api_response = api_instance.start_migration(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->start_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **start_migration1**
> WorkloadWorkload start_migration1(o_name, body)

Start Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Start Workload Migration operation
        api_response = api_instance.start_migration1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->start_migration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **update_workload**
> WorkloadWorkload update_workload(o_tenant, o_name, body)

Update Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Workload object
        api_response = api_instance.update_workload(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->update_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **update_workload1**
> WorkloadWorkload update_workload1(o_name, body)

Update Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
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
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
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
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Workload object
        api_response = api_instance.update_workload1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->update_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkload**](WorkloadWorkload.md)|  |

### Return type

[**WorkloadWorkload**](WorkloadWorkload.md)

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

# **watch_endpoint**
> WorkloadAutoMsgEndpointWatchHelper watch_endpoint(o_tenant)

Watch Endpoint objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_auto_msg_endpoint_watch_helper import WorkloadAutoMsgEndpointWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Endpoint objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_endpoint(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_endpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Endpoint objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_endpoint(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadAutoMsgEndpointWatchHelper**](WorkloadAutoMsgEndpointWatchHelper.md)

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

# **watch_endpoint1**
> WorkloadAutoMsgEndpointWatchHelper watch_endpoint1()

Watch Endpoint objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.workload_auto_msg_endpoint_watch_helper import WorkloadAutoMsgEndpointWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Endpoint objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_endpoint1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_endpoint1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadAutoMsgEndpointWatchHelper**](WorkloadAutoMsgEndpointWatchHelper.md)

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

# **watch_workload**
> WorkloadAutoMsgWorkloadWatchHelper watch_workload(o_tenant)

Watch Workload objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.workload_auto_msg_workload_watch_helper import WorkloadAutoMsgWorkloadWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Workload objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Workload objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadAutoMsgWorkloadWatchHelper**](WorkloadAutoMsgWorkloadWatchHelper.md)

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

# **watch_workload1**
> WorkloadAutoMsgWorkloadWatchHelper watch_workload1()

Watch Workload objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import workload_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.workload_auto_msg_workload_watch_helper import WorkloadAutoMsgWorkloadWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Workload objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**WorkloadAutoMsgWorkloadWatchHelper**](WorkloadAutoMsgWorkloadWatchHelper.md)

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

