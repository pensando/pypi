
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthV1Api* | [**add_authentication_policy**](../../../../pensando_cloud/docs/AuthV1Api.md#add_authentication_policy) | **POST** /configs/auth/v1/authn-policy | Create AuthenticationPolicy object
*AuthV1Api* | [**add_role**](../../../../pensando_cloud/docs/AuthV1Api.md#add_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles | Create Role object
*AuthV1Api* | [**add_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#add_role1) | **POST** /configs/auth/v1/roles | Create Role object
*AuthV1Api* | [**add_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#add_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | Create RoleBinding object
*AuthV1Api* | [**add_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#add_role_binding1) | **POST** /configs/auth/v1/role-bindings | Create RoleBinding object
*AuthV1Api* | [**add_user**](../../../../pensando_cloud/docs/AuthV1Api.md#add_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users | Create User object
*AuthV1Api* | [**add_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#add_user1) | **POST** /configs/auth/v1/users | Create User object
*AuthV1Api* | [**delete_role**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_role) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Delete Role object
*AuthV1Api* | [**delete_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_role1) | **DELETE** /configs/auth/v1/roles/{O.Name} | Delete Role object
*AuthV1Api* | [**delete_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_role_binding) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Delete RoleBinding object
*AuthV1Api* | [**delete_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_role_binding1) | **DELETE** /configs/auth/v1/role-bindings/{O.Name} | Delete RoleBinding object
*AuthV1Api* | [**delete_user**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_user) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Delete User object
*AuthV1Api* | [**delete_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#delete_user1) | **DELETE** /configs/auth/v1/users/{O.Name} | Delete User object
*AuthV1Api* | [**get_authentication_policy**](../../../../pensando_cloud/docs/AuthV1Api.md#get_authentication_policy) | **GET** /configs/auth/v1/authn-policy | Get AuthenticationPolicy object
*AuthV1Api* | [**get_role**](../../../../pensando_cloud/docs/AuthV1Api.md#get_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Get Role object
*AuthV1Api* | [**get_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#get_role1) | **GET** /configs/auth/v1/roles/{O.Name} | Get Role object
*AuthV1Api* | [**get_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#get_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Get RoleBinding object
*AuthV1Api* | [**get_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#get_role_binding1) | **GET** /configs/auth/v1/role-bindings/{O.Name} | Get RoleBinding object
*AuthV1Api* | [**get_user**](../../../../pensando_cloud/docs/AuthV1Api.md#get_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Get User object
*AuthV1Api* | [**get_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#get_user1) | **GET** /configs/auth/v1/users/{O.Name} | Get User object
*AuthV1Api* | [**get_user_preference**](../../../../pensando_cloud/docs/AuthV1Api.md#get_user_preference) | **GET** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Get UserPreference object
*AuthV1Api* | [**get_user_preference1**](../../../../pensando_cloud/docs/AuthV1Api.md#get_user_preference1) | **GET** /configs/auth/v1/user-preferences/{O.Name} | Get UserPreference object
*AuthV1Api* | [**is_authorized**](../../../../pensando_cloud/docs/AuthV1Api.md#is_authorized) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/IsAuthorized | Review authorization for user
*AuthV1Api* | [**is_authorized1**](../../../../pensando_cloud/docs/AuthV1Api.md#is_authorized1) | **POST** /configs/auth/v1/users/{O.Name}/IsAuthorized | Review authorization for user
*AuthV1Api* | [**label_authentication_policy**](../../../../pensando_cloud/docs/AuthV1Api.md#label_authentication_policy) | **POST** /configs/auth/v1/authn-policy/label | Label AuthenticationPolicy object
*AuthV1Api* | [**label_role**](../../../../pensando_cloud/docs/AuthV1Api.md#label_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name}/label | Label Role object
*AuthV1Api* | [**label_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#label_role1) | **POST** /configs/auth/v1/roles/{O.Name}/label | Label Role object
*AuthV1Api* | [**label_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#label_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name}/label | Label RoleBinding object
*AuthV1Api* | [**label_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#label_role_binding1) | **POST** /configs/auth/v1/role-bindings/{O.Name}/label | Label RoleBinding object
*AuthV1Api* | [**label_user**](../../../../pensando_cloud/docs/AuthV1Api.md#label_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/label | Label User object
*AuthV1Api* | [**label_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#label_user1) | **POST** /configs/auth/v1/users/{O.Name}/label | Label User object
*AuthV1Api* | [**label_user_preference**](../../../../pensando_cloud/docs/AuthV1Api.md#label_user_preference) | **POST** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name}/label | Label UserPreference object
*AuthV1Api* | [**label_user_preference1**](../../../../pensando_cloud/docs/AuthV1Api.md#label_user_preference1) | **POST** /configs/auth/v1/user-preferences/{O.Name}/label | Label UserPreference object
*AuthV1Api* | [**ldap_bind_check**](../../../../pensando_cloud/docs/AuthV1Api.md#ldap_bind_check) | **POST** /configs/auth/v1/authn-policy/LdapBindCheck | Test LDAP bind operation
*AuthV1Api* | [**ldap_connection_check**](../../../../pensando_cloud/docs/AuthV1Api.md#ldap_connection_check) | **POST** /configs/auth/v1/authn-policy/LdapConnectionCheck | Test LDAP connection
*AuthV1Api* | [**list_role**](../../../../pensando_cloud/docs/AuthV1Api.md#list_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles | List Role objects
*AuthV1Api* | [**list_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#list_role1) | **GET** /configs/auth/v1/roles | List Role objects
*AuthV1Api* | [**list_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#list_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | List RoleBinding objects
*AuthV1Api* | [**list_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#list_role_binding1) | **GET** /configs/auth/v1/role-bindings | List RoleBinding objects
*AuthV1Api* | [**list_user**](../../../../pensando_cloud/docs/AuthV1Api.md#list_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users | List User objects
*AuthV1Api* | [**list_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#list_user1) | **GET** /configs/auth/v1/users | List User objects
*AuthV1Api* | [**password_change**](../../../../pensando_cloud/docs/AuthV1Api.md#password_change) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordChange | Change user password
*AuthV1Api* | [**password_change1**](../../../../pensando_cloud/docs/AuthV1Api.md#password_change1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordChange | Change user password
*AuthV1Api* | [**password_reset**](../../../../pensando_cloud/docs/AuthV1Api.md#password_reset) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordReset | Reset user password
*AuthV1Api* | [**password_reset1**](../../../../pensando_cloud/docs/AuthV1Api.md#password_reset1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordReset | Reset user password
*AuthV1Api* | [**token_secret_generate**](../../../../pensando_cloud/docs/AuthV1Api.md#token_secret_generate) | **POST** /configs/auth/v1/authn-policy/TokenSecretGenerate | Generate secret for token signing
*AuthV1Api* | [**update_authentication_policy**](../../../../pensando_cloud/docs/AuthV1Api.md#update_authentication_policy) | **PUT** /configs/auth/v1/authn-policy | Update AuthenticationPolicy object
*AuthV1Api* | [**update_role**](../../../../pensando_cloud/docs/AuthV1Api.md#update_role) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Update Role object
*AuthV1Api* | [**update_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#update_role1) | **PUT** /configs/auth/v1/roles/{O.Name} | Update Role object
*AuthV1Api* | [**update_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#update_role_binding) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Update RoleBinding object
*AuthV1Api* | [**update_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#update_role_binding1) | **PUT** /configs/auth/v1/role-bindings/{O.Name} | Update RoleBinding object
*AuthV1Api* | [**update_user**](../../../../pensando_cloud/docs/AuthV1Api.md#update_user) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Update User object
*AuthV1Api* | [**update_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#update_user1) | **PUT** /configs/auth/v1/users/{O.Name} | Update User object
*AuthV1Api* | [**update_user_preference**](../../../../pensando_cloud/docs/AuthV1Api.md#update_user_preference) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Update UserPreference object
*AuthV1Api* | [**update_user_preference1**](../../../../pensando_cloud/docs/AuthV1Api.md#update_user_preference1) | **PUT** /configs/auth/v1/user-preferences/{O.Name} | Update UserPreference object
*AuthV1Api* | [**watch_authentication_policy**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_authentication_policy) | **GET** /configs/auth/v1/watch/authn-policy | Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_role) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/roles | Watch Role objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role1**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_role1) | **GET** /configs/auth/v1/watch/roles | Watch Role objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role_binding**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_role_binding) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role_binding1**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_role_binding1) | **GET** /configs/auth/v1/watch/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_user) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/users | Watch User objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user1**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_user1) | **GET** /configs/auth/v1/watch/users | Watch User objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user_preference**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_user_preference) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user_preference1**](../../../../pensando_cloud/docs/AuthV1Api.md#watch_user_preference1) | **GET** /configs/auth/v1/watch/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiLabel](../../../docs/ApiLabel.md)
 - [ApiListMeta](../../../docs/ApiListMeta.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [AuthAuthenticationPolicy](../../../docs/AuthAuthenticationPolicy.md)
 - [AuthAuthenticationPolicyList](../../../docs/AuthAuthenticationPolicyList.md)
 - [AuthAuthenticationPolicySpec](../../../docs/AuthAuthenticationPolicySpec.md)
 - [AuthAuthenticationPolicyStatus](../../../docs/AuthAuthenticationPolicyStatus.md)
 - [AuthAuthenticators](../../../docs/AuthAuthenticators.md)
 - [AuthAutoMsgAuthenticationPolicyWatchHelper](../../../docs/AuthAutoMsgAuthenticationPolicyWatchHelper.md)
 - [AuthAutoMsgAuthenticationPolicyWatchHelperWatchEvent](../../../docs/AuthAutoMsgAuthenticationPolicyWatchHelperWatchEvent.md)
 - [AuthAutoMsgRoleBindingWatchHelper](../../../docs/AuthAutoMsgRoleBindingWatchHelper.md)
 - [AuthAutoMsgRoleBindingWatchHelperWatchEvent](../../../docs/AuthAutoMsgRoleBindingWatchHelperWatchEvent.md)
 - [AuthAutoMsgRoleWatchHelper](../../../docs/AuthAutoMsgRoleWatchHelper.md)
 - [AuthAutoMsgRoleWatchHelperWatchEvent](../../../docs/AuthAutoMsgRoleWatchHelperWatchEvent.md)
 - [AuthAutoMsgUserPreferenceWatchHelper](../../../docs/AuthAutoMsgUserPreferenceWatchHelper.md)
 - [AuthAutoMsgUserPreferenceWatchHelperWatchEvent](../../../docs/AuthAutoMsgUserPreferenceWatchHelperWatchEvent.md)
 - [AuthAutoMsgUserWatchHelper](../../../docs/AuthAutoMsgUserWatchHelper.md)
 - [AuthAutoMsgUserWatchHelperWatchEvent](../../../docs/AuthAutoMsgUserWatchHelperWatchEvent.md)
 - [AuthLdap](../../../docs/AuthLdap.md)
 - [AuthLdapAttributeMapping](../../../docs/AuthLdapAttributeMapping.md)
 - [AuthLdapDomain](../../../docs/AuthLdapDomain.md)
 - [AuthLdapServer](../../../docs/AuthLdapServer.md)
 - [AuthLdapServerStatus](../../../docs/AuthLdapServerStatus.md)
 - [AuthOperation](../../../docs/AuthOperation.md)
 - [AuthOperationStatus](../../../docs/AuthOperationStatus.md)
 - [AuthPasswordChangeRequest](../../../docs/AuthPasswordChangeRequest.md)
 - [AuthPasswordResetRequest](../../../docs/AuthPasswordResetRequest.md)
 - [AuthPermission](../../../docs/AuthPermission.md)
 - [AuthRadius](../../../docs/AuthRadius.md)
 - [AuthRadiusDomain](../../../docs/AuthRadiusDomain.md)
 - [AuthRadiusServer](../../../docs/AuthRadiusServer.md)
 - [AuthRadiusServerStatus](../../../docs/AuthRadiusServerStatus.md)
 - [AuthResource](../../../docs/AuthResource.md)
 - [AuthRole](../../../docs/AuthRole.md)
 - [AuthRoleBinding](../../../docs/AuthRoleBinding.md)
 - [AuthRoleBindingList](../../../docs/AuthRoleBindingList.md)
 - [AuthRoleBindingSpec](../../../docs/AuthRoleBindingSpec.md)
 - [AuthRoleList](../../../docs/AuthRoleList.md)
 - [AuthRoleSpec](../../../docs/AuthRoleSpec.md)
 - [AuthSubjectAccessReviewRequest](../../../docs/AuthSubjectAccessReviewRequest.md)
 - [AuthTLSOptions](../../../docs/AuthTLSOptions.md)
 - [AuthTokenSecretRequest](../../../docs/AuthTokenSecretRequest.md)
 - [AuthUser](../../../docs/AuthUser.md)
 - [AuthUserList](../../../docs/AuthUserList.md)
 - [AuthUserPreference](../../../docs/AuthUserPreference.md)
 - [AuthUserPreferenceList](../../../docs/AuthUserPreferenceList.md)
 - [AuthUserPreferenceSpec](../../../docs/AuthUserPreferenceSpec.md)
 - [AuthUserSpec](../../../docs/AuthUserSpec.md)
 - [AuthUserStatus](../../../docs/AuthUserStatus.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm.apis and psm.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm.api.default_api import DefaultApi`
- `from psm.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm
from psm.apis import *
from psm.models import *
```
