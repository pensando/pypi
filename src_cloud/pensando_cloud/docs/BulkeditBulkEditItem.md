# BulkeditBulkEditItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional]  if omitted the server will use the default value of "create"
**object** | [**ApiAny**](ApiAny.md) |  | [optional] 
**uri** | **str** | URI field: For Create, update and delete operations, the backend uses the Kind, tenant and name fields in the Object to Infer the URI The URI field is expected to be filled in only for label(required) and delete(optional) operations For delete operation, if the URI is populated, the Object field can be left empty. If the URI is empty, the object field is expected to be populated with the Object to be deleted For label operations, the URI must be populated and the Object must be of api.Label type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


