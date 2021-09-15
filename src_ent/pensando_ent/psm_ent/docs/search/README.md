# search

This page provides working code examples for the **search** group.

Please see each listed method (i.e API Endpoints) for working code examples.

## Documentation for API Endpoints

All URIs are relative to `https://PSM-IP/`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SearchV1Api* | [**get_policy_query1**](../../../docs/SearchV1Api.md#get_policy_query1) | **GET** /search/v1/policy-query | Security Policy Query
*SearchV1Api* | [**get_query1**](../../../docs/SearchV1Api.md#get_query1) | **GET** /search/v1/query | Structured or free-form search
*SearchV1Api* | [**post_policy_query**](../../../docs/SearchV1Api.md#post_policy_query) | **POST** /search/v1/policy-query | Security Policy Query
*SearchV1Api* | [**post_query**](../../../docs/SearchV1Api.md#post_query) | **POST** /search/v1/query | Structured or free-form search


## README links for Model Groups

[aggwatch README.md](..//aggwatch/README.md)

[audit README.md](..//audit/README.md)

[auth README.md](..//auth/README.md)

[browser README.md](..//browser/README.md)

[cluster README.md](..//cluster/README.md)

[diagnostics README.md](..//diagnostics/README.md)

[events README.md](..//events/README.md)

[fwlog README.md](..//fwlog/README.md)

[monitoring README.md](..//monitoring/README.md)

[network README.md](..//network/README.md)

[objstore README.md](..//objstore/README.md)

[orchestration README.md](..//orchestration/README.md)

[preferences README.md](..//preferences/README.md)

[recoverykeys README.md](..//recoverykeys/README.md)

[rollout README.md](..//rollout/README.md)

[routing README.md](..//routing/README.md)

[search README.md](..//search/README.md)

[security README.md](..//security/README.md)

[staging README.md](..//staging/README.md)

[sysruntime README.md](..//sysruntime/README.md)

[telemetry_query README.md](..//telemetry_query/README.md)

[tokenauth README.md](..//tokenauth/README.md)

[workload README.md](..//workload/README.md)


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiAny](../../../docs/ApiAny.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [FieldsRequirement](../../../docs/FieldsRequirement.md)
 - [FieldsSelector](../../../docs/FieldsSelector.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [LabelsRequirement](../../../docs/LabelsRequirement.md)
 - [LabelsSelector](../../../docs/LabelsSelector.md)
 - [SearchCategoryAggregation](../../../docs/SearchCategoryAggregation.md)
 - [SearchCategoryPreview](../../../docs/SearchCategoryPreview.md)
 - [SearchEntry](../../../docs/SearchEntry.md)
 - [SearchEntryList](../../../docs/SearchEntryList.md)
 - [SearchError](../../../docs/SearchError.md)
 - [SearchKindAggregation](../../../docs/SearchKindAggregation.md)
 - [SearchKindPreview](../../../docs/SearchKindPreview.md)
 - [SearchPolicyMatchEntries](../../../docs/SearchPolicyMatchEntries.md)
 - [SearchPolicyMatchEntry](../../../docs/SearchPolicyMatchEntry.md)
 - [SearchPolicySearchRequest](../../../docs/SearchPolicySearchRequest.md)
 - [SearchPolicySearchResponse](../../../docs/SearchPolicySearchResponse.md)
 - [SearchRulesByPolicyName](../../../docs/SearchRulesByPolicyName.md)
 - [SearchSearchQuery](../../../docs/SearchSearchQuery.md)
 - [SearchSearchRequest](../../../docs/SearchSearchRequest.md)
 - [SearchSearchResponse](../../../docs/SearchSearchResponse.md)
 - [SearchTenantAggregation](../../../docs/SearchTenantAggregation.md)
 - [SearchTenantPreview](../../../docs/SearchTenantPreview.md)
 - [SearchTextRequirement](../../../docs/SearchTextRequirement.md)
 - [SecurityIPSecMatchRule](../../../docs/SecurityIPSecMatchRule.md)
 - [SecurityIPSecPolicyRule](../../../docs/SecurityIPSecPolicyRule.md)
 - [SecurityProtoPort](../../../docs/SecurityProtoPort.md)
 - [SecuritySGRule](../../../docs/SecuritySGRule.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in psm_ent.apis and psm_ent.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from psm_ent.api.default_api import DefaultApi`
- `from psm_ent.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import psm_ent
from psm_ent.apis import *
from psm_ent.models import *
```
