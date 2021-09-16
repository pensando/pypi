# SearchTextRequirement

TextRequirement is AND of text-strings in the list It is comprised of words or phrases for text search support. If a text-string has space separated multi-word, it will be interpreted as a phrase. In the example below : - \"link down\" will be a phrase query - network, production, staging will be a word query For eg: network                      (match network) link down                    (match \"link down\" phrase) network,production           (match network AND production) network,link down,staging    (match network AND \"link down\" AND staging).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **[str]** | AND of words or phrases to be matched The max text-string length is 256 bytes. Length of string should be between 0 and 256. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


