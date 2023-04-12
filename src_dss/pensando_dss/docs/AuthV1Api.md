# psm.AuthV1Api

All URIs are relative to *https://PSM-IP-addr*

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
[**unlock**](AuthV1Api.md#unlock) | **POST** /configs/auth/v1/tenant/{O.Tenant}/users/{O.Name}/Unlock | Unlock user
[**unlock1**](AuthV1Api.md#unlock1) | **POST** /configs/auth/v1/users/{O.Name}/Unlock | Unlock user
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthAuthenticationPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                local=AuthLocal(
                    allowed_failed_login_attempts=10,
                    failed_login_attempts_duration="60s",
                    password_length=9,
                ),
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRole(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthRole(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRoleBinding(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthRoleBinding(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthUser(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
            email="user@example.com, internal@test",
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
            failed_login_attempts=1,
            first_failed_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            locked=True,
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthUser(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
            email="user@example.com, internal@test",
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
            failed_login_attempts=1,
            first_failed_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            locked=True,
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
    except pensando_dss.psm.ApiException as e:
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
> AuthRole delete_role(o_tenant)

Delete Role object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Role object
        api_response = api_instance.delete_role(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Role object
        api_response = api_instance.delete_role1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> AuthRoleBinding delete_role_binding(o_tenant)

Delete RoleBinding object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoleBinding object
        api_response = api_instance.delete_role_binding(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_role_binding: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete RoleBinding object
        api_response = api_instance.delete_role_binding1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> AuthUser delete_user(o_tenant)

Delete User object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User object
        api_response = api_instance.delete_user(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->delete_user: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User object
        api_response = api_instance.delete_user1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    authenticators_authenticator_order = [
        "authenticators.authenticator-order_example",
    ] # [str] | Order in which authenticators are applied. If an authenticator returns success, others are skipped. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AuthenticationPolicy object
        api_response = api_instance.get_authentication_policy()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_authentication_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **authenticators_authenticator_order** | **[str]**| Order in which authenticators are applied. If an authenticator returns success, others are skipped. | [optional]

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
> AuthRole get_role(o_tenant)

Get Role object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role object
        api_response = api_instance.get_role(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role object
        api_response = api_instance.get_role1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

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
> AuthRoleBinding get_role_binding(o_tenant)

Get RoleBinding object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_users = [
        "spec.users_example",
    ] # [str] |  (optional)
    spec_role = "spec.role_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_users** | **[str]**|  | [optional]
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_users = [
        "spec.users_example",
    ] # [str] |  (optional)
    spec_role = "spec.role_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get RoleBinding object
        api_response = api_instance.get_role_binding1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_role_binding1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_users** | **[str]**|  | [optional]
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
> AuthUser get_user(o_tenant)

Get User object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_fullname = "spec.fullname_example" # str |  (optional)
    status_roles = [
        "status.roles_example",
    ] # [str] | Roles assigned to user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User object
        api_response = api_instance.get_user(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_fullname** | **str**|  | [optional]
 **status_roles** | **[str]**| Roles assigned to user. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_fullname = "spec.fullname_example" # str |  (optional)
    status_roles = [
        "status.roles_example",
    ] # [str] | Roles assigned to user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User object
        api_response = api_instance.get_user1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_fullname** | **str**|  | [optional]
 **status_roles** | **[str]**| Roles assigned to user. | [optional]

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
> AuthUserPreference get_user_preference(o_tenant)

Get UserPreference object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_options = "spec.options_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_options = "spec.options_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get UserPreference object
        api_response = api_instance.get_user_preference1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->get_user_preference1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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
> AuthUser is_authorized(o_tenant, body)

Review authorization for user

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_subject_access_review_request import AuthSubjectAccessReviewRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthSubjectAccessReviewRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.is_authorized(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->is_authorized: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_subject_access_review_request import AuthSubjectAccessReviewRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthSubjectAccessReviewRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthRole label_role(o_tenant, body)

Label Role object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.label_role(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthRoleBinding label_role_binding(o_tenant, body)

Label RoleBinding object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.label_role_binding(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_role_binding: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthUser label_user(o_tenant, body)

Label User object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.label_user(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthUserPreference label_user_preference(o_tenant, body)

Label UserPreference object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.label_user_preference(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->label_user_preference: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthAuthenticationPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                local=AuthLocal(
                    allowed_failed_login_attempts=10,
                    failed_login_attempts_duration="60s",
                    password_length=9,
                ),
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthAuthenticationPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                local=AuthLocal(
                    allowed_failed_login_attempts=10,
                    failed_login_attempts_duration="60s",
                    password_length=9,
                ),
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_list import AuthRoleList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Role objects
        api_response = api_instance.list_role(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_list import AuthRoleList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Role objects
        api_response = api_instance.list_role1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding_list import AuthRoleBindingList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RoleBinding objects
        api_response = api_instance.list_role_binding(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role_binding: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding_list import AuthRoleBindingList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List RoleBinding objects
        api_response = api_instance.list_role_binding1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_role_binding1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_user_list import AuthUserList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List User objects
        api_response = api_instance.list_user(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_user: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_user_list import AuthUserList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List User objects
        api_response = api_instance.list_user1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->list_user1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
> AuthUser password_change(o_tenant, body)

Change user password

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_password_change_request import AuthPasswordChangeRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthPasswordChangeRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.password_change(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_change: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_password_change_request import AuthPasswordChangeRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthPasswordChangeRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthUser password_reset(o_tenant, body)

Reset user password

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_password_reset_request import AuthPasswordResetRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthPasswordResetRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.password_reset(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->password_reset: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_password_reset_request import AuthPasswordResetRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthPasswordResetRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.auth_token_secret_request import AuthTokenSecretRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthTokenSecretRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

# **unlock**
> AuthUser unlock(o_tenant, body)

Unlock user

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_user_unlock_request import AuthUserUnlockRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthUserUnlockRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    ) # AuthUserUnlockRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Unlock user
        api_response = api_instance.unlock(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->unlock: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**AuthUserUnlockRequest**](AuthUserUnlockRequest.md)|  |

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

# **unlock1**
> AuthUser unlock1(o_name, body)

Unlock user

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.auth_user_unlock_request import AuthUserUnlockRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthUserUnlockRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    ) # AuthUserUnlockRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Unlock user
        api_response = api_instance.unlock1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->unlock1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**AuthUserUnlockRequest**](AuthUserUnlockRequest.md)|  |

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

# **update_authentication_policy**
> AuthAuthenticationPolicy update_authentication_policy(body)

Update AuthenticationPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_authentication_policy import AuthAuthenticationPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    body = AuthAuthenticationPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
                local=AuthLocal(
                    allowed_failed_login_attempts=10,
                    failed_login_attempts_duration="60s",
                    password_length=9,
                ),
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
    except pensando_dss.psm.ApiException as e:
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
> AuthRole update_role(o_tenant, body)

Update Role object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRole(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.update_role(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role: %s\n" % e)

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

# **update_role1**
> AuthRole update_role1(o_name, body)

Update Role object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_role import AuthRole
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthRole(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthRoleBinding update_role_binding(o_tenant, body)

Update RoleBinding object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthRoleBinding(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.update_role_binding(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_role_binding: %s\n" % e)

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

# **update_role_binding1**
> AuthRoleBinding update_role_binding1(o_name, body)

Update RoleBinding object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_role_binding import AuthRoleBinding
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthRoleBinding(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> AuthUser update_user(o_tenant, body)

Update User object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthUser(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
            email="user@example.com, internal@test",
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
            failed_login_attempts=1,
            first_failed_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            locked=True,
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
        api_response = api_instance.update_user(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user: %s\n" % e)

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

# **update_user1**
> AuthUser update_user1(o_name, body)

Update User object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user import AuthUser
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthUser(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
            email="user@example.com, internal@test",
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
            failed_login_attempts=1,
            first_failed_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_password_change=dateutil_parser('1970-01-01T00:00:00.00Z'),
            locked=True,
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
    except pensando_dss.psm.ApiException as e:
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
> AuthUserPreference update_user_preference(o_tenant, body)

Update UserPreference object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = AuthUserPreference(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.update_user_preference(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->update_user_preference: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_user_preference import AuthUserPreference
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = AuthUserPreference(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            display_name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_auto_msg_authentication_policy_watch_helper import AuthAutoMsgAuthenticationPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_authentication_policy()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_authentication_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_auto_msg_role_watch_helper import AuthAutoMsgRoleWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Role objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_auto_msg_role_watch_helper import AuthAutoMsgRoleWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Role objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_auto_msg_role_binding_watch_helper import AuthAutoMsgRoleBindingWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RoleBinding objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role_binding(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role_binding: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_auto_msg_role_binding_watch_helper import AuthAutoMsgRoleBindingWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch RoleBinding objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_role_binding1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_role_binding1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_auto_msg_user_watch_helper import AuthAutoMsgUserWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch User objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.auth_auto_msg_user_watch_helper import AuthAutoMsgUserWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch User objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_auto_msg_user_preference_watch_helper import AuthAutoMsgUserPreferenceWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch UserPreference objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user_preference(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user_preference: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import auth_v1_api
from pensando_dss.psm.models.auth import *
from pensando_dss.psm.model.auth_auto_msg_user_preference_watch_helper import AuthAutoMsgUserPreferenceWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_v1_api.AuthV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch UserPreference objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_user_preference1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling AuthV1Api->watch_user_preference1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

