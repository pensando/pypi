# NetworkNetworkFirewallProfile

Firewall features that can be enabled on the network Interaction with the global firewall profile setting is as follows: If the feature is disabled at the global and network levels, the feature is disabled on the network If the feature is enabled at the global and network levels, the feature is enabled on the network If the feature is disabled at the global level and enabled at the network, the feature is enabled on the network If the feature is enabled at the global level and disabled at the network level, the feature is enabled on the network. So to turn off the feature on a network, the feature must be disabled at both the global and network levels.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_fw_logging** | **bool** | EnableFwLogging enables flow logging on the network. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


