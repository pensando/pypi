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
[**delete_app**](SecurityV1Api.md#delete_app) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Delete App object
[**delete_app1**](SecurityV1Api.md#delete_app1) | **DELETE** /configs/security/v1/apps/{O.Name} | Delete App object
[**delete_ip_sec_policy**](SecurityV1Api.md#delete_ip_sec_policy) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Delete IPSecPolicy object
[**delete_ip_sec_policy1**](SecurityV1Api.md#delete_ip_sec_policy1) | **DELETE** /configs/security/v1/ipsecpolicies/{O.Name} | Delete IPSecPolicy object
[**delete_network_security_policy**](SecurityV1Api.md#delete_network_security_policy) | **DELETE** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Delete NetworkSecurityPolicy object
[**delete_network_security_policy1**](SecurityV1Api.md#delete_network_security_policy1) | **DELETE** /configs/security/v1/networksecuritypolicies/{O.Name} | Delete NetworkSecurityPolicy object
[**get_app**](SecurityV1Api.md#get_app) | **GET** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Get App object
[**get_app1**](SecurityV1Api.md#get_app1) | **GET** /configs/security/v1/apps/{O.Name} | Get App object
[**get_firewall_profile**](SecurityV1Api.md#get_firewall_profile) | **GET** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name} | Get FirewallProfile object
[**get_firewall_profile1**](SecurityV1Api.md#get_firewall_profile1) | **GET** /configs/security/v1/firewallprofiles/{O.Name} | Get FirewallProfile object
[**get_ip_sec_policy**](SecurityV1Api.md#get_ip_sec_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Get IPSecPolicy object
[**get_ip_sec_policy1**](SecurityV1Api.md#get_ip_sec_policy1) | **GET** /configs/security/v1/ipsecpolicies/{O.Name} | Get IPSecPolicy object
[**get_network_security_policy**](SecurityV1Api.md#get_network_security_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Get NetworkSecurityPolicy object
[**get_network_security_policy1**](SecurityV1Api.md#get_network_security_policy1) | **GET** /configs/security/v1/networksecuritypolicies/{O.Name} | Get NetworkSecurityPolicy object
[**label_app**](SecurityV1Api.md#label_app) | **POST** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name}/label | Label App object
[**label_app1**](SecurityV1Api.md#label_app1) | **POST** /configs/security/v1/apps/{O.Name}/label | Label App object
[**label_firewall_profile**](SecurityV1Api.md#label_firewall_profile) | **POST** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name}/label | Label FirewallProfile object
[**label_firewall_profile1**](SecurityV1Api.md#label_firewall_profile1) | **POST** /configs/security/v1/firewallprofiles/{O.Name}/label | Label FirewallProfile object
[**label_ip_sec_policy**](SecurityV1Api.md#label_ip_sec_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name}/label | Label IPSecPolicy object
[**label_ip_sec_policy1**](SecurityV1Api.md#label_ip_sec_policy1) | **POST** /configs/security/v1/ipsecpolicies/{O.Name}/label | Label IPSecPolicy object
[**label_network_security_policy**](SecurityV1Api.md#label_network_security_policy) | **POST** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name}/label | Label NetworkSecurityPolicy object
[**label_network_security_policy1**](SecurityV1Api.md#label_network_security_policy1) | **POST** /configs/security/v1/networksecuritypolicies/{O.Name}/label | Label NetworkSecurityPolicy object
[**list_app**](SecurityV1Api.md#list_app) | **GET** /configs/security/v1/tenant/{O.Tenant}/apps | List App objects
[**list_app1**](SecurityV1Api.md#list_app1) | **GET** /configs/security/v1/apps | List App objects
[**list_firewall_profile**](SecurityV1Api.md#list_firewall_profile) | **GET** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles | List FirewallProfile objects
[**list_firewall_profile1**](SecurityV1Api.md#list_firewall_profile1) | **GET** /configs/security/v1/firewallprofiles | List FirewallProfile objects
[**list_ip_sec_policy**](SecurityV1Api.md#list_ip_sec_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies | List IPSecPolicy objects
[**list_ip_sec_policy1**](SecurityV1Api.md#list_ip_sec_policy1) | **GET** /configs/security/v1/ipsecpolicies | List IPSecPolicy objects
[**list_network_security_policy**](SecurityV1Api.md#list_network_security_policy) | **GET** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies | List NetworkSecurityPolicy objects
[**list_network_security_policy1**](SecurityV1Api.md#list_network_security_policy1) | **GET** /configs/security/v1/networksecuritypolicies | List NetworkSecurityPolicy objects
[**update_app**](SecurityV1Api.md#update_app) | **PUT** /configs/security/v1/tenant/{O.Tenant}/apps/{O.Name} | Update App object
[**update_app1**](SecurityV1Api.md#update_app1) | **PUT** /configs/security/v1/apps/{O.Name} | Update App object
[**update_firewall_profile**](SecurityV1Api.md#update_firewall_profile) | **PUT** /configs/security/v1/tenant/{O.Tenant}/firewallprofiles/{O.Name} | Update FirewallProfile object
[**update_firewall_profile1**](SecurityV1Api.md#update_firewall_profile1) | **PUT** /configs/security/v1/firewallprofiles/{O.Name} | Update FirewallProfile object
[**update_ip_sec_policy**](SecurityV1Api.md#update_ip_sec_policy) | **PUT** /configs/security/v1/tenant/{O.Tenant}/ipsecpolicies/{O.Name} | Update IPSecPolicy object
[**update_ip_sec_policy1**](SecurityV1Api.md#update_ip_sec_policy1) | **PUT** /configs/security/v1/ipsecpolicies/{O.Name} | Update IPSecPolicy object
[**update_network_security_policy**](SecurityV1Api.md#update_network_security_policy) | **PUT** /configs/security/v1/tenant/{O.Tenant}/networksecuritypolicies/{O.Name} | Update NetworkSecurityPolicy object
[**update_network_security_policy1**](SecurityV1Api.md#update_network_security_policy1) | **PUT** /configs/security/v1/networksecuritypolicies/{O.Name} | Update NetworkSecurityPolicy object
[**watch_app**](SecurityV1Api.md#watch_app) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/apps | Watch App objects. Supports WebSockets or HTTP long poll
[**watch_app1**](SecurityV1Api.md#watch_app1) | **GET** /configs/security/v1/watch/apps | Watch App objects. Supports WebSockets or HTTP long poll
[**watch_firewall_profile**](SecurityV1Api.md#watch_firewall_profile) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/firewallprofiles | Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
[**watch_firewall_profile1**](SecurityV1Api.md#watch_firewall_profile1) | **GET** /configs/security/v1/watch/firewallprofiles | Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
[**watch_ip_sec_policy**](SecurityV1Api.md#watch_ip_sec_policy) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/ipsecpolicies | Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
[**watch_ip_sec_policy1**](SecurityV1Api.md#watch_ip_sec_policy1) | **GET** /configs/security/v1/watch/ipsecpolicies | Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
[**watch_network_security_policy**](SecurityV1Api.md#watch_network_security_policy) | **GET** /configs/security/v1/watch/tenant/{O.Tenant}/networksecuritypolicies | Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
[**watch_network_security_policy1**](SecurityV1Api.md#watch_network_security_policy1) | **GET** /configs/security/v1/watch/networksecuritypolicies | Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll


# **add_app**
> SecurityApp add_app(o_tenant, body)

Create App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
                ike_lifetime="1h",
                sa_lifetime="1h",
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
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
                ike_lifetime="1h",
                sa_lifetime="1h",
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
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    disable=True,
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_workload_groups=[
                        "from_workload_groups_example",
                    ],
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_workload_groups=[
                        "to_workload_groups_example",
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
            rule_metrics_status=[
                SecurityRuleMetricsStatus(
                    dsc_id="dsc_id_example",
                    policy_entries_consumed="policy_entries_consumed_example",
                    rule_entries_consumed="rule_entries_consumed_example",
                ),
            ],
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
    except pensando_dss.psm.ApiException as e:
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    disable=True,
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_workload_groups=[
                        "from_workload_groups_example",
                    ],
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_workload_groups=[
                        "to_workload_groups_example",
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
            rule_metrics_status=[
                SecurityRuleMetricsStatus(
                    dsc_id="dsc_id_example",
                    policy_entries_consumed="policy_entries_consumed_example",
                    rule_entries_consumed="rule_entries_consumed_example",
                ),
            ],
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
    except pensando_dss.psm.ApiException as e:
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

# **delete_app**
> SecurityApp delete_app(o_tenant)

Delete App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete App object
        api_response = api_instance.delete_app(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete App object
        api_response = api_instance.delete_app1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> SecurityIPSecPolicy delete_ip_sec_policy(o_tenant)

Delete IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPSecPolicy object
        api_response = api_instance.delete_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete IPSecPolicy object
        api_response = api_instance.delete_ip_sec_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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
> SecurityNetworkSecurityPolicy delete_network_security_policy(o_tenant)

Delete NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete NetworkSecurityPolicy object
        api_response = api_instance.delete_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->delete_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete NetworkSecurityPolicy object
        api_response = api_instance.delete_network_security_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
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

# **get_app**
> SecurityApp get_app(o_tenant)

Get App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    alg_type = "alg.type_example" # str |  (optional)
    status_attached_policies = [
        "status.attached-policies_example",
    ] # [str] | List of security group policies attached to the app. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get App object
        api_response = api_instance.get_app(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **alg_type** | **str**|  | [optional]
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    alg_type = "alg.type_example" # str |  (optional)
    status_attached_policies = [
        "status.attached-policies_example",
    ] # [str] | List of security group policies attached to the app. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get App object
        api_response = api_instance.get_app1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **alg_type** | **str**|  | [optional]
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
> SecurityFirewallProfile get_firewall_profile(o_tenant)

Get FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FirewallProfile object
        api_response = api_instance.get_firewall_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FirewallProfile object
        api_response = api_instance.get_firewall_profile1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_firewall_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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
> SecurityIPSecPolicy get_ip_sec_policy(o_tenant)

Get IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPSecPolicy object
        api_response = api_instance.get_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPSecPolicy object
        api_response = api_instance.get_ip_sec_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

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
> SecurityNetworkSecurityPolicy get_network_security_policy(o_tenant)

Get NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkSecurityPolicy object
        api_response = api_instance.get_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get NetworkSecurityPolicy object
        api_response = api_instance.get_network_security_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->get_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
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

# **label_app**
> SecurityApp label_app(o_tenant, body)

Label App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.security_app import SecurityApp
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.label_app(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.security_app import SecurityApp
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityFirewallProfile label_firewall_profile(o_tenant, body)

Label FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.label_firewall_profile(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityIPSecPolicy label_ip_sec_policy(o_tenant, body)

Label IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.label_ip_sec_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityNetworkSecurityPolicy label_network_security_policy(o_tenant, body)

Label NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.label_network_security_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->label_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
    except pensando_dss.psm.ApiException as e:
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

# **list_app**
> SecurityAppList list_app(o_tenant)

List App objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app_list import SecurityAppList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List App objects
        api_response = api_instance.list_app(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app_list import SecurityAppList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List App objects
        api_response = api_instance.list_app1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile_list import SecurityFirewallProfileList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FirewallProfile objects
        api_response = api_instance.list_firewall_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile_list import SecurityFirewallProfileList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FirewallProfile objects
        api_response = api_instance.list_firewall_profile1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_firewall_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy_list import SecurityIPSecPolicyList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List IPSecPolicy objects
        api_response = api_instance.list_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy_list import SecurityIPSecPolicyList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List IPSecPolicy objects
        api_response = api_instance.list_ip_sec_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy_list import SecurityNetworkSecurityPolicyList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List NetworkSecurityPolicy objects
        api_response = api_instance.list_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy_list import SecurityNetworkSecurityPolicyList
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List NetworkSecurityPolicy objects
        api_response = api_instance.list_network_security_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

# **update_app**
> SecurityApp update_app(o_tenant, body)

Update App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
        # Update App object
        api_response = api_instance.update_app(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_app: %s\n" % e)

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

# **update_app1**
> SecurityApp update_app1(o_name, body)

Update App object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app import SecurityApp
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityFirewallProfile update_firewall_profile(o_tenant, body)

Update FirewallProfile object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
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
        api_response = api_instance.update_firewall_profile(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_firewall_profile import SecurityFirewallProfile
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityIPSecPolicy update_ip_sec_policy(o_tenant, body)

Update IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
                ike_lifetime="1h",
                sa_lifetime="1h",
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
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
        api_response = api_instance.update_ip_sec_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_ip_sec_policy: %s\n" % e)

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

# **update_ip_sec_policy1**
> SecurityIPSecPolicy update_ip_sec_policy1(o_name, body)

Update IPSecPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_ip_sec_policy import SecurityIPSecPolicy
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
                ike_lifetime="1h",
                sa_lifetime="1h",
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
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
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
    except pensando_dss.psm.ApiException as e:
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
> SecurityNetworkSecurityPolicy update_network_security_policy(o_tenant, body)

Update NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    disable=True,
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_workload_groups=[
                        "from_workload_groups_example",
                    ],
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_workload_groups=[
                        "to_workload_groups_example",
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
            rule_metrics_status=[
                SecurityRuleMetricsStatus(
                    dsc_id="dsc_id_example",
                    policy_entries_consumed="policy_entries_consumed_example",
                    rule_entries_consumed="rule_entries_consumed_example",
                ),
            ],
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
        api_response = api_instance.update_network_security_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->update_network_security_policy: %s\n" % e)

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

# **update_network_security_policy1**
> SecurityNetworkSecurityPolicy update_network_security_policy1(o_name, body)

Update NetworkSecurityPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
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
            attach_tenant=True,
            priority=1,
            rules=[
                SecuritySGRule(
                    action="permit",
                    apps=[
                        "apps_example",
                    ],
                    description="description_example",
                    disable=True,
                    from_ip_addresses=[
                        "from_ip_addresses_example",
                    ],
                    from_workload_groups=[
                        "from_workload_groups_example",
                    ],
                    name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
                    proto_ports=[
                        SecurityProtoPort(
                            ports="ports_example",
                            protocol="protocol_example",
                        ),
                    ],
                    to_ip_addresses=[
                        "to_ip_addresses_example",
                    ],
                    to_workload_groups=[
                        "to_workload_groups_example",
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
            rule_metrics_status=[
                SecurityRuleMetricsStatus(
                    dsc_id="dsc_id_example",
                    policy_entries_consumed="policy_entries_consumed_example",
                    rule_entries_consumed="rule_entries_consumed_example",
                ),
            ],
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
    except pensando_dss.psm.ApiException as e:
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

# **watch_app**
> SecurityAutoMsgAppWatchHelper watch_app(o_tenant)

Watch App objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_app_watch_helper import SecurityAutoMsgAppWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch App objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_app(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_app: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_app_watch_helper import SecurityAutoMsgAppWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch App objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_app1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_app1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_firewall_profile_watch_helper import SecurityAutoMsgFirewallProfileWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_firewall_profile(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_firewall_profile: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_firewall_profile_watch_helper import SecurityAutoMsgFirewallProfileWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FirewallProfile objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_firewall_profile1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_firewall_profile1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_ip_sec_policy_watch_helper import SecurityAutoMsgIPSecPolicyWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ip_sec_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_ip_sec_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_auto_msg_ip_sec_policy_watch_helper import SecurityAutoMsgIPSecPolicyWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch IPSecPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_ip_sec_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_ip_sec_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.security_auto_msg_network_security_policy_watch_helper import SecurityAutoMsgNetworkSecurityPolicyWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_security_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_network_security_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.security_auto_msg_network_security_policy_watch_helper import SecurityAutoMsgNetworkSecurityPolicyWatchHelper
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
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch NetworkSecurityPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_network_security_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->watch_network_security_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

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

