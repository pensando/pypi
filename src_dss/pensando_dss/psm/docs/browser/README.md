
## Documentation for API Endpoints

All URIs are relative to *https://PSM-IP-addr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrowserV1Api* | [**get_query1**](../../../../pensando_dss/docs/BrowserV1Api.md#get_query1) | **GET** /configs/browser/v1/query | 
*BrowserV1Api* | [**get_references**](../../../../pensando_dss/docs/BrowserV1Api.md#get_references) | **GET** /configs/browser/v1/dependencies/** | 
*BrowserV1Api* | [**get_referrers**](../../../../pensando_dss/docs/BrowserV1Api.md#get_referrers) | **GET** /configs/browser/v1/dependedby/** | 
*BrowserV1Api* | [**post_query**](../../../../pensando_dss/docs/BrowserV1Api.md#post_query) | **POST** /configs/browser/v1/query | 


## Documentation For Models

 - [ApiAggWatchOptions](../../../docs/ApiAggWatchOptions.md)
 - [ApiKindWatchOptions](../../../docs/ApiKindWatchOptions.md)
 - [ApiListWatchOptions](../../../docs/ApiListWatchOptions.md)
 - [ApiObjectMeta](../../../docs/ApiObjectMeta.md)
 - [ApiObjectRef](../../../docs/ApiObjectRef.md)
 - [ApiStatus](../../../docs/ApiStatus.md)
 - [ApiStatusResult](../../../docs/ApiStatusResult.md)
 - [ApiTimestamp](../../../docs/ApiTimestamp.md)
 - [ApiTypeMeta](../../../docs/ApiTypeMeta.md)
 - [ApiWatchControl](../../../docs/ApiWatchControl.md)
 - [ApiWatchEvent](../../../docs/ApiWatchEvent.md)
 - [ApiWatchEventList](../../../docs/ApiWatchEventList.md)
 - [BrowserBrowseRequest](../../../docs/BrowserBrowseRequest.md)
 - [BrowserBrowseRequestList](../../../docs/BrowserBrowseRequestList.md)
 - [BrowserBrowseRequestObject](../../../docs/BrowserBrowseRequestObject.md)
 - [BrowserBrowseResponse](../../../docs/BrowserBrowseResponse.md)
 - [BrowserBrowseResponseList](../../../docs/BrowserBrowseResponseList.md)
 - [BrowserBrowseResponseObject](../../../docs/BrowserBrowseResponseObject.md)
 - [BrowserObject](../../../docs/BrowserObject.md)
 - [GoogleprotobufAny](../../../docs/GoogleprotobufAny.md)
 - [ObjectURIs](../../../docs/ObjectURIs.md)


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
