# MonitoringExportConfig

Export Config specifies server address and user credentials.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | IP address of the collector/entity to which the data is to be exported. Should be a valid IPv4 address. | [optional] 
**gateway** | **str** | Gateway of the dest IP address to which the data is to be exported. Should be a valid IPv4 address. | [optional] 
**transport** | **str** | protocol and Port number where an external collector is gathering the data example \&quot;UDP/2055\&quot;. Should be a valid layer 3 or layer 4 protocol and port/type (only support UDP currently). | [optional] 
**virtual_router** | **str** | Destination Virtual Router. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


