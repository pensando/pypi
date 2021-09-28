# psm.AuthV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_authentication_policy**](AuthV1Api.md#add_authentication_policy) | **POST** /configs/auth/v1/authn-policy | Create AuthenticationPolicy object
[**add_role**](AuthV1Api.md#add_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles | Create Role object
[**add_role1**](AuthV1Api.md#add_role1) | **POST** /configs/auth/v1/roles | Create Role object
[**add_role_binding**](AuthV1Api.md#add_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | Create RoleBinding object
[**add_role_binding1**](AuthV1Api.md#add_role_binding1) | **POST** /configs/auth/v1/role-bindings | Create RoleBinding object
[**add_user**](AuthV1Api.md#add_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users | Create User object
[**add_user1**](AuthV1Api.md#add_user1) | **POST** /configs/auth/v1/users | Create User object
[**delete_role**](AuthV1Api.md#delete_role) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Delete Role object
[**delete_role1**](AuthV1Api.md#delete_role1) | **DELETE** /configs/auth/v1/roles/{O.Name} | Delete Role object
[**delete_role_binding**](AuthV1Api.md#delete_role_binding) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Delete RoleBinding object
[**delete_role_binding1**](AuthV1Api.md#delete_role_binding1) | **DELETE** /configs/auth/v1/role-bindings/{O.Name} | Delete RoleBinding object
[**delete_user**](AuthV1Api.md#delete_user) | **DELETE** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Delete User object
[**delete_user1**](AuthV1Api.md#delete_user1) | **DELETE** /configs/auth/v1/users/{O.Name} | Delete User object
[**get_authentication_policy**](AuthV1Api.md#get_authentication_policy) | **GET** /configs/auth/v1/authn-policy | Get AuthenticationPolicy object
[**get_role**](AuthV1Api.md#get_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Get Role object
[**get_role1**](AuthV1Api.md#get_role1) | **GET** /configs/auth/v1/roles/{O.Name} | Get Role object
[**get_role_binding**](AuthV1Api.md#get_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Get RoleBinding object
[**get_role_binding1**](AuthV1Api.md#get_role_binding1) | **GET** /configs/auth/v1/role-bindings/{O.Name} | Get RoleBinding object
[**get_user**](AuthV1Api.md#get_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Get User object
[**get_user1**](AuthV1Api.md#get_user1) | **GET** /configs/auth/v1/users/{O.Name} | Get User object
[**get_user_preference**](AuthV1Api.md#get_user_preference) | **GET** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Get UserPreference object
[**get_user_preference1**](AuthV1Api.md#get_user_preference1) | **GET** /configs/auth/v1/user-preferences/{O.Name} | Get UserPreference object
[**is_authorized**](AuthV1Api.md#is_authorized) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/IsAuthorized | Review authorization for user
[**is_authorized1**](AuthV1Api.md#is_authorized1) | **POST** /configs/auth/v1/users/{O.Name}/IsAuthorized | Review authorization for user
[**label_authentication_policy**](AuthV1Api.md#label_authentication_policy) | **POST** /configs/auth/v1/authn-policy/label | Label AuthenticationPolicy object
[**label_role**](AuthV1Api.md#label_role) | **POST** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name}/label | Label Role object
[**label_role1**](AuthV1Api.md#label_role1) | **POST** /configs/auth/v1/roles/{O.Name}/label | Label Role object
[**label_role_binding**](AuthV1Api.md#label_role_binding) | **POST** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name}/label | Label RoleBinding object
[**label_role_binding1**](AuthV1Api.md#label_role_binding1) | **POST** /configs/auth/v1/role-bindings/{O.Name}/label | Label RoleBinding object
[**label_user**](AuthV1Api.md#label_user) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/label | Label User object
[**label_user1**](AuthV1Api.md#label_user1) | **POST** /configs/auth/v1/users/{O.Name}/label | Label User object
[**label_user_preference**](AuthV1Api.md#label_user_preference) | **POST** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name}/label | Label UserPreference object
[**label_user_preference1**](AuthV1Api.md#label_user_preference1) | **POST** /configs/auth/v1/user-preferences/{O.Name}/label | Label UserPreference object
[**ldap_bind_check**](AuthV1Api.md#ldap_bind_check) | **POST** /configs/auth/v1/authn-policy/LdapBindCheck | Test LDAP bind operation
[**ldap_connection_check**](AuthV1Api.md#ldap_connection_check) | **POST** /configs/auth/v1/authn-policy/LdapConnectionCheck | Test LDAP connection
[**list_role**](AuthV1Api.md#list_role) | **GET** /configs/auth/v1/tenant/{O.Tenant}/roles | List Role objects
[**list_role1**](AuthV1Api.md#list_role1) | **GET** /configs/auth/v1/roles | List Role objects
[**list_role_binding**](AuthV1Api.md#list_role_binding) | **GET** /configs/auth/v1/tenant/{O.Tenant}/role-bindings | List RoleBinding objects
[**list_role_binding1**](AuthV1Api.md#list_role_binding1) | **GET** /configs/auth/v1/role-bindings | List RoleBinding objects
[**list_user**](AuthV1Api.md#list_user) | **GET** /configs/auth/v1/tenant/{O.Tenant}/users | List User objects
[**list_user1**](AuthV1Api.md#list_user1) | **GET** /configs/auth/v1/users | List User objects
[**password_change**](AuthV1Api.md#password_change) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordChange | Change user password
[**password_change1**](AuthV1Api.md#password_change1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordChange | Change user password
[**password_reset**](AuthV1Api.md#password_reset) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/PasswordReset | Reset user password
[**password_reset1**](AuthV1Api.md#password_reset1) | **POST** /configs/auth/v1/users/{O.Name}/PasswordReset | Reset user password
[**token_secret_generate**](AuthV1Api.md#token_secret_generate) | **POST** /configs/auth/v1/authn-policy/TokenSecretGenerate | Generate secret for token signing
[**update_authentication_policy**](AuthV1Api.md#update_authentication_policy) | **PUT** /configs/auth/v1/authn-policy | Update AuthenticationPolicy object
[**update_role**](AuthV1Api.md#update_role) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/roles/{O.Name} | Update Role object
[**update_role1**](AuthV1Api.md#update_role1) | **PUT** /configs/auth/v1/roles/{O.Name} | Update Role object
[**update_role_binding**](AuthV1Api.md#update_role_binding) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/role-bindings/{O.Name} | Update RoleBinding object
[**update_role_binding1**](AuthV1Api.md#update_role_binding1) | **PUT** /configs/auth/v1/role-bindings/{O.Name} | Update RoleBinding object
[**update_user**](AuthV1Api.md#update_user) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name} | Update User object
[**update_user1**](AuthV1Api.md#update_user1) | **PUT** /configs/auth/v1/users/{O.Name} | Update User object
[**update_user_preference**](AuthV1Api.md#update_user_preference) | **PUT** /configs/auth/v1/tenant/{O.Tenant}/user-preferences/{O.Name} | Update UserPreference object
[**update_user_preference1**](AuthV1Api.md#update_user_preference1) | **PUT** /configs/auth/v1/user-preferences/{O.Name} | Update UserPreference object
[**watch_authentication_policy**](AuthV1Api.md#watch_authentication_policy) | **GET** /configs/auth/v1/watch/authn-policy | Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll
[**watch_role**](AuthV1Api.md#watch_role) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/roles | Watch Role objects. Supports WebSockets or HTTP long poll
[**watch_role1**](AuthV1Api.md#watch_role1) | **GET** /configs/auth/v1/watch/roles | Watch Role objects. Supports WebSockets or HTTP long poll
[**watch_role_binding**](AuthV1Api.md#watch_role_binding) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
[**watch_role_binding1**](AuthV1Api.md#watch_role_binding1) | **GET** /configs/auth/v1/watch/role-bindings | Watch RoleBinding objects. Supports WebSockets or HTTP long poll
[**watch_user**](AuthV1Api.md#watch_user) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/users | Watch User objects. Supports WebSockets or HTTP long poll
[**watch_user1**](AuthV1Api.md#watch_user1) | **GET** /configs/auth/v1/watch/users | Watch User objects. Supports WebSockets or HTTP long poll
[**watch_user_preference**](AuthV1Api.md#watch_user_preference) | **GET** /configs/auth/v1/watch/tenant/{O.Tenant}/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll
[**watch_user_preference1**](AuthV1Api.md#watch_user_preference1) | **GET** /configs/auth/v1/watch/user-preferences | Watch UserPreference objects. Supports WebSockets or HTTP long poll


# **add_authentication_policy**
> AuthAuthenticationPolicy add_authentication_policy(body)

Create AuthenticationPolicy object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Create AuthenticationPolicy object
        api_response = api_instance.add_authentication_policy(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> AuthRole add_role(o_tenant, body)

Create Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRole(
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
        spec=AuthRoleSpec(
            permissions=[
                AuthPermission(
                    actions=[
                        "actions_example",
                    ],
                    resource_group="resource_group_example",
                    resource_kind="resource_kind_example",
                    resource_names=[
                        "resource_names_example",
                    ],
                    resource_namespace="_All_",
                    resource_tenant="resource_tenant_example",
                ),
            ],
        ),
        status={},
    ) # AuthRole | 

    # example passing only required values which don't have defaults set
    try:
        # Create Role object
        api_response = api_instance.add_role(o_tenant, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**AuthRole**](AuthRole.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role1**
> AuthRole add_role1(body)

Create Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthRole(
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
        spec=AuthRoleSpec(
            permissions=[
                AuthPermission(
                    actions=[
                        "actions_example",
                    ],
                    resource_group="resource_group_example",
                    resource_kind="resource_kind_example",
                    resource_names=[
                        "resource_names_example",
                    ],
                    resource_namespace="_All_",
                    resource_tenant="resource_tenant_example",
                ),
            ],
        ),
        status={},
    ) # AuthRole | 

    # example passing only required values which don't have defaults set
    try:
        # Create Role object
        api_response = api_instance.add_role1(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthRole**](AuthRole.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_binding**
> AuthRoleBinding add_role_binding(o_tenant, body)

Create RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRoleBinding(
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
        spec=AuthRoleBindingSpec(
            role="role_example",
            user_groups=[
                "user_groups_example",
            ],
            users=[
                "users_example",
            ],
        ),
        status={},
    ) # AuthRoleBinding | 

    # example passing only required values which don't have defaults set
    try:
        # Create RoleBinding object
        api_response = api_instance.add_role_binding(o_tenant, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**AuthRoleBinding**](AuthRoleBinding.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_binding1**
> AuthRoleBinding add_role_binding1(body)

Create RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthRoleBinding(
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
        spec=AuthRoleBindingSpec(
            role="role_example",
            user_groups=[
                "user_groups_example",
            ],
            users=[
                "users_example",
            ],
        ),
        status={},
    ) # AuthRoleBinding | 

    # example passing only required values which don't have defaults set
    try:
        # Create RoleBinding object
        api_response = api_instance.add_role_binding1(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthRoleBinding**](AuthRoleBinding.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> AuthUser add_user(o_tenant, body)

Create User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthUser(
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
        spec=AuthUserSpec(
            email=".@zyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCm6w-v0dZfUofvKER.smInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8.ohR8pb-ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6.3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKGSDRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEk.auW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e.q9Z4WMWovY63G.6ixTd5NxRU25mQYd6VBLRGkQ5H9-FH2v5iUaMQ.iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVYtYsFB.8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h64.MeAEDz67NG9dihNlL1YPO1GvRUDnbs.0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFW.pSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Z.x6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYPH.63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWk3GoxqObZMXxUrUZPuO24g6xCEEGY.5NZ9BhURG1p1vKPKEsaka3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxuH.cKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFoJb4.VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53h1KEc7ag0ak9ETa6LnPl34V25.c4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW.X3CHj-n2hyQ.B8SPpfjus1nT.PTJPb-Hj0LrcV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m.ONPCsy2yJE2MQH9Vtj3dWmBLqETJauR.5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgvhhe4JPG5EYj.qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk.G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203.y3cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcKpa5ZkmXKIhuWWL1PB8JQFInAlUi.vIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqicd-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOef.2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.jzJY",
            fullname="fullname_example",
            password="password_example",
            type="local",
        ),
        status=AuthUserStatus(
            access_review=[
                AuthOperationStatus(
                    allowed=True,
                    message="message_example",
                    operation=AuthOperation(
                        action="all-actions",
                        resource=AuthResource(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            tenant="tenant_example",
                        ),
                    ),
                ),
            ],
            authenticators=[
                "authenticators_example",
            ],
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            roles=[
                "roles_example",
            ],
            user_groups=[
                "user_groups_example",
            ],
        ),
    ) # AuthUser | 

    # example passing only required values which don't have defaults set
    try:
        # Create User object
        api_response = api_instance.add_user(o_tenant, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**AuthUser**](AuthUser.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user1**
> AuthUser add_user1(body)

Create User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthUser(
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
        spec=AuthUserSpec(
            email=".@zyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCm6w-v0dZfUofvKER.smInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8.ohR8pb-ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6.3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKGSDRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEk.auW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e.q9Z4WMWovY63G.6ixTd5NxRU25mQYd6VBLRGkQ5H9-FH2v5iUaMQ.iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVYtYsFB.8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h64.MeAEDz67NG9dihNlL1YPO1GvRUDnbs.0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFW.pSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Z.x6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYPH.63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWk3GoxqObZMXxUrUZPuO24g6xCEEGY.5NZ9BhURG1p1vKPKEsaka3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxuH.cKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFoJb4.VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53h1KEc7ag0ak9ETa6LnPl34V25.c4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW.X3CHj-n2hyQ.B8SPpfjus1nT.PTJPb-Hj0LrcV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m.ONPCsy2yJE2MQH9Vtj3dWmBLqETJauR.5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgvhhe4JPG5EYj.qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk.G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203.y3cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcKpa5ZkmXKIhuWWL1PB8JQFInAlUi.vIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqicd-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOef.2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.jzJY",
            fullname="fullname_example",
            password="password_example",
            type="local",
        ),
        status=AuthUserStatus(
            access_review=[
                AuthOperationStatus(
                    allowed=True,
                    message="message_example",
                    operation=AuthOperation(
                        action="all-actions",
                        resource=AuthResource(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            tenant="tenant_example",
                        ),
                    ),
                ),
            ],
            authenticators=[
                "authenticators_example",
            ],
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            roles=[
                "roles_example",
            ],
            user_groups=[
                "user_groups_example",
            ],
        ),
    ) # AuthUser | 

    # example passing only required values which don't have defaults set
    try:
        # Create User object
        api_response = api_instance.add_user1(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->add_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthUser**](AuthUser.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> AuthRole delete_role(o_tenant, o_name)

Delete Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Role object
        api_response = api_instance.delete_role(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role1**
> AuthRole delete_role1(o_name)

Delete Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Role object
        api_response = api_instance.delete_role1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_binding**
> AuthRoleBinding delete_role_binding(o_tenant, o_name)

Delete RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoleBinding object
        api_response = api_instance.delete_role_binding(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_binding1**
> AuthRoleBinding delete_role_binding1(o_name)

Delete RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoleBinding object
        api_response = api_instance.delete_role_binding1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> AuthUser delete_user(o_tenant, o_name)

Delete User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User object
        api_response = api_instance.delete_user(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user1**
> AuthUser delete_user1(o_name)

Delete User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User object
        api_response = api_instance.delete_user1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_policy**
> AuthAuthenticationPolicy get_authentication_policy()

Get AuthenticationPolicy object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_name = "meta.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    authenticators_authenticator_order = [
        "authenticators.authenticator-order_example",
    ] # [str] | Order in which authenticators are applied. If an authenticator returns success, others are skipped. (optional)
    spec_secret = 'YQ==' # str | Secret used to sign JWT token. (optional)
    spec_token_expiry = "spec.token-expiry_example" # str | TokenExpiry is time duration after which JWT token expires. Default is 6 days. A duration string is a sequence of decimal number and a unit suffix, such as \"300ms\" or \"2h45m\". Valid time units are \"ns\", \"us\" (or \"µs\"), \"ms\", \"s\", \"m\", \"h\". Should be a valid time duration. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AuthenticationPolicy object
        api_response = api_instance.get_authentication_policy(t_kind=t_kind, t_api_version=t_api_version, meta_name=meta_name, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, authenticators_authenticator_order=authenticators_authenticator_order, spec_secret=spec_secret, spec_token_expiry=spec_token_expiry)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **authenticators_authenticator_order** | **[str]**| Order in which authenticators are applied. If an authenticator returns success, others are skipped. | [optional]
 **spec_secret** | **str**| Secret used to sign JWT token. | [optional]
 **spec_token_expiry** | **str**| TokenExpiry is time duration after which JWT token expires. Default is 6 days. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Should be a valid time duration. | [optional]

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> AuthRole get_role(o_tenant, o_name)

Get Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role object
        api_response = api_instance.get_role(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Role object
        api_response = api_instance.get_role(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role1**
> AuthRole get_role1(o_name)

Get Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role object
        api_response = api_instance.get_role1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Role object
        api_response = api_instance.get_role1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_binding**
> AuthRoleBinding get_role_binding(o_tenant, o_name)

Get RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_users = [
        "spec.users_example",
    ] # [str] |  (optional)
    spec_user_groups = [
        "spec.user-groups_example",
    ] # [str] |  (optional)
    spec_role = "spec.role_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_users=spec_users, spec_user_groups=spec_user_groups, spec_role=spec_role)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_users** | **[str]**|  | [optional]
 **spec_user_groups** | **[str]**|  | [optional]
 **spec_role** | **str**|  | [optional]

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_binding1**
> AuthRoleBinding get_role_binding1(o_name)

Get RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_users = [
        "spec.users_example",
    ] # [str] |  (optional)
    spec_user_groups = [
        "spec.user-groups_example",
    ] # [str] |  (optional)
    spec_role = "spec.role_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_users=spec_users, spec_user_groups=spec_user_groups, spec_role=spec_role)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_users** | **[str]**|  | [optional]
 **spec_user_groups** | **[str]**|  | [optional]
 **spec_role** | **str**|  | [optional]

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> AuthUser get_user(o_tenant, o_name)

Get User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_fullname = "spec.fullname_example" # str |  (optional)
    spec_email = "spec.email_example" # str | Must be a valid email. (optional)
    spec_password = "spec.password_example" # str | Password should be atleast 9 characters containing atleast 1 digit, 1 uppercase letter and 1 special character from \"~!@#$%^&*()_+`-={}|[]\\\\:\\\"<>?,./\". (optional)
    spec_type = "spec.type_example" # str |  (optional)
    status_roles = [
        "status.roles_example",
    ] # [str] | Roles assigned to user. (optional)
    status_user_groups = [
        "status.user-groups_example",
    ] # [str] | Groups that external user belongs to. (optional)
    status_last_login = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Last login time. (optional)
    status_authenticators = [
        "status.authenticators_example",
    ] # [str] | Authenticators used for last successful login. (optional)
    status_last_password_change = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Last password change time for local user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User object
        api_response = api_instance.get_user(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User object
        api_response = api_instance.get_user(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_fullname=spec_fullname, spec_email=spec_email, spec_password=spec_password, spec_type=spec_type, status_roles=status_roles, status_user_groups=status_user_groups, status_last_login=status_last_login, status_authenticators=status_authenticators, status_last_password_change=status_last_password_change)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_fullname** | **str**|  | [optional]
 **spec_email** | **str**| Must be a valid email. | [optional]
 **spec_password** | **str**| Password should be atleast 9 characters containing atleast 1 digit, 1 uppercase letter and 1 special character from \&quot;~!@#$%^&amp;*()_+&#x60;-&#x3D;{}|[]\\\\:\\\&quot;&lt;&gt;?,./\&quot;. | [optional]
 **spec_type** | **str**|  | [optional]
 **status_roles** | **[str]**| Roles assigned to user. | [optional]
 **status_user_groups** | **[str]**| Groups that external user belongs to. | [optional]
 **status_last_login** | **datetime**| Last login time. | [optional]
 **status_authenticators** | **[str]**| Authenticators used for last successful login. | [optional]
 **status_last_password_change** | **datetime**| Last password change time for local user. | [optional]

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user1**
> AuthUser get_user1(o_name)

Get User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_fullname = "spec.fullname_example" # str |  (optional)
    spec_email = "spec.email_example" # str | Must be a valid email. (optional)
    spec_password = "spec.password_example" # str | Password should be atleast 9 characters containing atleast 1 digit, 1 uppercase letter and 1 special character from \"~!@#$%^&*()_+`-={}|[]\\\\:\\\"<>?,./\". (optional)
    spec_type = "spec.type_example" # str |  (optional)
    status_roles = [
        "status.roles_example",
    ] # [str] | Roles assigned to user. (optional)
    status_user_groups = [
        "status.user-groups_example",
    ] # [str] | Groups that external user belongs to. (optional)
    status_last_login = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Last login time. (optional)
    status_authenticators = [
        "status.authenticators_example",
    ] # [str] | Authenticators used for last successful login. (optional)
    status_last_password_change = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Last password change time for local user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User object
        api_response = api_instance.get_user1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User object
        api_response = api_instance.get_user1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_fullname=spec_fullname, spec_email=spec_email, spec_password=spec_password, spec_type=spec_type, status_roles=status_roles, status_user_groups=status_user_groups, status_last_login=status_last_login, status_authenticators=status_authenticators, status_last_password_change=status_last_password_change)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_fullname** | **str**|  | [optional]
 **spec_email** | **str**| Must be a valid email. | [optional]
 **spec_password** | **str**| Password should be atleast 9 characters containing atleast 1 digit, 1 uppercase letter and 1 special character from \&quot;~!@#$%^&amp;*()_+&#x60;-&#x3D;{}|[]\\\\:\\\&quot;&lt;&gt;?,./\&quot;. | [optional]
 **spec_type** | **str**|  | [optional]
 **status_roles** | **[str]**| Roles assigned to user. | [optional]
 **status_user_groups** | **[str]**| Groups that external user belongs to. | [optional]
 **status_last_login** | **datetime**| Last login time. | [optional]
 **status_authenticators** | **[str]**| Authenticators used for last successful login. | [optional]
 **status_last_password_change** | **datetime**| Last password change time for local user. | [optional]

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_preference**
> AuthUserPreference get_user_preference(o_tenant, o_name)

Get UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_options = "spec.options_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference(o_tenant, o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_options=spec_options)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_options** | **str**|  | [optional]

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_preference1**
> AuthUserPreference get_user_preference1(o_name)

Get UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_options = "spec.options_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference1(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_options=spec_options)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_options** | **str**|  | [optional]

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_authorized**
> AuthUser is_authorized(o_tenant, o_name, body)

Review authorization for user

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_subject_access_review_request import AuthSubjectAccessReviewRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthSubjectAccessReviewRequest(
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
        operations=[
            AuthOperation(
                action="all-actions",
                resource=AuthResource(
                    group="group_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    tenant="tenant_example",
                ),
            ),
        ],
    ) # AuthSubjectAccessReviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Review authorization for user
        api_response = api_instance.is_authorized(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->is_authorized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthSubjectAccessReviewRequest**](AuthSubjectAccessReviewRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_authorized1**
> AuthUser is_authorized1(o_name, body)

Review authorization for user

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_subject_access_review_request import AuthSubjectAccessReviewRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthSubjectAccessReviewRequest(
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
        operations=[
            AuthOperation(
                action="all-actions",
                resource=AuthResource(
                    group="group_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    tenant="tenant_example",
                ),
            ),
        ],
    ) # AuthSubjectAccessReviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Review authorization for user
        api_response = api_instance.is_authorized1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->is_authorized1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthSubjectAccessReviewRequest**](AuthSubjectAccessReviewRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_authentication_policy**
> AuthAuthenticationPolicy label_authentication_policy(body)

Label AuthenticationPolicy object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AuthenticationPolicy object
        api_response = api_instance.label_authentication_policy(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_role**
> AuthRole label_role(o_tenant, o_name, body)

Label Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Role object
        api_response = api_instance.label_role(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_role1**
> AuthRole label_role1(o_name, body)

Label Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Role object
        api_response = api_instance.label_role1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_role_binding**
> AuthRoleBinding label_role_binding(o_tenant, o_name, body)

Label RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label RoleBinding object
        api_response = api_instance.label_role_binding(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_role_binding1**
> AuthRoleBinding label_role_binding1(o_name, body)

Label RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label RoleBinding object
        api_response = api_instance.label_role_binding1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_user**
> AuthUser label_user(o_tenant, o_name, body)

Label User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label User object
        api_response = api_instance.label_user(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_user1**
> AuthUser label_user1(o_name, body)

Label User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label User object
        api_response = api_instance.label_user1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_user_preference**
> AuthUserPreference label_user_preference(o_tenant, o_name, body)

Label UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label UserPreference object
        api_response = api_instance.label_user_preference(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_user_preference1**
> AuthUserPreference label_user_preference1(o_name, body)

Label UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label UserPreference object
        api_response = api_instance.label_user_preference1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user_preference1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_bind_check**
> AuthAuthenticationPolicy ldap_bind_check(body)

Test LDAP bind operation

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Test LDAP bind operation
        api_response = api_instance.ldap_bind_check(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->ldap_bind_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_connection_check**
> AuthAuthenticationPolicy ldap_connection_check(body)

Test LDAP connection

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Test LDAP connection
        api_response = api_instance.ldap_connection_check(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->ldap_connection_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role**
> AuthRoleList list_role(o_tenant)

List Role objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_list import AuthRoleList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Role objects
        api_response = api_instance.list_role(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Role objects
        api_response = api_instance.list_role(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthRoleList**](AuthRoleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role1**
> AuthRoleList list_role1()

List Role objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_list import AuthRoleList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Role objects
        api_response = api_instance.list_role1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthRoleList**](AuthRoleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_binding**
> AuthRoleBindingList list_role_binding(o_tenant)

List RoleBinding objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.auth_role_binding_list import AuthRoleBindingList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RoleBinding objects
        api_response = api_instance.list_role_binding(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role_binding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List RoleBinding objects
        api_response = api_instance.list_role_binding(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthRoleBindingList**](AuthRoleBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_binding1**
> AuthRoleBindingList list_role_binding1()

List RoleBinding objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.auth_role_binding_list import AuthRoleBindingList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List RoleBinding objects
        api_response = api_instance.list_role_binding1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthRoleBindingList**](AuthRoleBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user**
> AuthUserList list_user(o_tenant)

List User objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_list import AuthUserList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List User objects
        api_response = api_instance.list_user(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List User objects
        api_response = api_instance.list_user(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthUserList**](AuthUserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user1**
> AuthUserList list_user1()

List User objects

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_list import AuthUserList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List User objects
        api_response = api_instance.list_user1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthUserList**](AuthUserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_change**
> AuthUser password_change(o_tenant, o_name, body)

Change user password

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_password_change_request import AuthPasswordChangeRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthPasswordChangeRequest(
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
        new_password="new_password_example",
        old_password="old_password_example",
    ) # AuthPasswordChangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Change user password
        api_response = api_instance.password_change(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthPasswordChangeRequest**](AuthPasswordChangeRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_change1**
> AuthUser password_change1(o_name, body)

Change user password

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_password_change_request import AuthPasswordChangeRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthPasswordChangeRequest(
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
        new_password="new_password_example",
        old_password="old_password_example",
    ) # AuthPasswordChangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Change user password
        api_response = api_instance.password_change1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_change1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthPasswordChangeRequest**](AuthPasswordChangeRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset**
> AuthUser password_reset(o_tenant, o_name, body)

Reset user password

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_password_reset_request import AuthPasswordResetRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthPasswordResetRequest(
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
    ) # AuthPasswordResetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Reset user password
        api_response = api_instance.password_reset(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthPasswordResetRequest**](AuthPasswordResetRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset1**
> AuthUser password_reset1(o_name, body)

Reset user password

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_password_reset_request import AuthPasswordResetRequest
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthPasswordResetRequest(
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
    ) # AuthPasswordResetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Reset user password
        api_response = api_instance.password_reset1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_reset1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthPasswordResetRequest**](AuthPasswordResetRequest.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_secret_generate**
> AuthAuthenticationPolicy token_secret_generate(body)

Generate secret for token signing

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.auth_token_secret_request import AuthTokenSecretRequest
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthTokenSecretRequest(
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
    ) # AuthTokenSecretRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate secret for token signing
        api_response = api_instance.token_secret_generate(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->token_secret_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthTokenSecretRequest**](AuthTokenSecretRequest.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication_policy**
> AuthAuthenticationPolicy update_authentication_policy(body)

Update AuthenticationPolicy object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Update AuthenticationPolicy object
        api_response = api_instance.update_authentication_policy(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)|  |

### Return type

[**AuthAuthenticationPolicy**](AuthAuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> AuthRole update_role(o_tenant, o_name, body)

Update Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthRole(
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
        spec=AuthRoleSpec(
            permissions=[
                AuthPermission(
                    actions=[
                        "actions_example",
                    ],
                    resource_group="resource_group_example",
                    resource_kind="resource_kind_example",
                    resource_names=[
                        "resource_names_example",
                    ],
                    resource_namespace="_All_",
                    resource_tenant="resource_tenant_example",
                ),
            ],
        ),
        status={},
    ) # AuthRole | 

    # example passing only required values which don't have defaults set
    try:
        # Update Role object
        api_response = api_instance.update_role(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthRole**](AuthRole.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role1**
> AuthRole update_role1(o_name, body)

Update Role object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role import AuthRole
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthRole(
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
        spec=AuthRoleSpec(
            permissions=[
                AuthPermission(
                    actions=[
                        "actions_example",
                    ],
                    resource_group="resource_group_example",
                    resource_kind="resource_kind_example",
                    resource_names=[
                        "resource_names_example",
                    ],
                    resource_namespace="_All_",
                    resource_tenant="resource_tenant_example",
                ),
            ],
        ),
        status={},
    ) # AuthRole | 

    # example passing only required values which don't have defaults set
    try:
        # Update Role object
        api_response = api_instance.update_role1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthRole**](AuthRole.md)|  |

### Return type

[**AuthRole**](AuthRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_binding**
> AuthRoleBinding update_role_binding(o_tenant, o_name, body)

Update RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthRoleBinding(
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
        spec=AuthRoleBindingSpec(
            role="role_example",
            user_groups=[
                "user_groups_example",
            ],
            users=[
                "users_example",
            ],
        ),
        status={},
    ) # AuthRoleBinding | 

    # example passing only required values which don't have defaults set
    try:
        # Update RoleBinding object
        api_response = api_instance.update_role_binding(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthRoleBinding**](AuthRoleBinding.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_binding1**
> AuthRoleBinding update_role_binding1(o_name, body)

Update RoleBinding object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_role_binding import AuthRoleBinding
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthRoleBinding(
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
        spec=AuthRoleBindingSpec(
            role="role_example",
            user_groups=[
                "user_groups_example",
            ],
            users=[
                "users_example",
            ],
        ),
        status={},
    ) # AuthRoleBinding | 

    # example passing only required values which don't have defaults set
    try:
        # Update RoleBinding object
        api_response = api_instance.update_role_binding1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthRoleBinding**](AuthRoleBinding.md)|  |

### Return type

[**AuthRoleBinding**](AuthRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> AuthUser update_user(o_tenant, o_name, body)

Update User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthUser(
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
        spec=AuthUserSpec(
            email=".@zyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCm6w-v0dZfUofvKER.smInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8.ohR8pb-ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6.3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKGSDRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEk.auW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e.q9Z4WMWovY63G.6ixTd5NxRU25mQYd6VBLRGkQ5H9-FH2v5iUaMQ.iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVYtYsFB.8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h64.MeAEDz67NG9dihNlL1YPO1GvRUDnbs.0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFW.pSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Z.x6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYPH.63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWk3GoxqObZMXxUrUZPuO24g6xCEEGY.5NZ9BhURG1p1vKPKEsaka3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxuH.cKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFoJb4.VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53h1KEc7ag0ak9ETa6LnPl34V25.c4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW.X3CHj-n2hyQ.B8SPpfjus1nT.PTJPb-Hj0LrcV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m.ONPCsy2yJE2MQH9Vtj3dWmBLqETJauR.5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgvhhe4JPG5EYj.qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk.G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203.y3cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcKpa5ZkmXKIhuWWL1PB8JQFInAlUi.vIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqicd-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOef.2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.jzJY",
            fullname="fullname_example",
            password="password_example",
            type="local",
        ),
        status=AuthUserStatus(
            access_review=[
                AuthOperationStatus(
                    allowed=True,
                    message="message_example",
                    operation=AuthOperation(
                        action="all-actions",
                        resource=AuthResource(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            tenant="tenant_example",
                        ),
                    ),
                ),
            ],
            authenticators=[
                "authenticators_example",
            ],
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            roles=[
                "roles_example",
            ],
            user_groups=[
                "user_groups_example",
            ],
        ),
    ) # AuthUser | 

    # example passing only required values which don't have defaults set
    try:
        # Update User object
        api_response = api_instance.update_user(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthUser**](AuthUser.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user1**
> AuthUser update_user1(o_name, body)

Update User object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user import AuthUser
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthUser(
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
        spec=AuthUserSpec(
            email=".@zyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCm6w-v0dZfUofvKER.smInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8.ohR8pb-ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6.3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKGSDRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEk.auW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e.q9Z4WMWovY63G.6ixTd5NxRU25mQYd6VBLRGkQ5H9-FH2v5iUaMQ.iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVYtYsFB.8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h64.MeAEDz67NG9dihNlL1YPO1GvRUDnbs.0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFW.pSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Z.x6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYPH.63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWk3GoxqObZMXxUrUZPuO24g6xCEEGY.5NZ9BhURG1p1vKPKEsaka3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxuH.cKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFoJb4.VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53h1KEc7ag0ak9ETa6LnPl34V25.c4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW.X3CHj-n2hyQ.B8SPpfjus1nT.PTJPb-Hj0LrcV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m.ONPCsy2yJE2MQH9Vtj3dWmBLqETJauR.5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgvhhe4JPG5EYj.qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk.G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203.y3cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcKpa5ZkmXKIhuWWL1PB8JQFInAlUi.vIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqicd-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOef.2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.jzJY",
            fullname="fullname_example",
            password="password_example",
            type="local",
        ),
        status=AuthUserStatus(
            access_review=[
                AuthOperationStatus(
                    allowed=True,
                    message="message_example",
                    operation=AuthOperation(
                        action="all-actions",
                        resource=AuthResource(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            tenant="tenant_example",
                        ),
                    ),
                ),
            ],
            authenticators=[
                "authenticators_example",
            ],
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            roles=[
                "roles_example",
            ],
            user_groups=[
                "user_groups_example",
            ],
        ),
    ) # AuthUser | 

    # example passing only required values which don't have defaults set
    try:
        # Update User object
        api_response = api_instance.update_user1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthUser**](AuthUser.md)|  |

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preference**
> AuthUserPreference update_user_preference(o_tenant, o_name, body)

Update UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = AuthUserPreference(
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
        spec=AuthUserPreferenceSpec(
            options="options_example",
        ),
        status={},
    ) # AuthUserPreference | 

    # example passing only required values which don't have defaults set
    try:
        # Update UserPreference object
        api_response = api_instance.update_user_preference(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**AuthUserPreference**](AuthUserPreference.md)|  |

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preference1**
> AuthUserPreference update_user_preference1(o_name, body)

Update UserPreference object

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_user_preference import AuthUserPreference
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthUserPreference(
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
        spec=AuthUserPreferenceSpec(
            options="options_example",
        ),
        status={},
    ) # AuthUserPreference | 

    # example passing only required values which don't have defaults set
    try:
        # Update UserPreference object
        api_response = api_instance.update_user_preference1(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user_preference1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthUserPreference**](AuthUserPreference.md)|  |

### Return type

[**AuthUserPreference**](AuthUserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_authentication_policy**
> AuthAutoMsgAuthenticationPolicyWatchHelper watch_authentication_policy()

Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_authentication_policy_watch_helper import AuthAutoMsgAuthenticationPolicyWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_authentication_policy(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgAuthenticationPolicyWatchHelper**](AuthAutoMsgAuthenticationPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_role**
> AuthAutoMsgRoleWatchHelper watch_role(o_tenant)

Watch Role objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_role_watch_helper import AuthAutoMsgRoleWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Role objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Role objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgRoleWatchHelper**](AuthAutoMsgRoleWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_role1**
> AuthAutoMsgRoleWatchHelper watch_role1()

Watch Role objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_role_watch_helper import AuthAutoMsgRoleWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Role objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgRoleWatchHelper**](AuthAutoMsgRoleWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_role_binding**
> AuthAutoMsgRoleBindingWatchHelper watch_role_binding(o_tenant)

Watch RoleBinding objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_role_binding_watch_helper import AuthAutoMsgRoleBindingWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RoleBinding objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role_binding(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role_binding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch RoleBinding objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role_binding(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgRoleBindingWatchHelper**](AuthAutoMsgRoleBindingWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_role_binding1**
> AuthAutoMsgRoleBindingWatchHelper watch_role_binding1()

Watch RoleBinding objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_role_binding_watch_helper import AuthAutoMsgRoleBindingWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch RoleBinding objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role_binding1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role_binding1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgRoleBindingWatchHelper**](AuthAutoMsgRoleBindingWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_user**
> AuthAutoMsgUserWatchHelper watch_user(o_tenant)

Watch User objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_user_watch_helper import AuthAutoMsgUserWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch User objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch User objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgUserWatchHelper**](AuthAutoMsgUserWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_user1**
> AuthAutoMsgUserWatchHelper watch_user1()

Watch User objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_user_watch_helper import AuthAutoMsgUserWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch User objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgUserWatchHelper**](AuthAutoMsgUserWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_user_preference**
> AuthAutoMsgUserPreferenceWatchHelper watch_user_preference(o_tenant)

Watch UserPreference objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_user_preference_watch_helper import AuthAutoMsgUserPreferenceWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch UserPreference objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user_preference(o_tenant)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch UserPreference objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user_preference(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgUserPreferenceWatchHelper**](AuthAutoMsgUserPreferenceWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_user_preference1**
> AuthAutoMsgUserPreferenceWatchHelper watch_user_preference1()

Watch UserPreference objects. Supports WebSockets or HTTP long poll

### Example

```python
import time
import psm
from api import auth_v1_api
from pensando_ent.psm.model.auth_auto_msg_user_preference_watch_helper import AuthAutoMsgUserPreferenceWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch UserPreference objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user_preference1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user_preference1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**AuthAutoMsgUserPreferenceWatchHelper**](AuthAutoMsgUserPreferenceWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

