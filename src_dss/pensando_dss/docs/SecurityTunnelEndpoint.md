# SecurityTunnelEndpoint

Applies to North-South Traffic only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dse** | **str** |  | [optional] 
**ike_sa** | [**SecurityIKESAParameters**](SecurityIKESAParameters.md) |  | [optional] 
**ike_version** | **str** |  | [optional]  if omitted the server will use the default value of "IKEv2"
**interface_name** | **str** |  | [optional] 
**ipsec_sa** | [**SecurityIPsecSAParameters**](SecurityIPsecSAParameters.md) |  | [optional] 
**local_identifier** | [**IKEParametersIdentifier**](IKEParametersIdentifier.md) |  | [optional] 
**remote_identifier** | [**IKEParametersIdentifier**](IKEParametersIdentifier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


