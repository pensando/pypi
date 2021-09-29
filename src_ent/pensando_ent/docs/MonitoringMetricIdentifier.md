# MonitoringMetricIdentifier

MetricIdentifier - uniquely identifies an metric that needs to be monitored as part of the policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field belonging to the kind e.g. ConnectionsPerSecond. This is the attribute that will be monitored and alerts will be created/resolved based on the thresholds. | [optional] 
**group** | **str** | Metric group - e.g. ftestats, flowstats, etc. | [optional] 
**kind** | **str** | Sub-category within the group e.g. MaxSessionThresholdDrops, FlowMissPackets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


