# AuthRadiusServerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message contains error message in case of failed check or a success message. | [optional] 
**nas_id** | **str** | NasID is a string identifying the NAS(API Gw) originating the Access-Request. | [optional] 
**result** | **str** | Result indicates if radius check was successful. | [optional]  if omitted the server will use the default value of "connect-success"
**server** | [**AuthRadiusServer**](AuthRadiusServer.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


