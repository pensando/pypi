# AuthRadiusServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** | AuthMethod is authentication method to use with the RADIUS server. | [optional]  if omitted the server will use the default value of "pap"
**secret** | **str** | Secret is the shared secret between API Gw and RADIUS server. | [optional] 
**trusted_certs** | **str** | TrustedCerts defines the set of PEM encoded root certificate authorities that will be used when verifying server certificates. It is used in PEAP and EAP_TTLS auth methods. | [optional] 
**url** | **str** | &lt;IP address&gt;:&lt;Port&gt; of the RADIUS server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


