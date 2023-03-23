# ApiObjectMeta

ObjectMeta contains metadata that all objects stored in kvstore must have.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **datetime** | System generated and updated, not updatable by user. | [optional] 
**display_name** | **str** | If setting the DisplayName, please leave the Name field empty. The Name field will be set to the Object UUID if the DisplayName is set If the Name field is set, the DisplayName is expected to be empty, both fields are mutually exclusive The DisplayName is expected to be unique among Objects of the same (kind, tenant). Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional] 
**generation_id** | **str** | This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional] 
**labels** | **{str: (str,)}** |  | [optional] 
**mod_time** | **datetime** | System generated and updated, not updatable by user. | [optional] 
**name** | **str** | Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional] 
**namespace** | **str** | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional] 
**resource_version** | **str** | This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional] 
**self_link** | **str** | When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional] 
**tenant** | **str** | This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional] 
**uuid** | **str** | This is generated on creation of the object. System generated, not updatable by user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


