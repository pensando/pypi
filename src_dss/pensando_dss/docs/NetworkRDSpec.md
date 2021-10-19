# NetworkRDSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** | Address family where this config applies. | [optional]  if omitted the server will use the default value of "ipv4-unicast"
**rd** | [**NetworkRouteDistinguisher**](NetworkRouteDistinguisher.md) |  | [optional] 
**rd_auto** | **bool** | True indicates the system will generate the RD automatically. | [optional] 
**rt_export** | [**[NetworkRouteDistinguisher]**](NetworkRouteDistinguisher.md) | Route Targets to Export. | [optional] 
**rt_import** | [**[NetworkRouteDistinguisher]**](NetworkRouteDistinguisher.md) | Route Targets to Import. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


