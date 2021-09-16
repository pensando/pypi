# psm_cloud.NetworkV1Api

All URIs are relative to `https://PSM-IP/`

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

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_ipam_policy1**
> NetworkIPAMPolicy add_ipam_policy1(body)

Create IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_network**
> NetworkNetwork add_network(o_tenant, body)

Create Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_network1**
> NetworkNetwork add_network1(body)

Create Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_policer_profile**
> NetworkPolicerProfile add_policer_profile(o_tenant, body)

Create PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_policer_profile1**
> NetworkPolicerProfile add_policer_profile1(body)

Create PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_routing_config**
> NetworkRoutingConfig add_routing_config(body)

Create RoutingConfig object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_routing_config import NetworkRoutingConfig
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_virtual_router**
> NetworkVirtualRouter add_virtual_router(o_tenant, body)

Create VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_virtual_router1**
> NetworkVirtualRouter add_virtual_router1(body)

Create VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup add_virtual_router_peering_group(o_tenant, body)

Create VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **add_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup add_virtual_router_peering_group1(body)

Create VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_ipam_policy**
> NetworkIPAMPolicy delete_ipam_policy(o_tenant, o_name)

Delete IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPAMPolicy object
        api_response = api_instance.delete_ipam_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->delete_ipam_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_ipam_policy1**
> NetworkIPAMPolicy delete_ipam_policy1(o_name)

Delete IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPAMPolicy object
        api_response = api_instance.delete_ipam_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_network**
> NetworkNetwork delete_network(o_tenant, o_name)

