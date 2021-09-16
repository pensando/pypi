# NetworkHealthCheckSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**declare_healthy_count** | **int** | # of successful probes before we declare the backend back up. | [optional] 
**interval** | **int** | Health check interval. | [optional] 
**max_timeouts** | **int** | timeout for declaring backend down. | [optional] 
**probe_port_or_url** | **str** | probe URL. | [optional] 
**probes_per_interval** | **int** | # of probes per interval. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


