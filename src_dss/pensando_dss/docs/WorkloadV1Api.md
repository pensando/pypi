# psm.WorkloadV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_migration**](WorkloadV1Api.md#abort_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
[**abort_migration1**](WorkloadV1Api.md#abort_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/AbortMigration | Abort Workload Migration operation
[**add_workload**](WorkloadV1Api.md#add_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads | Create Workload object
[**add_workload1**](WorkloadV1Api.md#add_workload1) | **POST** /configs/workload/v1/workloads | Create Workload object
[**add_workload_group**](WorkloadV1Api.md#add_workload_group) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups | Create WorkloadGroup object
[**add_workload_group1**](WorkloadV1Api.md#add_workload_group1) | **POST** /configs/workload/v1/workloadgroups | Create WorkloadGroup object
[**delete_workload**](WorkloadV1Api.md#delete_workload) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Delete Workload object
[**delete_workload1**](WorkloadV1Api.md#delete_workload1) | **DELETE** /configs/workload/v1/workloads/{O.Name} | Delete Workload object
[**delete_workload_group**](WorkloadV1Api.md#delete_workload_group) | **DELETE** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Delete WorkloadGroup object
[**delete_workload_group1**](WorkloadV1Api.md#delete_workload_group1) | **DELETE** /configs/workload/v1/workloadgroups/{O.Name} | Delete WorkloadGroup object
[**final_sync_migration**](WorkloadV1Api.md#final_sync_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
[**final_sync_migration1**](WorkloadV1Api.md#final_sync_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinalSyncMigration | Initiates the final sync for the Workload Migration operation
[**finish_migration**](WorkloadV1Api.md#finish_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
[**finish_migration1**](WorkloadV1Api.md#finish_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/FinishMigration | Finish Workload Migration operation
[**get_endpoint**](WorkloadV1Api.md#get_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints/{O.Name} | Get Endpoint object
[**get_endpoint1**](WorkloadV1Api.md#get_endpoint1) | **GET** /configs/workload/v1/endpoints/{O.Name} | Get Endpoint object
[**get_workload**](WorkloadV1Api.md#get_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Get Workload object
[**get_workload1**](WorkloadV1Api.md#get_workload1) | **GET** /configs/workload/v1/workloads/{O.Name} | Get Workload object
[**get_workload_group**](WorkloadV1Api.md#get_workload_group) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Get WorkloadGroup object
[**get_workload_group1**](WorkloadV1Api.md#get_workload_group1) | **GET** /configs/workload/v1/workloadgroups/{O.Name} | Get WorkloadGroup object
[**label_workload**](WorkloadV1Api.md#label_workload) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/label | Label Workload object
[**label_workload1**](WorkloadV1Api.md#label_workload1) | **POST** /configs/workload/v1/workloads/{O.Name}/label | Label Workload object
[**label_workload_group**](WorkloadV1Api.md#label_workload_group) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name}/label | Label WorkloadGroup object
[**label_workload_group1**](WorkloadV1Api.md#label_workload_group1) | **POST** /configs/workload/v1/workloadgroups/{O.Name}/label | Label WorkloadGroup object
[**list_endpoint**](WorkloadV1Api.md#list_endpoint) | **GET** /configs/workload/v1/tenant/{O.Tenant}/endpoints | List Endpoint objects
[**list_endpoint1**](WorkloadV1Api.md#list_endpoint1) | **GET** /configs/workload/v1/endpoints | List Endpoint objects
[**list_workload**](WorkloadV1Api.md#list_workload) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloads | List Workload objects
[**list_workload1**](WorkloadV1Api.md#list_workload1) | **GET** /configs/workload/v1/workloads | List Workload objects
[**list_workload_group**](WorkloadV1Api.md#list_workload_group) | **GET** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups | List WorkloadGroup objects
[**list_workload_group1**](WorkloadV1Api.md#list_workload_group1) | **GET** /configs/workload/v1/workloadgroups | List WorkloadGroup objects
[**start_migration**](WorkloadV1Api.md#start_migration) | **POST** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name}/StartMigration | Start Workload Migration operation
[**start_migration1**](WorkloadV1Api.md#start_migration1) | **POST** /configs/workload/v1/workloads/{O.Name}/StartMigration | Start Workload Migration operation
[**update_workload**](WorkloadV1Api.md#update_workload) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloads/{O.Name} | Update Workload object
[**update_workload1**](WorkloadV1Api.md#update_workload1) | **PUT** /configs/workload/v1/workloads/{O.Name} | Update Workload object
[**update_workload_group**](WorkloadV1Api.md#update_workload_group) | **PUT** /configs/workload/v1/tenant/{O.Tenant}/workloadgroups/{O.Name} | Update WorkloadGroup object
[**update_workload_group1**](WorkloadV1Api.md#update_workload_group1) | **PUT** /configs/workload/v1/workloadgroups/{O.Name} | Update WorkloadGroup object
[**watch_endpoint**](WorkloadV1Api.md#watch_endpoint) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
[**watch_endpoint1**](WorkloadV1Api.md#watch_endpoint1) | **GET** /configs/workload/v1/watch/endpoints | Watch Endpoint objects. Supports WebSockets or HTTP long poll
[**watch_workload**](WorkloadV1Api.md#watch_workload) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
[**watch_workload1**](WorkloadV1Api.md#watch_workload1) | **GET** /configs/workload/v1/watch/workloads | Watch Workload objects. Supports WebSockets or HTTP long poll
[**watch_workload_group**](WorkloadV1Api.md#watch_workload_group) | **GET** /configs/workload/v1/watch/tenant/{O.Tenant}/workloadgroups | Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll
[**watch_workload_group1**](WorkloadV1Api.md#watch_workload_group1) | **GET** /configs/workload/v1/watch/workloadgroups | Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll


# **abort_migration**
> WorkloadWorkload abort_migration(o_tenant, body)

Abort Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Abort Workload Migration operation
        api_response = api_instance.abort_migration(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->abort_migration: %s\n" % e)

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

# **abort_migration1**
> WorkloadWorkload abort_migration1(o_name, body)

Abort Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Abort Workload Migration operation
        api_response = api_instance.abort_migration1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workload object
        api_response = api_instance.add_workload(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workload object
        api_response = api_instance.add_workload1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

# **add_workload_group**
> WorkloadWorkloadGroup add_workload_group(o_tenant, body)

Create WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkloadGroup(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        spec=WorkloadWorkloadGroupSpec(
            ip_block=[
                WorkloadIPBlock(
                    cidr="10.1.1.1/24, ff02::5/32 ",
                ),
            ],
            workload_selector=[
                LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        status=WorkloadWorkloadGroupStatus(
            id=1,
        ),
    ) # WorkloadWorkloadGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create WorkloadGroup object
        api_response = api_instance.add_workload_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->add_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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

# **add_workload_group1**
> WorkloadWorkloadGroup add_workload_group1(body)

Create WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    body = WorkloadWorkloadGroup(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        spec=WorkloadWorkloadGroupSpec(
            ip_block=[
                WorkloadIPBlock(
                    cidr="10.1.1.1/24, ff02::5/32 ",
                ),
            ],
            workload_selector=[
                LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        status=WorkloadWorkloadGroupStatus(
            id=1,
        ),
    ) # WorkloadWorkloadGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create WorkloadGroup object
        api_response = api_instance.add_workload_group1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->add_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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
> WorkloadWorkload delete_workload(o_tenant)

Delete Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Workload object
        api_response = api_instance.delete_workload(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->delete_workload: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Workload object
        api_response = api_instance.delete_workload1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

# **delete_workload_group**
> WorkloadWorkloadGroup delete_workload_group(o_tenant)

Delete WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete WorkloadGroup object
        api_response = api_instance.delete_workload_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->delete_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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

# **delete_workload_group1**
> WorkloadWorkloadGroup delete_workload_group1(o_name)

Delete WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete WorkloadGroup object
        api_response = api_instance.delete_workload_group1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->delete_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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
> WorkloadWorkload final_sync_migration(o_tenant, body)

Initiates the final sync for the Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the final sync for the Workload Migration operation
        api_response = api_instance.final_sync_migration(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->final_sync_migration: %s\n" % e)

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

# **final_sync_migration1**
> WorkloadWorkload final_sync_migration1(o_name, body)

Initiates the final sync for the Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the final sync for the Workload Migration operation
        api_response = api_instance.final_sync_migration1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> WorkloadWorkload finish_migration(o_tenant, body)

Finish Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Finish Workload Migration operation
        api_response = api_instance.finish_migration(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->finish_migration: %s\n" % e)

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

# **finish_migration1**
> WorkloadWorkload finish_migration1(o_name, body)

Finish Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Finish Workload Migration operation
        api_response = api_instance.finish_migration1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> WorkloadEndpoint get_endpoint(o_tenant)

Get Endpoint object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_endpoint import WorkloadEndpoint
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_node_uuid_list = [
        "spec.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_endpoint import WorkloadEndpoint
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_node_uuid_list = [
        "spec.node-uuid-list_example",
    ] # [str] | NodeUUIDList has the list of DSCs where a EP is supposed to go to. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Endpoint object
        api_response = api_instance.get_endpoint1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_endpoint1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_node_uuid_list** | **[str]**| NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional]

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
> WorkloadWorkload get_workload(o_tenant)

Get Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this workload. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Workload object
        api_response = api_instance.get_workload(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] | MirrorSessions list of mirror sessions enabled on this workload. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Workload object
        api_response = api_instance.get_workload1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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

# **get_workload_group**
> WorkloadWorkloadGroup get_workload_group(o_tenant)

Get WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get WorkloadGroup object
        api_response = api_instance.get_workload_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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

# **get_workload_group1**
> WorkloadWorkloadGroup get_workload_group1(o_name)

Get WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get WorkloadGroup object
        api_response = api_instance.get_workload_group1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->get_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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
> WorkloadWorkload label_workload(o_tenant, body)

Label Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.label_workload(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->label_workload: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

# **label_workload_group**
> WorkloadWorkloadGroup label_workload_group(o_tenant, body)

Label WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        # Label WorkloadGroup object
        api_response = api_instance.label_workload_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->label_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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

# **label_workload_group1**
> WorkloadWorkloadGroup label_workload_group1(o_name, body)

Label WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        # Label WorkloadGroup object
        api_response = api_instance.label_workload_group1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->label_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_endpoint_list import WorkloadEndpointList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Endpoint objects
        api_response = api_instance.list_endpoint(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_endpoint: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_endpoint_list import WorkloadEndpointList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Endpoint objects
        api_response = api_instance.list_endpoint1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_endpoint1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_list import WorkloadWorkloadList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Workload objects
        api_response = api_instance.list_workload(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_list import WorkloadWorkloadList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Workload objects
        api_response = api_instance.list_workload1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

# **list_workload_group**
> WorkloadWorkloadGroupList list_workload_group(o_tenant)

List WorkloadGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group_list import WorkloadWorkloadGroupList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List WorkloadGroup objects
        api_response = api_instance.list_workload_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**WorkloadWorkloadGroupList**](WorkloadWorkloadGroupList.md)

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

# **list_workload_group1**
> WorkloadWorkloadGroupList list_workload_group1()

List WorkloadGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group_list import WorkloadWorkloadGroupList
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List WorkloadGroup objects
        api_response = api_instance.list_workload_group1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->list_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**WorkloadWorkloadGroupList**](WorkloadWorkloadGroupList.md)

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
> WorkloadWorkload start_migration(o_tenant, body)

Start Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Start Workload Migration operation
        api_response = api_instance.start_migration(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->start_migration: %s\n" % e)

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

# **start_migration1**
> WorkloadWorkload start_migration1(o_name, body)

Start Workload Migration operation

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Start Workload Migration operation
        api_response = api_instance.start_migration1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> WorkloadWorkload update_workload(o_tenant, body)

Update Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Workload object
        api_response = api_instance.update_workload(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->update_workload: %s\n" % e)

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

# **update_workload1**
> WorkloadWorkload update_workload1(o_name, body)

Update Workload object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload import WorkloadWorkload
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                    pending_workload_groups=[
                        "pending_workload_groups_example",
                    ],
                    vni=1,
                    workload_groups=[
                        "workload_groups_example",
                    ],
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                flow_migration_status=[
                    WorkloadInterfaceMigrationStatus(
                        errors=[
                            "errors_example",
                        ],
                        ip_addresses="ip_addresses_example",
                        mac_address="mac_address_example",
                    ),
                ],
                from_host_name="from_host_name_example",
                migration_id="migration_id_example",
                migration_transaction_id=1,
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
                to_host_name="to_host_name_example",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=WorkloadPropagationStatus(
                endpoint_prop_status=[
                    WorkloadEndpointPropStatus(
                        dse_status=[
                            ApiDSEStatus(
                                dse_id="dse_id_example",
                                dse_info_status="dse_info_status_example",
                            ),
                        ],
                        generation_id="generation_id_example",
                        mac_address="mac_address_example",
                        name="name_example",
                        pdt_status=[
                            ApiPDTStatus(
                                name="name_example",
                                pending=1,
                                pending_dses=[
                                    "pending_dses_example",
                                ],
                                status="status_example",
                                updated=1,
                            ),
                        ],
                        pending=1,
                        pending_dses=[
                            "pending_dses_example",
                        ],
                        status="status_example",
                        updated=1,
                    ),
                ],
                status="status_example",
            ),
            workload_groups=[],
        ),
    ) # WorkloadWorkload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Workload object
        api_response = api_instance.update_workload1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

# **update_workload_group**
> WorkloadWorkloadGroup update_workload_group(o_tenant, body)

Update WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = WorkloadWorkloadGroup(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        spec=WorkloadWorkloadGroupSpec(
            ip_block=[
                WorkloadIPBlock(
                    cidr="10.1.1.1/24, ff02::5/32 ",
                ),
            ],
            workload_selector=[
                LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        status=WorkloadWorkloadGroupStatus(
            id=1,
        ),
    ) # WorkloadWorkloadGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update WorkloadGroup object
        api_response = api_instance.update_workload_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->update_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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

# **update_workload_group1**
> WorkloadWorkloadGroup update_workload_group1(o_name, body)

Update WorkloadGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_workload_group import WorkloadWorkloadGroup
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = WorkloadWorkloadGroup(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        spec=WorkloadWorkloadGroupSpec(
            ip_block=[
                WorkloadIPBlock(
                    cidr="10.1.1.1/24, ff02::5/32 ",
                ),
            ],
            workload_selector=[
                LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        status=WorkloadWorkloadGroupStatus(
            id=1,
        ),
    ) # WorkloadWorkloadGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update WorkloadGroup object
        api_response = api_instance.update_workload_group1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->update_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)|  |

### Return type

[**WorkloadWorkloadGroup**](WorkloadWorkloadGroup.md)

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_endpoint_watch_helper import WorkloadAutoMsgEndpointWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Endpoint objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_endpoint(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_endpoint: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_endpoint_watch_helper import WorkloadAutoMsgEndpointWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Endpoint objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_endpoint1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_endpoint1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_workload_watch_helper import WorkloadAutoMsgWorkloadWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Workload objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_workload_watch_helper import WorkloadAutoMsgWorkloadWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Workload objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

# **watch_workload_group**
> WorkloadAutoMsgWorkloadGroupWatchHelper watch_workload_group(o_tenant)

Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_workload_group_watch_helper import WorkloadAutoMsgWorkloadGroupWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**WorkloadAutoMsgWorkloadGroupWatchHelper**](WorkloadAutoMsgWorkloadGroupWatchHelper.md)

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

# **watch_workload_group1**
> WorkloadAutoMsgWorkloadGroupWatchHelper watch_workload_group1()

Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import workload_v1_api
from pensando_dss.psm.models.workload import *
from pensando_dss.psm.model.workload_auto_msg_workload_group_watch_helper import WorkloadAutoMsgWorkloadGroupWatchHelper
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
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch WorkloadGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_workload_group1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->watch_workload_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**WorkloadAutoMsgWorkloadGroupWatchHelper**](WorkloadAutoMsgWorkloadGroupWatchHelper.md)

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