Delete Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Network object
        api_response = api_instance.delete_network(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_network1**
> NetworkNetwork delete_network1(o_name)

Delete Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Network object
        api_response = api_instance.delete_network1(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_policer_profile**
> NetworkPolicerProfile delete_policer_profile(o_tenant, o_name)

Delete PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete PolicerProfile object
        api_response = api_instance.delete_policer_profile(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->delete_policer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_policer_profile1**
> NetworkPolicerProfile delete_policer_profile1(o_name)

Delete PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete PolicerProfile object
        api_response = api_instance.delete_policer_profile1(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_routing_config**
> NetworkRoutingConfig delete_routing_config(o_name)

Delete RoutingConfig object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_routing_config import NetworkRoutingConfig
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoutingConfig object
        api_response = api_instance.delete_routing_config(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_virtual_router**
> NetworkVirtualRouter delete_virtual_router(o_tenant, o_name)

Delete VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouter object
        api_response = api_instance.delete_virtual_router(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_virtual_router1**
> NetworkVirtualRouter delete_virtual_router1(o_name)

Delete VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouter object
        api_response = api_instance.delete_virtual_router1(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup delete_virtual_router_peering_group(o_tenant, o_name)

Delete VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouterPeeringGroup object
        api_response = api_instance.delete_virtual_router_peering_group(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->delete_virtual_router_peering_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **delete_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup delete_virtual_router_peering_group1(o_name)

Delete VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete VirtualRouterPeeringGroup object
        api_response = api_instance.delete_virtual_router_peering_group1(o_name)
        pprint(api_response)
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_ipam_policy**
> NetworkIPAMPolicy get_ipam_policy(o_tenant, o_name)

Get IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy: %s\n" % e)
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
 **spec_type** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_ipam_policy1**
> NetworkIPAMPolicy get_ipam_policy1(o_name)

Get IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get IPAMPolicy object
        api_response = api_instance.get_ipam_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_ipam_policy1: %s\n" % e)
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
 **spec_type** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_network**
> NetworkNetwork get_network(o_tenant, o_name)

Get Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str | type of network. (vlan/vxlan/routed etc). (optional)
    spec_ipv4_subnet = "spec.ipv4-subnet_example" # str | IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block. (optional)
    spec_ipv4_gateway = "spec.ipv4-gateway_example" # str | IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address. (optional)
    spec_ipv6_subnet = "spec.ipv6-subnet_example" # str | IPv6 subnet CIDR. (optional)
    spec_ipv6_gateway = "spec.ipv6-gateway_example" # str | IPv6 gateway. (optional)
    spec_vlan_id = 1 # int | Vlan ID for the network. Value should be between 0 and 4095. (optional)
    spec_vxlan_vni = 1 # int | Vxlan VNI for the network. Value should be between 0 and 16777215. (optional)
    spec_virtual_router = "spec.virtual-router_example" # str | VirtualRouter specifies the VRF this network belongs to. (optional)
    spec_ipam_policy = "spec.ipam-policy_example" # str | Relay Configuration if any. (optional)
    route_import_export_address_family = "route-import-export.address-family_example" # str | Address family where this config applies. (optional)
    route_import_export_rd_auto = True # bool | True indicates the system will generate the RD automatically. (optional)
    rd_type = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    rd_assigned_value = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    spec_ingress_security_policy = [
        "spec.ingress-security-policy_example",
    ] # [str] | Security Policy to apply in the ingress direction. (optional)
    spec_egress_security_policy = [
        "spec.egress-security-policy_example",
    ] # [str] | Security Policy to apply in the egress direction. (optional)
    status_workloads = [
        "status.workloads_example",
    ] # [str] | list of all workloads in this network. (optional)
    status_allocated_ipv4_addrs = 'YQ==' # str | allocated IPv4 addresses (bitmap). (optional)
    status_id = "status.id_example" # str | Handle is the internal Handle allocated to this network. (optional)
    status_oper_state = "status.oper-state_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Network object
        api_response = api_instance.get_network(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Network object
        api_response = api_instance.get_network(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, spec_ipv4_subnet=spec_ipv4_subnet, spec_ipv4_gateway=spec_ipv4_gateway, spec_ipv6_subnet=spec_ipv6_subnet, spec_ipv6_gateway=spec_ipv6_gateway, spec_vlan_id=spec_vlan_id, spec_vxlan_vni=spec_vxlan_vni, spec_virtual_router=spec_virtual_router, spec_ipam_policy=spec_ipam_policy, route_import_export_address_family=route_import_export_address_family, route_import_export_rd_auto=route_import_export_rd_auto, rd_type=rd_type, admin_value_format=admin_value_format, admin_value_value=admin_value_value, rd_assigned_value=rd_assigned_value, spec_ingress_security_policy=spec_ingress_security_policy, spec_egress_security_policy=spec_egress_security_policy, status_workloads=status_workloads, status_allocated_ipv4_addrs=status_allocated_ipv4_addrs, status_id=status_id, status_oper_state=status_oper_state, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network: %s\n" % e)
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
 **spec_type** | **str**| type of network. (vlan/vxlan/routed etc). | [optional]
 **spec_ipv4_subnet** | **str**| IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block. | [optional]
 **spec_ipv4_gateway** | **str**| IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address. | [optional]
 **spec_ipv6_subnet** | **str**| IPv6 subnet CIDR. | [optional]
 **spec_ipv6_gateway** | **str**| IPv6 gateway. | [optional]
 **spec_vlan_id** | **int**| Vlan ID for the network. Value should be between 0 and 4095. | [optional]
 **spec_vxlan_vni** | **int**| Vxlan VNI for the network. Value should be between 0 and 16777215. | [optional]
 **spec_virtual_router** | **str**| VirtualRouter specifies the VRF this network belongs to. | [optional]
 **spec_ipam_policy** | **str**| Relay Configuration if any. | [optional]
 **route_import_export_address_family** | **str**| Address family where this config applies. | [optional]
 **route_import_export_rd_auto** | **bool**| True indicates the system will generate the RD automatically. | [optional]
 **rd_type** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **rd_assigned_value** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **spec_ingress_security_policy** | **[str]**| Security Policy to apply in the ingress direction. | [optional]
 **spec_egress_security_policy** | **[str]**| Security Policy to apply in the egress direction. | [optional]
 **status_workloads** | **[str]**| list of all workloads in this network. | [optional]
 **status_allocated_ipv4_addrs** | **str**| allocated IPv4 addresses (bitmap). | [optional]
 **status_id** | **str**| Handle is the internal Handle allocated to this network. | [optional]
 **status_oper_state** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_network1**
> NetworkNetwork get_network1(o_name)

Get Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str | type of network. (vlan/vxlan/routed etc). (optional)
    spec_ipv4_subnet = "spec.ipv4-subnet_example" # str | IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block. (optional)
    spec_ipv4_gateway = "spec.ipv4-gateway_example" # str | IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address. (optional)
    spec_ipv6_subnet = "spec.ipv6-subnet_example" # str | IPv6 subnet CIDR. (optional)
    spec_ipv6_gateway = "spec.ipv6-gateway_example" # str | IPv6 gateway. (optional)
    spec_vlan_id = 1 # int | Vlan ID for the network. Value should be between 0 and 4095. (optional)
    spec_vxlan_vni = 1 # int | Vxlan VNI for the network. Value should be between 0 and 16777215. (optional)
    spec_virtual_router = "spec.virtual-router_example" # str | VirtualRouter specifies the VRF this network belongs to. (optional)
    spec_ipam_policy = "spec.ipam-policy_example" # str | Relay Configuration if any. (optional)
    route_import_export_address_family = "route-import-export.address-family_example" # str | Address family where this config applies. (optional)
    route_import_export_rd_auto = True # bool | True indicates the system will generate the RD automatically. (optional)
    rd_type = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    rd_assigned_value = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    spec_ingress_security_policy = [
        "spec.ingress-security-policy_example",
    ] # [str] | Security Policy to apply in the ingress direction. (optional)
    spec_egress_security_policy = [
        "spec.egress-security-policy_example",
    ] # [str] | Security Policy to apply in the egress direction. (optional)
    status_workloads = [
        "status.workloads_example",
    ] # [str] | list of all workloads in this network. (optional)
    status_allocated_ipv4_addrs = 'YQ==' # str | allocated IPv4 addresses (bitmap). (optional)
    status_id = "status.id_example" # str | Handle is the internal Handle allocated to this network. (optional)
    status_oper_state = "status.oper-state_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Network object
        api_response = api_instance.get_network1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Network object
        api_response = api_instance.get_network1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, spec_ipv4_subnet=spec_ipv4_subnet, spec_ipv4_gateway=spec_ipv4_gateway, spec_ipv6_subnet=spec_ipv6_subnet, spec_ipv6_gateway=spec_ipv6_gateway, spec_vlan_id=spec_vlan_id, spec_vxlan_vni=spec_vxlan_vni, spec_virtual_router=spec_virtual_router, spec_ipam_policy=spec_ipam_policy, route_import_export_address_family=route_import_export_address_family, route_import_export_rd_auto=route_import_export_rd_auto, rd_type=rd_type, admin_value_format=admin_value_format, admin_value_value=admin_value_value, rd_assigned_value=rd_assigned_value, spec_ingress_security_policy=spec_ingress_security_policy, spec_egress_security_policy=spec_egress_security_policy, status_workloads=status_workloads, status_allocated_ipv4_addrs=status_allocated_ipv4_addrs, status_id=status_id, status_oper_state=status_oper_state, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network1: %s\n" % e)
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
 **spec_type** | **str**| type of network. (vlan/vxlan/routed etc). | [optional]
 **spec_ipv4_subnet** | **str**| IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block. | [optional]
 **spec_ipv4_gateway** | **str**| IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address. | [optional]
 **spec_ipv6_subnet** | **str**| IPv6 subnet CIDR. | [optional]
 **spec_ipv6_gateway** | **str**| IPv6 gateway. | [optional]
 **spec_vlan_id** | **int**| Vlan ID for the network. Value should be between 0 and 4095. | [optional]
 **spec_vxlan_vni** | **int**| Vxlan VNI for the network. Value should be between 0 and 16777215. | [optional]
 **spec_virtual_router** | **str**| VirtualRouter specifies the VRF this network belongs to. | [optional]
 **spec_ipam_policy** | **str**| Relay Configuration if any. | [optional]
 **route_import_export_address_family** | **str**| Address family where this config applies. | [optional]
 **route_import_export_rd_auto** | **bool**| True indicates the system will generate the RD automatically. | [optional]
 **rd_type** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **rd_assigned_value** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **spec_ingress_security_policy** | **[str]**| Security Policy to apply in the ingress direction. | [optional]
 **spec_egress_security_policy** | **[str]**| Security Policy to apply in the egress direction. | [optional]
 **status_workloads** | **[str]**| list of all workloads in this network. | [optional]
 **status_allocated_ipv4_addrs** | **str**| allocated IPv4 addresses (bitmap). | [optional]
 **status_id** | **str**| Handle is the internal Handle allocated to this network. | [optional]
 **status_oper_state** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_network_interface**
> NetworkNetworkInterface get_network_interface(o_name)

Get NetworkInterface object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_network_interface import NetworkNetworkInterface
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_admin_status = "spec.admin-status_example" # str | desired Admin state of the port. (optional)
    spec_speed = "spec.speed_example" # str | Intefaae speed. (optional)
    spec_mtu = 1 # int | Mtu of the interface. (optional)
    pause_type = "pause.type_example" # str | Pause type. (optional)
    pause_tx_pause_enabled = True # bool | TX Pause enabled. (optional)
    pause_rx_pause_enabled = True # bool | RX Pause enabled. (optional)
    spec_type = "spec.type_example" # str | Type specifies the type of interface. (optional)
    spec_attach_tenant = "spec.attach-tenant_example" # str |  (optional)
    spec_attach_network = "spec.attach-network_example" # str | AttachNetwork associates the interface with a Network. This is only valid for host interfaces (host-pf/host-vf). (optional)
    spec_ip_alloc_type = "spec.ip-alloc-type_example" # str |  (optional)
    ip_config_ip_address = "ip-config.ip-address_example" # str | IPAddress contains the Management IP address of the DistributedServiceCard in CIDR format. Should be a valid v4 or v6 CIDR block. (optional)
    ip_config_default_gw = "ip-config.default-gw_example" # str | DefaultGW contains the default gateway's IP address. Should be a valid v4 or v6 IP address. (optional)
    ip_config_dns_servers = [
        "ip-config.dns-servers_example",
    ] # [str] | DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. (optional)
    spec_mac_address = "spec.mac-address_example" # str | Override system allocated MAC address. Should be a valid MAC address. (optional)
    spec_connection_tracking = True # bool | ConnectionTracking enables connection tracking on the interface. This is valid only for host interfaces (host-pf/host-vf). (optional)
    spec_tx_policer = "spec.tx-policer_example" # str |  (optional)
    spec_enable_fw_logging = True # bool | EnableFwLogging enables flow logging on the interface. This is valid only for host interfaces (host-pf/host-vf). (optional)
    spec_vnf_attached = True # bool | VNFAttached knob on the interface. This is valid only for host interfaces (host-pf/host-vf). (optional)
    status_name = "status.name_example" # str |  (optional)
    status_dsc = "status.dsc_example" # str |  (optional)
    status_type = "status.type_example" # str |  (optional)
    status_oper_status = "status.oper-status_example" # str |  (optional)
    status_primary_mac = "status.primary-mac_example" # str | Should be a valid MAC address. (optional)
    if_host_status_host_ifname = "if-host-status.host-ifname_example" # str | interface name seen by the host driver. (optional)
    if_host_status_device_id = "if-host-status.device-id_example" # str | PCIE Device ID. (optional)
    if_host_status_mac_address = "if-host-status.mac-address_example" # str | mac address of the interface. (optional)
    if_uplink_status_link_speed = "if-uplink-status.link-speed_example" # str | LinkSpeed auto-negotiated. (optional)
    transceiver_status_state = "transceiver-status.state_example" # str |  (optional)
    transceiver_status_cable_type = "transceiver-status.cable-type_example" # str |  (optional)
    transceiver_status_pid = "transceiver-status.pid_example" # str |  (optional)
    ip_config_ip_address2 = "ip-config.ip-address_example" # str | IPAddress contains the Management IP address of the DistributedServiceCard in CIDR format. Should be a valid v4 or v6 CIDR block. (optional)
    ip_config_default_gw2 = "ip-config.default-gw_example" # str | DefaultGW contains the default gateway's IP address. Should be a valid v4 or v6 IP address. (optional)
    ip_config_dns_servers2 = [
        "ip-config.dns-servers_example",
    ] # [str] | DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. (optional)
    lldp_neighbor_chassis_id = "lldp-neighbor.chassis-id_example" # str | Chassis  ID. (optional)
    lldp_neighbor_sys_name = "lldp-neighbor.sys-name_example" # str | System Name. (optional)
    lldp_neighbor_sys_description = "lldp-neighbor.sys-description_example" # str | System Description. (optional)
    lldp_neighbor_port_id = "lldp-neighbor.port-id_example" # str | Port Name. (optional)
    lldp_neighbor_port_description = "lldp-neighbor.port-description_example" # str | Port Description. (optional)
    lldp_neighbor_mgmt_address = "lldp-neighbor.mgmt-address_example" # str | Mgmt IP. (optional)
    status_mirror_sessions = [
        "status.mirror-sessions_example",
    ] # [str] |  (optional)
    status_cluster_node = "status.cluster-node_example" # str | Set only if interface is on Venice Node. (optional)
    status_dsc_id = "status.dsc-id_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkInterface object
        api_response = api_instance.get_network_interface(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network_interface: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get NetworkInterface object
        api_response = api_instance.get_network_interface(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_admin_status=spec_admin_status, spec_speed=spec_speed, spec_mtu=spec_mtu, pause_type=pause_type, pause_tx_pause_enabled=pause_tx_pause_enabled, pause_rx_pause_enabled=pause_rx_pause_enabled, spec_type=spec_type, spec_attach_tenant=spec_attach_tenant, spec_attach_network=spec_attach_network, spec_ip_alloc_type=spec_ip_alloc_type, ip_config_ip_address=ip_config_ip_address, ip_config_default_gw=ip_config_default_gw, ip_config_dns_servers=ip_config_dns_servers, spec_mac_address=spec_mac_address, spec_connection_tracking=spec_connection_tracking, spec_tx_policer=spec_tx_policer, spec_enable_fw_logging=spec_enable_fw_logging, spec_vnf_attached=spec_vnf_attached, status_name=status_name, status_dsc=status_dsc, status_type=status_type, status_oper_status=status_oper_status, status_primary_mac=status_primary_mac, if_host_status_host_ifname=if_host_status_host_ifname, if_host_status_device_id=if_host_status_device_id, if_host_status_mac_address=if_host_status_mac_address, if_uplink_status_link_speed=if_uplink_status_link_speed, transceiver_status_state=transceiver_status_state, transceiver_status_cable_type=transceiver_status_cable_type, transceiver_status_pid=transceiver_status_pid, ip_config_ip_address2=ip_config_ip_address2, ip_config_default_gw2=ip_config_default_gw2, ip_config_dns_servers2=ip_config_dns_servers2, lldp_neighbor_chassis_id=lldp_neighbor_chassis_id, lldp_neighbor_sys_name=lldp_neighbor_sys_name, lldp_neighbor_sys_description=lldp_neighbor_sys_description, lldp_neighbor_port_id=lldp_neighbor_port_id, lldp_neighbor_port_description=lldp_neighbor_port_description, lldp_neighbor_mgmt_address=lldp_neighbor_mgmt_address, status_mirror_sessions=status_mirror_sessions, status_cluster_node=status_cluster_node, status_dsc_id=status_dsc_id, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_network_interface: %s\n" % e)
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
 **spec_admin_status** | **str**| desired Admin state of the port. | [optional]
 **spec_speed** | **str**| Intefaae speed. | [optional]
 **spec_mtu** | **int**| Mtu of the interface. | [optional]
 **pause_type** | **str**| Pause type. | [optional]
 **pause_tx_pause_enabled** | **bool**| TX Pause enabled. | [optional]
 **pause_rx_pause_enabled** | **bool**| RX Pause enabled. | [optional]
 **spec_type** | **str**| Type specifies the type of interface. | [optional]
 **spec_attach_tenant** | **str**|  | [optional]
 **spec_attach_network** | **str**| AttachNetwork associates the interface with a Network. This is only valid for host interfaces (host-pf/host-vf). | [optional]
 **spec_ip_alloc_type** | **str**|  | [optional]
 **ip_config_ip_address** | **str**| IPAddress contains the Management IP address of the DistributedServiceCard in CIDR format. Should be a valid v4 or v6 CIDR block. | [optional]
 **ip_config_default_gw** | **str**| DefaultGW contains the default gateway&#39;s IP address. Should be a valid v4 or v6 IP address. | [optional]
 **ip_config_dns_servers** | **[str]**| DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. | [optional]
 **spec_mac_address** | **str**| Override system allocated MAC address. Should be a valid MAC address. | [optional]
 **spec_connection_tracking** | **bool**| ConnectionTracking enables connection tracking on the interface. This is valid only for host interfaces (host-pf/host-vf). | [optional]
 **spec_tx_policer** | **str**|  | [optional]
 **spec_enable_fw_logging** | **bool**| EnableFwLogging enables flow logging on the interface. This is valid only for host interfaces (host-pf/host-vf). | [optional]
 **spec_vnf_attached** | **bool**| VNFAttached knob on the interface. This is valid only for host interfaces (host-pf/host-vf). | [optional]
 **status_name** | **str**|  | [optional]
 **status_dsc** | **str**|  | [optional]
 **status_type** | **str**|  | [optional]
 **status_oper_status** | **str**|  | [optional]
 **status_primary_mac** | **str**| Should be a valid MAC address. | [optional]
 **if_host_status_host_ifname** | **str**| interface name seen by the host driver. | [optional]
 **if_host_status_device_id** | **str**| PCIE Device ID. | [optional]
 **if_host_status_mac_address** | **str**| mac address of the interface. | [optional]
 **if_uplink_status_link_speed** | **str**| LinkSpeed auto-negotiated. | [optional]
 **transceiver_status_state** | **str**|  | [optional]
 **transceiver_status_cable_type** | **str**|  | [optional]
 **transceiver_status_pid** | **str**|  | [optional]
 **ip_config_ip_address2** | **str**| IPAddress contains the Management IP address of the DistributedServiceCard in CIDR format. Should be a valid v4 or v6 CIDR block. | [optional]
 **ip_config_default_gw2** | **str**| DefaultGW contains the default gateway&#39;s IP address. Should be a valid v4 or v6 IP address. | [optional]
 **ip_config_dns_servers2** | **[str]**| DNSServers contains a list of DNS Servers that can be used on DistributedServiceCard. | [optional]
 **lldp_neighbor_chassis_id** | **str**| Chassis  ID. | [optional]
 **lldp_neighbor_sys_name** | **str**| System Name. | [optional]
 **lldp_neighbor_sys_description** | **str**| System Description. | [optional]
 **lldp_neighbor_port_id** | **str**| Port Name. | [optional]
 **lldp_neighbor_port_description** | **str**| Port Description. | [optional]
 **lldp_neighbor_mgmt_address** | **str**| Mgmt IP. | [optional]
 **status_mirror_sessions** | **[str]**|  | [optional]
 **status_cluster_node** | **str**| Set only if interface is on Venice Node. | [optional]
 **status_dsc_id** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_policer_profile**
> NetworkPolicerProfile get_policer_profile(o_tenant, o_name)

Get PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    criteria_bytes_per_second = "criteria.bytes-per-second_example" # str | Maximum permissible bytes per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. (optional)
    criteria_packets_per_second = "criteria.packets-per-second_example" # str | Maximum permissible packets per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. (optional)
    criteria_burst_size = "criteria.burst-size_example" # str | Burst size in number of packets/bytes as policer criteria. (optional)
    exceed_action_policer_action = "exceed-action.policer-action_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, criteria_bytes_per_second=criteria_bytes_per_second, criteria_packets_per_second=criteria_packets_per_second, criteria_burst_size=criteria_burst_size, exceed_action_policer_action=exceed_action_policer_action, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile: %s\n" % e)
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
 **criteria_bytes_per_second** | **str**| Maximum permissible bytes per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. | [optional]
 **criteria_packets_per_second** | **str**| Maximum permissible packets per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. | [optional]
 **criteria_burst_size** | **str**| Burst size in number of packets/bytes as policer criteria. | [optional]
 **exceed_action_policer_action** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_policer_profile1**
> NetworkPolicerProfile get_policer_profile1(o_name)

Get PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    criteria_bytes_per_second = "criteria.bytes-per-second_example" # str | Maximum permissible bytes per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. (optional)
    criteria_packets_per_second = "criteria.packets-per-second_example" # str | Maximum permissible packets per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. (optional)
    criteria_burst_size = "criteria.burst-size_example" # str | Burst size in number of packets/bytes as policer criteria. (optional)
    exceed_action_policer_action = "exceed-action.policer-action_example" # str |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get PolicerProfile object
        api_response = api_instance.get_policer_profile1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, criteria_bytes_per_second=criteria_bytes_per_second, criteria_packets_per_second=criteria_packets_per_second, criteria_burst_size=criteria_burst_size, exceed_action_policer_action=exceed_action_policer_action, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_policer_profile1: %s\n" % e)
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
 **criteria_bytes_per_second** | **str**| Maximum permissible bytes per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. | [optional]
 **criteria_packets_per_second** | **str**| Maximum permissible packets per second before policer will start dropping traffic. Either BytesPerSecond/PacketsPerSecond can be specified. | [optional]
 **criteria_burst_size** | **str**| Burst size in number of packets/bytes as policer criteria. | [optional]
 **exceed_action_policer_action** | **str**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_route_table**
> NetworkRouteTable get_route_table(o_tenant, o_name)

Get RouteTable object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_route_table import NetworkRouteTable
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_route_table1**
> NetworkRouteTable get_route_table1(o_name)

Get RouteTable object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_route_table import NetworkRouteTable
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RouteTable object
        api_response = api_instance.get_route_table1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_route_table1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_routing_config**
> NetworkRoutingConfig get_routing_config(o_name)

Get RoutingConfig object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_routing_config import NetworkRoutingConfig
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    bgp_config_router_id = "bgp-config.router-id_example" # str | Router ID for the BGP Instance. Should be a valid v4 or v6 IP address. (optional)
    as_number_as_number = 1 # int |  (optional)
    bgp_config_keepalive_interval = 1 # int | KeepaliveInterval is time interval at which keepalive messages are sent. Value should be between 0 and 3600. (optional)
    bgp_config_holdtime = 1 # int | Holdtime is time for which not receiving a keepalive message results in declaring the peer as dead. Value should be between 0 and 3600. (optional)
    bgp_config_dsc_auto_config = True # bool | DSCAutoConfig sets the flag that this config is to be used as a template for auto configuration. (optional)
    bgp_config_suppress_default_resolution = True # bool | SuppressDefaultResolution excludes default route from being used to resolve nexthop reachability in the underlay. WARNING: modifying this has network-wide data traffic impact as it temporarily deactivates and then re-activates all underlay and overlay routes on every node where this config is applied. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoutingConfig object
        api_response = api_instance.get_routing_config(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_routing_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RoutingConfig object
        api_response = api_instance.get_routing_config(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, bgp_config_router_id=bgp_config_router_id, as_number_as_number=as_number_as_number, bgp_config_keepalive_interval=bgp_config_keepalive_interval, bgp_config_holdtime=bgp_config_holdtime, bgp_config_dsc_auto_config=bgp_config_dsc_auto_config, bgp_config_suppress_default_resolution=bgp_config_suppress_default_resolution, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_routing_config: %s\n" % e)
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
 **bgp_config_router_id** | **str**| Router ID for the BGP Instance. Should be a valid v4 or v6 IP address. | [optional]
 **as_number_as_number** | **int**|  | [optional]
 **bgp_config_keepalive_interval** | **int**| KeepaliveInterval is time interval at which keepalive messages are sent. Value should be between 0 and 3600. | [optional]
 **bgp_config_holdtime** | **int**| Holdtime is time for which not receiving a keepalive message results in declaring the peer as dead. Value should be between 0 and 3600. | [optional]
 **bgp_config_dsc_auto_config** | **bool**| DSCAutoConfig sets the flag that this config is to be used as a template for auto configuration. | [optional]
 **bgp_config_suppress_default_resolution** | **bool**| SuppressDefaultResolution excludes default route from being used to resolve nexthop reachability in the underlay. WARNING: modifying this has network-wide data traffic impact as it temporarily deactivates and then re-activates all underlay and overlay routes on every node where this config is applied. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_virtual_router**
> NetworkVirtualRouter get_virtual_router(o_tenant, o_name)

Get VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str |  (optional)
    spec_router_mac_address = "spec.router-mac-address_example" # str | Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. (optional)
    spec_vxlan_vni = 1 # int | VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. (optional)
    route_import_export_address_family = "route-import-export.address-family_example" # str | Address family where this config applies. (optional)
    route_import_export_rd_auto = True # bool | True indicates the system will generate the RD automatically. (optional)
    rd_type = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    rd_assigned_value = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    spec_default_ipam_policy = "spec.default-ipam-policy_example" # str | Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. (optional)
    status_id = "status.id_example" # str | Handle allocated in the system. (optional)
    status_route_table = "status.route-table_example" # str |  (optional)
    rd_type2 = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format2 = "admin-value.Format_example" # str |  (optional)
    admin_value_value2 = 1 # int |  (optional)
    rd_assigned_value2 = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, spec_router_mac_address=spec_router_mac_address, spec_vxlan_vni=spec_vxlan_vni, route_import_export_address_family=route_import_export_address_family, route_import_export_rd_auto=route_import_export_rd_auto, rd_type=rd_type, admin_value_format=admin_value_format, admin_value_value=admin_value_value, rd_assigned_value=rd_assigned_value, spec_default_ipam_policy=spec_default_ipam_policy, status_id=status_id, status_route_table=status_route_table, rd_type2=rd_type2, admin_value_format2=admin_value_format2, admin_value_value2=admin_value_value2, rd_assigned_value2=rd_assigned_value2, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router: %s\n" % e)
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
 **spec_type** | **str**|  | [optional]
 **spec_router_mac_address** | **str**| Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. | [optional]
 **spec_vxlan_vni** | **int**| VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. | [optional]
 **route_import_export_address_family** | **str**| Address family where this config applies. | [optional]
 **route_import_export_rd_auto** | **bool**| True indicates the system will generate the RD automatically. | [optional]
 **rd_type** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **rd_assigned_value** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **spec_default_ipam_policy** | **str**| Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. | [optional]
 **status_id** | **str**| Handle allocated in the system. | [optional]
 **status_route_table** | **str**|  | [optional]
 **rd_type2** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format2** | **str**|  | [optional]
 **admin_value_value2** | **int**|  | [optional]
 **rd_assigned_value2** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_virtual_router1**
> NetworkVirtualRouter get_virtual_router1(o_name)

Get VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    spec_type = "spec.type_example" # str |  (optional)
    spec_router_mac_address = "spec.router-mac-address_example" # str | Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. (optional)
    spec_vxlan_vni = 1 # int | VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. (optional)
    route_import_export_address_family = "route-import-export.address-family_example" # str | Address family where this config applies. (optional)
    route_import_export_rd_auto = True # bool | True indicates the system will generate the RD automatically. (optional)
    rd_type = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format = "admin-value.Format_example" # str |  (optional)
    admin_value_value = 1 # int |  (optional)
    rd_assigned_value = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    spec_default_ipam_policy = "spec.default-ipam-policy_example" # str | Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. (optional)
    status_id = "status.id_example" # str | Handle allocated in the system. (optional)
    status_route_table = "status.route-table_example" # str |  (optional)
    rd_type2 = "rd.type_example" # str | RD Type as in rfc4364. (optional)
    admin_value_format2 = "admin-value.Format_example" # str |  (optional)
    admin_value_value2 = 1 # int |  (optional)
    rd_assigned_value2 = 1 # int | Assigned subfield of Value. Length depends on Type. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VirtualRouter object
        api_response = api_instance.get_virtual_router1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, spec_router_mac_address=spec_router_mac_address, spec_vxlan_vni=spec_vxlan_vni, route_import_export_address_family=route_import_export_address_family, route_import_export_rd_auto=route_import_export_rd_auto, rd_type=rd_type, admin_value_format=admin_value_format, admin_value_value=admin_value_value, rd_assigned_value=rd_assigned_value, spec_default_ipam_policy=spec_default_ipam_policy, status_id=status_id, status_route_table=status_route_table, rd_type2=rd_type2, admin_value_format2=admin_value_format2, admin_value_value2=admin_value_value2, rd_assigned_value2=rd_assigned_value2, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router1: %s\n" % e)
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
 **spec_type** | **str**|  | [optional]
 **spec_router_mac_address** | **str**| Default Router MAC Address to use for this Virtual Router. Should be a valid MAC address. | [optional]
 **spec_vxlan_vni** | **int**| VxlAN VNI for the Virtual Router. Value should be between 0 and 16777215. | [optional]
 **route_import_export_address_family** | **str**| Address family where this config applies. | [optional]
 **route_import_export_rd_auto** | **bool**| True indicates the system will generate the RD automatically. | [optional]
 **rd_type** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format** | **str**|  | [optional]
 **admin_value_value** | **int**|  | [optional]
 **rd_assigned_value** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **spec_default_ipam_policy** | **str**| Default IPAM policy for networks belonging to this Virtual Router. Any IPAM Policy specified in the Network overrides this. | [optional]
 **status_id** | **str**| Handle allocated in the system. | [optional]
 **status_route_table** | **str**|  | [optional]
 **rd_type2** | **str**| RD Type as in rfc4364. | [optional]
 **admin_value_format2** | **str**|  | [optional]
 **admin_value_value2** | **int**|  | [optional]
 **rd_assigned_value2** | **int**| Assigned subfield of Value. Length depends on Type. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup get_virtual_router_peering_group(o_tenant, o_name)

Get VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group: %s\n" % e)
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
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **get_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup get_virtual_router_peering_group1(o_name)

Get VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VirtualRouterPeeringGroup object
        api_response = api_instance.get_virtual_router_peering_group1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->get_virtual_router_peering_group1: %s\n" % e)
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
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_ipam_policy**
> NetworkIPAMPolicy label_ipam_policy(o_tenant, o_name, body)

Label IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label IPAMPolicy object
        api_response = api_instance.label_ipam_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->label_ipam_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_ipam_policy1**
> NetworkIPAMPolicy label_ipam_policy1(o_name, body)

Label IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_network**
> NetworkNetwork label_network(o_tenant, o_name, body)

Label Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label Network object
        api_response = api_instance.label_network(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->label_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_network1**
> NetworkNetwork label_network1(o_name, body)

Label Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_network_interface**
> NetworkNetworkInterface label_network_interface(o_name, body)

Label NetworkInterface object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_network_interface import NetworkNetworkInterface
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_policer_profile**
> NetworkPolicerProfile label_policer_profile(o_tenant, o_name, body)

Label PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label PolicerProfile object
        api_response = api_instance.label_policer_profile(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->label_policer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_policer_profile1**
> NetworkPolicerProfile label_policer_profile1(o_name, body)

Label PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_routing_config**
> NetworkRoutingConfig label_routing_config(o_name, body)

Label RoutingConfig object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.network_routing_config import NetworkRoutingConfig
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_virtual_router**
> NetworkVirtualRouter label_virtual_router(o_tenant, o_name, body)

Label VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label VirtualRouter object
        api_response = api_instance.label_virtual_router(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_virtual_router1**
> NetworkVirtualRouter label_virtual_router1(o_name, body)

Label VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup label_virtual_router_peering_group(o_tenant, o_name, body)

Label VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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
        # Label VirtualRouterPeeringGroup object
        api_response = api_instance.label_virtual_router_peering_group(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->label_virtual_router_peering_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **label_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup label_virtual_router_peering_group1(o_name, body)

Label VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_label import ApiLabel
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_ipam_policy**
> NetworkIPAMPolicyList list_ipam_policy(o_tenant)

List IPAMPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_ipam_policy_list import NetworkIPAMPolicyList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List IPAMPolicy objects
        api_response = api_instance.list_ipam_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_ipam_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List IPAMPolicy objects
        api_response = api_instance.list_ipam_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_ipam_policy: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_ipam_policy1**
> NetworkIPAMPolicyList list_ipam_policy1()

List IPAMPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_ipam_policy_list import NetworkIPAMPolicyList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List IPAMPolicy objects
        api_response = api_instance.list_ipam_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_ipam_policy1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_network**
> NetworkNetworkList list_network(o_tenant)

List Network objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network_list import NetworkNetworkList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List Network objects
        api_response = api_instance.list_network(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network objects
        api_response = api_instance.list_network(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_network: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_network1**
> NetworkNetworkList list_network1()

List Network objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network_list import NetworkNetworkList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network objects
        api_response = api_instance.list_network1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_network1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_network_interface**
> NetworkNetworkInterfaceList list_network_interface()

List NetworkInterface objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_network_interface_list import NetworkNetworkInterfaceList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List NetworkInterface objects
        api_response = api_instance.list_network_interface(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_network_interface: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_policer_profile**
> NetworkPolicerProfileList list_policer_profile(o_tenant)

List PolicerProfile objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_policer_profile_list import NetworkPolicerProfileList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List PolicerProfile objects
        api_response = api_instance.list_policer_profile(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_policer_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List PolicerProfile objects
        api_response = api_instance.list_policer_profile(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_policer_profile: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_policer_profile1**
> NetworkPolicerProfileList list_policer_profile1()

List PolicerProfile objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_policer_profile_list import NetworkPolicerProfileList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List PolicerProfile objects
        api_response = api_instance.list_policer_profile1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_policer_profile1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_route_table**
> NetworkRouteTableList list_route_table(o_tenant)

List RouteTable objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_route_table_list import NetworkRouteTableList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List RouteTable objects
        api_response = api_instance.list_route_table(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_route_table: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List RouteTable objects
        api_response = api_instance.list_route_table(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_route_table: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_route_table1**
> NetworkRouteTableList list_route_table1()

List RouteTable objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_route_table_list import NetworkRouteTableList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List RouteTable objects
        api_response = api_instance.list_route_table1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_route_table1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_routing_config**
> NetworkRoutingConfigList list_routing_config()

List RoutingConfig objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_routing_config_list import NetworkRoutingConfigList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List RoutingConfig objects
        api_response = api_instance.list_routing_config(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_routing_config: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_virtual_router**
> NetworkVirtualRouterList list_virtual_router(o_tenant)

List VirtualRouter objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_list import NetworkVirtualRouterList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouter objects
        api_response = api_instance.list_virtual_router(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List VirtualRouter objects
        api_response = api_instance.list_virtual_router(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_virtual_router1**
> NetworkVirtualRouterList list_virtual_router1()

List VirtualRouter objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_list import NetworkVirtualRouterList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List VirtualRouter objects
        api_response = api_instance.list_virtual_router1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroupList list_virtual_router_peering_group(o_tenant)

List VirtualRouterPeeringGroup objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group_list import NetworkVirtualRouterPeeringGroupList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # List VirtualRouterPeeringGroup objects
        api_response = api_instance.list_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router_peering_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List VirtualRouterPeeringGroup objects
        api_response = api_instance.list_virtual_router_peering_group(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router_peering_group: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **list_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroupList list_virtual_router_peering_group1()

List VirtualRouterPeeringGroup objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group_list import NetworkVirtualRouterPeeringGroupList
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List VirtualRouterPeeringGroup objects
        api_response = api_instance.list_virtual_router_peering_group1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router_peering_group1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_ipam_policy**
> NetworkIPAMPolicy update_ipam_policy(o_tenant, o_name, body)

Update IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_ipam_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->update_ipam_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_ipam_policy1**
> NetworkIPAMPolicy update_ipam_policy1(o_name, body)

Update IPAMPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_ipam_policy import NetworkIPAMPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_network**
> NetworkNetwork update_network(o_tenant, o_name, body)

Update Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_network(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->update_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_network1**
> NetworkNetwork update_network1(o_name, body)

Update Network object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_network import NetworkNetwork
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_network_interface**
> NetworkNetworkInterface update_network_interface(o_name, body)

Update NetworkInterface object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_network_interface import NetworkNetworkInterface
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_policer_profile**
> NetworkPolicerProfile update_policer_profile(o_tenant, o_name, body)

Update PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_policer_profile(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->update_policer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_policer_profile1**
> NetworkPolicerProfile update_policer_profile1(o_name, body)

Update PolicerProfile object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_policer_profile import NetworkPolicerProfile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_routing_config**
> NetworkRoutingConfig update_routing_config(o_name, body)

Update RoutingConfig object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_routing_config import NetworkRoutingConfig
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_virtual_router**
> NetworkVirtualRouter update_virtual_router(o_tenant, o_name, body)

Update VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_virtual_router(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_virtual_router1**
> NetworkVirtualRouter update_virtual_router1(o_name, body)

Update VirtualRouter object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router import NetworkVirtualRouter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_virtual_router_peering_group**
> NetworkVirtualRouterPeeringGroup update_virtual_router_peering_group(o_tenant, o_name, body)

Update VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_virtual_router_peering_group(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->update_virtual_router_peering_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **update_virtual_router_peering_group1**
> NetworkVirtualRouterPeeringGroup update_virtual_router_peering_group1(o_name, body)

Update VirtualRouterPeeringGroup object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_virtual_router_peering_group import NetworkVirtualRouterPeeringGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
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
    except ApiException as e:
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_ipam_policy**
> NetworkAutoMsgIPAMPolicyWatchHelper watch_ipam_policy(o_tenant)

Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_ipam_policy_watch_helper import NetworkAutoMsgIPAMPolicyWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ipam_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_ipam_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ipam_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_ipam_policy: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_ipam_policy1**
> NetworkAutoMsgIPAMPolicyWatchHelper watch_ipam_policy1()

Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_ipam_policy_watch_helper import NetworkAutoMsgIPAMPolicyWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ipam_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_ipam_policy1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_network**
> NetworkAutoMsgNetworkWatchHelper watch_network(o_tenant)

Watch Network objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_auto_msg_network_watch_helper import NetworkAutoMsgNetworkWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch Network objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Network objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_network1**
> NetworkAutoMsgNetworkWatchHelper watch_network1()

Watch Network objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_auto_msg_network_watch_helper import NetworkAutoMsgNetworkWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Network objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_network_interface**
> NetworkAutoMsgNetworkInterfaceWatchHelper watch_network_interface()

Watch NetworkInterface objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_network_interface_watch_helper import NetworkAutoMsgNetworkInterfaceWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch NetworkInterface objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_interface(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_network_interface: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_policer_profile**
> NetworkAutoMsgPolicerProfileWatchHelper watch_policer_profile(o_tenant)

Watch PolicerProfile objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_auto_msg_policer_profile_watch_helper import NetworkAutoMsgPolicerProfileWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_policer_profile(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_policer_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_policer_profile(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_policer_profile: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_policer_profile1**
> NetworkAutoMsgPolicerProfileWatchHelper watch_policer_profile1()

Watch PolicerProfile objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pensando_cloud.psm_cloud.model.network_auto_msg_policer_profile_watch_helper import NetworkAutoMsgPolicerProfileWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_policer_profile1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_policer_profile1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_route_table**
> NetworkAutoMsgRouteTableWatchHelper watch_route_table(o_tenant)

Watch RouteTable objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_route_table_watch_helper import NetworkAutoMsgRouteTableWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch RouteTable objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_route_table(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_route_table: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch RouteTable objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_route_table(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_route_table: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_route_table1**
> NetworkAutoMsgRouteTableWatchHelper watch_route_table1()

Watch RouteTable objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_route_table_watch_helper import NetworkAutoMsgRouteTableWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch RouteTable objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_route_table1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_route_table1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_routing_config**
> NetworkAutoMsgRoutingConfigWatchHelper watch_routing_config()

Watch RoutingConfig objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_routing_config_watch_helper import NetworkAutoMsgRoutingConfigWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch RoutingConfig objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_routing_config(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_routing_config: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_virtual_router**
> NetworkAutoMsgVirtualRouterWatchHelper watch_virtual_router(o_tenant)

Watch VirtualRouter objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_virtual_router_watch_helper import NetworkAutoMsgVirtualRouterWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_virtual_router1**
> NetworkAutoMsgVirtualRouterWatchHelper watch_virtual_router1()

Watch VirtualRouter objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_virtual_router_watch_helper import NetworkAutoMsgVirtualRouterWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_virtual_router_peering_group**
> NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper watch_virtual_router_peering_group(o_tenant)

Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_virtual_router_peering_group_watch_helper import NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        # Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router_peering_group(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router_peering_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router_peering_group(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router_peering_group: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

# **watch_virtual_router_peering_group1**
> NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper watch_virtual_router_peering_group1()

Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_cloud
from pensando_cloud.psm_cloud.api import network_v1_api
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.models.network import *
from pensando_cloud.psm_cloud  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_cloud.psm_cloud.model.network_auto_msg_virtual_router_peering_group_watch_helper import NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper
from pensando_cloud.psm_cloud.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_cloud.psm_cloud.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_virtual_router_peering_group1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkV1Api->watch_virtual_router_peering_group1: %s\n" % e)
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

[[Back to psm_cloud.NetworkV1Api top]](#psm_cloud.NetworkV1Api) [[Back to network README]](../psm_cloud/docs/network/README.md) [[Back to pensando_cloud README]](../README.md)

