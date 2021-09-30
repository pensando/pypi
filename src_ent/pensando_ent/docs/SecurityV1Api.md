# psm.SecurityV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_app**](SecurityV1Api.md#add_app) | **POST** /configs/security/v1/tenant/{O.Tenant}/apps | Create App object
[**add_app1**](SecurityV1Api.md#add_app1) | **POST** /configs/security/v1/apps | Create App object
[**add_ip_sec_policy**](SecurityV1Api.md#add_ip_sec_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies | Create IPSecPolicy object
[**add_ip_sec_policy1**](SecurityV1Api.md#add_ip_sec_policy1) | **POST** /configs/security/v1/ipsecpolicies | Create IPSecPolicy object
[**add_network_security_policy**](SecurityV1Api.md#add_network_security_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies | Create NetworkSecurityPolicy object
[**add_network_security_policy1**](SecurityV1Api.md#add_network_security_policy1) | **POST** /configs/security/v1/networksecuritypolicies | Create NetworkSecurityPolicy object
[**add_security_group**](SecurityV1Api.md#add_security_group) | **POST** /configs/security/v1/tenant/{O.Tenant}/security-groups | Create SecurityGroup object
[**add_security_group1**](SecurityV1Api.md#add_security_group1) | **POST** /configs/security/v1/security-groups | Create SecurityGroup object
[**delete_app**](SecurityV1Api.md#delete_app) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Delete App object
[**delete_app1**](SecurityV1Api.md#delete_app1) | **DELETE** /configs/security/v1/apps/{O.Name} | Delete App object
[**delete_ip_sec_policy**](SecurityV1Api.md#delete_ip_sec_policy) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Delete IPSecPolicy object
[**delete_ip_sec_policy1**](SecurityV1Api.md#delete_ip_sec_policy1) | **DELETE** /configs/security/v1/ipsecpolicies/{O.Name} | Delete IPSecPolicy object
[**delete_network_security_policy**](SecurityV1Api.md#delete_network_security_policy) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Delete NetworkSecurityPolicy object
[**delete_network_security_policy1**](SecurityV1Api.md#delete_network_security_policy1) | **DELETE** /configs/security/v1/networksecuritypolicies/{O.Name} | Delete NetworkSecurityPolicy object
[**delete_security_group**](SecurityV1Api.md#delete_security_group) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/security-groups/{O.Name} | Delete SecurityGroup object
[**delete_security_group1**](SecurityV1Api.md#delete_security_group1) | **DELETE** /configs/security/v1/security-groups/{O.Name} | Delete SecurityGroup object
[**get_app**](SecurityV1Api.md#get_app) | **GET** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Get App object
[**get_app1**](SecurityV1Api.md#get_app1) | **GET** /configs/security/v1/apps/{O.Name} | Get App object
[**get_firewall_profile**](SecurityV1Api.md#get_firewall_profile) | **GET** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name} | Get FirewallProfile object
[**get_firewall_profile1**](SecurityV1Api.md#get_firewall_profile1) | **GET** /configs/security/v1/firewallprofiles/{O.Name} | Get FirewallProfile object
[**get_ip_sec_policy**](SecurityV1Api.md#get_ip_sec_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Get IPSecPolicy object
[**get_ip_sec_policy1**](SecurityV1Api.md#get_ip_sec_policy1) | **GET** /configs/security/v1/ipsecpolicies/{O.Name} | Get IPSecPolicy object
[**get_network_security_policy**](SecurityV1Api.md#get_network_security_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Get NetworkSecurityPolicy object
[**get_network_security_policy1**](SecurityV1Api.md#get_network_security_policy1) | **GET** /configs/security/v1/networksecuritypolicies/{O.Name} | Get NetworkSecurityPolicy object
[**get_security_group**](SecurityV1Api.md#get_security_group) | **GET** /configs/security/v1/tenant/{O.Tenant}/security-groups/{O.Name} | Get SecurityGroup object
[**get_security_group1**](SecurityV1Api.md#get_security_group1) | **GET** /configs/security/v1/security-groups/{O.Name} | Get SecurityGroup object
[**label_app**](SecurityV1Api.md#label_app) | **POST** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name}/label | Label App object
[**label_app1**](SecurityV1Api.md#label_app1) | **POST** /configs/security/v1/apps/{O.Name}/label | Label App object
[**label_firewall_profile**](SecurityV1Api.md#label_firewall_profile) | **POST** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name}/label | Label FirewallProfile object
[**label_firewall_profile1**](SecurityV1Api.md#label_firewall_profile1) | **POST** /configs/security/v1/firewallprofiles/{O.Name}/label | Label FirewallProfile object
[**label_ip_sec_policy**](SecurityV1Api.md#label_ip_sec_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name}/label | Label IPSecPolicy object
[**label_ip_sec_policy1**](SecurityV1Api.md#label_ip_sec_policy1) | **POST** /configs/security/v1/ipsecpolicies/{O.Name}/label | Label IPSecPolicy object
[**label_network_security_policy**](SecurityV1Api.md#label_network_security_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name}/label | Label NetworkSecurityPolicy object
[**label_network_security_policy1**](SecurityV1Api.md#label_network_security_policy1) | **POST** /configs/security/v1/networksecuritypolicies/{O.Name}/label | Label NetworkSecurityPolicy object
[**label_security_group**](SecurityV1Api.md#label_security_group) | **POST** /configs/security/v1/tenant/{O.Tenant}/security-groups/{O.Name}/label | Label SecurityGroup object
[**label_security_group1**](SecurityV1Api.md#label_security_group1) | **POST** /configs/security/v1/security-groups/{O.Name}/label | Label SecurityGroup object
[**list_app**](SecurityV1Api.md#list_app) | **GET** /configs/security/v1/tenant/{O.Tenant}/apps | List App objects
[**list_app1**](SecurityV1Api.md#list_app1) | **GET** /configs/security/v1/apps | List App objects
[**list_firewall_profile**](SecurityV1Api.md#list_firewall_profile) | **GET** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles | List FirewallProfile objects
[**list_firewall_profile1**](SecurityV1Api.md#list_firewall_profile1) | **GET** /configs/security/v1/firewallprofiles | List FirewallProfile objects
[**list_ip_sec_policy**](SecurityV1Api.md#list_ip_sec_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies | List IPSecPolicy objects
[**list_ip_sec_policy1**](SecurityV1Api.md#list_ip_sec_policy1) | **GET** /configs/security/v1/ipsecpolicies | List IPSecPolicy objects
[**list_network_security_policy**](SecurityV1Api.md#list_network_security_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies | List NetworkSecurityPolicy objects
[**list_network_security_policy1**](SecurityV1Api.md#list_network_security_policy1) | **GET** /configs/security/v1/networksecuritypolicies | List NetworkSecurityPolicy objects
[**list_security_group**](SecurityV1Api.md#list_security_group) | **GET** /configs/security/v1/tenant/{O.Tenant}/security-groups | List SecurityGroup objects
[**list_security_group1**](SecurityV1Api.md#list_security_group1) | **GET** /configs/security/v1/security-groups | List SecurityGroup objects
[**update_app**](SecurityV1Api.md#update_app) | **PUT** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Update App object
[**update_app1**](SecurityV1Api.md#update_app1) | **PUT** /configs/security/v1/apps/{O.Name} | Update App object
[**update_firewall_profile**](SecurityV1Api.md#update_firewall_profile) | **PUT** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name} | Update FirewallProfile object
[**update_firewall_profile1**](SecurityV1Api.md#update_firewall_profile1) | **PUT** /configs/security/v1/firewallprofiles/{O.Name} | Update FirewallProfile object
[**update_ip_sec_policy**](SecurityV1Api.md#update_ip_sec_policy) | **PUT** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Update IPSecPolicy object
[**update_ip_sec_policy1**](SecurityV1Api.md#update_ip_sec_policy1) | **PUT** /configs/security/v1/ipsecpolicies/{O.Name} | Update IPSecPolicy object
[**update_network_security_policy**](SecurityV1Api.md#update_network_security_policy) | **PUT** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Update NetworkSecurityPolicy object
[**update_network_security_policy1**](SecurityV1Api.md#update_network_security_policy1) | **PUT** /configs/security/v1/networksecuritypolicies/{O.Name} | Update NetworkSecurityPolicy object
[**update_security_group**](SecurityV1Api.md#update_security_group) | **PUT** /configs/security/v1/tenant/{O.Tenant}/security-groups/{O.Name} | Update SecurityGroup object
[**update_security_group1**](SecurityV1Api.md#update_security_group1) | **PUT** /configs/security/v1/security-groups/{O.Name} | Update SecurityGroup object
[**watch_app**](SecurityV1Api.md#watch_app) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/apps | Watch App objects. Supports WebSockets or HTTP long poll
[**watch_app1**](SecurityV1Api.md#watch_app1) | **GET** /configs/security/v1/watch/apps | Watch App objects. Supports WebSockets or HTTP long poll
[**watch_firewall_profile**](SecurityV1Api.md#watch_firewall_profile) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/firewallprofiles | Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
[**watch_firewall_profile1**](SecurityV1Api.md#watch_firewall_profile1) | **GET** /configs/security/v1/watch/firewallprofiles | Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
[**watch_ip_sec_policy**](SecurityV1Api.md#watch_ip_sec_policy) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/ipsecpolicies | Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
[**watch_ip_sec_policy1**](SecurityV1Api.md#watch_ip_sec_policy1) | **GET** /configs/security/v1/watch/ipsecpolicies | Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
[**watch_network_security_policy**](SecurityV1Api.md#watch_network_security_policy) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/networksecuritypolicies | Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
[**watch_network_security_policy1**](SecurityV1Api.md#watch_network_security_policy1) | **GET** /configs/security/v1/watch/networksecuritypolicies | Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
[**watch_security_group**](SecurityV1Api.md#watch_security_group) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/security-groups | Watch SecurityGroup objects. Supports WebSockets or HTTP long poll
[**watch_security_group1**](SecurityV1Api.md#watch_security_group1) | **GET** /configs/security/v1/watch/security-groups | Watch SecurityGroup objects. Supports WebSockets or HTTP long poll


# **add_app**
> SecurityApp add_app(o_tenant, body)

Create App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = SecurityApp(
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
        spec=SecurityAppSpec(
            alg=SecurityALG(
                dns=SecurityDns(
                    drop_large_domain_name_packets=True,
                    drop_long_label_packets=True,
                    drop_multi_question_packets=True,
                    max_message_length=1,
                    query_response_timeout="60s",
                ),
                ftp=SecurityFtp(
                    allow_mismatch_ip_address=True,
                ),
                icmp=SecurityIcmp(
                    code="code_example",
                    type="type_example",
                ),
                msrpc=[
                    SecurityMsrpc(
                        program_uuid="program_uuid_example",
                        timeout="60s",
                    ),
                ],
                sunrpc=[
                    SecuritySunrpc(
                        program_id="program_id_example",
                        timeout="60s",
                    ),
                ],
                type="icmp",
            ),
            proto_ports=[
                SecurityProtoPort(
                    ports="ports_example",
                    protocol="protocol_example",
                ),
            ],
            timeout="60s",
        ),
        status=SecurityAppStatus(
            attached_policies=[
                "attached_policies_example",
            ],
        ),
    ) # SecurityApp | 

    # example passing only required values which don't have defaults set
    try:
        # Create App object
        api_response = api_instance.add_app(o_tenant, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**SecurityApp**](SecurityApp.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **add_app1**
> SecurityApp add_app1(body)

Create App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    body = SecurityApp(
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
        spec=SecurityAppSpec(
            alg=SecurityALG(
                dns=SecurityDns(
                    drop_large_domain_name_packets=True,
                    drop_long_label_packets=True,
                    drop_multi_question_packets=True,
                    max_message_length=1,
                    query_response_timeout="60s",
                ),
                ftp=SecurityFtp(
                    allow_mismatch_ip_address=True,
                ),
                icmp=SecurityIcmp(
                    code="code_example",
                    type="type_example",
                ),
                msrpc=[
                    SecurityMsrpc(
                        program_uuid="program_uuid_example",
                        timeout="60s",
                    ),
                ],
                sunrpc=[
                    SecuritySunrpc(
                        program_id="program_id_example",
                        timeout="60s",
                    ),
                ],
                type="icmp",
            ),
            proto_ports=[
                SecurityProtoPort(
                    ports="ports_example",
                    protocol="protocol_example",
                ),
            ],
            timeout="60s",
        ),
        status=SecurityAppStatus(
            attached_policies=[
                "attached_policies_example",
            ],
        ),
    ) # SecurityApp | 

    # example passing only required values which don't have defaults set
    try:
        # Create App object
        api_response = api_instance.add_app1(body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityApp**](SecurityApp.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **add_ip_sec_policy**
> SecurityIPSecPolicy add_ip_sec_policy(o_tenant, body)

Create IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = SecurityIPSecPolicy(
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
        spec=SecurityIPSecPolicySpec(
            config=SecurityIPSecConfig(
                ike_lifetime="60s",
                sa_lifetime="60s",
            ),
            rules=[
                SecurityIPSecPolicyRule(
                    action="clear",
                    description="description_example",
                    match_rule=SecurityIPSecMatchRule(
                        apps=[
                            "apps_example",
                        ],
                        dst_ip_addresses=[
                            "dst_ip_addresses_example",
                        ],
                        proto_ports=[
                            SecurityProtoPort(
                                ports="ports_example",
                                protocol="protocol_example",
                            ),
                        ],
                        src_ip_addresses=[
                            "src_ip_addresses_example",
                        ],
                    ),
                ),
            ],
        ),
        status=SecurityIPSecPolicyStatus(
            esp_params="esp_params_example",
            ike_params="ike_params_example",
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecurityIPSecRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityIPSecPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create IPSecPolicy object
        api_response = api_instance.add_ip_sec_policy(o_tenant, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **add_ip_sec_policy1**
> SecurityIPSecPolicy add_ip_sec_policy1(body)

Create IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    body = SecurityIPSecPolicy(
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
        spec=SecurityIPSecPolicySpec(
            config=SecurityIPSecConfig(
                ike_lifetime="60s",
                sa_lifetime="60s",
            ),
            rules=[
                SecurityIPSecPolicyRule(
                    action="clear",
                    description="description_example",
                    match_rule=SecurityIPSecMatchRule(
                        apps=[
                            "apps_example",
                        ],
                        dst_ip_addresses=[
                            "dst_ip_addresses_example",
                        ],
                        proto_ports=[
                            SecurityProtoPort(
                                ports="ports_example",
                                protocol="protocol_example",
                            ),
                        ],
                        src_ip_addresses=[
                            "src_ip_addresses_example",
                        ],
                    ),
                ),
            ],
        ),
        status=SecurityIPSecPolicyStatus(
            esp_params="esp_params_example",
            ike_params="ike_params_example",
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecurityIPSecRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityIPSecPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create IPSecPolicy object
        api_response = api_instance.add_ip_sec_policy1(body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **add_network_security_policy**
> SecurityNetworkSecurityPolicy add_network_security_policy(o_tenant, body)

Create NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = SecurityNetworkSecurityPolicy(
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
        spec=SecurityNetworkSecurityPolicySpec(
            attach_groups=[
                "attach_groups_example",
            ],
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_security_groups=[
                        "from_security_groups_example",
                    ],
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_security_groups=[
                        "to_security_groups_example",
                    ],
                ),
            ],
        ),
        status=SecurityNetworkSecurityPolicyStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecuritySGRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityNetworkSecurityPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create NetworkSecurityPolicy object
        api_response = api_instance.add_network_security_policy(o_tenant, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **add_network_security_policy1**
> SecurityNetworkSecurityPolicy add_network_security_policy1(body)

Create NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    body = SecurityNetworkSecurityPolicy(
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
        spec=SecurityNetworkSecurityPolicySpec(
            attach_groups=[
                "attach_groups_example",
            ],
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_security_groups=[
                        "from_security_groups_example",
                    ],
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_security_groups=[
                        "to_security_groups_example",
                    ],
                ),
            ],
        ),
        status=SecurityNetworkSecurityPolicyStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecuritySGRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityNetworkSecurityPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create NetworkSecurityPolicy object
        api_response = api_instance.add_network_security_policy1(body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **add_security_group**
> SecuritySecurityGroup add_security_group(o_tenant, body)

Create SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = SecuritySecurityGroup(
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
        spec=SecuritySecurityGroupSpec(
            match_prefixes=[
                "match_prefixes_example",
            ],
            service_labels=[
                "service_labels_example",
            ],
            workload_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ),
        status=SecuritySecurityGroupStatus(
            policies=[
                "policies_example",
            ],
            workloads=[
                "workloads_example",
            ],
        ),
    ) # SecuritySecurityGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create SecurityGroup object
        api_response = api_instance.add_security_group(o_tenant, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_security_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**SecuritySecurityGroup**](SecuritySecurityGroup.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **add_security_group1**
> SecuritySecurityGroup add_security_group1(body)

Create SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    body = SecuritySecurityGroup(
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
        spec=SecuritySecurityGroupSpec(
            match_prefixes=[
                "match_prefixes_example",
            ],
            service_labels=[
                "service_labels_example",
            ],
            workload_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ),
        status=SecuritySecurityGroupStatus(
            policies=[
                "policies_example",
            ],
            workloads=[
                "workloads_example",
            ],
        ),
    ) # SecuritySecurityGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create SecurityGroup object
        api_response = api_instance.add_security_group1(body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->add_security_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecuritySecurityGroup**](SecuritySecurityGroup.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **delete_app**
> SecurityApp delete_app(o_tenant, o_name)

Delete App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete App object
        api_response = api_instance.delete_app(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **delete_app1**
> SecurityApp delete_app1(o_name)

Delete App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete App object
        api_response = api_instance.delete_app1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **delete_ip_sec_policy**
> SecurityIPSecPolicy delete_ip_sec_policy(o_tenant, o_name)

Delete IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPSecPolicy object
        api_response = api_instance.delete_ip_sec_policy(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **delete_ip_sec_policy1**
> SecurityIPSecPolicy delete_ip_sec_policy1(o_name)

Delete IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPSecPolicy object
        api_response = api_instance.delete_ip_sec_policy1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **delete_network_security_policy**
> SecurityNetworkSecurityPolicy delete_network_security_policy(o_tenant, o_name)

Delete NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete NetworkSecurityPolicy object
        api_response = api_instance.delete_network_security_policy(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **delete_network_security_policy1**
> SecurityNetworkSecurityPolicy delete_network_security_policy1(o_name)

Delete NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete NetworkSecurityPolicy object
        api_response = api_instance.delete_network_security_policy1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **delete_security_group**
> SecuritySecurityGroup delete_security_group(o_tenant, o_name)

Delete SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete SecurityGroup object
        api_response = api_instance.delete_security_group(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_security_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **delete_security_group1**
> SecuritySecurityGroup delete_security_group1(o_name)

Delete SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete SecurityGroup object
        api_response = api_instance.delete_security_group1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_security_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **get_app**
> SecurityApp get_app(o_tenant, o_name)

Get App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_timeout = "spec.timeout_example" # str | Timeout specifies for how long the connection be kept before removing the flow entry, specified in string as '200s', '5m', etc. Should be a valid time duration. (optional)
    alg_type = "alg.type_example" # str |  (optional)
    icmp_type = "icmp.type_example" # str | ICMP Type. (optional)
    icmp_code = "icmp.code_example" # str | ICMP Code is sub-command for a given ICMP Type. (optional)
    dns_drop_multi_question_packets = True # bool | Drop packet if number of questions is more than one. (optional)
    dns_drop_large_domain_name_packets = True # bool | Drop if domain name size is > 255 bytes. (optional)
    dns_drop_long_label_packets = True # bool | Drop if label length is 64 bytes or higher. (optional)
    dns_max_message_length = 1 # int | Maximum message length, default value is 512, maximum specified user value is 8129. (optional)
    dns_query_response_timeout = "dns.query-response-timeout_example" # str | Timeout for DNS Query, default 60s. Should be a valid time duration. (optional)
    ftp_allow_mismatch_ip_address = True # bool | Allow Mismatch IP Address in the payload compared to what is present in the IP header. (optional)
    status_attached_policies = [
        "status.attached-policies_example",
    ] # [str] | List of security group policies attached to the app. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get App object
        api_response = api_instance.get_app(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_app: %s\n" % e)

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
 **spec_timeout** | **str**| Timeout specifies for how long the connection be kept before removing the flow entry, specified in string as &#39;200s&#39;, &#39;5m&#39;, etc. Should be a valid time duration. | [optional]
 **alg_type** | **str**|  | [optional]
 **icmp_type** | **str**| ICMP Type. | [optional]
 **icmp_code** | **str**| ICMP Code is sub-command for a given ICMP Type. | [optional]
 **dns_drop_multi_question_packets** | **bool**| Drop packet if number of questions is more than one. | [optional]
 **dns_drop_large_domain_name_packets** | **bool**| Drop if domain name size is &gt; 255 bytes. | [optional]
 **dns_drop_long_label_packets** | **bool**| Drop if label length is 64 bytes or higher. | [optional]
 **dns_max_message_length** | **int**| Maximum message length, default value is 512, maximum specified user value is 8129. | [optional]
 **dns_query_response_timeout** | **str**| Timeout for DNS Query, default 60s. Should be a valid time duration. | [optional]
 **ftp_allow_mismatch_ip_address** | **bool**| Allow Mismatch IP Address in the payload compared to what is present in the IP header. | [optional]
 **status_attached_policies** | **[str]**| List of security group policies attached to the app. | [optional]

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **get_app1**
> SecurityApp get_app1(o_name)

Get App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_timeout = "spec.timeout_example" # str | Timeout specifies for how long the connection be kept before removing the flow entry, specified in string as '200s', '5m', etc. Should be a valid time duration. (optional)
    alg_type = "alg.type_example" # str |  (optional)
    icmp_type = "icmp.type_example" # str | ICMP Type. (optional)
    icmp_code = "icmp.code_example" # str | ICMP Code is sub-command for a given ICMP Type. (optional)
    dns_drop_multi_question_packets = True # bool | Drop packet if number of questions is more than one. (optional)
    dns_drop_large_domain_name_packets = True # bool | Drop if domain name size is > 255 bytes. (optional)
    dns_drop_long_label_packets = True # bool | Drop if label length is 64 bytes or higher. (optional)
    dns_max_message_length = 1 # int | Maximum message length, default value is 512, maximum specified user value is 8129. (optional)
    dns_query_response_timeout = "dns.query-response-timeout_example" # str | Timeout for DNS Query, default 60s. Should be a valid time duration. (optional)
    ftp_allow_mismatch_ip_address = True # bool | Allow Mismatch IP Address in the payload compared to what is present in the IP header. (optional)
    status_attached_policies = [
        "status.attached-policies_example",
    ] # [str] | List of security group policies attached to the app. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get App object
        api_response = api_instance.get_app1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_app1: %s\n" % e)

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
 **spec_timeout** | **str**| Timeout specifies for how long the connection be kept before removing the flow entry, specified in string as &#39;200s&#39;, &#39;5m&#39;, etc. Should be a valid time duration. | [optional]
 **alg_type** | **str**|  | [optional]
 **icmp_type** | **str**| ICMP Type. | [optional]
 **icmp_code** | **str**| ICMP Code is sub-command for a given ICMP Type. | [optional]
 **dns_drop_multi_question_packets** | **bool**| Drop packet if number of questions is more than one. | [optional]
 **dns_drop_large_domain_name_packets** | **bool**| Drop if domain name size is &gt; 255 bytes. | [optional]
 **dns_drop_long_label_packets** | **bool**| Drop if label length is 64 bytes or higher. | [optional]
 **dns_max_message_length** | **int**| Maximum message length, default value is 512, maximum specified user value is 8129. | [optional]
 **dns_query_response_timeout** | **str**| Timeout for DNS Query, default 60s. Should be a valid time duration. | [optional]
 **ftp_allow_mismatch_ip_address** | **bool**| Allow Mismatch IP Address in the payload compared to what is present in the IP header. | [optional]
 **status_attached_policies** | **[str]**| List of security group policies attached to the app. | [optional]

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **get_firewall_profile**
> SecurityFirewallProfile get_firewall_profile(o_tenant, o_name)

Get FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_session_idle_timeout = "spec.session-idle-timeout_example" # str | Session idle timeout removes/deletes the session/flow if there is inactivity; this value is superceded by any value specified in App object. Should be a valid time duration between 30s and 48h0m0s. (optional)
    spec_tcp_connection_setup_timeout = "spec.tcp-connection-setup-timeout_example" # str | TCP Connection Setup Timeout is the period TCP session is kept to see the response of a SYN. Should be a valid time duration between 1s and 1m0s. (optional)
    spec_tcp_close_timeout = "spec.tcp-close-timeout_example" # str | TCP Close Timeout is the time for which TCP session is kept after a FIN is seen. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_tcp_half_closed_timeout = "spec.tcp-half-closed-timeout_example" # str | TCP Half Closed Timeout is the time for which tCP session is kept when connection is half closed i.e. FIN sent by FIN_Ack not received. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_tcp_drop_timeout = "spec.tcp-drop-timeout_example" # str | TCP Drop Timeout is the period for which a drop entry is installed for a denied TCP flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_udp_drop_timeout = "spec.udp-drop-timeout_example" # str | UDP Drop Timeout is the period for which a drop entry is installed for a denied UDP flow. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_icmp_drop_timeout = "spec.icmp-drop-timeout_example" # str | ICMP Drop Timeout is the period for which a drop entry is installed for a denied ICMP flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_drop_timeout = "spec.drop-timeout_example" # str | Drop Timeout is the period for which a drop entry is installed for a denied non tcp/udp/icmp flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_tcp_timeout = "spec.tcp-timeout_example" # str | Tcp Timeout is the period for which a TCP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_udp_timeout = "spec.udp-timeout_example" # str | Udp Timeout is the period for which a UDP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_icmp_timeout = "spec.icmp-timeout_example" # str | Icmp Timeout is the period for which a ICMP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_tcp_half_open_session_limit = 1 # int | Tcp half open session limit config after which new open requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_udp_active_session_limit = 1 # int | Udp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_icmp_active_session_limit = 1 # int | Icmp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_detect_app = True # bool | Set the Application Identification Detection config for DSCs. (optional)
    spec_connection_tracking = True # bool | Enable/disable Connection Tracking. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FirewallProfile object
        api_response = api_instance.get_firewall_profile(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_firewall_profile: %s\n" % e)

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
 **spec_session_idle_timeout** | **str**| Session idle timeout removes/deletes the session/flow if there is inactivity; this value is superceded by any value specified in App object. Should be a valid time duration between 30s and 48h0m0s. | [optional]
 **spec_tcp_connection_setup_timeout** | **str**| TCP Connection Setup Timeout is the period TCP session is kept to see the response of a SYN. Should be a valid time duration between 1s and 1m0s. | [optional]
 **spec_tcp_close_timeout** | **str**| TCP Close Timeout is the time for which TCP session is kept after a FIN is seen. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_tcp_half_closed_timeout** | **str**| TCP Half Closed Timeout is the time for which tCP session is kept when connection is half closed i.e. FIN sent by FIN_Ack not received. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_tcp_drop_timeout** | **str**| TCP Drop Timeout is the period for which a drop entry is installed for a denied TCP flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_udp_drop_timeout** | **str**| UDP Drop Timeout is the period for which a drop entry is installed for a denied UDP flow. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_icmp_drop_timeout** | **str**| ICMP Drop Timeout is the period for which a drop entry is installed for a denied ICMP flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_drop_timeout** | **str**| Drop Timeout is the period for which a drop entry is installed for a denied non tcp/udp/icmp flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_tcp_timeout** | **str**| Tcp Timeout is the period for which a TCP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_udp_timeout** | **str**| Udp Timeout is the period for which a UDP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_icmp_timeout** | **str**| Icmp Timeout is the period for which a ICMP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_tcp_half_open_session_limit** | **int**| Tcp half open session limit config after which new open requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_udp_active_session_limit** | **int**| Udp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_icmp_active_session_limit** | **int**| Icmp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_detect_app** | **bool**| Set the Application Identification Detection config for DSCs. | [optional]
 **spec_connection_tracking** | **bool**| Enable/disable Connection Tracking. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **get_firewall_profile1**
> SecurityFirewallProfile get_firewall_profile1(o_name)

Get FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_session_idle_timeout = "spec.session-idle-timeout_example" # str | Session idle timeout removes/deletes the session/flow if there is inactivity; this value is superceded by any value specified in App object. Should be a valid time duration between 30s and 48h0m0s. (optional)
    spec_tcp_connection_setup_timeout = "spec.tcp-connection-setup-timeout_example" # str | TCP Connection Setup Timeout is the period TCP session is kept to see the response of a SYN. Should be a valid time duration between 1s and 1m0s. (optional)
    spec_tcp_close_timeout = "spec.tcp-close-timeout_example" # str | TCP Close Timeout is the time for which TCP session is kept after a FIN is seen. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_tcp_half_closed_timeout = "spec.tcp-half-closed-timeout_example" # str | TCP Half Closed Timeout is the time for which tCP session is kept when connection is half closed i.e. FIN sent by FIN_Ack not received. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_tcp_drop_timeout = "spec.tcp-drop-timeout_example" # str | TCP Drop Timeout is the period for which a drop entry is installed for a denied TCP flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_udp_drop_timeout = "spec.udp-drop-timeout_example" # str | UDP Drop Timeout is the period for which a drop entry is installed for a denied UDP flow. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_icmp_drop_timeout = "spec.icmp-drop-timeout_example" # str | ICMP Drop Timeout is the period for which a drop entry is installed for a denied ICMP flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_drop_timeout = "spec.drop-timeout_example" # str | Drop Timeout is the period for which a drop entry is installed for a denied non tcp/udp/icmp flow. Should be a valid time duration between 1s and 5m0s. (optional)
    spec_tcp_timeout = "spec.tcp-timeout_example" # str | Tcp Timeout is the period for which a TCP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_udp_timeout = "spec.udp-timeout_example" # str | Udp Timeout is the period for which a UDP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_icmp_timeout = "spec.icmp-timeout_example" # str | Icmp Timeout is the period for which a ICMP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. (optional)
    spec_tcp_half_open_session_limit = 1 # int | Tcp half open session limit config after which new open requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_udp_active_session_limit = 1 # int | Udp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_icmp_active_session_limit = 1 # int | Icmp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. (optional)
    spec_detect_app = True # bool | Set the Application Identification Detection config for DSCs. (optional)
    spec_connection_tracking = True # bool | Enable/disable Connection Tracking. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FirewallProfile object
        api_response = api_instance.get_firewall_profile1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_firewall_profile1: %s\n" % e)

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
 **spec_session_idle_timeout** | **str**| Session idle timeout removes/deletes the session/flow if there is inactivity; this value is superceded by any value specified in App object. Should be a valid time duration between 30s and 48h0m0s. | [optional]
 **spec_tcp_connection_setup_timeout** | **str**| TCP Connection Setup Timeout is the period TCP session is kept to see the response of a SYN. Should be a valid time duration between 1s and 1m0s. | [optional]
 **spec_tcp_close_timeout** | **str**| TCP Close Timeout is the time for which TCP session is kept after a FIN is seen. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_tcp_half_closed_timeout** | **str**| TCP Half Closed Timeout is the time for which tCP session is kept when connection is half closed i.e. FIN sent by FIN_Ack not received. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_tcp_drop_timeout** | **str**| TCP Drop Timeout is the period for which a drop entry is installed for a denied TCP flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_udp_drop_timeout** | **str**| UDP Drop Timeout is the period for which a drop entry is installed for a denied UDP flow. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_icmp_drop_timeout** | **str**| ICMP Drop Timeout is the period for which a drop entry is installed for a denied ICMP flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_drop_timeout** | **str**| Drop Timeout is the period for which a drop entry is installed for a denied non tcp/udp/icmp flow. Should be a valid time duration between 1s and 5m0s. | [optional]
 **spec_tcp_timeout** | **str**| Tcp Timeout is the period for which a TCP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_udp_timeout** | **str**| Udp Timeout is the period for which a UDP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_icmp_timeout** | **str**| Icmp Timeout is the period for which a ICMP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]
 **spec_tcp_half_open_session_limit** | **int**| Tcp half open session limit config after which new open requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_udp_active_session_limit** | **int**| Udp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_icmp_active_session_limit** | **int**| Icmp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]
 **spec_detect_app** | **bool**| Set the Application Identification Detection config for DSCs. | [optional]
 **spec_connection_tracking** | **bool**| Enable/disable Connection Tracking. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **get_ip_sec_policy**
> SecurityIPSecPolicy get_ip_sec_policy(o_tenant, o_name)

Get IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    config_sa_lifetime = "config.sa-lifetime_example" # str | How long a particular instance of a connection should last, from successful negotiation to expiry The connection will be re-negotiated before it expires. Post succesful re-negotation, the new connection will have new(different) keys and a new SPI Default 8h, Max 24h, set it to an empty string to disable rekeying. Should be a valid time duration between 1h0m0s and 24h0m0s. (optional)
    config_ike_lifetime = "config.ike-lifetime_example" # str | Time to schedule Internet Key Exchange (IKE) reauthentication. IKE reauthentication recreates the IKE SA from scratch and re-evaluates the credentials Default 24h, set it to an empty string to disable reauthentication. Should be a valid time duration between 1h0m0s and 24h0m0s. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_ike_params = "status.ike-params_example" # str | Encryption and Algorithm details used for IKEv2 key exchange. (optional)
    status_esp_params = "status.esp-params_example" # str | Encryption and Algorithm details used for encrypting data traffic (ESP). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPSecPolicy object
        api_response = api_instance.get_ip_sec_policy(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_ip_sec_policy: %s\n" % e)

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
 **config_sa_lifetime** | **str**| How long a particular instance of a connection should last, from successful negotiation to expiry The connection will be re-negotiated before it expires. Post succesful re-negotation, the new connection will have new(different) keys and a new SPI Default 8h, Max 24h, set it to an empty string to disable rekeying. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]
 **config_ike_lifetime** | **str**| Time to schedule Internet Key Exchange (IKE) reauthentication. IKE reauthentication recreates the IKE SA from scratch and re-evaluates the credentials Default 24h, set it to an empty string to disable reauthentication. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_ike_params** | **str**| Encryption and Algorithm details used for IKEv2 key exchange. | [optional]
 **status_esp_params** | **str**| Encryption and Algorithm details used for encrypting data traffic (ESP). | [optional]

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **get_ip_sec_policy1**
> SecurityIPSecPolicy get_ip_sec_policy1(o_name)

Get IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    config_sa_lifetime = "config.sa-lifetime_example" # str | How long a particular instance of a connection should last, from successful negotiation to expiry The connection will be re-negotiated before it expires. Post succesful re-negotation, the new connection will have new(different) keys and a new SPI Default 8h, Max 24h, set it to an empty string to disable rekeying. Should be a valid time duration between 1h0m0s and 24h0m0s. (optional)
    config_ike_lifetime = "config.ike-lifetime_example" # str | Time to schedule Internet Key Exchange (IKE) reauthentication. IKE reauthentication recreates the IKE SA from scratch and re-evaluates the credentials Default 24h, set it to an empty string to disable reauthentication. Should be a valid time duration between 1h0m0s and 24h0m0s. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_ike_params = "status.ike-params_example" # str | Encryption and Algorithm details used for IKEv2 key exchange. (optional)
    status_esp_params = "status.esp-params_example" # str | Encryption and Algorithm details used for encrypting data traffic (ESP). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPSecPolicy object
        api_response = api_instance.get_ip_sec_policy1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_ip_sec_policy1: %s\n" % e)

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
 **config_sa_lifetime** | **str**| How long a particular instance of a connection should last, from successful negotiation to expiry The connection will be re-negotiated before it expires. Post succesful re-negotation, the new connection will have new(different) keys and a new SPI Default 8h, Max 24h, set it to an empty string to disable rekeying. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]
 **config_ike_lifetime** | **str**| Time to schedule Internet Key Exchange (IKE) reauthentication. IKE reauthentication recreates the IKE SA from scratch and re-evaluates the credentials Default 24h, set it to an empty string to disable reauthentication. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_ike_params** | **str**| Encryption and Algorithm details used for IKEv2 key exchange. | [optional]
 **status_esp_params** | **str**| Encryption and Algorithm details used for encrypting data traffic (ESP). | [optional]

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **get_network_security_policy**
> SecurityNetworkSecurityPolicy get_network_security_policy(o_tenant, o_name)

Get NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_attach_groups = [
        "spec.attach-groups_example",
    ] # [str] | list of security groups this policy is attached to. (optional)
    spec_attach_tenant = True # bool | specifies if the set of rules need to be attached globally to a tenant. (optional)
    spec_priority = 1 # int | Policy priority. If not specified, it will be assigned automatically in increments of 1000. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkSecurityPolicy object
        api_response = api_instance.get_network_security_policy(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_network_security_policy: %s\n" % e)

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
 **spec_attach_groups** | **[str]**| list of security groups this policy is attached to. | [optional]
 **spec_attach_tenant** | **bool**| specifies if the set of rules need to be attached globally to a tenant. | [optional]
 **spec_priority** | **int**| Policy priority. If not specified, it will be assigned automatically in increments of 1000. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **get_network_security_policy1**
> SecurityNetworkSecurityPolicy get_network_security_policy1(o_name)

Get NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_attach_groups = [
        "spec.attach-groups_example",
    ] # [str] | list of security groups this policy is attached to. (optional)
    spec_attach_tenant = True # bool | specifies if the set of rules need to be attached globally to a tenant. (optional)
    spec_priority = 1 # int | Policy priority. If not specified, it will be assigned automatically in increments of 1000. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest Naples. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkSecurityPolicy object
        api_response = api_instance.get_network_security_policy1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_network_security_policy1: %s\n" % e)

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
 **spec_attach_groups** | **[str]**| list of security groups this policy is attached to. | [optional]
 **spec_attach_tenant** | **bool**| specifies if the set of rules need to be attached globally to a tenant. | [optional]
 **spec_priority** | **int**| Policy priority. If not specified, it will be assigned automatically in increments of 1000. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest Naples. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **get_security_group**
> SecuritySecurityGroup get_security_group(o_tenant, o_name)

Get SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_service_labels = [
        "spec.service-labels_example",
    ] # [str] | Service object selector. (optional)
    spec_match_prefixes = [
        "spec.match-prefixes_example",
    ] # [str] | list of CIDRs that are part of this security group. (optional)
    status_workloads = [
        "status.workloads_example",
    ] # [str] | list of workloads that are part of this security group. (optional)
    status_policies = [
        "status.Policies_example",
    ] # [str] | list of all policies attached to this security group. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SecurityGroup object
        api_response = api_instance.get_security_group(o_tenant, o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_security_group: %s\n" % e)

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
 **spec_service_labels** | **[str]**| Service object selector. | [optional]
 **spec_match_prefixes** | **[str]**| list of CIDRs that are part of this security group. | [optional]
 **status_workloads** | **[str]**| list of workloads that are part of this security group. | [optional]
 **status_policies** | **[str]**| list of all policies attached to this security group. | [optional]

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **get_security_group1**
> SecuritySecurityGroup get_security_group1(o_name)

Get SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    spec_service_labels = [
        "spec.service-labels_example",
    ] # [str] | Service object selector. (optional)
    spec_match_prefixes = [
        "spec.match-prefixes_example",
    ] # [str] | list of CIDRs that are part of this security group. (optional)
    status_workloads = [
        "status.workloads_example",
    ] # [str] | list of workloads that are part of this security group. (optional)
    status_policies = [
        "status.Policies_example",
    ] # [str] | list of all policies attached to this security group. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SecurityGroup object
        api_response = api_instance.get_security_group1(o_name)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_security_group1: %s\n" % e)

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
 **spec_service_labels** | **[str]**| Service object selector. | [optional]
 **spec_match_prefixes** | **[str]**| list of CIDRs that are part of this security group. | [optional]
 **status_workloads** | **[str]**| list of workloads that are part of this security group. | [optional]
 **status_policies** | **[str]**| list of all policies attached to this security group. | [optional]

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **label_app**
> SecurityApp label_app(o_tenant, o_name, body)

Label App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label App object
        api_response = api_instance.label_app(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **label_app1**
> SecurityApp label_app1(o_name, body)

Label App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label App object
        api_response = api_instance.label_app1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **label_firewall_profile**
> SecurityFirewallProfile label_firewall_profile(o_tenant, o_name, body)

Label FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label FirewallProfile object
        api_response = api_instance.label_firewall_profile(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **label_firewall_profile1**
> SecurityFirewallProfile label_firewall_profile1(o_name, body)

Label FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label FirewallProfile object
        api_response = api_instance.label_firewall_profile1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_firewall_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **label_ip_sec_policy**
> SecurityIPSecPolicy label_ip_sec_policy(o_tenant, o_name, body)

Label IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label IPSecPolicy object
        api_response = api_instance.label_ip_sec_policy(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **label_ip_sec_policy1**
> SecurityIPSecPolicy label_ip_sec_policy1(o_name, body)

Label IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label IPSecPolicy object
        api_response = api_instance.label_ip_sec_policy1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **label_network_security_policy**
> SecurityNetworkSecurityPolicy label_network_security_policy(o_tenant, o_name, body)

Label NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label NetworkSecurityPolicy object
        api_response = api_instance.label_network_security_policy(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **label_network_security_policy1**
> SecurityNetworkSecurityPolicy label_network_security_policy1(o_name, body)

Label NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label NetworkSecurityPolicy object
        api_response = api_instance.label_network_security_policy1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **label_security_group**
> SecuritySecurityGroup label_security_group(o_tenant, o_name, body)

Label SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label SecurityGroup object
        api_response = api_instance.label_security_group(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_security_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **label_security_group1**
> SecuritySecurityGroup label_security_group1(o_name, body)

Label SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Label SecurityGroup object
        api_response = api_instance.label_security_group1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_security_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **list_app**
> SecurityAppList list_app(o_tenant)

List App objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app_list import SecurityAppList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # List App objects
        api_response = api_instance.list_app(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_app: %s\n" % e)

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

[**SecurityAppList**](SecurityAppList.md)

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

# **list_app1**
> SecurityAppList list_app1()

List App objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app_list import SecurityAppList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # List App objects
        api_response = api_instance.list_app1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_app1: %s\n" % e)

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

[**SecurityAppList**](SecurityAppList.md)

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

# **list_firewall_profile**
> SecurityFirewallProfileList list_firewall_profile(o_tenant)

List FirewallProfile objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile_list import SecurityFirewallProfileList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # List FirewallProfile objects
        api_response = api_instance.list_firewall_profile(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_firewall_profile: %s\n" % e)

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

[**SecurityFirewallProfileList**](SecurityFirewallProfileList.md)

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

# **list_firewall_profile1**
> SecurityFirewallProfileList list_firewall_profile1()

List FirewallProfile objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile_list import SecurityFirewallProfileList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # List FirewallProfile objects
        api_response = api_instance.list_firewall_profile1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_firewall_profile1: %s\n" % e)

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

[**SecurityFirewallProfileList**](SecurityFirewallProfileList.md)

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

# **list_ip_sec_policy**
> SecurityIPSecPolicyList list_ip_sec_policy(o_tenant)

List IPSecPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy_list import SecurityIPSecPolicyList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # List IPSecPolicy objects
        api_response = api_instance.list_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_ip_sec_policy: %s\n" % e)

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

[**SecurityIPSecPolicyList**](SecurityIPSecPolicyList.md)

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

# **list_ip_sec_policy1**
> SecurityIPSecPolicyList list_ip_sec_policy1()

List IPSecPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy_list import SecurityIPSecPolicyList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # List IPSecPolicy objects
        api_response = api_instance.list_ip_sec_policy1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_ip_sec_policy1: %s\n" % e)

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

[**SecurityIPSecPolicyList**](SecurityIPSecPolicyList.md)

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

# **list_network_security_policy**
> SecurityNetworkSecurityPolicyList list_network_security_policy(o_tenant)

List NetworkSecurityPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy_list import SecurityNetworkSecurityPolicyList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # List NetworkSecurityPolicy objects
        api_response = api_instance.list_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_network_security_policy: %s\n" % e)

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

[**SecurityNetworkSecurityPolicyList**](SecurityNetworkSecurityPolicyList.md)

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

# **list_network_security_policy1**
> SecurityNetworkSecurityPolicyList list_network_security_policy1()

List NetworkSecurityPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy_list import SecurityNetworkSecurityPolicyList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # List NetworkSecurityPolicy objects
        api_response = api_instance.list_network_security_policy1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_network_security_policy1: %s\n" % e)

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

[**SecurityNetworkSecurityPolicyList**](SecurityNetworkSecurityPolicyList.md)

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

# **list_security_group**
> SecuritySecurityGroupList list_security_group(o_tenant)

List SecurityGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group_list import SecuritySecurityGroupList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # List SecurityGroup objects
        api_response = api_instance.list_security_group(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_security_group: %s\n" % e)

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

[**SecuritySecurityGroupList**](SecuritySecurityGroupList.md)

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

# **list_security_group1**
> SecuritySecurityGroupList list_security_group1()

List SecurityGroup objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group_list import SecuritySecurityGroupList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # List SecurityGroup objects
        api_response = api_instance.list_security_group1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_security_group1: %s\n" % e)

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

[**SecuritySecurityGroupList**](SecuritySecurityGroupList.md)

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

# **update_app**
> SecurityApp update_app(o_tenant, o_name, body)

Update App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = SecurityApp(
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
        spec=SecurityAppSpec(
            alg=SecurityALG(
                dns=SecurityDns(
                    drop_large_domain_name_packets=True,
                    drop_long_label_packets=True,
                    drop_multi_question_packets=True,
                    max_message_length=1,
                    query_response_timeout="60s",
                ),
                ftp=SecurityFtp(
                    allow_mismatch_ip_address=True,
                ),
                icmp=SecurityIcmp(
                    code="code_example",
                    type="type_example",
                ),
                msrpc=[
                    SecurityMsrpc(
                        program_uuid="program_uuid_example",
                        timeout="60s",
                    ),
                ],
                sunrpc=[
                    SecuritySunrpc(
                        program_id="program_id_example",
                        timeout="60s",
                    ),
                ],
                type="icmp",
            ),
            proto_ports=[
                SecurityProtoPort(
                    ports="ports_example",
                    protocol="protocol_example",
                ),
            ],
            timeout="60s",
        ),
        status=SecurityAppStatus(
            attached_policies=[
                "attached_policies_example",
            ],
        ),
    ) # SecurityApp | 

    # example passing only required values which don't have defaults set
    try:
        # Update App object
        api_response = api_instance.update_app(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**SecurityApp**](SecurityApp.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **update_app1**
> SecurityApp update_app1(o_name, body)

Update App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_app import SecurityApp
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = SecurityApp(
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
        spec=SecurityAppSpec(
            alg=SecurityALG(
                dns=SecurityDns(
                    drop_large_domain_name_packets=True,
                    drop_long_label_packets=True,
                    drop_multi_question_packets=True,
                    max_message_length=1,
                    query_response_timeout="60s",
                ),
                ftp=SecurityFtp(
                    allow_mismatch_ip_address=True,
                ),
                icmp=SecurityIcmp(
                    code="code_example",
                    type="type_example",
                ),
                msrpc=[
                    SecurityMsrpc(
                        program_uuid="program_uuid_example",
                        timeout="60s",
                    ),
                ],
                sunrpc=[
                    SecuritySunrpc(
                        program_id="program_id_example",
                        timeout="60s",
                    ),
                ],
                type="icmp",
            ),
            proto_ports=[
                SecurityProtoPort(
                    ports="ports_example",
                    protocol="protocol_example",
                ),
            ],
            timeout="60s",
        ),
        status=SecurityAppStatus(
            attached_policies=[
                "attached_policies_example",
            ],
        ),
    ) # SecurityApp | 

    # example passing only required values which don't have defaults set
    try:
        # Update App object
        api_response = api_instance.update_app1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**SecurityApp**](SecurityApp.md)|  |

### Return type

[**SecurityApp**](SecurityApp.md)

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

# **update_firewall_profile**
> SecurityFirewallProfile update_firewall_profile(o_tenant, o_name, body)

Update FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = SecurityFirewallProfile(
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
        spec=SecurityFirewallProfileSpec(
            connection_tracking=True,
            detect_app=False,
            drop_timeout="60s",
            icmp_active_session_limit=0,
            icmp_drop_timeout="60s",
            icmp_timeout="60s",
            session_idle_timeout="60s",
            tcp_close_timeout="60s",
            tcp_connection_setup_timeout="60s",
            tcp_drop_timeout="60s",
            tcp_half_closed_timeout="60s",
            tcp_half_open_session_limit=0,
            tcp_timeout="60s",
            udp_active_session_limit=0,
            udp_drop_timeout="60s",
            udp_timeout="60s",
        ),
        status=SecurityFirewallProfileStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
        ),
    ) # SecurityFirewallProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update FirewallProfile object
        api_response = api_instance.update_firewall_profile(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**SecurityFirewallProfile**](SecurityFirewallProfile.md)|  |

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **update_firewall_profile1**
> SecurityFirewallProfile update_firewall_profile1(o_name, body)

Update FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_firewall_profile import SecurityFirewallProfile
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = SecurityFirewallProfile(
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
        spec=SecurityFirewallProfileSpec(
            connection_tracking=True,
            detect_app=False,
            drop_timeout="60s",
            icmp_active_session_limit=0,
            icmp_drop_timeout="60s",
            icmp_timeout="60s",
            session_idle_timeout="60s",
            tcp_close_timeout="60s",
            tcp_connection_setup_timeout="60s",
            tcp_drop_timeout="60s",
            tcp_half_closed_timeout="60s",
            tcp_half_open_session_limit=0,
            tcp_timeout="60s",
            udp_active_session_limit=0,
            udp_drop_timeout="60s",
            udp_timeout="60s",
        ),
        status=SecurityFirewallProfileStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
        ),
    ) # SecurityFirewallProfile | 

    # example passing only required values which don't have defaults set
    try:
        # Update FirewallProfile object
        api_response = api_instance.update_firewall_profile1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_firewall_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**SecurityFirewallProfile**](SecurityFirewallProfile.md)|  |

### Return type

[**SecurityFirewallProfile**](SecurityFirewallProfile.md)

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

# **update_ip_sec_policy**
> SecurityIPSecPolicy update_ip_sec_policy(o_tenant, o_name, body)

Update IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = SecurityIPSecPolicy(
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
        spec=SecurityIPSecPolicySpec(
            config=SecurityIPSecConfig(
                ike_lifetime="60s",
                sa_lifetime="60s",
            ),
            rules=[
                SecurityIPSecPolicyRule(
                    action="clear",
                    description="description_example",
                    match_rule=SecurityIPSecMatchRule(
                        apps=[
                            "apps_example",
                        ],
                        dst_ip_addresses=[
                            "dst_ip_addresses_example",
                        ],
                        proto_ports=[
                            SecurityProtoPort(
                                ports="ports_example",
                                protocol="protocol_example",
                            ),
                        ],
                        src_ip_addresses=[
                            "src_ip_addresses_example",
                        ],
                    ),
                ),
            ],
        ),
        status=SecurityIPSecPolicyStatus(
            esp_params="esp_params_example",
            ike_params="ike_params_example",
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecurityIPSecRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityIPSecPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update IPSecPolicy object
        api_response = api_instance.update_ip_sec_policy(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **update_ip_sec_policy1**
> SecurityIPSecPolicy update_ip_sec_policy1(o_name, body)

Update IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = SecurityIPSecPolicy(
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
        spec=SecurityIPSecPolicySpec(
            config=SecurityIPSecConfig(
                ike_lifetime="60s",
                sa_lifetime="60s",
            ),
            rules=[
                SecurityIPSecPolicyRule(
                    action="clear",
                    description="description_example",
                    match_rule=SecurityIPSecMatchRule(
                        apps=[
                            "apps_example",
                        ],
                        dst_ip_addresses=[
                            "dst_ip_addresses_example",
                        ],
                        proto_ports=[
                            SecurityProtoPort(
                                ports="ports_example",
                                protocol="protocol_example",
                            ),
                        ],
                        src_ip_addresses=[
                            "src_ip_addresses_example",
                        ],
                    ),
                ),
            ],
        ),
        status=SecurityIPSecPolicyStatus(
            esp_params="esp_params_example",
            ike_params="ike_params_example",
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecurityIPSecRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityIPSecPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update IPSecPolicy object
        api_response = api_instance.update_ip_sec_policy1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)|  |

### Return type

[**SecurityIPSecPolicy**](SecurityIPSecPolicy.md)

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

# **update_network_security_policy**
> SecurityNetworkSecurityPolicy update_network_security_policy(o_tenant, o_name, body)

Update NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = SecurityNetworkSecurityPolicy(
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
        spec=SecurityNetworkSecurityPolicySpec(
            attach_groups=[
                "attach_groups_example",
            ],
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_security_groups=[
                        "from_security_groups_example",
                    ],
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_security_groups=[
                        "to_security_groups_example",
                    ],
                ),
            ],
        ),
        status=SecurityNetworkSecurityPolicyStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecuritySGRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityNetworkSecurityPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update NetworkSecurityPolicy object
        api_response = api_instance.update_network_security_policy(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **update_network_security_policy1**
> SecurityNetworkSecurityPolicy update_network_security_policy1(o_name, body)

Update NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = SecurityNetworkSecurityPolicy(
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
        spec=SecurityNetworkSecurityPolicySpec(
            attach_groups=[
                "attach_groups_example",
            ],
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_security_groups=[
                        "from_security_groups_example",
                    ],
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_security_groups=[
                        "to_security_groups_example",
                    ],
                ),
            ],
        ),
        status=SecurityNetworkSecurityPolicyStatus(
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            rule_status=[
                SecuritySGRuleStatus(
                    rule_hash="rule_hash_example",
                ),
            ],
        ),
    ) # SecurityNetworkSecurityPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update NetworkSecurityPolicy object
        api_response = api_instance.update_network_security_policy1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)|  |

### Return type

[**SecurityNetworkSecurityPolicy**](SecurityNetworkSecurityPolicy.md)

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

# **update_security_group**
> SecuritySecurityGroup update_security_group(o_tenant, o_name, body)

Update SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = SecuritySecurityGroup(
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
        spec=SecuritySecurityGroupSpec(
            match_prefixes=[
                "match_prefixes_example",
            ],
            service_labels=[
                "service_labels_example",
            ],
            workload_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ),
        status=SecuritySecurityGroupStatus(
            policies=[
                "policies_example",
            ],
            workloads=[
                "workloads_example",
            ],
        ),
    ) # SecuritySecurityGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update SecurityGroup object
        api_response = api_instance.update_security_group(o_tenant, o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_security_group: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**SecuritySecurityGroup**](SecuritySecurityGroup.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **update_security_group1**
> SecuritySecurityGroup update_security_group1(o_name, body)

Update SecurityGroup object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_security_group import SecuritySecurityGroup
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = SecuritySecurityGroup(
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
        spec=SecuritySecurityGroupSpec(
            match_prefixes=[
                "match_prefixes_example",
            ],
            service_labels=[
                "service_labels_example",
            ],
            workload_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ),
        status=SecuritySecurityGroupStatus(
            policies=[
                "policies_example",
            ],
            workloads=[
                "workloads_example",
            ],
        ),
    ) # SecuritySecurityGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Update SecurityGroup object
        api_response = api_instance.update_security_group1(o_name, body)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_security_group1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**SecuritySecurityGroup**](SecuritySecurityGroup.md)|  |

### Return type

[**SecuritySecurityGroup**](SecuritySecurityGroup.md)

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

# **watch_app**
> SecurityAutoMsgAppWatchHelper watch_app(o_tenant)

Watch App objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_app_watch_helper import SecurityAutoMsgAppWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Watch App objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_app(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_app: %s\n" % e)

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

[**SecurityAutoMsgAppWatchHelper**](SecurityAutoMsgAppWatchHelper.md)

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

# **watch_app1**
> SecurityAutoMsgAppWatchHelper watch_app1()

Watch App objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_app_watch_helper import SecurityAutoMsgAppWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # Watch App objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_app1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_app1: %s\n" % e)

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

[**SecurityAutoMsgAppWatchHelper**](SecurityAutoMsgAppWatchHelper.md)

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

# **watch_firewall_profile**
> SecurityAutoMsgFirewallProfileWatchHelper watch_firewall_profile(o_tenant)

Watch FirewallProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_firewall_profile_watch_helper import SecurityAutoMsgFirewallProfileWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_firewall_profile(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_firewall_profile: %s\n" % e)

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

[**SecurityAutoMsgFirewallProfileWatchHelper**](SecurityAutoMsgFirewallProfileWatchHelper.md)

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

# **watch_firewall_profile1**
> SecurityAutoMsgFirewallProfileWatchHelper watch_firewall_profile1()

Watch FirewallProfile objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_firewall_profile_watch_helper import SecurityAutoMsgFirewallProfileWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_firewall_profile1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_firewall_profile1: %s\n" % e)

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

[**SecurityAutoMsgFirewallProfileWatchHelper**](SecurityAutoMsgFirewallProfileWatchHelper.md)

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

# **watch_ip_sec_policy**
> SecurityAutoMsgIPSecPolicyWatchHelper watch_ip_sec_policy(o_tenant)

Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_ip_sec_policy_watch_helper import SecurityAutoMsgIPSecPolicyWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_ip_sec_policy: %s\n" % e)

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

[**SecurityAutoMsgIPSecPolicyWatchHelper**](SecurityAutoMsgIPSecPolicyWatchHelper.md)

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

# **watch_ip_sec_policy1**
> SecurityAutoMsgIPSecPolicyWatchHelper watch_ip_sec_policy1()

Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_ip_sec_policy_watch_helper import SecurityAutoMsgIPSecPolicyWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ip_sec_policy1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_ip_sec_policy1: %s\n" % e)

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

[**SecurityAutoMsgIPSecPolicyWatchHelper**](SecurityAutoMsgIPSecPolicyWatchHelper.md)

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

# **watch_network_security_policy**
> SecurityAutoMsgNetworkSecurityPolicyWatchHelper watch_network_security_policy(o_tenant)

Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_network_security_policy_watch_helper import SecurityAutoMsgNetworkSecurityPolicyWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_network_security_policy: %s\n" % e)

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

[**SecurityAutoMsgNetworkSecurityPolicyWatchHelper**](SecurityAutoMsgNetworkSecurityPolicyWatchHelper.md)

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

# **watch_network_security_policy1**
> SecurityAutoMsgNetworkSecurityPolicyWatchHelper watch_network_security_policy1()

Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_network_security_policy_watch_helper import SecurityAutoMsgNetworkSecurityPolicyWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_security_policy1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_network_security_policy1: %s\n" % e)

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

[**SecurityAutoMsgNetworkSecurityPolicyWatchHelper**](SecurityAutoMsgNetworkSecurityPolicyWatchHelper.md)

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

# **watch_security_group**
> SecurityAutoMsgSecurityGroupWatchHelper watch_security_group(o_tenant)

Watch SecurityGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_security_group_watch_helper import SecurityAutoMsgSecurityGroupWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
        # Watch SecurityGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_security_group(o_tenant)
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_security_group: %s\n" % e)

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

[**SecurityAutoMsgSecurityGroupWatchHelper**](SecurityAutoMsgSecurityGroupWatchHelper.md)

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

# **watch_security_group1**
> SecurityAutoMsgSecurityGroupWatchHelper watch_security_group1()

Watch SecurityGroup objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent
import pensando_ent.psm
from pensando_ent.psm.api import security_v1_api
from pensando_ent.psm.model.security_auto_msg_security_group_watch_helper import SecurityAutoMsgSecurityGroupWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_ent.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
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
    try:
        # Watch SecurityGroup objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_security_group1()
        pprint(api_response)
    except pensando_ent.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_security_group1: %s\n" % e)

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

[**SecurityAutoMsgSecurityGroupWatchHelper**](SecurityAutoMsgSecurityGroupWatchHelper.md)

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

