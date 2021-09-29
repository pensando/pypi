# ClusterUpdateTLSConfigRequest

UpdateTLSConfigRequest is to update certs and key for API Gateway TLS.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**certs** | **str** | Certs is the pem encoded certificate bundle used for API Gateway TLS. | [optional] 
**key** | **str** | Key is the pem encoded private key used for API Gateway TLS. We support RSA or ECDSA. | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


