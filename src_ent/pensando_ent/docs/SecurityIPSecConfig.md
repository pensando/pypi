# SecurityIPSecConfig

These are the cluster wide IPSec parameters that are common to all IPSec SecurityAssociations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_lifetime** | **str** | Time to schedule Internet Key Exchange (IKE) reauthentication. IKE reauthentication recreates the IKE SA from scratch and re-evaluates the credentials Default 24h, set it to an empty string to disable reauthentication. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]  if omitted the server will use the default value of "24h"
**sa_lifetime** | **str** | How long a particular instance of a connection should last, from successful negotiation to expiry The connection will be re-negotiated before it expires. Post succesful re-negotation, the new connection will have new(different) keys and a new SPI Default 8h, Max 24h, set it to an empty string to disable rekeying. Should be a valid time duration between 1h0m0s and 24h0m0s. | [optional]  if omitted the server will use the default value of "8h"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


