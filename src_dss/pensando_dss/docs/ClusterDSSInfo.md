# ClusterDSSInfo

Distributed service switch (DSS) information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsms** | [**[ClusterDSM]**](ClusterDSM.md) | Distributed service module information. | [optional] 
**fault_info** | [**ClusterFault**](ClusterFault.md) |  | [optional] 
**forwarding_profile** | **str** | ForwardingProfile is the active forwarding profile on the DSS. Supported forwarding profiles on the DSS platform are Leaf, Spine, Border-Leaf, L3-Core &amp; L3-Agg. It cannot be changed from PSM, it&#39;s reported to PSM for display purposes. | [optional] 
**ha_peer** | [**ClusterPeer**](ClusterPeer.md) |  | [optional] 
**host_name** | **str** | Hostname of the switch. | [optional] 
**link_info** | [**[ClusterNeighborPortInfo]**](ClusterNeighborPortInfo.md) | Information of the remote port mac amd local port of a link. | [optional] 
**version** | **str** | switch software version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


