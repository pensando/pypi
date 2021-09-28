# psm.TelemetryQueryV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics1**](TelemetryQueryV1Api.md#get_metrics1) | **GET** /telemetry/v1/metrics | telemetry metrics query
[**post_metrics**](TelemetryQueryV1Api.md#post_metrics) | **POST** /telemetry/v1/metrics | telemetry metrics query


# **get_metrics1**
> TelemetryQueryMetricsQueryResponse get_metrics1()

telemetry metrics query

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import telemetry_query_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.telemetry_query import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.telemetry_query_metrics_query_response import TelemetryQueryMetricsQueryResponse
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
    api_instance = telemetry_query_v1_api.TelemetryQueryV1Api(api_client)
    tenant = "tenant_example" # str | Tenant for the request. (optional)
    namespace = "namespace_example" # str | Namespace for the request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # telemetry metrics query
        api_response = api_instance.get_metrics1(tenant=tenant, namespace=namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TelemetryQueryV1Api->get_metrics1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**| Tenant for the request. | [optional]
 **namespace** | **str**| Namespace for the request. | [optional]

### Return type

[**TelemetryQueryMetricsQueryResponse**](TelemetryQueryMetricsQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm.TelemetryQueryV1Api top]](#psm.TelemetryQueryV1Api) [[Back to telemetry_query README]](../psm/docs/telemetry_query/README.md) [[Back to pensando_ent README]](../README.md)

# **post_metrics**
> TelemetryQueryMetricsQueryResponse post_metrics(body)

telemetry metrics query

### Example

```python
#!/usr/bin/env python3
import time
import .psm
from pensando_ent.psm.api import telemetry_query_v1_api
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.models.telemetry_query import *
from pensando_ent.psm  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_ent.psm.model.telemetry_query_metrics_query_list import TelemetryQueryMetricsQueryList
from pensando_ent.psm.model.telemetry_query_metrics_query_response import TelemetryQueryMetricsQueryResponse
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
    api_instance = telemetry_query_v1_api.TelemetryQueryV1Api(api_client)
    body = TelemetryQueryMetricsQueryList(
        namespace="namespace_example",
        queries=[
            TelemetryQueryMetricsQuerySpec(
                api_version="api_version_example",
                bottom_param=TelemetryQueryBottomSpec(
                    bottom_n=1,
                ),
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields=[
                    "fields_example",
                ],
                function="none",
                group_by_field="gB98JLe5iL60,aa,-Ctq9dcsc-2,7",
                group_by_time="60s",
                kind="kind_example",
                name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
                pagination=TelemetryQueryPaginationSpec(
                    count=1,
                    offset=0,
                ),
                selector=FieldsSelector(
                    requirements=[
                        FieldsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                sort_order="ascending",
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subquery=TelemetryQueryMetricsQuerySpec(TelemetryQueryMetricsQuerySpec),
                top_param=TelemetryQueryTopSpec(
                    top_n=1,
                ),
            ),
        ],
        tenant="tenant_example",
    ) # TelemetryQueryMetricsQueryList | 

    # example passing only required values which don't have defaults set
    try:
        # telemetry metrics query
        api_response = api_instance.post_metrics(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TelemetryQueryV1Api->post_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TelemetryQueryMetricsQueryList**](TelemetryQueryMetricsQueryList.md)|  |

### Return type

[**TelemetryQueryMetricsQueryResponse**](TelemetryQueryMetricsQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to psm.TelemetryQueryV1Api top]](#psm.TelemetryQueryV1Api) [[Back to telemetry_query README]](../psm/docs/telemetry_query/README.md) [[Back to pensando_ent README]](../README.md)

