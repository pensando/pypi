# network

This page provides working code examples for the **network** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NetworkV1Api* | [**add_ipam_policy**](../../../docs/NetworkV1Api.md#add_ipam_policy) | **POST** /configs/network/v1/tenant/{O.Tenant}/ipam-policies | Create IPAMPolicy object
*NetworkV1Api* | [**add_ipam_policy1**](../../../docs/NetworkV1Api.md#add_ipam_policy1) | **POST** /configs/network/v1/ipam-policies | Create IPAMPolicy object
*NetworkV1Api* | [**add_network**](../../../docs/NetworkV1Api.md#add_network) | **POST** /configs/network/v1/tenant/{O.Tenant}/networks | Create Network object
*NetworkV1Api* | [**add_network1**](../../../docs/NetworkV1Api.md#add_network1) | **POST** /configs/network/v1/networks | Create Network object
*NetworkV1Api* | [**add_policer_profile**](../../../docs/NetworkV1Api.md#add_policer_profile) | **POST** /configs/network/v1/tenant/{O.Tenant}/policer-profile | Create PolicerProfile object
*NetworkV1Api* | [**add_policer_profile1**](../../../docs/NetworkV1Api.md#add_policer_profile1) | **POST** /configs/network/v1/policer-profile | Create PolicerProfile object
*NetworkV1Api* | [**add_routing_config**](../../../docs/NetworkV1Api.md#add_routing_config) | **POST** /configs/network/v1/routing-config | Create RoutingConfig object
*NetworkV1Api* | [**add_virtual_router**](../../../docs/NetworkV1Api.md#add_virtual_router) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtualrouters | Create VirtualRouter object
*NetworkV1Api* | [**add_virtual_router1**](../../../docs/NetworkV1Api.md#add_virtual_router1) | **POST** /configs/network/v1/virtualrouters | Create VirtualRouter object
*NetworkV1Api* | [**add_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#add_virtual_router_peering_group) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups | Create VirtualRouterPeeringGroup object
*NetworkV1Api* | [**add_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#add_virtual_router_peering_group1) | **POST** /configs/network/v1/virtual-router-peering-groups | Create VirtualRouterPeeringGroup object
*NetworkV1Api* | [**delete_ipam_policy**](../../../docs/NetworkV1Api.md#delete_ipam_policy) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Delete IPAMPolicy object
*NetworkV1Api* | [**delete_ipam_policy1**](../../../docs/NetworkV1Api.md#delete_ipam_policy1) | **DELETE** /configs/network/v1/ipam-policies/{O.Name} | Delete IPAMPolicy object
*NetworkV1Api* | [**delete_network**](../../../docs/NetworkV1Api.md#delete_network) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Delete Network object
*NetworkV1Api* | [**delete_network1**](../../../docs/NetworkV1Api.md#delete_network1) | **DELETE** /configs/network/v1/networks/{O.Name} | Delete Network object
*NetworkV1Api* | [**delete_policer_profile**](../../../docs/NetworkV1Api.md#delete_policer_profile) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Delete PolicerProfile object
*NetworkV1Api* | [**delete_policer_profile1**](../../../docs/NetworkV1Api.md#delete_policer_profile1) | **DELETE** /configs/network/v1/policer-profile/{O.Name} | Delete PolicerProfile object
*NetworkV1Api* | [**delete_routing_config**](../../../docs/NetworkV1Api.md#delete_routing_config) | **DELETE** /configs/network/v1/routing-config/{O.Name} | Delete RoutingConfig object
*NetworkV1Api* | [**delete_virtual_router**](../../../docs/NetworkV1Api.md#delete_virtual_router) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Delete VirtualRouter object
*NetworkV1Api* | [**delete_virtual_router1**](../../../docs/NetworkV1Api.md#delete_virtual_router1) | **DELETE** /configs/network/v1/virtualrouters/{O.Name} | Delete VirtualRouter object
*NetworkV1Api* | [**delete_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#delete_virtual_router_peering_group) | **DELETE** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Delete VirtualRouterPeeringGroup object
*NetworkV1Api* | [**delete_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#delete_virtual_router_peering_group1) | **DELETE** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Delete VirtualRouterPeeringGroup object
*NetworkV1Api* | [**get_ipam_policy**](../../../docs/NetworkV1Api.md#get_ipam_policy) | **GET** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Get IPAMPolicy object
*NetworkV1Api* | [**get_ipam_policy1**](../../../docs/NetworkV1Api.md#get_ipam_policy1) | **GET** /configs/network/v1/ipam-policies/{O.Name} | Get IPAMPolicy object
*NetworkV1Api* | [**get_network**](../../../docs/NetworkV1Api.md#get_network) | **GET** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Get Network object
*NetworkV1Api* | [**get_network1**](../../../docs/NetworkV1Api.md#get_network1) | **GET** /configs/network/v1/networks/{O.Name} | Get Network object
*NetworkV1Api* | [**get_network_interface**](../../../docs/NetworkV1Api.md#get_network_interface) | **GET** /configs/network/v1/networkinterfaces/{O.Name} | Get NetworkInterface object
*NetworkV1Api* | [**get_policer_profile**](../../../docs/NetworkV1Api.md#get_policer_profile) | **GET** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Get PolicerProfile object
*NetworkV1Api* | [**get_policer_profile1**](../../../docs/NetworkV1Api.md#get_policer_profile1) | **GET** /configs/network/v1/policer-profile/{O.Name} | Get PolicerProfile object
*NetworkV1Api* | [**get_route_table**](../../../docs/NetworkV1Api.md#get_route_table) | **GET** /configs/network/v1/tenant/{O.Tenant}/route-tables/{O.Name} | Get RouteTable object
*NetworkV1Api* | [**get_route_table1**](../../../docs/NetworkV1Api.md#get_route_table1) | **GET** /configs/network/v1/route-tables/{O.Name} | Get RouteTable object
*NetworkV1Api* | [**get_routing_config**](../../../docs/NetworkV1Api.md#get_routing_config) | **GET** /configs/network/v1/routing-config/{O.Name} | Get RoutingConfig object
*NetworkV1Api* | [**get_virtual_router**](../../../docs/NetworkV1Api.md#get_virtual_router) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Get VirtualRouter object
*NetworkV1Api* | [**get_virtual_router1**](../../../docs/NetworkV1Api.md#get_virtual_router1) | **GET** /configs/network/v1/virtualrouters/{O.Name} | Get VirtualRouter object
*NetworkV1Api* | [**get_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#get_virtual_router_peering_group) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Get VirtualRouterPeeringGroup object
*NetworkV1Api* | [**get_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#get_virtual_router_peering_group1) | **GET** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Get VirtualRouterPeeringGroup object
*NetworkV1Api* | [**label_ipam_policy**](../../../docs/NetworkV1Api.md#label_ipam_policy) | **POST** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name}/label | Label IPAMPolicy object
*NetworkV1Api* | [**label_ipam_policy1**](../../../docs/NetworkV1Api.md#label_ipam_policy1) | **POST** /configs/network/v1/ipam-policies/{O.Name}/label | Label IPAMPolicy object
*NetworkV1Api* | [**label_network**](../../../docs/NetworkV1Api.md#label_network) | **POST** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name}/label | Label Network object
*NetworkV1Api* | [**label_network1**](../../../docs/NetworkV1Api.md#label_network1) | **POST** /configs/network/v1/networks/{O.Name}/label | Label Network object
*NetworkV1Api* | [**label_network_interface**](../../../docs/NetworkV1Api.md#label_network_interface) | **POST** /configs/network/v1/networkinterfaces/{O.Name}/label | Label NetworkInterface object
*NetworkV1Api* | [**label_policer_profile**](../../../docs/NetworkV1Api.md#label_policer_profile) | **POST** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name}/label | Label PolicerProfile object
*NetworkV1Api* | [**label_policer_profile1**](../../../docs/NetworkV1Api.md#label_policer_profile1) | **POST** /configs/network/v1/policer-profile/{O.Name}/label | Label PolicerProfile object
*NetworkV1Api* | [**label_routing_config**](../../../docs/NetworkV1Api.md#label_routing_config) | **POST** /configs/network/v1/routing-config/{O.Name}/label | Label RoutingConfig object
*NetworkV1Api* | [**label_virtual_router**](../../../docs/NetworkV1Api.md#label_virtual_router) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name}/label | Label VirtualRouter object
*NetworkV1Api* | [**label_virtual_router1**](../../../docs/NetworkV1Api.md#label_virtual_router1) | **POST** /configs/network/v1/virtualrouters/{O.Name}/label | Label VirtualRouter object
*NetworkV1Api* | [**label_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#label_virtual_router_peering_group) | **POST** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name}/label | Label VirtualRouterPeeringGroup object
*NetworkV1Api* | [**label_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#label_virtual_router_peering_group1) | **POST** /configs/network/v1/virtual-router-peering-groups/{O.Name}/label | Label VirtualRouterPeeringGroup object
*NetworkV1Api* | [**list_ipam_policy**](../../../docs/NetworkV1Api.md#list_ipam_policy) | **GET** /configs/network/v1/tenant/{O.Tenant}/ipam-policies | List IPAMPolicy objects
*NetworkV1Api* | [**list_ipam_policy1**](../../../docs/NetworkV1Api.md#list_ipam_policy1) | **GET** /configs/network/v1/ipam-policies | List IPAMPolicy objects
*NetworkV1Api* | [**list_network**](../../../docs/NetworkV1Api.md#list_network) | **GET** /configs/network/v1/tenant/{O.Tenant}/networks | List Network objects
*NetworkV1Api* | [**list_network1**](../../../docs/NetworkV1Api.md#list_network1) | **GET** /configs/network/v1/networks | List Network objects
*NetworkV1Api* | [**list_network_interface**](../../../docs/NetworkV1Api.md#list_network_interface) | **GET** /configs/network/v1/networkinterfaces | List NetworkInterface objects
*NetworkV1Api* | [**list_policer_profile**](../../../docs/NetworkV1Api.md#list_policer_profile) | **GET** /configs/network/v1/tenant/{O.Tenant}/policer-profile | List PolicerProfile objects
*NetworkV1Api* | [**list_policer_profile1**](../../../docs/NetworkV1Api.md#list_policer_profile1) | **GET** /configs/network/v1/policer-profile | List PolicerProfile objects
*NetworkV1Api* | [**list_route_table**](../../../docs/NetworkV1Api.md#list_route_table) | **GET** /configs/network/v1/tenant/{O.Tenant}/route-tables | List RouteTable objects
*NetworkV1Api* | [**list_route_table1**](../../../docs/NetworkV1Api.md#list_route_table1) | **GET** /configs/network/v1/route-tables | List RouteTable objects
*NetworkV1Api* | [**list_routing_config**](../../../docs/NetworkV1Api.md#list_routing_config) | **GET** /configs/network/v1/routing-config | List RoutingConfig objects
*NetworkV1Api* | [**list_virtual_router**](../../../docs/NetworkV1Api.md#list_virtual_router) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtualrouters | List VirtualRouter objects
*NetworkV1Api* | [**list_virtual_router1**](../../../docs/NetworkV1Api.md#list_virtual_router1) | **GET** /configs/network/v1/virtualrouters | List VirtualRouter objects
*NetworkV1Api* | [**list_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#list_virtual_router_peering_group) | **GET** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups | List VirtualRouterPeeringGroup objects
*NetworkV1Api* | [**list_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#list_virtual_router_peering_group1) | **GET** /configs/network/v1/virtual-router-peering-groups | List VirtualRouterPeeringGroup objects
*NetworkV1Api* | [**update_ipam_policy**](../../../docs/NetworkV1Api.md#update_ipam_policy) | **PUT** /configs/network/v1/tenant/{O.Tenant}/ipam-policies/{O.Name} | Update IPAMPolicy object
*NetworkV1Api* | [**update_ipam_policy1**](../../../docs/NetworkV1Api.md#update_ipam_policy1) | **PUT** /configs/network/v1/ipam-policies/{O.Name} | Update IPAMPolicy object
*NetworkV1Api* | [**update_network**](../../../docs/NetworkV1Api.md#update_network) | **PUT** /configs/network/v1/tenant/{O.Tenant}/networks/{O.Name} | Update Network object
*NetworkV1Api* | [**update_network1**](../../../docs/NetworkV1Api.md#update_network1) | **PUT** /configs/network/v1/networks/{O.Name} | Update Network object
*NetworkV1Api* | [**update_network_interface**](../../../docs/NetworkV1Api.md#update_network_interface) | **PUT** /configs/network/v1/networkinterfaces/{O.Name} | Update NetworkInterface object
*NetworkV1Api* | [**update_policer_profile**](../../../docs/NetworkV1Api.md#update_policer_profile) | **PUT** /configs/network/v1/tenant/{O.Tenant}/policer-profile/{O.Name} | Update PolicerProfile object
*NetworkV1Api* | [**update_policer_profile1**](../../../docs/NetworkV1Api.md#update_policer_profile1) | **PUT** /configs/network/v1/policer-profile/{O.Name} | Update PolicerProfile object
*NetworkV1Api* | [**update_routing_config**](../../../docs/NetworkV1Api.md#update_routing_config) | **PUT** /configs/network/v1/routing-config/{O.Name} | Update RoutingConfig object
*NetworkV1Api* | [**update_virtual_router**](../../../docs/NetworkV1Api.md#update_virtual_router) | **PUT** /configs/network/v1/tenant/{O.Tenant}/virtualrouters/{O.Name} | Update VirtualRouter object
*NetworkV1Api* | [**update_virtual_router1**](../../../docs/NetworkV1Api.md#update_virtual_router1) | **PUT** /configs/network/v1/virtualrouters/{O.Name} | Update VirtualRouter object
*NetworkV1Api* | [**update_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#update_virtual_router_peering_group) | **PUT** /configs/network/v1/tenant/{O.Tenant}/virtual-router-peering-groups/{O.Name} | Update VirtualRouterPeeringGroup object
*NetworkV1Api* | [**update_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#update_virtual_router_peering_group1) | **PUT** /configs/network/v1/virtual-router-peering-groups/{O.Name} | Update VirtualRouterPeeringGroup object
*NetworkV1Api* | [**watch_ipam_policy**](../../../docs/NetworkV1Api.md#watch_ipam_policy) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/ipam-policies | Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_ipam_policy1**](../../../docs/NetworkV1Api.md#watch_ipam_policy1) | **GET** /configs/network/v1/watch/ipam-policies | Watch IPAMPolicy objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_network**](../../../docs/NetworkV1Api.md#watch_network) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/networks | Watch Network objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_network1**](../../../docs/NetworkV1Api.md#watch_network1) | **GET** /configs/network/v1/watch/networks | Watch Network objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_network_interface**](../../../docs/NetworkV1Api.md#watch_network_interface) | **GET** /configs/network/v1/watch/networkinterfaces | Watch NetworkInterface objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_policer_profile**](../../../docs/NetworkV1Api.md#watch_policer_profile) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/policer-profile | Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_policer_profile1**](../../../docs/NetworkV1Api.md#watch_policer_profile1) | **GET** /configs/network/v1/watch/policer-profile | Watch PolicerProfile objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_route_table**](../../../docs/NetworkV1Api.md#watch_route_table) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/route-tables | Watch RouteTable objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_route_table1**](../../../docs/NetworkV1Api.md#watch_route_table1) | **GET** /configs/network/v1/watch/route-tables | Watch RouteTable objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_routing_config**](../../../docs/NetworkV1Api.md#watch_routing_config) | **GET** /configs/network/v1/watch/routing-config | Watch RoutingConfig objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_virtual_router**](../../../docs/NetworkV1Api.md#watch_virtual_router) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/virtualrouters | Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_virtual_router1**](../../../docs/NetworkV1Api.md#watch_virtual_router1) | **GET** /configs/network/v1/watch/virtualrouters | Watch VirtualRouter objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_virtual_router_peering_group**](../../../docs/NetworkV1Api.md#watch_virtual_router_peering_group) | **GET** /configs/network/v1/watch/tenant/{O.Tenant}/virtual-router-peering-groups | Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll
*NetworkV1Api* | [**watch_virtual_router_peering_group1**](../../../docs/NetworkV1Api.md#watch_virtual_router_peering_group1) | **GET** /configs/network/v1/watch/virtual-router-peering-groups | Watch VirtualRouterPeeringGroup objects. Supports WebSockets or HTTP long poll


## README links for Model Groups

[aggwatch README.md](..//aggwatch/README.md)

[audit README.md](..//audit/README.md)

[auth README.md](..//auth/README.md)

[browser README.md](..//browser/README.md)

[cluster README.md](..//cluster/README.md)

[diagnostics README.md](..//diagnostics/README.md)

[events README.md](..//events/README.md)

[fwlog README.md](..//fwlog/README.md)

[monitoring README.md](..//monitoring/README.md)

[network README.md](..//network/README.md)

[objstore README.md](..//objstore/README.md)

[orchestration README.md](..//orchestration/README.md)

[preferences README.md](..//preferences/README.md)

[recoverykeys README.md](..//recoverykeys/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[sysruntime README.md](..//sysruntime/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiBgpAsn](../../../docs/ApiBgpAsn.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiLabel](../../../docs/ApiLabel.md)
 - [ApiListMeta](../../../docs/ApiListMeta.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiRDAdminValue](../../../docs/ApiRDAdminValue.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [ClusterIPConfig](../../../docs/ClusterIPConfig.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [NetworkAutoMsgIPAMPolicyWatchHelper](../../../docs/NetworkAutoMsgIPAMPolicyWatchHelper.md)
 - [NetworkAutoMsgIPAMPolicyWatchHelperWatchEvent](../../../docs/NetworkAutoMsgIPAMPolicyWatchHelperWatchEvent.md)
 - [NetworkAutoMsgLbPolicyWatchHelper](../../../docs/NetworkAutoMsgLbPolicyWatchHelper.md)
 - [NetworkAutoMsgLbPolicyWatchHelperWatchEvent](../../../docs/NetworkAutoMsgLbPolicyWatchHelperWatchEvent.md)
 - [NetworkAutoMsgNetworkInterfaceWatchHelper](../../../docs/NetworkAutoMsgNetworkInterfaceWatchHelper.md)
 - [NetworkAutoMsgNetworkInterfaceWatchHelperWatchEvent](../../../docs/NetworkAutoMsgNetworkInterfaceWatchHelperWatchEvent.md)
 - [NetworkAutoMsgNetworkWatchHelper](../../../docs/NetworkAutoMsgNetworkWatchHelper.md)
 - [NetworkAutoMsgNetworkWatchHelperWatchEvent](../../../docs/NetworkAutoMsgNetworkWatchHelperWatchEvent.md)
 - [NetworkAutoMsgPolicerProfileWatchHelper](../../../docs/NetworkAutoMsgPolicerProfileWatchHelper.md)
 - [NetworkAutoMsgPolicerProfileWatchHelperWatchEvent](../../../docs/NetworkAutoMsgPolicerProfileWatchHelperWatchEvent.md)
 - [NetworkAutoMsgRouteTableWatchHelper](../../../docs/NetworkAutoMsgRouteTableWatchHelper.md)
 - [NetworkAutoMsgRouteTableWatchHelperWatchEvent](../../../docs/NetworkAutoMsgRouteTableWatchHelperWatchEvent.md)
 - [NetworkAutoMsgRoutingConfigWatchHelper](../../../docs/NetworkAutoMsgRoutingConfigWatchHelper.md)
 - [NetworkAutoMsgRoutingConfigWatchHelperWatchEvent](../../../docs/NetworkAutoMsgRoutingConfigWatchHelperWatchEvent.md)
 - [NetworkAutoMsgServiceWatchHelper](../../../docs/NetworkAutoMsgServiceWatchHelper.md)
 - [NetworkAutoMsgServiceWatchHelperWatchEvent](../../../docs/NetworkAutoMsgServiceWatchHelperWatchEvent.md)
 - [NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper](../../../docs/NetworkAutoMsgVirtualRouterPeeringGroupWatchHelper.md)
 - [NetworkAutoMsgVirtualRouterPeeringGroupWatchHelperWatchEvent](../../../docs/NetworkAutoMsgVirtualRouterPeeringGroupWatchHelperWatchEvent.md)
 - [NetworkAutoMsgVirtualRouterWatchHelper](../../../docs/NetworkAutoMsgVirtualRouterWatchHelper.md)
 - [NetworkAutoMsgVirtualRouterWatchHelperWatchEvent](../../../docs/NetworkAutoMsgVirtualRouterWatchHelperWatchEvent.md)
 - [NetworkBGPAuthStatus](../../../docs/NetworkBGPAuthStatus.md)
 - [NetworkBGPConfig](../../../docs/NetworkBGPConfig.md)
 - [NetworkBGPNeighbor](../../../docs/NetworkBGPNeighbor.md)
 - [NetworkDHCPRelayPolicy](../../../docs/NetworkDHCPRelayPolicy.md)
 - [NetworkDHCPServer](../../../docs/NetworkDHCPServer.md)
 - [NetworkHealthCheckSpec](../../../docs/NetworkHealthCheckSpec.md)
 - [NetworkIPAMPolicy](../../../docs/NetworkIPAMPolicy.md)
 - [NetworkIPAMPolicyList](../../../docs/NetworkIPAMPolicyList.md)
 - [NetworkIPAMPolicySpec](../../../docs/NetworkIPAMPolicySpec.md)
 - [NetworkIPAMPolicyStatus](../../../docs/NetworkIPAMPolicyStatus.md)
 - [NetworkLLDPNeighbor](../../../docs/NetworkLLDPNeighbor.md)
 - [NetworkLbPolicy](../../../docs/NetworkLbPolicy.md)
 - [NetworkLbPolicyList](../../../docs/NetworkLbPolicyList.md)
 - [NetworkLbPolicySpec](../../../docs/NetworkLbPolicySpec.md)
 - [NetworkLbPolicyStatus](../../../docs/NetworkLbPolicyStatus.md)
 - [NetworkNetwork](../../../docs/NetworkNetwork.md)
 - [NetworkNetworkInterface](../../../docs/NetworkNetworkInterface.md)
 - [NetworkNetworkInterfaceHostStatus](../../../docs/NetworkNetworkInterfaceHostStatus.md)
 - [NetworkNetworkInterfaceList](../../../docs/NetworkNetworkInterfaceList.md)
 - [NetworkNetworkInterfaceSpec](../../../docs/NetworkNetworkInterfaceSpec.md)
 - [NetworkNetworkInterfaceStatus](../../../docs/NetworkNetworkInterfaceStatus.md)
 - [NetworkNetworkInterfaceUplinkStatus](../../../docs/NetworkNetworkInterfaceUplinkStatus.md)
 - [NetworkNetworkList](../../../docs/NetworkNetworkList.md)
 - [NetworkNetworkSpec](../../../docs/NetworkNetworkSpec.md)
 - [NetworkNetworkStatus](../../../docs/NetworkNetworkStatus.md)
 - [NetworkOrchestratorInfo](../../../docs/NetworkOrchestratorInfo.md)
 - [NetworkPauseSpec](../../../docs/NetworkPauseSpec.md)
 - [NetworkPolicerAction](../../../docs/NetworkPolicerAction.md)
 - [NetworkPolicerCriteria](../../../docs/NetworkPolicerCriteria.md)
 - [NetworkPolicerProfile](../../../docs/NetworkPolicerProfile.md)
 - [NetworkPolicerProfileList](../../../docs/NetworkPolicerProfileList.md)
 - [NetworkPolicerProfileSpec](../../../docs/NetworkPolicerProfileSpec.md)
 - [NetworkPolicerProfileStatus](../../../docs/NetworkPolicerProfileStatus.md)
 - [NetworkRDSpec](../../../docs/NetworkRDSpec.md)
 - [NetworkRoute](../../../docs/NetworkRoute.md)
 - [NetworkRouteDistinguisher](../../../docs/NetworkRouteDistinguisher.md)
 - [NetworkRouteTable](../../../docs/NetworkRouteTable.md)
 - [NetworkRouteTableList](../../../docs/NetworkRouteTableList.md)
 - [NetworkRouteTableStatus](../../../docs/NetworkRouteTableStatus.md)
 - [NetworkRoutingConfig](../../../docs/NetworkRoutingConfig.md)
 - [NetworkRoutingConfigList](../../../docs/NetworkRoutingConfigList.md)
 - [NetworkRoutingConfigSpec](../../../docs/NetworkRoutingConfigSpec.md)
 - [NetworkRoutingConfigStatus](../../../docs/NetworkRoutingConfigStatus.md)
 - [NetworkService](../../../docs/NetworkService.md)
 - [NetworkServiceList](../../../docs/NetworkServiceList.md)
 - [NetworkServiceSpec](../../../docs/NetworkServiceSpec.md)
 - [NetworkServiceStatus](../../../docs/NetworkServiceStatus.md)
 - [NetworkTLSClientPolicySpec](../../../docs/NetworkTLSClientPolicySpec.md)
 - [NetworkTLSServerPolicySpec](../../../docs/NetworkTLSServerPolicySpec.md)
 - [NetworkTransceiverStatus](../../../docs/NetworkTransceiverStatus.md)
 - [NetworkVirtualRouter](../../../docs/NetworkVirtualRouter.md)
 - [NetworkVirtualRouterList](../../../docs/NetworkVirtualRouterList.md)
 - [NetworkVirtualRouterPeeringGroup](../../../docs/NetworkVirtualRouterPeeringGroup.md)
 - [NetworkVirtualRouterPeeringGroupList](../../../docs/NetworkVirtualRouterPeeringGroupList.md)
 - [NetworkVirtualRouterPeeringGroupSpec](../../../docs/NetworkVirtualRouterPeeringGroupSpec.md)
 - [NetworkVirtualRouterPeeringGroupStatus](../../../docs/NetworkVirtualRouterPeeringGroupStatus.md)
 - [NetworkVirtualRouterPeeringRoute](../../../docs/NetworkVirtualRouterPeeringRoute.md)
 - [NetworkVirtualRouterPeeringRouteTable](../../../docs/NetworkVirtualRouterPeeringRouteTable.md)
 - [NetworkVirtualRouterPeeringSpec](../../../docs/NetworkVirtualRouterPeeringSpec.md)
 - [NetworkVirtualRouterSpec](../../../docs/NetworkVirtualRouterSpec.md)
 - [NetworkVirtualRouterStatus](../../../docs/NetworkVirtualRouterStatus.md)
 - [SecurityDSCStatus](../../../docs/SecurityDSCStatus.md)
 - [SecurityPropagationStatus](../../../docs/SecurityPropagationStatus.md)


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
