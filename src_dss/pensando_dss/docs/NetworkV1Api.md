# psm.NetworkV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ipam_policy**](NetworkV1Api.md#add_ipam_policy) | **POST** /configs/network/v1/tenant/{O.Tenant}/ipam-policies | Create IPAMPolicy object
[**add_ipam_policy1**](NetworkV1Api.md#add_ipam_policy1) | **POST** /configs/network/v1/ipam-policies | Create IPAMPolicy object
[**add_network**](NetworkV1Api.md#add_network) | **POST** /configs/network/v1/tenant/{O.Tenant}/networks | Create Network object
[**add_network1**](NetworkV1Api.md#add_network1) | **POST** /configs/network/v1/networks | Create Network object
[**add_policer_profile**](NetworkV1Api.md#add_policer_profile) | **POST** /configs/network/v1/tenant/{O.Tenant}/policer-profile | Create PolicerProfile object
[**add_policer_profile1**](NetworkV1Api.md#add_policer_profile1) | **POST** /configs/network/v1/policer-profile | Create PolicerProfile object
[**add_routing_config**](NetworkV1Api.md#add_routing_config) | **POST** /configs/network/v1/routing-config | Create RoutingConfig object
[**add_virtual_router**](NetworkV1Api.md#add_virtual_router) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtualrouters | Create VirtualRouter object
[**add_virtual_router1**](NetworkV1Api.md#add_virtual_router1) | **POST** /configs/network/v1/virtualrouters | Create VirtualRouter object
[**add_virtual_router_peering_group**](NetworkV1Api.md#add_virtual_router_peering_group) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups | Create VirtualRouterPeeringGroup object
[**add_virtual_router_peering_group1**](NetworkV1Api.md#add_virtual_router_peering_group1) | **POST** /configs/network/v1/virtual-router-peering-groups | Create VirtualRouterPeeringGroup object
[**delete_ipam_policy**](NetworkV1Api.md#delete_ipam_policy) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Delete IPAMPolicy object
[**delete_ipam_policy1**](NetworkV1Api.md#delete_ipam_policy1) | **DELETE** /configs/network/v1/ipam-policies/{O.Name} | Delete IPAMPolicy object
[**delete_network**](NetworkV1Api.md#delete_network) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Delete Network object
[**delete_network1**](NetworkV1Api.md#delete_network1) | **DELETE** /configs/network/v1/networks/{O.Name} | Delete Network object
[**delete_policer_profile**](NetworkV1Api.md#delete_policer_profile) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Delete PolicerProfile object
[**delete_policer_profile1**](NetworkV1Api.md#delete_policer_profile1) | **DELETE** /configs/network/v1/policer-profile/{O.Name} | Delete PolicerProfile object
[**delete_routing_config**](NetworkV1Api.md#delete_routing_config) | **DELETE** /configs/network/v1/routing-config/{O.Name} | Delete RoutingConfig object
[**delete_virtual_router**](NetworkV1Api.md#delete_virtual_router) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Delete VirtualRouter object
[**delete_virtual_router1**](NetworkV1Api.md#delete_virtual_router1) | **DELETE** /configs/network/v1/virtualrouters/{O.Name} | Delete VirtualRouter object
[**delete_virtual_router_peering_group**](NetworkV1Api.md#delete_virtual_router_peering_group) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Delete VirtualRouterPeeringGroup object
[**delete_virtual_router_peering_group1**](NetworkV1Api.md#delete_virtual_router_peering_group1) | **DELETE** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Delete VirtualRouterPeeringGroup object
[**get_ipam_policy**](NetworkV1Api.md#get_ipam_policy) | **GET** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Get IPAMPolicy object
[**get_ipam_policy1**](NetworkV1Api.md#get_ipam_policy1) | **GET** /configs/network/v1/ipam-policies/{O.Name} | Get IPAMPolicy object
[**get_network**](NetworkV1Api.md#get_network) | **GET** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Get Network object
[**get_network1**](NetworkV1Api.md#get_network1) | **GET** /configs/network/v1/networks/{O.Name} | Get Network object
[**get_network_interface**](NetworkV1Api.md#get_network_interface) | **GET** /configs/network/v1/networkinterfaces/{O.Name} | Get NetworkInterface object
[**get_policer_profile**](NetworkV1Api.md#get_policer_profile) | **GET** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Get PolicerProfile object
[**get_policer_profile1**](NetworkV1Api.md#get_policer_profile1) | **GET** /configs/network/v1/policer-profile/{O.Name} | Get PolicerProfile object
[**get_route_table**](NetworkV1Api.md#get_route_table) | **GET** /configs/network/v1/tenant/{O.Tenant}/route-tables/{O.Name} | Get RouteTable object
[**get_route_table1**](NetworkV1Api.md#get_route_table1) | **GET** /configs/network/v1/route-tables/{O.Name} | Get RouteTable object
[**get_routing_config**](NetworkV1Api.md#get_routing_config) | **GET** /configs/network/v1/routing-config/{O.Name} | Get RoutingConfig object
[**get_virtual_router**](NetworkV1Api.md#get_virtual_router) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Get VirtualRouter object
[**get_virtual_router1**](NetworkV1Api.md#get_virtual_router1) | **GET** /configs/network/v1/virtualrouters/{O.Name} | Get VirtualRouter object
[**get_virtual_router_peering_group**](NetworkV1Api.md#get_virtual_router_peering_group) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Get VirtualRouterPeeringGroup object
[**get_virtual_router_peering_group1**](NetworkV1Api.md#get_virtual_router_peering_group1) | **GET** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Get VirtualRouterPeeringGroup object
[**label_ipam_policy**](NetworkV1Api.md#label_ipam_policy) | **POST** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name}/label | Label IPAMPolicy object
[**label_ipam_policy1**](NetworkV1Api.md#label_ipam_policy1) | **POST** /configs/network/v1/ipam-policies/{O.Name}/label | Label IPAMPolicy object
[**label_network**](NetworkV1Api.md#label_network) | **POST** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name}/label | Label Network object
[**label_network1**](NetworkV1Api.md#label_network1) | **POST** /configs/network/v1/networks/{O.Name}/label | Label Network object
[**label_network_interface**](NetworkV1Api.md#label_network_interface) | **POST** /configs/network/v1/networkinterfaces/{O.Name}/label | Label NetworkInterface object
[**label_policer_profile**](NetworkV1Api.md#label_policer_profile) | **POST** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name}/label | Label PolicerProfile object
[**label_policer_profile1**](NetworkV1Api.md#label_policer_profile1) | **POST** /configs/network/v1/policer-profile/{O.Name}/label | Label PolicerProfile object
[**label_routing_config**](NetworkV1Api.md#label_routing_config) | **POST** /configs/network/v1/routing-config/{O.Name}/label | Label RoutingConfig object
[**label_virtual_router**](NetworkV1Api.md#label_virtual_router) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name}/label | Label VirtualRouter object
[**label_virtual_router1**](NetworkV1Api.md#label_virtual_router1) | **POST** /configs/network/v1/virtualrouters/{O.Name}/label | Label VirtualRouter object
[**label_virtual_router_peering_group**](NetworkV1Api.md#label_virtual_router_peering_group) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name}/label | Label VirtualRouterPeeringGroup object
[**label_virtual_router_peering_group1**](NetworkV1Api.md#label_virtual_router_peering_group1) | **POST** /configs/network/v1/virtual-router-peering-groups/{O.Name}/label | Label VirtualRouterPeeringGroup object
[**list_ipam_policy**](NetworkV1Api.md#list_ipam_policy) | **GET** /configs/network/v1/tenant/{O.Tenant}/ipam-policies | List IPAMPolicy objects
[**list_ipam_policy1**](NetworkV1Api.md#list_ipam_policy1) | **GET** /configs/network/v1/ipam-policies | List IPAMPolicy objects
[**list_network**](NetworkV1Api.md#list_network) | **GET** /configs/network/v1/tenant/{O.Tenant}/networks | List Network objects
[**list_network1**](NetworkV1Api.md#list_network1) | **GET** /configs/network/v1/networks | List Network objects
[**list_network_interface**](NetworkV1Api.md#list_network_interface) | **GET** /configs/network/v1/networkinterfaces | List NetworkInterface objects
[**list_policer_profile**](NetworkV1Api.md#list_policer_profile) | **GET** /configs/network/v1/tenant/{O.Tenant}/policer-profile | List PolicerProfile objects
[**list_policer_profile1**](NetworkV1Api.md#list_policer_profile1) | **GET** /configs/network/v1/policer-profile | List PolicerProfile objects
[**list_route_table**](NetworkV1Api.md#list_route_table) | **GET** /configs/network/v1/tenant/{O.Tenant}/route-tables | List RouteTable objects
[**list_route_table1**](NetworkV1Api.md#list_route_table1) | **GET** /configs/network/v1/route-tables | List RouteTable objects
[**list_routing_config**](NetworkV1Api.md#list_routing_config) | **GET** /configs/network/v1/routing-config | List RoutingConfig objects
[**list_virtual_router**](NetworkV1Api.md#list_virtual_router) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtualrouters | List VirtualRouter objects
[**list_virtual_router1**](NetworkV1Api.md#list_virtual_router1) | **GET** /configs/network/v1/virtualrouters | List VirtualRouter objects
[**list_virtual_router_peering_group**](NetworkV1Api.md#list_virtual_router_peering_group) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups | List VirtualRouterPeeringGroup objects
[**list_virtual_router_peering_group1**](NetworkV1Api.md#list_virtual_router_peering_group1) | **GET** /configs/network/v1/virtual-router-peering-groups | List VirtualRouterPeeringGroup objects
[**update_ipam_policy**](NetworkV1Api.md#update_ipam_policy) | **PUT** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Update IPAMPolicy object
[**update_ipam_policy1**](NetworkV1Api.md#update_ipam_policy1) | **PUT** /configs/network/v1/ipam-policies/{O.Name} | Update IPAMPolicy object
[**update_network**](NetworkV1Api.md#update_network) | **PUT** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Update Network object
[**update_network1**](NetworkV1Api.md#update_network1) | **PUT** /configs/network/v1/networks/{O.Name} | Update Network object
[**update_network_interface**](NetworkV1Api.md#update_network_interface) | **PUT** /configs/network/v1/networkinterfaces/{O.Name} | Update NetworkInterface object
[**update_policer_profile**](NetworkV1Api.md#update_policer_profile) | **PUT** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Update PolicerProfile object
[**update_policer_profile1**](NetworkV1Api.md#update_policer_profile1) | **PUT** /configs/network/v1/policer-profile/{O.Name} | Update PolicerProfile object
[**update_routing_config**](NetworkV1Api.md#update_routing_config) | **PUT** /configs/network/v1/routing-config/{O.Name} | Update RoutingConfig object
[**update_virtual_router**](NetworkV1Api.md#update_virtual_router) | **PUT** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Update VirtualRouter object
[**update_virtual_router1**](NetworkV1Api.md#update_virtual_router1) | **PUT** /configs/network/v1/virtualrouters/{O.Name} | Update VirtualRouter object
[**update_virtual_router_peering_group**](NetworkV1Api.md#update_virtual_router_peering_group) | **PUT** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Update VirtualRouterPeeringGroup object
[**update_virtual_router_peering_group1**](NetworkV1Api.md#update_virtual_router_peering_group1) | **PUT** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Update VirtualRouterPeeringGroup object
[**watch_ipam_policy**](NetworkV1Api.md#watch_ipam_policy) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/ipam-policies | Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
[**watch_ipam_policy1**](NetworkV1Api.md#watch_ipam_policy1) | **GET** /configs/network/v1/watch/ipam-policies | Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
[**watch_network**](NetworkV1Api.md#watch_network) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/networks | Watch Network objects. Supports WebSockets or HTTP long poll
[**watch_network1**](NetworkV1Api.md#watch_network1) | **GET** /configs/network/v1/watch/networks | Watch Network objects. Supports WebSockets or HTTP long poll
[**watch_network_interface**](NetworkV1Api.md#watch_network_interface) | **GET** /configs/network/v1/watch/networkinterfaces | Watch NetworkInterface objects. Supports WebSockets or HTTP long poll
[**watch_policer_profile**](NetworkV1Api.md#watch_policer_profile) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/policer-profile | Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
[**watch_policer_profile1**](NetworkV1Api.md#watch_policer_profile1) | **GET** /configs/network/v1/watch/policer-profile | Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
[**watch_route_table**](NetworkV1Api.md#watch_route_table) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/route-tables | Watch RouteTable objects. Supports WebSockets or HTTP long poll
[**watch_route_table1**](NetworkV1Api.md#watch_route_table1) | **GET** /configs/network/v1/watch/route-tables | Watch RouteTable objects. Supports WebSockets or HTTP long poll
[**watch_routing_config**](NetworkV1Api.md#watch_routing_config) | **GET** /configs/network/v1/watch/routing-config | Watch RoutingConfig objects. Supports WebSockets or HTTP long poll
[**watch_virtual_router**](NetworkV1Api.md#watch_virtual_router) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/virtualrouters | Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
[**watch_virtual_router1**](NetworkV1Api.md#watch_virtual_router1) | **GET** /configs/network/v1/watch/virtualrouters | Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
[**watch_virtual_router_peering_group**](NetworkV1Api.md#watch_virtual_router_peering_group) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/virtual-router-peering-groups | Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
[**watch_virtual_router_peering_group1**](NetworkV1Api.md#watch_virtual_router_peering_group1) | **GET** /configs/network/v1/watch/virtual-router-peering-groups | Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll


# **add_ipam_policy**
> NetworkIPAMPolicy add_ipam_policy(o_tenant, body)

Create IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkIPAMPolicy(
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
        spec=NetworkIPAMPolicySpec(
            dhcp_relay=NetworkDHCPRelayPolicy(
                relay_servers=[
                    NetworkDHCPServer(
                        ip_address="10.1.1.1, ff02::5 ",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
            type="dhcp-relay",
        ),
        status=NetworkIPAMPolicyStatus(
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
    ) # NetworkIPAMPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create IPAMPolicy object
        api_response = api_instance.add_ipam_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **add_ipam_policy1**
> NetworkIPAMPolicy add_ipam_policy1(body)

Create IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkIPAMPolicy(
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
        spec=NetworkIPAMPolicySpec(
            dhcp_relay=NetworkDHCPRelayPolicy(
                relay_servers=[
                    NetworkDHCPServer(
                        ip_address="10.1.1.1, ff02::5 ",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
            type="dhcp-relay",
        ),
        status=NetworkIPAMPolicyStatus(
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
    ) # NetworkIPAMPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create IPAMPolicy object
        api_response = api_instance.add_ipam_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **add_network**
> NetworkNetwork add_network(o_tenant, body)

Create Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkNetwork(
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
        spec=NetworkNetworkSpec(
            egress_security_policy=[
                "egress_security_policy_example",
            ],
            ingress_security_policy=[
                "ingress_security_policy_example",
            ],
            ipam_config=NetworkIPAMConfig(
                ipv4_ipam_pool=[
                    NetworkIPAMPoolInfo(
                        ip_address_end="ip_address_end_example",
                        ip_address_start="ip_address_start_example",
                    ),
                ],
            ),
            ipam_policy="ipam_policy_example",
            ipv4_gateway="10.1.1.1, ff02::5 ",
            ipv4_subnet="10.1.1.1/24, ff02::5/32 ",
            ipv6_gateway="ipv6_gateway_example",
            ipv6_subnet="ipv6_subnet_example",
            orchestrators=[
                NetworkOrchestratorInfo(
                    namespace="namespace_example",
                    orchestrator_name="orchestrator_name_example",
                ),
            ],
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            type="bridged",
            virtual_router="virtual_router_example",
            vlan_id=0,
            vxlan_vni=0,
        ),
        status=NetworkNetworkStatus(
            allocated_ipv4_addrs='YQ==',
            id="id_example",
            oper_state="active",
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
            workloads=[
                "workloads_example",
            ],
        ),
    ) # NetworkNetwork | 

    # example passing only required values which don't have defaults set
    try:
        # Create Network object
        api_response = api_instance.add_network(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkNetwork**](NetworkNetwork.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **add_network1**
> NetworkNetwork add_network1(body)

Create Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkNetwork(
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
        spec=NetworkNetworkSpec(
            egress_security_policy=[
                "egress_security_policy_example",
            ],
            ingress_security_policy=[
                "ingress_security_policy_example",
            ],
            ipam_config=NetworkIPAMConfig(
                ipv4_ipam_pool=[
                    NetworkIPAMPoolInfo(
                        ip_address_end="ip_address_end_example",
                        ip_address_start="ip_address_start_example",
                    ),
                ],
            ),
            ipam_policy="ipam_policy_example",
            ipv4_gateway="10.1.1.1, ff02::5 ",
            ipv4_subnet="10.1.1.1/24, ff02::5/32 ",
            ipv6_gateway="ipv6_gateway_example",
            ipv6_subnet="ipv6_subnet_example",
            orchestrators=[
                NetworkOrchestratorInfo(
                    namespace="namespace_example",
                    orchestrator_name="orchestrator_name_example",
                ),
            ],
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            type="bridged",
            virtual_router="virtual_router_example",
            vlan_id=0,
            vxlan_vni=0,
        ),
        status=NetworkNetworkStatus(
            allocated_ipv4_addrs='YQ==',
            id="id_example",
            oper_state="active",
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
            workloads=[
                "workloads_example",
            ],
        ),
    ) # NetworkNetwork | 

    # example passing only required values which don't have defaults set
    try:
        # Create Network object
        api_response = api_instance.add_network1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkNetwork**](NetworkNetwork.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **add_policer_profile**
> NetworkPolicerProfile add_policer_profile(o_tenant, body)

Create PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkPolicerProfile(
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
        spec=NetworkPolicerProfileSpec(
            criteria=NetworkPolicerCriteria(
                burst_size="burst_size_example",
                bytes_per_second="bytes_per_second_example",
                packets_per_second="packets_per_second_example",
            ),
            exceed_action=NetworkPolicerAction(
                policer_action="drop",
            ),
        ),
        status=NetworkPolicerProfileStatus(
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
    ) # NetworkPolicerProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Create PolicerProfile object
        api_response = api_instance.add_policer_profile(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkPolicerProfile**](NetworkPolicerProfile.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **add_policer_profile1**
> NetworkPolicerProfile add_policer_profile1(body)

Create PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkPolicerProfile(
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
        spec=NetworkPolicerProfileSpec(
            criteria=NetworkPolicerCriteria(
                burst_size="burst_size_example",
                bytes_per_second="bytes_per_second_example",
                packets_per_second="packets_per_second_example",
            ),
            exceed_action=NetworkPolicerAction(
                policer_action="drop",
            ),
        ),
        status=NetworkPolicerProfileStatus(
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
    ) # NetworkPolicerProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Create PolicerProfile object
        api_response = api_instance.add_policer_profile1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkPolicerProfile**](NetworkPolicerProfile.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **add_routing_config**
> NetworkRoutingConfig add_routing_config(body)

Create RoutingConfig object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config import NetworkRoutingConfig
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkRoutingConfig(
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
        spec=NetworkRoutingConfigSpec(
            bgp_config=NetworkBGPConfig(
                as_number=ApiBgpAsn(
                    as_number=1,
                ),
                dsc_auto_config=True,
                holdtime=180,
                keepalive_interval=60,
                neighbors=[
                    NetworkBGPNeighbor(
                        allow_as_in=0,
                        dsc_auto_config=True,
                        enable_address_families=[
                            "enable_address_families_example",
                        ],
                        holdtime=0,
                        ip_address="10.1.1.1, ff02::5 ",
                        keepalive_interval=0,
                        multi_hop=64,
                        password="password_example",
                        remote_as=ApiBgpAsn(
                            as_number=1,
                        ),
                        shutdown=True,
                    ),
                ],
                router_id="10.1.1.1, ff02::5 ",
                suppress_default_resolution=True,
            ),
        ),
        status=NetworkRoutingConfigStatus(
            auth_config_status=[
                NetworkBGPAuthStatus(
                    ip_address="ip_address_example",
                    remote_as=ApiBgpAsn(
                        as_number=1,
                    ),
                    status="disabled",
                ),
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
    ) # NetworkRoutingConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Create RoutingConfig object
        api_response = api_instance.add_routing_config(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkRoutingConfig**](NetworkRoutingConfig.md)|  |

### Return type

[**NetworkRoutingConfig**](NetworkRoutingConfig.md)

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

# **add_virtual_router**
> NetworkVirtualRouter add_virtual_router(o_tenant, body)

Create VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkVirtualRouter(
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
        spec=NetworkVirtualRouterSpec(
            default_ipam_policy="default_ipam_policy_example",
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            router_mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            type="unknown",
            vxlan_vni=0,
        ),
        status=NetworkVirtualRouterStatus(
            id="id_example",
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
            rd=NetworkRouteDistinguisher(
                admin_value={},
                assigned_value=1,
                type="type0",
            ),
            route_table="route_table_example",
        ),
    ) # NetworkVirtualRouter | 

    # example passing only required values which don't have defaults set
    try:
        # Create VirtualRouter object
        api_response = api_instance.add_virtual_router(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkVirtualRouter**](NetworkVirtualRouter.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **add_virtual_router1**
> NetworkVirtualRouter add_virtual_router1(body)

Create VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkVirtualRouter(
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
        spec=NetworkVirtualRouterSpec(
            default_ipam_policy="default_ipam_policy_example",
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            router_mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            type="unknown",
            vxlan_vni=0,
        ),
        status=NetworkVirtualRouterStatus(
            id="id_example",
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
            rd=NetworkRouteDistinguisher(
                admin_value={},
                assigned_value=1,
                type="type0",
            ),
            route_table="route_table_example",
        ),
    ) # NetworkVirtualRouter | 

    # example passing only required values which don't have defaults set
    try:
        # Create VirtualRouter object
        api_response = api_instance.add_virtual_router1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkVirtualRouter**](NetworkVirtualRouter.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **add_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup add_virtual_router_peering_group(o_tenant, body)

Create VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkVirtualRouterPeeringGroup(
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
        spec=NetworkVirtualRouterPeeringGroupSpec(
            items=[
                NetworkVirtualRouterPeeringSpec(
                    ipv4_prefixes=[
                        "10.1.1.1/24, ff02::5/32 ",
                    ],
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status=NetworkVirtualRouterPeeringGroupStatus(
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
            route_tables={
                "key": NetworkVirtualRouterPeeringRouteTable(
                    routes=[
                        NetworkVirtualRouterPeeringRoute(
                            dest_virtual_router="dest_virtual_router_example",
                            ipv4_prefix="10.1.1.1/24, ff02::5/32 ",
                        ),
                    ],
                ),
            },
        ),
    ) # NetworkVirtualRouterPeeringGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create VirtualRouterPeeringGroup object
        api_response = api_instance.add_virtual_router_peering_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **add_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup add_virtual_router_peering_group1(body)

Create VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    body = NetworkVirtualRouterPeeringGroup(
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
        spec=NetworkVirtualRouterPeeringGroupSpec(
            items=[
                NetworkVirtualRouterPeeringSpec(
                    ipv4_prefixes=[
                        "10.1.1.1/24, ff02::5/32 ",
                    ],
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status=NetworkVirtualRouterPeeringGroupStatus(
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
            route_tables={
                "key": NetworkVirtualRouterPeeringRouteTable(
                    routes=[
                        NetworkVirtualRouterPeeringRoute(
                            dest_virtual_router="dest_virtual_router_example",
                            ipv4_prefix="10.1.1.1/24, ff02::5/32 ",
                        ),
                    ],
                ),
            },
        ),
    ) # NetworkVirtualRouterPeeringGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create VirtualRouterPeeringGroup object
        api_response = api_instance.add_virtual_router_peering_group1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->add_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **delete_ipam_policy**
> NetworkIPAMPolicy delete_ipam_policy(o_tenant)

Delete IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPAMPolicy object
        api_response = api_instance.delete_ipam_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **delete_ipam_policy1**
> NetworkIPAMPolicy delete_ipam_policy1(o_name)

Delete IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPAMPolicy object
        api_response = api_instance.delete_ipam_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **delete_network**
> NetworkNetwork delete_network(o_tenant)

Delete Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Network object
        api_response = api_instance.delete_network(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **delete_network1**
> NetworkNetwork delete_network1(o_name)

Delete Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Network object
        api_response = api_instance.delete_network1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **delete_policer_profile**
> NetworkPolicerProfile delete_policer_profile(o_tenant)

Delete PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete PolicerProfile object
        api_response = api_instance.delete_policer_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **delete_policer_profile1**
> NetworkPolicerProfile delete_policer_profile1(o_name)

Delete PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete PolicerProfile object
        api_response = api_instance.delete_policer_profile1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **delete_routing_config**
> NetworkRoutingConfig delete_routing_config(o_name)

Delete RoutingConfig object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config import NetworkRoutingConfig
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoutingConfig object
        api_response = api_instance.delete_routing_config(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkRoutingConfig**](NetworkRoutingConfig.md)

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

# **delete_virtual_router**
> NetworkVirtualRouter delete_virtual_router(o_tenant)

Delete VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouter object
        api_response = api_instance.delete_virtual_router(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **delete_virtual_router1**
> NetworkVirtualRouter delete_virtual_router1(o_name)

Delete VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouter object
        api_response = api_instance.delete_virtual_router1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **delete_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup delete_virtual_router_peering_group(o_tenant)

Delete VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouterPeeringGroup object
        api_response = api_instance.delete_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **delete_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup delete_virtual_router_peering_group1(o_name)

Delete VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouterPeeringGroup object
        api_response = api_instance.delete_virtual_router_peering_group1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **get_ipam_policy**
> NetworkIPAMPolicy get_ipam_policy(o_tenant)

Get IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **get_ipam_policy1**
> NetworkIPAMPolicy get_ipam_policy1(o_name)

Get IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **get_network**
> NetworkNetwork get_network(o_tenant)

Get Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    spec_ingress_security_policy = [
        "spec.ingress-security-policy_example",
    ] # [str] | Security Policy to apply in the ingress direction. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Network object
        api_response = api_instance.get_network(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **spec_ingress_security_policy** | **[str]**| Security Policy to apply in the ingress direction. | [optional]

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **get_network1**
> NetworkNetwork get_network1(o_name)

Get Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    spec_ingress_security_policy = [
        "spec.ingress-security-policy_example",
    ] # [str] | Security Policy to apply in the ingress direction. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Network object
        api_response = api_instance.get_network1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **spec_ingress_security_policy** | **[str]**| Security Policy to apply in the ingress direction. | [optional]

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **get_network_interface**
> NetworkNetworkInterface get_network_interface(o_name)

Get NetworkInterface object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network_interface import NetworkNetworkInterface
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_attach_tenant = "spec.attach-tenant_example" # str |  (optional)
    ip_config_dns_servers = [
        "ip-config.dns-servers_example",
    ] # [str] | DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkInterface object
        api_response = api_instance.get_network_interface(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_network_interface: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_attach_tenant** | **str**|  | [optional]
 **ip_config_dns_servers** | **[str]**| DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. | [optional]
 **status_mirror_sessions** | **[str]**|  | [optional]

### Return type

[**NetworkNetworkInterface**](NetworkNetworkInterface.md)

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

# **get_policer_profile**
> NetworkPolicerProfile get_policer_profile(o_tenant)

Get PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    exceed_action_policer_action = "exceed-action.policer-action_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **exceed_action_policer_action** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **get_policer_profile1**
> NetworkPolicerProfile get_policer_profile1(o_name)

Get PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    exceed_action_policer_action = "exceed-action.policer-action_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **exceed_action_policer_action** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **get_route_table**
> NetworkRouteTable get_route_table(o_tenant)

Get RouteTable object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_route_table import NetworkRouteTable
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**NetworkRouteTable**](NetworkRouteTable.md)

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

# **get_route_table1**
> NetworkRouteTable get_route_table1(o_name)

Get RouteTable object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_route_table import NetworkRouteTable
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**NetworkRouteTable**](NetworkRouteTable.md)

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

# **get_routing_config**
> NetworkRoutingConfig get_routing_config(o_name)

Get RoutingConfig object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config import NetworkRoutingConfig
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    as_number_as_number = 1 # int |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoutingConfig object
        api_response = api_instance.get_routing_config(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **as_number_as_number** | **int**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkRoutingConfig**](NetworkRoutingConfig.md)

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

# **get_virtual_router**
> NetworkVirtualRouter get_virtual_router(o_tenant)

Get VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **get_virtual_router1**
> NetworkVirtualRouter get_virtual_router1(o_name)

Get VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **get_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup get_virtual_router_peering_group(o_tenant)

Get VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **get_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup get_virtual_router_peering_group1(o_name)

Get VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **label_ipam_policy**
> NetworkIPAMPolicy label_ipam_policy(o_tenant, body)

Label IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label IPAMPolicy object
        api_response = api_instance.label_ipam_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **label_ipam_policy1**
> NetworkIPAMPolicy label_ipam_policy1(o_name, body)

Label IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label IPAMPolicy object
        api_response = api_instance.label_ipam_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **label_network**
> NetworkNetwork label_network(o_tenant, body)

Label Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label Network object
        api_response = api_instance.label_network(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **label_network1**
> NetworkNetwork label_network1(o_name, body)

Label Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label Network object
        api_response = api_instance.label_network1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **label_network_interface**
> NetworkNetworkInterface label_network_interface(o_name, body)

Label NetworkInterface object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.network_network_interface import NetworkNetworkInterface
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label NetworkInterface object
        api_response = api_instance.label_network_interface(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_network_interface: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkNetworkInterface**](NetworkNetworkInterface.md)

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

# **label_policer_profile**
> NetworkPolicerProfile label_policer_profile(o_tenant, body)

Label PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label PolicerProfile object
        api_response = api_instance.label_policer_profile(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **label_policer_profile1**
> NetworkPolicerProfile label_policer_profile1(o_name, body)

Label PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label PolicerProfile object
        api_response = api_instance.label_policer_profile1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **label_routing_config**
> NetworkRoutingConfig label_routing_config(o_name, body)

Label RoutingConfig object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config import NetworkRoutingConfig
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label RoutingConfig object
        api_response = api_instance.label_routing_config(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkRoutingConfig**](NetworkRoutingConfig.md)

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

# **label_virtual_router**
> NetworkVirtualRouter label_virtual_router(o_tenant, body)

Label VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label VirtualRouter object
        api_response = api_instance.label_virtual_router(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **label_virtual_router1**
> NetworkVirtualRouter label_virtual_router1(o_name, body)

Label VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label VirtualRouter object
        api_response = api_instance.label_virtual_router1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **label_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup label_virtual_router_peering_group(o_tenant, body)

Label VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        # Label VirtualRouterPeeringGroup object
        api_response = api_instance.label_virtual_router_peering_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **label_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup label_virtual_router_peering_group1(o_name, body)

Label VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label VirtualRouterPeeringGroup object
        api_response = api_instance.label_virtual_router_peering_group1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **list_ipam_policy**
> NetworkIPAMPolicyList list_ipam_policy(o_tenant)

List IPAMPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_ipam_policy_list import NetworkIPAMPolicyList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List IPAMPolicy objects
        api_response = api_instance.list_ipam_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkIPAMPolicyList**](NetworkIPAMPolicyList.md)

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

# **list_ipam_policy1**
> NetworkIPAMPolicyList list_ipam_policy1()

List IPAMPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_ipam_policy_list import NetworkIPAMPolicyList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List IPAMPolicy objects
        api_response = api_instance.list_ipam_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkIPAMPolicyList**](NetworkIPAMPolicyList.md)

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

# **list_network**
> NetworkNetworkList list_network(o_tenant)

List Network objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network_list import NetworkNetworkList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Network objects
        api_response = api_instance.list_network(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkNetworkList**](NetworkNetworkList.md)

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

# **list_network1**
> NetworkNetworkList list_network1()

List Network objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network_list import NetworkNetworkList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Network objects
        api_response = api_instance.list_network1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkNetworkList**](NetworkNetworkList.md)

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

# **list_network_interface**
> NetworkNetworkInterfaceList list_network_interface()

List NetworkInterface objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network_interface_list import NetworkNetworkInterfaceList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List NetworkInterface objects
        api_response = api_instance.list_network_interface()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_network_interface: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkNetworkInterfaceList**](NetworkNetworkInterfaceList.md)

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

# **list_policer_profile**
> NetworkPolicerProfileList list_policer_profile(o_tenant)

List PolicerProfile objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile_list import NetworkPolicerProfileList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List PolicerProfile objects
        api_response = api_instance.list_policer_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkPolicerProfileList**](NetworkPolicerProfileList.md)

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

# **list_policer_profile1**
> NetworkPolicerProfileList list_policer_profile1()

List PolicerProfile objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile_list import NetworkPolicerProfileList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List PolicerProfile objects
        api_response = api_instance.list_policer_profile1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkPolicerProfileList**](NetworkPolicerProfileList.md)

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

# **list_route_table**
> NetworkRouteTableList list_route_table(o_tenant)

List RouteTable objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_route_table_list import NetworkRouteTableList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RouteTable objects
        api_response = api_instance.list_route_table(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_route_table: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkRouteTableList**](NetworkRouteTableList.md)

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

# **list_route_table1**
> NetworkRouteTableList list_route_table1()

List RouteTable objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_route_table_list import NetworkRouteTableList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RouteTable objects
        api_response = api_instance.list_route_table1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_route_table1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkRouteTableList**](NetworkRouteTableList.md)

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

# **list_routing_config**
> NetworkRoutingConfigList list_routing_config()

List RoutingConfig objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config_list import NetworkRoutingConfigList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RoutingConfig objects
        api_response = api_instance.list_routing_config()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkRoutingConfigList**](NetworkRoutingConfigList.md)

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

# **list_virtual_router**
> NetworkVirtualRouterList list_virtual_router(o_tenant)

List VirtualRouter objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_list import NetworkVirtualRouterList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouter objects
        api_response = api_instance.list_virtual_router(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkVirtualRouterList**](NetworkVirtualRouterList.md)

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

# **list_virtual_router1**
> NetworkVirtualRouterList list_virtual_router1()

List VirtualRouter objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_list import NetworkVirtualRouterList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouter objects
        api_response = api_instance.list_virtual_router1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkVirtualRouterList**](NetworkVirtualRouterList.md)

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

# **list_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroupList list_virtual_router_peering_group(o_tenant)

List VirtualRouterPeeringGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group_list import NetworkVirtualRouterPeeringGroupList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouterPeeringGroup objects
        api_response = api_instance.list_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkVirtualRouterPeeringGroupList**](NetworkVirtualRouterPeeringGroupList.md)

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

# **list_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroupList list_virtual_router_peering_group1()

List VirtualRouterPeeringGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group_list import NetworkVirtualRouterPeeringGroupList
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouterPeeringGroup objects
        api_response = api_instance.list_virtual_router_peering_group1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkVirtualRouterPeeringGroupList**](NetworkVirtualRouterPeeringGroupList.md)

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

# **update_ipam_policy**
> NetworkIPAMPolicy update_ipam_policy(o_tenant, body)

Update IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkIPAMPolicy(
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
        spec=NetworkIPAMPolicySpec(
            dhcp_relay=NetworkDHCPRelayPolicy(
                relay_servers=[
                    NetworkDHCPServer(
                        ip_address="10.1.1.1, ff02::5 ",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
            type="dhcp-relay",
        ),
        status=NetworkIPAMPolicyStatus(
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
    ) # NetworkIPAMPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update IPAMPolicy object
        api_response = api_instance.update_ipam_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **update_ipam_policy1**
> NetworkIPAMPolicy update_ipam_policy1(o_name, body)

Update IPAMPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_ipam_policy import NetworkIPAMPolicy
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkIPAMPolicy(
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
        spec=NetworkIPAMPolicySpec(
            dhcp_relay=NetworkDHCPRelayPolicy(
                relay_servers=[
                    NetworkDHCPServer(
                        ip_address="10.1.1.1, ff02::5 ",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
            type="dhcp-relay",
        ),
        status=NetworkIPAMPolicyStatus(
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
    ) # NetworkIPAMPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update IPAMPolicy object
        api_response = api_instance.update_ipam_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)|  |

### Return type

[**NetworkIPAMPolicy**](NetworkIPAMPolicy.md)

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

# **update_network**
> NetworkNetwork update_network(o_tenant, body)

Update Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkNetwork(
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
        spec=NetworkNetworkSpec(
            egress_security_policy=[
                "egress_security_policy_example",
            ],
            ingress_security_policy=[
                "ingress_security_policy_example",
            ],
            ipam_config=NetworkIPAMConfig(
                ipv4_ipam_pool=[
                    NetworkIPAMPoolInfo(
                        ip_address_end="ip_address_end_example",
                        ip_address_start="ip_address_start_example",
                    ),
                ],
            ),
            ipam_policy="ipam_policy_example",
            ipv4_gateway="10.1.1.1, ff02::5 ",
            ipv4_subnet="10.1.1.1/24, ff02::5/32 ",
            ipv6_gateway="ipv6_gateway_example",
            ipv6_subnet="ipv6_subnet_example",
            orchestrators=[
                NetworkOrchestratorInfo(
                    namespace="namespace_example",
                    orchestrator_name="orchestrator_name_example",
                ),
            ],
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            type="bridged",
            virtual_router="virtual_router_example",
            vlan_id=0,
            vxlan_vni=0,
        ),
        status=NetworkNetworkStatus(
            allocated_ipv4_addrs='YQ==',
            id="id_example",
            oper_state="active",
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
            workloads=[
                "workloads_example",
            ],
        ),
    ) # NetworkNetwork | 

    # example passing only required values which don't have defaults set
    try:
        # Update Network object
        api_response = api_instance.update_network(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkNetwork**](NetworkNetwork.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **update_network1**
> NetworkNetwork update_network1(o_name, body)

Update Network object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkNetwork(
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
        spec=NetworkNetworkSpec(
            egress_security_policy=[
                "egress_security_policy_example",
            ],
            ingress_security_policy=[
                "ingress_security_policy_example",
            ],
            ipam_config=NetworkIPAMConfig(
                ipv4_ipam_pool=[
                    NetworkIPAMPoolInfo(
                        ip_address_end="ip_address_end_example",
                        ip_address_start="ip_address_start_example",
                    ),
                ],
            ),
            ipam_policy="ipam_policy_example",
            ipv4_gateway="10.1.1.1, ff02::5 ",
            ipv4_subnet="10.1.1.1/24, ff02::5/32 ",
            ipv6_gateway="ipv6_gateway_example",
            ipv6_subnet="ipv6_subnet_example",
            orchestrators=[
                NetworkOrchestratorInfo(
                    namespace="namespace_example",
                    orchestrator_name="orchestrator_name_example",
                ),
            ],
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            type="bridged",
            virtual_router="virtual_router_example",
            vlan_id=0,
            vxlan_vni=0,
        ),
        status=NetworkNetworkStatus(
            allocated_ipv4_addrs='YQ==',
            id="id_example",
            oper_state="active",
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
            workloads=[
                "workloads_example",
            ],
        ),
    ) # NetworkNetwork | 

    # example passing only required values which don't have defaults set
    try:
        # Update Network object
        api_response = api_instance.update_network1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkNetwork**](NetworkNetwork.md)|  |

### Return type

[**NetworkNetwork**](NetworkNetwork.md)

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

# **update_network_interface**
> NetworkNetworkInterface update_network_interface(o_name, body)

Update NetworkInterface object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network_interface import NetworkNetworkInterface
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkNetworkInterface(
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
        spec=NetworkNetworkInterfaceSpec(
            admin_status="up",
            attach_network="attach_network_example",
            attach_tenant="attach_tenant_example",
            connection_tracking=False,
            enable_fw_logging=True,
            ip_alloc_type="none",
            ip_config=ClusterIPConfig(
                default_gw="10.1.1.1, ff02::5 ",
                dns_servers=[
                    "dns_servers_example",
                ],
                ip_address="10.1.1.1/24, ff02::5/32 ",
            ),
            mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            mtu=1,
            pause=NetworkPauseSpec(
                rx_pause_enabled=True,
                tx_pause_enabled=True,
                type="disable",
            ),
            speed="speed_example",
            tx_policer="tx_policer_example",
            type="none",
            vnf_attached=True,
        ),
        status=NetworkNetworkInterfaceStatus(
            cluster_node="cluster_node_example",
            dsc="dsc_example",
            dsc_id="dsc_id_example",
            if_host_status=NetworkNetworkInterfaceHostStatus(
                device_id="device_id_example",
                host_ifname="host_ifname_example",
                mac_address="mac_address_example",
            ),
            if_uplink_status=NetworkNetworkInterfaceUplinkStatus(
                ip_config=ClusterIPConfig(
                    default_gw="10.1.1.1, ff02::5 ",
                    dns_servers=[],
                    ip_address="10.1.1.1/24, ff02::5/32 ",
                ),
                link_speed="link_speed_example",
                lldp_neighbor=NetworkLLDPNeighbor(
                    chassis_id="chassis_id_example",
                    mgmt_address="mgmt_address_example",
                    port_description="port_description_example",
                    port_id="port_id_example",
                    sys_description="sys_description_example",
                    sys_name="sys_name_example",
                ),
                transceiver_status=NetworkTransceiverStatus(
                    cable_type="none",
                    pid="unknown",
                    state="state_na",
                ),
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            name="name_example",
            oper_status="up",
            primary_mac="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
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
            type="none",
        ),
    ) # NetworkNetworkInterface | 

    # example passing only required values which don't have defaults set
    try:
        # Update NetworkInterface object
        api_response = api_instance.update_network_interface(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_network_interface: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkNetworkInterface**](NetworkNetworkInterface.md)|  |

### Return type

[**NetworkNetworkInterface**](NetworkNetworkInterface.md)

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

# **update_policer_profile**
> NetworkPolicerProfile update_policer_profile(o_tenant, body)

Update PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkPolicerProfile(
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
        spec=NetworkPolicerProfileSpec(
            criteria=NetworkPolicerCriteria(
                burst_size="burst_size_example",
                bytes_per_second="bytes_per_second_example",
                packets_per_second="packets_per_second_example",
            ),
            exceed_action=NetworkPolicerAction(
                policer_action="drop",
            ),
        ),
        status=NetworkPolicerProfileStatus(
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
    ) # NetworkPolicerProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update PolicerProfile object
        api_response = api_instance.update_policer_profile(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkPolicerProfile**](NetworkPolicerProfile.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **update_policer_profile1**
> NetworkPolicerProfile update_policer_profile1(o_name, body)

Update PolicerProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_policer_profile import NetworkPolicerProfile
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkPolicerProfile(
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
        spec=NetworkPolicerProfileSpec(
            criteria=NetworkPolicerCriteria(
                burst_size="burst_size_example",
                bytes_per_second="bytes_per_second_example",
                packets_per_second="packets_per_second_example",
            ),
            exceed_action=NetworkPolicerAction(
                policer_action="drop",
            ),
        ),
        status=NetworkPolicerProfileStatus(
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
    ) # NetworkPolicerProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update PolicerProfile object
        api_response = api_instance.update_policer_profile1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkPolicerProfile**](NetworkPolicerProfile.md)|  |

### Return type

[**NetworkPolicerProfile**](NetworkPolicerProfile.md)

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

# **update_routing_config**
> NetworkRoutingConfig update_routing_config(o_name, body)

Update RoutingConfig object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_routing_config import NetworkRoutingConfig
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkRoutingConfig(
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
        spec=NetworkRoutingConfigSpec(
            bgp_config=NetworkBGPConfig(
                as_number=ApiBgpAsn(
                    as_number=1,
                ),
                dsc_auto_config=True,
                holdtime=180,
                keepalive_interval=60,
                neighbors=[
                    NetworkBGPNeighbor(
                        allow_as_in=0,
                        dsc_auto_config=True,
                        enable_address_families=[
                            "enable_address_families_example",
                        ],
                        holdtime=0,
                        ip_address="10.1.1.1, ff02::5 ",
                        keepalive_interval=0,
                        multi_hop=64,
                        password="password_example",
                        remote_as=ApiBgpAsn(
                            as_number=1,
                        ),
                        shutdown=True,
                    ),
                ],
                router_id="10.1.1.1, ff02::5 ",
                suppress_default_resolution=True,
            ),
        ),
        status=NetworkRoutingConfigStatus(
            auth_config_status=[
                NetworkBGPAuthStatus(
                    ip_address="ip_address_example",
                    remote_as=ApiBgpAsn(
                        as_number=1,
                    ),
                    status="disabled",
                ),
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
    ) # NetworkRoutingConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Update RoutingConfig object
        api_response = api_instance.update_routing_config(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkRoutingConfig**](NetworkRoutingConfig.md)|  |

### Return type

[**NetworkRoutingConfig**](NetworkRoutingConfig.md)

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

# **update_virtual_router**
> NetworkVirtualRouter update_virtual_router(o_tenant, body)

Update VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkVirtualRouter(
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
        spec=NetworkVirtualRouterSpec(
            default_ipam_policy="default_ipam_policy_example",
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            router_mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            type="unknown",
            vxlan_vni=0,
        ),
        status=NetworkVirtualRouterStatus(
            id="id_example",
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
            rd=NetworkRouteDistinguisher(
                admin_value={},
                assigned_value=1,
                type="type0",
            ),
            route_table="route_table_example",
        ),
    ) # NetworkVirtualRouter | 

    # example passing only required values which don't have defaults set
    try:
        # Update VirtualRouter object
        api_response = api_instance.update_virtual_router(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkVirtualRouter**](NetworkVirtualRouter.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **update_virtual_router1**
> NetworkVirtualRouter update_virtual_router1(o_name, body)

Update VirtualRouter object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkVirtualRouter(
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
        spec=NetworkVirtualRouterSpec(
            default_ipam_policy="default_ipam_policy_example",
            route_import_export=NetworkRDSpec(
                address_family="ipv4-unicast",
                rd=NetworkRouteDistinguisher(
                    admin_value={},
                    assigned_value=1,
                    type="type0",
                ),
                rd_auto=True,
                rt_export=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
                rt_import=[
                    NetworkRouteDistinguisher(
                        admin_value={},
                        assigned_value=1,
                        type="type0",
                    ),
                ],
            ),
            router_mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
            type="unknown",
            vxlan_vni=0,
        ),
        status=NetworkVirtualRouterStatus(
            id="id_example",
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
            rd=NetworkRouteDistinguisher(
                admin_value={},
                assigned_value=1,
                type="type0",
            ),
            route_table="route_table_example",
        ),
    ) # NetworkVirtualRouter | 

    # example passing only required values which don't have defaults set
    try:
        # Update VirtualRouter object
        api_response = api_instance.update_virtual_router1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkVirtualRouter**](NetworkVirtualRouter.md)|  |

### Return type

[**NetworkVirtualRouter**](NetworkVirtualRouter.md)

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

# **update_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup update_virtual_router_peering_group(o_tenant, body)

Update VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = NetworkVirtualRouterPeeringGroup(
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
        spec=NetworkVirtualRouterPeeringGroupSpec(
            items=[
                NetworkVirtualRouterPeeringSpec(
                    ipv4_prefixes=[
                        "10.1.1.1/24, ff02::5/32 ",
                    ],
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status=NetworkVirtualRouterPeeringGroupStatus(
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
            route_tables={
                "key": NetworkVirtualRouterPeeringRouteTable(
                    routes=[
                        NetworkVirtualRouterPeeringRoute(
                            dest_virtual_router="dest_virtual_router_example",
                            ipv4_prefix="10.1.1.1/24, ff02::5/32 ",
                        ),
                    ],
                ),
            },
        ),
    ) # NetworkVirtualRouterPeeringGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update VirtualRouterPeeringGroup object
        api_response = api_instance.update_virtual_router_peering_group(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **update_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup update_virtual_router_peering_group1(o_name, body)

Update VirtualRouterPeeringGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = NetworkVirtualRouterPeeringGroup(
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
        spec=NetworkVirtualRouterPeeringGroupSpec(
            items=[
                NetworkVirtualRouterPeeringSpec(
                    ipv4_prefixes=[
                        "10.1.1.1/24, ff02::5/32 ",
                    ],
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status=NetworkVirtualRouterPeeringGroupStatus(
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
            route_tables={
                "key": NetworkVirtualRouterPeeringRouteTable(
                    routes=[
                        NetworkVirtualRouterPeeringRoute(
                            dest_virtual_router="dest_virtual_router_example",
                            ipv4_prefix="10.1.1.1/24, ff02::5/32 ",
                        ),
                    ],
                ),
            },
        ),
    ) # NetworkVirtualRouterPeeringGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update VirtualRouterPeeringGroup object
        api_response = api_instance.update_virtual_router_peering_group1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)|  |

### Return type

[**NetworkVirtualRouterPeeringGroup**](NetworkVirtualRouterPeeringGroup.md)

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

# **watch_ipam_policy**
> NetworkAutoMsgIPAMPolicyWatchHelper watch_ipam_policy(o_tenant)

Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_ipam_policy_watch_helper import NetworkAutoMsgIPAMPolicyWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ipam_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_ipam_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgIPAMPolicyWatchHelper**](NetworkAutoMsgIPAMPolicyWatchHelper.md)

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

# **watch_ipam_policy1**
> NetworkAutoMsgIPAMPolicyWatchHelper watch_ipam_policy1()

Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_ipam_policy_watch_helper import NetworkAutoMsgIPAMPolicyWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ipam_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_ipam_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgIPAMPolicyWatchHelper**](NetworkAutoMsgIPAMPolicyWatchHelper.md)

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

# **watch_network**
> NetworkAutoMsgNetworkWatchHelper watch_network(o_tenant)

Watch Network objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_network_watch_helper import NetworkAutoMsgNetworkWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Network objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgNetworkWatchHelper**](NetworkAutoMsgNetworkWatchHelper.md)

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

# **watch_network1**
> NetworkAutoMsgNetworkWatchHelper watch_network1()

Watch Network objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_network_watch_helper import NetworkAutoMsgNetworkWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Network objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgNetworkWatchHelper**](NetworkAutoMsgNetworkWatchHelper.md)

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

# **watch_network_interface**
> NetworkAutoMsgNetworkInterfaceWatchHelper watch_network_interface()

Watch NetworkInterface objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_auto_msg_network_interface_watch_helper import NetworkAutoMsgNetworkInterfaceWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch NetworkInterface objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_interface()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network_interface: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgNetworkInterfaceWatchHelper**](NetworkAutoMsgNetworkInterfaceWatchHelper.md)

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

# **watch_policer_profile**
> NetworkAutoMsgPolicerProfileWatchHelper watch_policer_profile(o_tenant)

Watch PolicerProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_policer_profile_watch_helper import NetworkAutoMsgPolicerProfileWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_policer_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_policer_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgPolicerProfileWatchHelper**](NetworkAutoMsgPolicerProfileWatchHelper.md)

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

# **watch_policer_profile1**
> NetworkAutoMsgPolicerProfileWatchHelper watch_policer_profile1()

Watch PolicerProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_policer_profile_watch_helper import NetworkAutoMsgPolicerProfileWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_policer_profile1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_policer_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgPolicerProfileWatchHelper**](NetworkAutoMsgPolicerProfileWatchHelper.md)

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

# **watch_route_table**
> NetworkAutoMsgRouteTableWatchHelper watch_route_table(o_tenant)

Watch RouteTable objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_auto_msg_route_table_watch_helper import NetworkAutoMsgRouteTableWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RouteTable objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_route_table(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_route_table: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgRouteTableWatchHelper**](NetworkAutoMsgRouteTableWatchHelper.md)

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

# **watch_route_table1**
> NetworkAutoMsgRouteTableWatchHelper watch_route_table1()

Watch RouteTable objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.network_auto_msg_route_table_watch_helper import NetworkAutoMsgRouteTableWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RouteTable objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_route_table1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_route_table1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgRouteTableWatchHelper**](NetworkAutoMsgRouteTableWatchHelper.md)

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

# **watch_routing_config**
> NetworkAutoMsgRoutingConfigWatchHelper watch_routing_config()

Watch RoutingConfig objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_routing_config_watch_helper import NetworkAutoMsgRoutingConfigWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RoutingConfig objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_routing_config()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_routing_config: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgRoutingConfigWatchHelper**](NetworkAutoMsgRoutingConfigWatchHelper.md)

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

# **watch_virtual_router**
> NetworkAutoMsgVirtualRouterWatchHelper watch_virtual_router(o_tenant)

Watch VirtualRouter objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_virtual_router_watch_helper import NetworkAutoMsgVirtualRouterWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgVirtualRouterWatchHelper**](NetworkAutoMsgVirtualRouterWatchHelper.md)

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

# **watch_virtual_router1**
> NetworkAutoMsgVirtualRouterWatchHelper watch_virtual_router1()

Watch VirtualRouter objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_virtual_router_watch_helper import NetworkAutoMsgVirtualRouterWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgVirtualRouterWatchHelper**](NetworkAutoMsgVirtualRouterWatchHelper.md)

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

# **watch_virtual_router_peering_group**
> NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper watch_virtual_router_peering_group(o_tenant)

Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_virtual_router_peering_group_watch_helper import NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router_peering_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper**](NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper.md)

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

# **watch_virtual_router_peering_group1**
> NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper watch_virtual_router_peering_group1()

Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_auto_msg_virtual_router_peering_group_watch_helper import NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper
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
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router_peering_group1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router_peering_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper**](NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper.md)

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

