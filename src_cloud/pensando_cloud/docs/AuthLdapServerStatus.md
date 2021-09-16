# AuthLdapServerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | The LDAP base DN to be used in a user search. | [optional] 
**bind_dn** | **str** | The bind DN is the string that Venice uses to log in to the LDAP server. Venice uses this account to validate the remote user attempting to log in. The base DN is the container name and path in the LDAPserver where Venice searches for the remote user account. This is where the password is validated. This contains the user authorization and assigned RBAC roles for use on Venice. Venice requests the attribute from theLDAP server. | [optional] 
**bind_password** | **str** | The password for the LDAP database account specified in the Root DN field. | [optional] 
**message** | **str** | Message contains error message in case of failed check or a success message. | [optional] 
**result** | **str** | Result indicates if ldap check was successful. | [optional]  if omitted the server will use the default value of "connect-success"
**server** | [**AuthLdapServer**](AuthLdapServer.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


