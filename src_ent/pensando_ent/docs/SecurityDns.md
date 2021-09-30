# SecurityDns

DNS ALG configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_large_domain_name_packets** | **bool** | Drop if domain name size is &gt; 255 bytes. | [optional] 
**drop_long_label_packets** | **bool** | Drop if label length is 64 bytes or higher. | [optional] 
**drop_multi_question_packets** | **bool** | Drop packet if number of questions is more than one. | [optional] 
**max_message_length** | **int** | Maximum message length, default value is 512, maximum specified user value is 8129. | [optional] 
**query_response_timeout** | **str** | Timeout for DNS Query, default 60s. Should be a valid time duration. | [optional]  if omitted the server will use the default value of "60s"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


