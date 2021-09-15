# NetworkBGPConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | [**ApiBgpAsn**](ApiBgpAsn.md) |  | [optional] 
**dsc_auto_config** | **bool** | DSCAutoConfig sets the flag that this config is to be used as a template for auto configuration. | [optional] 
**holdtime** | **int** | Holdtime is time for which not receiving a keepalive message results in declaring the peer as dead. Value should be between 0 and 3600. | [optional]  if omitted the server will use the default value of 180
**keepalive_interval** | **int** | KeepaliveInterval is time interval at which keepalive messages are sent. Value should be between 0 and 3600. | [optional]  if omitted the server will use the default value of 60
**neighbors** | [**[NetworkBGPNeighbor]**](NetworkBGPNeighbor.md) | List of all neighbors. | [optional] 
**router_id** | **str** | Router ID for the BGP Instance. Should be a valid v4 or v6 IP address. | [optional] 
**suppress_default_resolution** | **bool** | SuppressDefaultResolution excludes default route from being used to resolve nexthop reachability in the underlay. WARNING: modifying this has network-wide data traffic impact as it temporarily deactivates and then re-activates all underlay and overlay routes on every node where this config is applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


