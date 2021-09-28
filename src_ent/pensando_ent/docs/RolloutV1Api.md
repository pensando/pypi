# psm.RolloutV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rollout**](RolloutV1Api.md#create_rollout) | **POST** /configs/rollout/v1/rollout/CreateRollout | Start Rollout operation
[**get_rollout**](RolloutV1Api.md#get_rollout) | **GET** /configs/rollout/v1/rollout/{O.Name} | Get Rollout object
[**list_rollout**](RolloutV1Api.md#list_rollout) | **GET** /configs/rollout/v1/rollout | List Rollout objects
[**remove_rollout**](RolloutV1Api.md#remove_rollout) | **POST** /configs/rollout/v1/rollout/RemoveRollout | Remove a Rollout
[**stop_rollout**](RolloutV1Api.md#stop_rollout) | **POST** /configs/rollout/v1/rollout/StopRollout | Stop a Rollout operation
[**update_rollout**](RolloutV1Api.md#update_rollout) | **POST** /configs/rollout/v1/rollout/UpdateRollout | Update Rollout configuration
[**watch_rollout**](RolloutV1Api.md#watch_rollout) | **GET** /configs/rollout/v1/watch/rollout | Watch Rollout objects. Supports WebSockets or HTTP long poll


# **create_rollout**
> RolloutRollout create_rollout(body)

Start Rollout operation

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
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
        spec=RolloutRolloutSpec(
            dsc_must_match_constraint=True,
            dscs_only=True,
            max_nic_failures_before_abort=1,
            max_parallel=2,
            order_constraints=[
                LabelsSelector(
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
            ],
            retry=True,
            scheduled_end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            scheduled_start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            strategy="linear",
            suspend=True,
            upgrade_type="graceful",
            version="version_example",
        ),
        status=RolloutRolloutStatus(
            completion_percent=1,
            controller_nodes_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            controller_services_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            dscs_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            prev_version="prev_version_example",
            reason="reason_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            state="progressing",
        ),
    ) # RolloutRollout | 

    # example passing only required values which don't have defaults set
    try:
        # Start Rollout operation
        api_response = api_instance.create_rollout(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->create_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **get_rollout**
> RolloutRollout get_rollout(o_name)

Get Rollout object

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
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
    spec_version = "spec.version_example" # str | New Version of the image to rollout to. (optional)
    spec_scheduled_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Time, if specified, at which the rollout is supposed to start. (example:\"2002-10-02T15:00:00.05Z\"). (optional)
    spec_scheduled_end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ScheduledEndTime, if specified, after which the rollout is supposed to stop, if not completed by that time Typically represents the end of Maintenance window. (example:\"2002-10-02T15:00:00.05Z\"). (optional)
    spec_strategy = "spec.strategy_example" # str |  (optional)
    spec_max_parallel = 1 # int | MaxParallel is the maximum number of nodes getting updated at any time This setting is applicable only to DistributedServiceCards. Controller nodes are always upgraded one after another. (optional)
    spec_max_nic_failures_before_abort = 1 # int | After these many failures are observed during DSC upgrade, the rollout process stops This setting applies to DSCs only. The controller nodes are rollout first and any failure there stops the rollout of DistributedServiceCards. (optional)
    spec_suspend = True # bool | When Set to true, the current rollout is suspended. Existing Nodes/Services/DistributedServiceCards in the middle of rollout continue rollout execution but any Nodes/Services/DistributedServiceCards which has not started Rollout will not be scheduled one. (optional)
    spec_dscs_only = True # bool | Dont upgrade Controller but only upgrade DistributedServiceCards. (optional)
    spec_dsc_must_match_constraint = True # bool | When DSCMustMatchConstraint is true, Any DSC which does not match OrderConstraints does not go through rollout. (optional)
    spec_upgrade_type = "spec.upgrade-type_example" # str |  (optional)
    spec_retry = True # bool | If enabled, will retry rollout of failed naples within the maintenance window upto a max of 5 times. (optional)
    status_state = "status.state_example" # str |  (optional)
    status_completion_percent = 1 # int | Heuristic value of percentage completion of the rollout. (optional)
    status_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start time of Rollout. (optional)
    status_end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End time of Rollout. (optional)
    status_prev_version = "status.prev-version_example" # str | Version of the cluster before the start of rollout. (optional)
    status_reason = "status.reason_example" # str | details the reason for overall Failure or Suspend. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Rollout object
        api_response = api_instance.get_rollout(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->get_rollout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Rollout object
        api_response = api_instance.get_rollout(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_version=spec_version, spec_scheduled_start_time=spec_scheduled_start_time, spec_scheduled_end_time=spec_scheduled_end_time, spec_strategy=spec_strategy, spec_max_parallel=spec_max_parallel, spec_max_nic_failures_before_abort=spec_max_nic_failures_before_abort, spec_suspend=spec_suspend, spec_dscs_only=spec_dscs_only, spec_dsc_must_match_constraint=spec_dsc_must_match_constraint, spec_upgrade_type=spec_upgrade_type, spec_retry=spec_retry, status_state=status_state, status_completion_percent=status_completion_percent, status_start_time=status_start_time, status_end_time=status_end_time, status_prev_version=status_prev_version, status_reason=status_reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->get_rollout: %s\n" % e)
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
 **spec_version** | **str**| New Version of the image to rollout to. | [optional]
 **spec_scheduled_start_time** | **datetime**| Time, if specified, at which the rollout is supposed to start. (example:\&quot;2002-10-02T15:00:00.05Z\&quot;). | [optional]
 **spec_scheduled_end_time** | **datetime**| ScheduledEndTime, if specified, after which the rollout is supposed to stop, if not completed by that time Typically represents the end of Maintenance window. (example:\&quot;2002-10-02T15:00:00.05Z\&quot;). | [optional]
 **spec_strategy** | **str**|  | [optional]
 **spec_max_parallel** | **int**| MaxParallel is the maximum number of nodes getting updated at any time This setting is applicable only to DistributedServiceCards. Controller nodes are always upgraded one after another. | [optional]
 **spec_max_nic_failures_before_abort** | **int**| After these many failures are observed during DSC upgrade, the rollout process stops This setting applies to DSCs only. The controller nodes are rollout first and any failure there stops the rollout of DistributedServiceCards. | [optional]
 **spec_suspend** | **bool**| When Set to true, the current rollout is suspended. Existing Nodes/Services/DistributedServiceCards in the middle of rollout continue rollout execution but any Nodes/Services/DistributedServiceCards which has not started Rollout will not be scheduled one. | [optional]
 **spec_dscs_only** | **bool**| Dont upgrade Controller but only upgrade DistributedServiceCards. | [optional]
 **spec_dsc_must_match_constraint** | **bool**| When DSCMustMatchConstraint is true, Any DSC which does not match OrderConstraints does not go through rollout. | [optional]
 **spec_upgrade_type** | **str**|  | [optional]
 **spec_retry** | **bool**| If enabled, will retry rollout of failed naples within the maintenance window upto a max of 5 times. | [optional]
 **status_state** | **str**|  | [optional]
 **status_completion_percent** | **int**| Heuristic value of percentage completion of the rollout. | [optional]
 **status_start_time** | **datetime**| Start time of Rollout. | [optional]
 **status_end_time** | **datetime**| End time of Rollout. | [optional]
 **status_prev_version** | **str**| Version of the cluster before the start of rollout. | [optional]
 **status_reason** | **str**| details the reason for overall Failure or Suspend. | [optional]

### Return type

[**RolloutRollout**](RolloutRollout.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **list_rollout**
> RolloutRolloutList list_rollout()

List Rollout objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout_list import RolloutRolloutList
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
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
        # List Rollout objects
        api_response = api_instance.list_rollout(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->list_rollout: %s\n" % e)
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

[**RolloutRolloutList**](RolloutRolloutList.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **remove_rollout**
> RolloutRollout remove_rollout(body)

Remove a Rollout

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
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
        spec=RolloutRolloutSpec(
            dsc_must_match_constraint=True,
            dscs_only=True,
            max_nic_failures_before_abort=1,
            max_parallel=2,
            order_constraints=[
                LabelsSelector(
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
            ],
            retry=True,
            scheduled_end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            scheduled_start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            strategy="linear",
            suspend=True,
            upgrade_type="graceful",
            version="version_example",
        ),
        status=RolloutRolloutStatus(
            completion_percent=1,
            controller_nodes_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            controller_services_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            dscs_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            prev_version="prev_version_example",
            reason="reason_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            state="progressing",
        ),
    ) # RolloutRollout | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a Rollout
        api_response = api_instance.remove_rollout(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->remove_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **stop_rollout**
> RolloutRollout stop_rollout(body)

Stop a Rollout operation

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
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
        spec=RolloutRolloutSpec(
            dsc_must_match_constraint=True,
            dscs_only=True,
            max_nic_failures_before_abort=1,
            max_parallel=2,
            order_constraints=[
                LabelsSelector(
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
            ],
            retry=True,
            scheduled_end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            scheduled_start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            strategy="linear",
            suspend=True,
            upgrade_type="graceful",
            version="version_example",
        ),
        status=RolloutRolloutStatus(
            completion_percent=1,
            controller_nodes_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            controller_services_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            dscs_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            prev_version="prev_version_example",
            reason="reason_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            state="progressing",
        ),
    ) # RolloutRollout | 

    # example passing only required values which don't have defaults set
    try:
        # Stop a Rollout operation
        api_response = api_instance.stop_rollout(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->stop_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **update_rollout**
> RolloutRollout update_rollout(body)

Update Rollout configuration

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_rollout import RolloutRollout
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
    body = RolloutRollout(
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
        spec=RolloutRolloutSpec(
            dsc_must_match_constraint=True,
            dscs_only=True,
            max_nic_failures_before_abort=1,
            max_parallel=2,
            order_constraints=[
                LabelsSelector(
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
            ],
            retry=True,
            scheduled_end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            scheduled_start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            strategy="linear",
            suspend=True,
            upgrade_type="graceful",
            version="version_example",
        ),
        status=RolloutRolloutStatus(
            completion_percent=1,
            controller_nodes_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            controller_services_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            dscs_status=[
                RolloutRolloutPhase(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    name="name_example",
                    num_retries=0,
                    phase="pre-check",
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            prev_version="prev_version_example",
            reason="reason_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            state="progressing",
        ),
    ) # RolloutRollout | 

    # example passing only required values which don't have defaults set
    try:
        # Update Rollout configuration
        api_response = api_instance.update_rollout(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->update_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolloutRollout**](RolloutRollout.md)|  |

### Return type

[**RolloutRollout**](RolloutRollout.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

# **watch_rollout**
> RolloutAutoMsgRolloutWatchHelper watch_rollout()

Watch Rollout objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import rollout_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.rollout import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.rollout_auto_msg_rollout_watch_helper import RolloutAutoMsgRolloutWatchHelper
from pensando_ent.psm.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rollout_v1_api.RolloutV1Api(api_client)
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
        # Watch Rollout objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_rollout(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolloutV1Api->watch_rollout: %s\n" % e)
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

[**RolloutAutoMsgRolloutWatchHelper**](RolloutAutoMsgRolloutWatchHelper.md)

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

[[Back to psm.RolloutV1Api top]](#psm.RolloutV1Api) [[Back to rollout README]](../psm/docs/rollout/README.md) [[Back to pensando_ent README]](../README.md)

