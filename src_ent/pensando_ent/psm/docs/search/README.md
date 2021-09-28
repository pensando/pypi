```python

import time
import psm
from pprint import pprint
from api import search_v1_api
from pensando_ent.psm.model.search_policy_search_request import SearchPolicySearchRequest
from pensando_ent.psm.model.search_policy_search_response import SearchPolicySearchResponse
from pensando_ent.psm.model.search_search_request import SearchSearchRequest
from pensando_ent.psm.model.search_search_response import SearchSearchResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_v1_api.SearchV1Api(api_client)
    tenant = "tenant_example" # str | Tenant Name, to perform query within a Tenant's scope. The default tenant is \"default\". In the backend this field gets auto-filled & validated by apigw-hook based on user login context. (optional)
namespace = "namespace_example" # str | Namespace is optional. If provided policy-search will be limited to the specified namespace. (optional)
app = "app_example" # str | App specification,  predefined apps and alg config. (optional)
protocol = "protocol_example" # str | Protocol eg: tcp, udp, icmp. (optional)
port = "port_example" # str | TCP or UDP Port number. (optional)
from_ip_address = "from-ip-address_example" # str | Inbound ip-address, use any to refer to all ipaddresses eg: 10.1.1.1, any. (optional)
to_ip_address = "to-ip-address_example" # str | Outbound ip-address, use any to refer to all ipaddresses eg: 20.1.1.1, any. (optional)
from_security_group = "from-security-group_example" # str | Inbound security group. (optional)
to_security_group = "to-security-group_example" # str | Outbound security group. (optional)
kinds = [
        "kinds_example",
    ] # [str] | Kind of the policy that this request should act on. It should be either NetworkSecurityPolicy or IPSecPolicy. (optional)
name = "name_example" # str | Name is optional. If provided policy-search will be limited to the specified policy of the given name on the given kind. If empty, then all the policies of the given kind will be searched. (optional)
action = "action_example" # str | Action, e.g. PERMIT, DENY or REJECT/CLEAR, PROTECT_PERMISSIVE or PROTECT_STRICT. (optional)

    try:
        # Security Policy Query
        api_response = api_instance.get_policy_query1(tenant=tenant, namespace=namespace, app=app, protocol=protocol, port=port, from_ip_address=from_ip_address, to_ip_address=to_ip_address, from_security_group=from_security_group, to_security_group=to_security_group, kinds=kinds, name=name, action=action)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling SearchV1Api->get_policy_query1: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SearchV1Api* | [**get_policy_query1**](docs/SearchV1Api.md#get_policy_query1) | **GET** /search/v1/policy-query | Security Policy Query
*SearchV1Api* | [**get_query1**](docs/SearchV1Api.md#get_query1) | **GET** /search/v1/query | Structured or free-form search
*SearchV1Api* | [**post_policy_query**](docs/SearchV1Api.md#post_policy_query) | **POST** /search/v1/policy-query | Security Policy Query
*SearchV1Api* | [**post_query**](docs/SearchV1Api.md#post_query) | **POST** /search/v1/query | Structured or free-form search


## Documentation For Models

 - [ApiAggWatchOptions](docs/ApiAggWatchOptions.md)
 - [ApiAny](docs/ApiAny.md)
 - [ApiKindWatchOptions](docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](docs/ApiObjectMeta.md)
 - [ApiObjectRef](docs/ApiObjectRef.md)
 - [ApiStatus](docs/ApiStatus.md)
 - [ApiStatusResult](docs/ApiStatusResult.md)
 - [ApiTimestamp](docs/ApiTimestamp.md)
 - [ApiWatchControl](docs/ApiWatchControl.md)
 - [ApiWatchEvent](docs/ApiWatchEvent.md)
 - [ApiWatchEventList](docs/ApiWatchEventList.md)
 - [FieldsRequirement](docs/FieldsRequirement.md)
 - [FieldsSelector](docs/FieldsSelector.md)
 - [GoogleprotobufAny](docs/GoogleprotobufAny.md)
 - [LabelsRequirement](docs/LabelsRequirement.md)
 - [LabelsSelector](docs/LabelsSelector.md)
 - [SearchCategoryAggregation](docs/SearchCategoryAggregation.md)
 - [SearchCategoryPreview](docs/SearchCategoryPreview.md)
 - [SearchEntry](docs/SearchEntry.md)
 - [SearchEntryList](docs/SearchEntryList.md)
 - [SearchError](docs/SearchError.md)
 - [SearchKindAggregation](docs/SearchKindAggregation.md)
 - [SearchKindPreview](docs/SearchKindPreview.md)
 - [SearchPolicyMatchEntries](docs/SearchPolicyMatchEntries.md)
 - [SearchPolicyMatchEntry](docs/SearchPolicyMatchEntry.md)
 - [SearchPolicySearchRequest](docs/SearchPolicySearchRequest.md)
 - [SearchPolicySearchResponse](docs/SearchPolicySearchResponse.md)
 - [SearchRulesByPolicyName](docs/SearchRulesByPolicyName.md)
 - [SearchSearchQuery](docs/SearchSearchQuery.md)
 - [SearchSearchRequest](docs/SearchSearchRequest.md)
 - [SearchSearchResponse](docs/SearchSearchResponse.md)
 - [SearchTenantAggregation](docs/SearchTenantAggregation.md)
 - [SearchTenantPreview](docs/SearchTenantPreview.md)
 - [SearchTextRequirement](docs/SearchTextRequirement.md)
 - [SecurityIPSecMatchRule](docs/SecurityIPSecMatchRule.md)
 - [SecurityIPSecPolicyRule](docs/SecurityIPSecPolicyRule.md)
 - [SecurityProtoPort](docs/SecurityProtoPort.md)
 - [SecuritySGRule](docs/SecuritySGRule.md)


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
