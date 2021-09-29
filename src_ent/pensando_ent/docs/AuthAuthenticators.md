# AuthAuthenticators

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_order** | **[str]** | Order in which authenticators are applied. If an authenticator returns success, others are skipped. | [optional] 
**ldap** | [**AuthLdap**](AuthLdap.md) |  | [optional] 
**local** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**radius** | [**AuthRadius**](AuthRadius.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


