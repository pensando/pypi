# RecoverykeysRecoveryKeys

RecoveryKeys is a message that allows user to retrieve root cluster keys.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** | PrivateKey is the private key generated at cluster bootstrap. | [optional] 
**psm_version** | **str** | PsmVersion is the version of the PSM SW corresponding to the recovery keys. | [optional] 
**trust_chain** | **[str]** | TrustChain is the chain of intermediate certificates that are needed to establish the validity of the public key. | [optional] 
**trust_roots** | **[str]** | TrustRoot is the certificate of an entity used as a root CA. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


