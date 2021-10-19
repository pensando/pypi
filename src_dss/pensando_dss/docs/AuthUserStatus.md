# AuthUserStatus

status part of user object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_review** | [**[AuthOperationStatus]**](AuthOperationStatus.md) | Authorization information about requested operations. | [optional] 
**authenticators** | **[str]** | Authenticators used for last successful login. | [optional] 
**last_login** | **datetime** | Last login time. | [optional] 
**last_password_change** | **datetime** | Last password change time for local user. | [optional] 
**roles** | **[str]** | Roles assigned to user. | [optional] 
**user_groups** | **[str]** | Groups that external user belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


