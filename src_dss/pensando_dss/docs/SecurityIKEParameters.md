# SecurityIKEParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_sa** | [**SecurityIKESAParameters**](SecurityIKESAParameters.md) |  | [optional] 
**ike_version** | **str** | IKEVersion is for IPv4 only. IPv6 always uses IKEv2. | [optional]  if omitted the server will use the default value of "IKEv2"
**ipsec_sa** | [**SecurityIPsecSAParameters**](SecurityIPsecSAParameters.md) |  | [optional] 
**local_identifier** | [**IKEParametersIdentifier**](IKEParametersIdentifier.md) |  | [optional] 
**remote_identifier** | [**IKEParametersIdentifier**](IKEParametersIdentifier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


