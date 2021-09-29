# psm.OrchestrationV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_orchestrator**](OrchestrationV1Api.md#add_orchestrator) | **POST** /configs/orchestration/v1/orchestrator | Create Orchestrator object
[**delete_orchestrator**](OrchestrationV1Api.md#delete_orchestrator) | **DELETE** /configs/orchestration/v1/orchestrator/{O.Name} | Delete Orchestrator object
[**get_orchestrator**](OrchestrationV1Api.md#get_orchestrator) | **GET** /configs/orchestration/v1/orchestrator/{O.Name} | Get Orchestrator object
[**label_orchestrator**](OrchestrationV1Api.md#label_orchestrator) | **POST** /configs/orchestration/v1/orchestrator/{O.Name}/label | Label Orchestrator object
[**list_orchestrator**](OrchestrationV1Api.md#list_orchestrator) | **GET** /configs/orchestration/v1/orchestrator | List Orchestrator objects
[**update_orchestrator**](OrchestrationV1Api.md#update_orchestrator) | **PUT** /configs/orchestration/v1/orchestrator/{O.Name} | Update Orchestrator object
[**watch_orchestrator**](OrchestrationV1Api.md#watch_orchestrator) | **GET** /configs/orchestration/v1/watch/orchestrator | Watch Orchestrator objects. Supports WebSockets or HTTP long poll


# **add_orchestrator**
> OrchestrationOrchestrator add_orchestrator(body)

Create Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    body = OrchestrationOrchestrator(
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
        spec=OrchestrationOrchestratorSpec(
            credentials=MonitoringExternalCred(
                auth_type="none",
                bearer_token="bearer_token_example",
                ca_data="ca_data_example",
                cert_data="cert_data_example",
                disable_server_authentication=True,
                key_data="key_data_example",
                password="password_example",
                username="username_example",
            ),
            namespaces=[
                OrchestrationNamespaceSpec(
                    managed_spec=OrchestrationManagedNamespaceSpec(
                        discovery_operation="disc-op-default",
                        discovery_protocol="disc-proto-default",
                        mtu=0,
                        multicast_filter="mcast-filter-default",
                        override_vlan_end=4087,
                        override_vlan_start=3832,
                    ),
                    mode="managed",
                    monitored_spec={},
                    name="name_example",
                ),
            ],
            type="vcenter",
            uri="uri_example",
        ),
        status=OrchestrationOrchestratorStatus(
            connection_status="unknown",
            discovered_namespaces=[
                "discovered_namespaces_example",
            ],
            incompatible_dscs=[
                "incompatible_dscs_example",
            ],
            last_transition_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            message="message_example",
            orch_id=1,
        ),
    ) # OrchestrationOrchestrator | 

    # example passing only required values which don't have defaults set
    try:
        # Create Orchestrator object
        api_response = api_instance.add_orchestrator(body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->add_orchestrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **delete_orchestrator**
> OrchestrationOrchestrator delete_orchestrator(o_name)

Delete Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Orchestrator object
        api_response = api_instance.delete_orchestrator(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->delete_orchestrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **get_orchestrator**
> OrchestrationOrchestrator get_orchestrator(o_name)

Get Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
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
    spec_type = "spec.type_example" # str | Type of orchestrator. (optional)
    spec_uri = "spec.uri_example" # str | URI of the orchestrator. Length of string should be at least 1. (optional)
    credentials_auth_type = "credentials.auth-type_example" # str | AuthType is the authentication type used in this config. (optional)
    credentials_username = "credentials.username_example" # str | UserName is the login id to be used towards the external entity. (optional)
    credentials_password = "credentials.password_example" # str | Password is one time specified, not visibile on read operations Only valid when UserName is defined. (optional)
    credentials_bearer_token = "credentials.bearer-token_example" # str | External entity supports bearer tokens for authentication and authorization Token refresh is not supported using OAuth2. (optional)
    credentials_cert_data = "credentials.cert-data_example" # str | CertData holds PEM-encoded bytes (typically read from a client certificate file). (optional)
    credentials_key_data = "credentials.key-data_example" # str | KeyData holds PEM-encoded bytes (typically read from a client certificate key file). (optional)
    credentials_ca_data = "credentials.ca-data_example" # str | CaData holds PEM-encoded bytes (typically read from a root certificates bundle). CaData is used by client to autheticate external server. This is applicable to all authentication methods. (optional)
    credentials_disable_server_authentication = True # bool | DisableServerAuthentication flag can be used when a client does not want to authenticate a server. (optional)
    status_connection_status = "status.connection-status_example" # str |  (optional)
    status_last_transition_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    status_message = "status.message_example" # str |  (optional)
    status_orch_id = 1 # int |  (optional)
    status_discovered_namespaces = [
        "status.discovered-namespaces_example",
    ] # [str] |  (optional)
    status_incompatible_dscs = [
        "status.incompatible-dscs_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Orchestrator object
        api_response = api_instance.get_orchestrator(o_name)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->get_orchestrator: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Orchestrator object
        api_response = api_instance.get_orchestrator(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, spec_uri=spec_uri, credentials_auth_type=credentials_auth_type, credentials_username=credentials_username, credentials_password=credentials_password, credentials_bearer_token=credentials_bearer_token, credentials_cert_data=credentials_cert_data, credentials_key_data=credentials_key_data, credentials_ca_data=credentials_ca_data, credentials_disable_server_authentication=credentials_disable_server_authentication, status_connection_status=status_connection_status, status_last_transition_time=status_last_transition_time, status_message=status_message, status_orch_id=status_orch_id, status_discovered_namespaces=status_discovered_namespaces, status_incompatible_dscs=status_incompatible_dscs)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->get_orchestrator: %s\n" % e)
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
 **spec_type** | **str**| Type of orchestrator. | [optional]
 **spec_uri** | **str**| URI of the orchestrator. Length of string should be at least 1. | [optional]
 **credentials_auth_type** | **str**| AuthType is the authentication type used in this config. | [optional]
 **credentials_username** | **str**| UserName is the login id to be used towards the external entity. | [optional]
 **credentials_password** | **str**| Password is one time specified, not visibile on read operations Only valid when UserName is defined. | [optional]
 **credentials_bearer_token** | **str**| External entity supports bearer tokens for authentication and authorization Token refresh is not supported using OAuth2. | [optional]
 **credentials_cert_data** | **str**| CertData holds PEM-encoded bytes (typically read from a client certificate file). | [optional]
 **credentials_key_data** | **str**| KeyData holds PEM-encoded bytes (typically read from a client certificate key file). | [optional]
 **credentials_ca_data** | **str**| CaData holds PEM-encoded bytes (typically read from a root certificates bundle). CaData is used by client to autheticate external server. This is applicable to all authentication methods. | [optional]
 **credentials_disable_server_authentication** | **bool**| DisableServerAuthentication flag can be used when a client does not want to authenticate a server. | [optional]
 **status_connection_status** | **str**|  | [optional]
 **status_last_transition_time** | **datetime**|  | [optional]
 **status_message** | **str**|  | [optional]
 **status_orch_id** | **int**|  | [optional]
 **status_discovered_namespaces** | **[str]**|  | [optional]
 **status_incompatible_dscs** | **[str]**|  | [optional]

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **label_orchestrator**
> OrchestrationOrchestrator label_orchestrator(o_name, body)

Label Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
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
        # Label Orchestrator object
        api_response = api_instance.label_orchestrator(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->label_orchestrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **list_orchestrator**
> OrchestrationOrchestratorList list_orchestrator()

List Orchestrator objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.orchestration_orchestrator_list import OrchestrationOrchestratorList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
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
        # List Orchestrator objects
        api_response = api_instance.list_orchestrator(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->list_orchestrator: %s\n" % e)
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

[**OrchestrationOrchestratorList**](OrchestrationOrchestratorList.md)

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

# **update_orchestrator**
> OrchestrationOrchestrator update_orchestrator(o_name, body)

Update Orchestrator object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.orchestration_orchestrator import OrchestrationOrchestrator
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = OrchestrationOrchestrator(
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
        spec=OrchestrationOrchestratorSpec(
            credentials=MonitoringExternalCred(
                auth_type="none",
                bearer_token="bearer_token_example",
                ca_data="ca_data_example",
                cert_data="cert_data_example",
                disable_server_authentication=True,
                key_data="key_data_example",
                password="password_example",
                username="username_example",
            ),
            namespaces=[
                OrchestrationNamespaceSpec(
                    managed_spec=OrchestrationManagedNamespaceSpec(
                        discovery_operation="disc-op-default",
                        discovery_protocol="disc-proto-default",
                        mtu=0,
                        multicast_filter="mcast-filter-default",
                        override_vlan_end=4087,
                        override_vlan_start=3832,
                    ),
                    mode="managed",
                    monitored_spec={},
                    name="name_example",
                ),
            ],
            type="vcenter",
            uri="uri_example",
        ),
        status=OrchestrationOrchestratorStatus(
            connection_status="unknown",
            discovered_namespaces=[
                "discovered_namespaces_example",
            ],
            incompatible_dscs=[
                "incompatible_dscs_example",
            ],
            last_transition_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            message="message_example",
            orch_id=1,
        ),
    ) # OrchestrationOrchestrator | 

    # example passing only required values which don't have defaults set
    try:
        # Update Orchestrator object
        api_response = api_instance.update_orchestrator(o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->update_orchestrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)|  |

### Return type

[**OrchestrationOrchestrator**](OrchestrationOrchestrator.md)

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

# **watch_orchestrator**
> OrchestrationAutoMsgOrchestratorWatchHelper watch_orchestrator()

Watch Orchestrator objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_ent.psm
from pensando_ent.psm.api import orchestration_v1_api
from pensando_ent.psm.model.orchestration_auto_msg_orchestrator_watch_helper import OrchestrationAutoMsgOrchestratorWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orchestration_v1_api.OrchestrationV1Api(api_client)
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
        # Watch Orchestrator objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_orchestrator(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling OrchestrationV1Api->watch_orchestrator: %s\n" % e)
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

[**OrchestrationAutoMsgOrchestratorWatchHelper**](OrchestrationAutoMsgOrchestratorWatchHelper.md)

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

