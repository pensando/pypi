# NetworkBGPNeighbor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_as_in** | **int** | AllowASIn allows local ASN to be in received routes. The value indicates how many instances are allowed. 0 disables the feature. Value should be between 0 and 255. | [optional] 
**dsc_auto_config** | **bool** | DSCAutoConfig sets the flag that this neighbor config is to be used as a template for auto configuration. | [optional] 
**enable_address_families** | **[str]** | Address families to enable on the neighbor. | [optional] 
**holdtime** | **int** | Holdtime is time for which not receiving a keepalive message results in declaring the peer as dead. Value should be between 0 and 3600. | [optional] 
**ip_address** | **str** | Neighbor IP Address. Should be a valid v4 or v6 IP address. | [optional] 
**keepalive_interval** | **int** | KeepaliveInterval is time interval at which keepalive messages are sent. Value should be between 0 and 3600. | [optional] 
**multi_hop** | **int** | BGP Multihop configuration. Value should be between 1 and 255. | [optional]  if omitted the server will use the default value of 64
**password** | **str** | Enable Password authentication. Disabled if the string is empty. Length of string should be between 1 and 128. | [optional] 
**remote_as** | [**ApiBgpAsn**](ApiBgpAsn.md) |  | [optional] 
**shutdown** | **bool** | Shutdown this neighbor session. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


