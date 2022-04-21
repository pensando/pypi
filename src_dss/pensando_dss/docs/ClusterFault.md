# ClusterFault

Captures any fault at DSS end.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the fault occured. | [optional] 
**last_occured_time** | **str** | Time at which the fault occured. | [optional] 
**mitigation** | **str** | Mitigation action,if any possible. | [optional]  if omitted the server will use the default value of "system-reboot"
**severity** | **str** | Severity of fault occured at DSS end. | [optional]  if omitted the server will use the default value of "info"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


