# AuditEventAttributes

Attributes contains all the audit log attributes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action that was requested/performed on the referred object. For non API server resources, it is the http method. | [optional] 
**client_ips** | **[str]** | IP addresses of client and intermediate proxies from where API request was made. | [optional] 
**data** | **{str: (str,)}** | Data is unstructured key value map stored with audit log that may be set by hooks in API Gateway. We can store Signature in JWS compact serialization format in this map. Data in this map will not be signed. | [optional] 
**external_id** | **str** | ID passed in by an external application to link audit event to the request. It should be AlphaNumeric and can contain -. Maximum length supported is 64. Length of string should be between 0 and 64. Must be alpha numeric and can have -. | [optional] 
**gateway_ip** | **str** | IP address of API Gateway where action was observed. | [optional] 
**gateway_node** | **str** | Name of the venice node where action was observed. | [optional] 
**level** | **str** | Level to control amount of audit information logged. | [optional]  if omitted the server will use the default value of "basic"
**outcome** | **str** | Outcome represents the outcome of action on resource. | [optional]  if omitted the server will use the default value of "success"
**request_object** | **str** | Object from the request in JSON format. | [optional] 
**request_uri** | **str** | RequestURI is the request URI as sent by the client. Should be a valid URI. | [optional] 
**resource** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 
**response_object** | **str** | Object from the response in JSON format to be sent to the client. | [optional] 
**service_name** | **str** | Name of service that handled the request and performed the requested operation for ex: search, events etc. | [optional] 
**stage** | **str** | Request handling stage at which audit log was generated. | [optional]  if omitted the server will use the default value of "requestauthorization"
**user** | [**ApiObjectRef**](ApiObjectRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


