# OrchestrationManagedNamespaceSpec

ManagedNamespaceSpec contains namespace specific configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_operation** | **str** |  | [optional]  if omitted the server will use the default value of "disc-op-default"
**discovery_protocol** | **str** |  | [optional]  if omitted the server will use the default value of "disc-proto-default"
**mtu** | **int** | MTU, 0 &#x3D; Use system-default or orchestrator settings. | [optional]  if omitted the server will use the default value of 0
**multicast_filter** | **str** |  | [optional]  if omitted the server will use the default value of "mcast-filter-default"
**override_vlan_end** | **int** | End of vlan range (inclusive) to be used for overrides. Range should be &gt;&#x3D; number of vnics expected per host. Value should be between 0 and 4095. | [optional]  if omitted the server will use the default value of 4087
**override_vlan_start** | **int** | Start of vlan range to be used for overrides. Range should be &gt;&#x3D; number of vnics expected per host. Value should be between 0 and 4095. | [optional]  if omitted the server will use the default value of 3832

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


