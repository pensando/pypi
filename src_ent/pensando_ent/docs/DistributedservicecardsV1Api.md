# psm.DistributedservicecardsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_query_connection**](DistributedservicecardsV1Api.md#post_query_connection) | **POST** /sysruntime/distributedservicecards/v1/{DSCName}/connections | Active Connection Query


# **post_query_connection**
> SysruntimeConnectionStatus post_query_connection(dsc_name, body)

Active Connection Query

### Example

```python
import time
import pensando_ent.psm
from pensando_ent.psm.api import distributedservicecards_v1_api
from pensando_ent.psm.model.sysruntime_connection_request import SysruntimeConnectionRequest
from pensando_ent.psm.model.sysruntime_connection_status import SysruntimeConnectionStatus
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
    api_instance = distributedservicecards_v1_api.DistributedservicecardsV1Api(api_client)
    dsc_name = "DSCName_example" # str | 
    body = SysruntimeConnectionRequest(
        api_version="api_version_example",
        dsc_name="dsc_name_example",
        filters=[
            SysruntimeConnectionFilter(
                destination=SysruntimeWorkloadSelector(
                    ip_address="10.1.1.1 ",
                ),
                destination_port=1,
                protocol="none",
                source=SysruntimeWorkloadSelector(
                    ip_address="10.1.1.1 ",
                ),
                source_port=1,
            ),
        ],
        kind="kind_example",
        list=ApiListWatchOptions(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            field_change_selector=[
                "field_change_selector_example",
            ],
            field_selector="field_selector_example",
            _from=1,
            generation_id="generation_id_example",
            label_selector="label_selector_example",
            labels={
                "key": "key_example",
            },
            max_results=1,
            meta_only=False,
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            sort_order="none",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # SysruntimeConnectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Active Connection Query
        api_response = api_instance.post_query_connection(dsc_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling DistributedservicecardsV1Api->post_query_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dsc_name** | **str**|  |
 **body** | [**SysruntimeConnectionRequest**](SysruntimeConnectionRequest.md)|  |

### Return type

[**SysruntimeConnectionStatus**](SysruntimeConnectionStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

