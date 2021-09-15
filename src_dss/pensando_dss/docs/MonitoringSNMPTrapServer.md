# MonitoringSNMPTrapServer

SNMPTrapServer contains the configuration for sending SNMP traps to a receiver.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_config** | [**MonitoringAuthConfig**](MonitoringAuthConfig.md) |  | [optional] 
**community_or_user** | **str** | CommunityOrUser contains community string for v2c, user for v3. | [optional] 
**host** | **str** | Host where the trap needs to be sent. | [optional] 
**port** | **str** | Port on the Host where the trap needs to be sent, default is 162. | [optional]  if omitted the server will use the default value of "162"
**privacy_config** | [**MonitoringPrivacyConfig**](MonitoringPrivacyConfig.md) |  | [optional] 
**version** | **str** |  | [optional]  if omitted the server will use the default value of "v2c"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


