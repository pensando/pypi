```python

import time
import psm
from pprint import pprint
from api import auth_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.auth_auto_msg_authentication_policy_watch_helper import AuthAutoMsgAuthenticationPolicyWatchHelper
from pensando_ent.psm.model.auth_auto_msg_role_binding_watch_helper import AuthAutoMsgRoleBindingWatchHelper
from pensando_ent.psm.model.auth_auto_msg_role_watch_helper import AuthAutoMsgRoleWatchHelper
from pensando_ent.psm.model.auth_auto_msg_user_preference_watch_helper import AuthAutoMsgUserPreferenceWatchHelper
from pensando_ent.psm.model.auth_auto_msg_user_watch_helper import AuthAutoMsgUserWatchHelper
from pensando_ent.psm.model.auth_password_change_request import AuthPasswordChangeRequest
from pensando_ent.psm.model.auth_password_reset_request import AuthPasswordResetRequest
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.auth_role_binding_list import AuthRoleBindingList
from pensando_ent.psm.model.auth_role_list import AuthRoleList
from pensando_ent.psm.model.auth_subject_access_review_request import AuthSubjectAccessReviewRequest
from pensando_ent.psm.model.auth_token_secret_request import AuthTokenSecretRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.auth_user_list import AuthUserList
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthAuthenticationPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=AuthAuthenticationPolicySpec(
            authenticators=AuthAuthenticators(
                authenticator_order=[
                    "authenticator_order_example",
                ],
                ldap=AuthLdap(
                    domains=[
                        AuthLdapDomain(
                            attribute_mapping=AuthLdapAttributeMapping(
                                email="email_example",
                                fullname="fullname_example",
                                group="group_example",
                                group_object_class="group_object_class_example",
                                tenant="tenant_example",
                                user="user_example",
                                user_object_class="user_object_class_example",
                            ),
                            base_dn="base_dn_example",
                            bind_dn="bind_dn_example",
                            bind_password="bind_password_example",
                            servers=[
                                AuthLdapServer(
                                    tls_options=AuthTLSOptions(
                                        server_name="server_name_example",
                                        skip_server_cert_verification=True,
                                        start_tls=True,
                                        trusted_certs="trusted_certs_example",
                                    ),
                                    url="url_example",
                                ),
                            ],
                            tag="tag_example",
                        ),
                    ],
                ),
                local={},
                radius=AuthRadius(
                    domains=[
                        AuthRadiusDomain(
                            nas_id="nas_id_example",
                            servers=[
                                AuthRadiusServer(
                                    auth_method="pap",
                                    secret="secret_example",
                                    trusted_certs="trusted_certs_example",
                                    url="url_example",
                                ),
                            ],
                            tag="tag_example",
                        ),
                    ],
                ),
            ),
            secret='YQ==',
            token_expiry="60s",
        ),
        status=AuthAuthenticationPolicyStatus(
            ldap_servers=[
                AuthLdapServerStatus(
                    base_dn="base_dn_example",
                    bind_dn="bind_dn_example",
                    bind_password="bind_password_example",
                    message="message_example",
                    result="connect-success",
                    server=AuthLdapServer(
                        tls_options=AuthTLSOptions(
                            server_name="server_name_example",
                            skip_server_cert_verification=True,
                            start_tls=True,
                            trusted_certs="trusted_certs_example",
                        ),
                        url="url_example",
                    ),
                ),
            ],
            radius_servers=[
                AuthRadiusServerStatus(
                    message="message_example",
                    nas_id="nas_id_example",
                    result="connect-success",
                    server=AuthRadiusServer(
                        auth_method="pap",
                        secret="secret_example",
                        trusted_certs="trusted_certs_example",
                        url="url_example",
                    ),
                ),
            ],
        ),
    ) # AuthAuthenticationPolicy | 

    try:
        # Create AuthenticationPolicy object
        api_response = api_instance.add_authentication_policy(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_authentication_policy: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthV1Api* | [**add_authentication_policy**](docs/AuthV1Api.md#add_authentication_policy) | **POST** /configs/auth/v1/authn-policy | Create AuthenticationPolicy object
*AuthV1Api* | [**add_role**](docs/AuthV1Api.md#add_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles | Create Role object
*AuthV1Api* | [**add_role1**](docs/AuthV1Api.md#add_role1) | **POST** /configs/auth/v1/roles | Create Role object
*AuthV1Api* | [**add_role_binding**](docs/AuthV1Api.md#add_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | Create RoleBinding object
*AuthV1Api* | [**add_role_binding1**](docs/AuthV1Api.md#add_role_binding1) | **POST** /configs/auth/v1/role-bindings | Create RoleBinding object
*AuthV1Api* | [**add_user**](docs/AuthV1Api.md#add_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users | Create User object
*AuthV1Api* | [**add_user1**](docs/AuthV1Api.md#add_user1) | **POST** /configs/auth/v1/users | Create User object
*AuthV1Api* | [**delete_role**](docs/AuthV1Api.md#delete_role) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Delete Role object
*AuthV1Api* | [**delete_role1**](docs/AuthV1Api.md#delete_role1) | **DELETE** /configs/auth/v1/roles/{O.Name} | Delete Role object
*AuthV1Api* | [**delete_role_binding**](docs/AuthV1Api.md#delete_role_binding) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Delete RoleBinding object
*AuthV1Api* | [**delete_role_binding1**](docs/AuthV1Api.md#delete_role_binding1) | **DELETE** /configs/auth/v1/role-bindings/{O.Name} | Delete RoleBinding object
*AuthV1Api* | [**delete_user**](docs/AuthV1Api.md#delete_user) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Delete User object
*AuthV1Api* | [**delete_user1**](docs/AuthV1Api.md#delete_user1) | **DELETE** /configs/auth/v1/users/{O.Name} | Delete User object
*AuthV1Api* | [**get_authentication_policy**](docs/AuthV1Api.md#get_authentication_policy) | **GET** /configs/auth/v1/authn-policy | Get AuthenticationPolicy object
*AuthV1Api* | [**get_role**](docs/AuthV1Api.md#get_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Get Role object
*AuthV1Api* | [**get_role1**](docs/AuthV1Api.md#get_role1) | **GET** /configs/auth/v1/roles/{O.Name} | Get Role object
*AuthV1Api* | [**get_role_binding**](docs/AuthV1Api.md#get_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Get RoleBinding object
*AuthV1Api* | [**get_role_binding1**](docs/AuthV1Api.md#get_role_binding1) | **GET** /configs/auth/v1/role-bindings/{O.Name} | Get RoleBinding object
*AuthV1Api* | [**get_user**](docs/AuthV1Api.md#get_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Get User object
*AuthV1Api* | [**get_user1**](docs/AuthV1Api.md#get_user1) | **GET** /configs/auth/v1/users/{O.Name} | Get User object
*AuthV1Api* | [**get_user_preference**](docs/AuthV1Api.md#get_user_preference) | **GET** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Get UserPreference object
*AuthV1Api* | [**get_user_preference1**](docs/AuthV1Api.md#get_user_preference1) | **GET** /configs/auth/v1/user-preferences/{O.Name} | Get UserPreference object
*AuthV1Api* | [**is_authorized**](docs/AuthV1Api.md#is_authorized) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/IsAuthorized | Review authorization for user
*AuthV1Api* | [**is_authorized1**](docs/AuthV1Api.md#is_authorized1) | **POST** /configs/auth/v1/users/{O.Name}/IsAuthorized | Review authorization for user
*AuthV1Api* | [**label_authentication_policy**](docs/AuthV1Api.md#label_authentication_policy) | **POST** /configs/auth/v1/authn-policy/label | Label AuthenticationPolicy object
*AuthV1Api* | [**label_role**](docs/AuthV1Api.md#label_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name}/label | Label Role object
*AuthV1Api* | [**label_role1**](docs/AuthV1Api.md#label_role1) | **POST** /configs/auth/v1/roles/{O.Name}/label | Label Role object
*AuthV1Api* | [**label_role_binding**](docs/AuthV1Api.md#label_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name}/label | Label RoleBinding object
*AuthV1Api* | [**label_role_binding1**](docs/AuthV1Api.md#label_role_binding1) | **POST** /configs/auth/v1/role-bindings/{O.Name}/label | Label RoleBinding object
*AuthV1Api* | [**label_user**](docs/AuthV1Api.md#label_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/label | Label User object
*AuthV1Api* | [**label_user1**](docs/AuthV1Api.md#label_user1) | **POST** /configs/auth/v1/users/{O.Name}/label | Label User object
*AuthV1Api* | [**label_user_preference**](docs/AuthV1Api.md#label_user_preference) | **POST** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name}/label | Label UserPreference object
*AuthV1Api* | [**label_user_preference1**](docs/AuthV1Api.md#label_user_preference1) | **POST** /configs/auth/v1/user-preferences/{O.Name}/label | Label UserPreference object
*AuthV1Api* | [**ldap_bind_check**](docs/AuthV1Api.md#ldap_bind_check) | **POST** /configs/auth/v1/authn-policy/LdapBindCheck | Test LDAP bind operation
*AuthV1Api* | [**ldap_connection_check**](docs/AuthV1Api.md#ldap_connection_check) | **POST** /configs/auth/v1/authn-policy/LdapConnectionCheck | Test LDAP connection
*AuthV1Api* | [**list_role**](docs/AuthV1Api.md#list_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles | List Role objects
*AuthV1Api* | [**list_role1**](docs/AuthV1Api.md#list_role1) | **GET** /configs/auth/v1/roles | List Role objects
*AuthV1Api* | [**list_role_binding**](docs/AuthV1Api.md#list_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | List RoleBinding objects
*AuthV1Api* | [**list_role_binding1**](docs/AuthV1Api.md#list_role_binding1) | **GET** /configs/auth/v1/role-bindings | List RoleBinding objects
*AuthV1Api* | [**list_user**](docs/AuthV1Api.md#list_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users | List User objects
*AuthV1Api* | [**list_user1**](docs/AuthV1Api.md#list_user1) | **GET** /configs/auth/v1/users | List User objects
*AuthV1Api* | [**password_change**](docs/AuthV1Api.md#password_change) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordChange | Change user password
*AuthV1Api* | [**password_change1**](docs/AuthV1Api.md#password_change1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordChange | Change user password
*AuthV1Api* | [**password_reset**](docs/AuthV1Api.md#password_reset) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordReset | Reset user password
*AuthV1Api* | [**password_reset1**](docs/AuthV1Api.md#password_reset1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordReset | Reset user password
*AuthV1Api* | [**token_secret_generate**](docs/AuthV1Api.md#token_secret_generate) | **POST** /configs/auth/v1/authn-policy/TokenSecretGenerate | Generate secret for token signing
*AuthV1Api* | [**update_authentication_policy**](docs/AuthV1Api.md#update_authentication_policy) | **PUT** /configs/auth/v1/authn-policy | Update AuthenticationPolicy object
*AuthV1Api* | [**update_role**](docs/AuthV1Api.md#update_role) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Update Role object
*AuthV1Api* | [**update_role1**](docs/AuthV1Api.md#update_role1) | **PUT** /configs/auth/v1/roles/{O.Name} | Update Role object
*AuthV1Api* | [**update_role_binding**](docs/AuthV1Api.md#update_role_binding) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Update RoleBinding object
*AuthV1Api* | [**update_role_binding1**](docs/AuthV1Api.md#update_role_binding1) | **PUT** /configs/auth/v1/role-bindings/{O.Name} | Update RoleBinding object
*AuthV1Api* | [**update_user**](docs/AuthV1Api.md#update_user) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Update User object
*AuthV1Api* | [**update_user1**](docs/AuthV1Api.md#update_user1) | **PUT** /configs/auth/v1/users/{O.Name} | Update User object
*AuthV1Api* | [**update_user_preference**](docs/AuthV1Api.md#update_user_preference) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Update UserPreference object
*AuthV1Api* | [**update_user_preference1**](docs/AuthV1Api.md#update_user_preference1) | **PUT** /configs/auth/v1/user-preferences/{O.Name} | Update UserPreference object
*AuthV1Api* | [**watch_authentication_policy**](docs/AuthV1Api.md#watch_authentication_policy) | **GET** /configs/auth/v1/watch/authn-policy | Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role**](docs/AuthV1Api.md#watch_role) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/roles | Watch Role objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role1**](docs/AuthV1Api.md#watch_role1) | **GET** /configs/auth/v1/watch/roles | Watch Role objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role_binding**](docs/AuthV1Api.md#watch_role_binding) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_role_binding1**](docs/AuthV1Api.md#watch_role_binding1) | **GET** /configs/auth/v1/watch/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user**](docs/AuthV1Api.md#watch_user) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/users | Watch User objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user1**](docs/AuthV1Api.md#watch_user1) | **GET** /configs/auth/v1/watch/users | Watch User objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user_preference**](docs/AuthV1Api.md#watch_user_preference) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll
*AuthV1Api* | [**watch_user_preference1**](docs/AuthV1Api.md#watch_user_preference1) | **GET** /configs/auth/v1/watch/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiLabel](docs/ApiLabel.md)
 - [ApiListMeta](docs/ApiListMeta.md)
 - [ApiListWatchOptions](docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](docs/ApiObjectMeta.md)
 - [ApiObjectRef](docs/ApiObjectRef.md)
 - [ApiStatus](docs/ApiStatus.md)
 - [ApiStatusResult](docs/ApiStatusResult.md)
 - [ApiTimestamp](docs/ApiTimestamp.md)
 - [ApiTypeMeta](docs/ApiTypeMeta.md)
 - [ApiWatchControl](docs/ApiWatchControl.md)
 - [ApiWatchEvent](docs/ApiWatchEvent.md)
 - [ApiWatchEventList](docs/ApiWatchEventList.md)
 - [AuthAuthenticationPolicy](docs/AuthAuthenticationPolicy.md)
 - [AuthAuthenticationPolicyList](docs/AuthAuthenticationPolicyList.md)
 - [AuthAuthenticationPolicySpec](docs/AuthAuthenticationPolicySpec.md)
 - [AuthAuthenticationPolicyStatus](docs/AuthAuthenticationPolicyStatus.md)
 - [AuthAuthenticators](docs/AuthAuthenticators.md)
 - [AuthAutoMsgAuthenticationPolicyWatchHelper](docs/AuthAutoMsgAuthenticationPolicyWatchHelper.md)
 - [AuthAutoMsgAuthenticationPolicyWatchHelperWatchEvent](docs/AuthAutoMsgAuthenticationPolicyWatchHelperWatchEvent.md)
 - [AuthAutoMsgRoleBindingWatchHelper](docs/AuthAutoMsgRoleBindingWatchHelper.md)
 - [AuthAutoMsgRoleBindingWatchHelperWatchEvent](docs/AuthAutoMsgRoleBindingWatchHelperWatchEvent.md)
 - [AuthAutoMsgRoleWatchHelper](docs/AuthAutoMsgRoleWatchHelper.md)
 - [AuthAutoMsgRoleWatchHelperWatchEvent](docs/AuthAutoMsgRoleWatchHelperWatchEvent.md)
 - [AuthAutoMsgUserPreferenceWatchHelper](docs/AuthAutoMsgUserPreferenceWatchHelper.md)
 - [AuthAutoMsgUserPreferenceWatchHelperWatchEvent](docs/AuthAutoMsgUserPreferenceWatchHelperWatchEvent.md)
 - [AuthAutoMsgUserWatchHelper](docs/AuthAutoMsgUserWatchHelper.md)
 - [AuthAutoMsgUserWatchHelperWatchEvent](docs/AuthAutoMsgUserWatchHelperWatchEvent.md)
 - [AuthLdap](docs/AuthLdap.md)
 - [AuthLdapAttributeMapping](docs/AuthLdapAttributeMapping.md)
 - [AuthLdapDomain](docs/AuthLdapDomain.md)
 - [AuthLdapServer](docs/AuthLdapServer.md)
 - [AuthLdapServerStatus](docs/AuthLdapServerStatus.md)
 - [AuthOperation](docs/AuthOperation.md)
 - [AuthOperationStatus](docs/AuthOperationStatus.md)
 - [AuthPasswordChangeRequest](docs/AuthPasswordChangeRequest.md)
 - [AuthPasswordResetRequest](docs/AuthPasswordResetRequest.md)
 - [AuthPermission](docs/AuthPermission.md)
 - [AuthRadius](docs/AuthRadius.md)
 - [AuthRadiusDomain](docs/AuthRadiusDomain.md)
 - [AuthRadiusServer](docs/AuthRadiusServer.md)
 - [AuthRadiusServerStatus](docs/AuthRadiusServerStatus.md)
 - [AuthResource](docs/AuthResource.md)
 - [AuthRole](docs/AuthRole.md)
 - [AuthRoleBinding](docs/AuthRoleBinding.md)
 - [AuthRoleBindingList](docs/AuthRoleBindingList.md)
 - [AuthRoleBindingSpec](docs/AuthRoleBindingSpec.md)
 - [AuthRoleList](docs/AuthRoleList.md)
 - [AuthRoleSpec](docs/AuthRoleSpec.md)
 - [AuthSubjectAccessReviewRequest](docs/AuthSubjectAccessReviewRequest.md)
 - [AuthTLSOptions](docs/AuthTLSOptions.md)
 - [AuthTokenSecretRequest](docs/AuthTokenSecretRequest.md)
 - [AuthUser](docs/AuthUser.md)
 - [AuthUserList](docs/AuthUserList.md)
 - [AuthUserPreference](docs/AuthUserPreference.md)
 - [AuthUserPreferenceList](docs/AuthUserPreferenceList.md)
 - [AuthUserPreferenceSpec](docs/AuthUserPreferenceSpec.md)
 - [AuthUserSpec](docs/AuthUserSpec.md)
 - [AuthUserStatus](docs/AuthUserStatus.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)


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
