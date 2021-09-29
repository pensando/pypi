# AuditAuditEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**client_ips** | **[str]** |  | [optional] 
**data** | **{str: (str,)}** |  | [optional] 
**external_id** | **str** | Length of string should be between 0 and 64. Must be alpha numeric and can have -. | [optional] 
**gateway_ip** | **str** |  | [optional] 
**gateway_node** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**level** | **str** |  | [optional]  if omitted the server will use the default value of "basic"
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**outcome** | **str** |  | [optional]  if omitted the server will use the default value of "success"
**request_object** | **str** |  | [optional] 
**request_uri** | **str** | Should be a valid URI. | [optional] 
**resource** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 
**response_object** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**stage** | **str** |  | [optional]  if omitted the server will use the default value of "requestauthorization"
**user** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


