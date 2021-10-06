# RolloutRolloutSpec

RolloutSpec is the Spec of a Rollout.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsc_must_match_constraint** | **bool** | When DSCMustMatchConstraint is true, Any DSC which does not match OrderConstraints does not go through rollout. | [optional] 
**dscs_only** | **bool** | Dont upgrade Controller but only upgrade DistributedServiceCards. | [optional] 
**max_nic_failures_before_abort** | **int** | After these many failures are observed during DSC upgrade, the rollout process stops This setting applies to DSCs only. The controller nodes are rollout first and any failure there stops the rollout of DistributedServiceCards. | [optional] 
**max_parallel** | **int** | MaxParallel is the maximum number of nodes getting updated at any time This setting is applicable only to DistributedServiceCards. Controller nodes are always upgraded one after another. | [optional]  if omitted the server will use the default value of 2
**order_constraints** | [**[LabelsSelector]**](LabelsSelector.md) | If specified, this is the sequence in which the DistributedServiceCards are upgraded based on their labels. if a DistributedServiceCard matches multiple constraints, the first one is used. Any DistributedServiceCard which does not match the constraints is upgraded at the end. This order is mainly for the DSCs on Hosts Controller nodes are always rollout one after other. | [optional] 
**retry** | **bool** | If enabled, will retry rollout of failed naples within the maintenance window upto a max of 5 times. | [optional] 
**scheduled_end_time** | **datetime** | ScheduledEndTime, if specified, after which the rollout is supposed to stop, if not completed by that time Typically represents the end of Maintenance window. (example:\&quot;2002-10-02T15:00:00.05Z\&quot;). | [optional] 
**scheduled_start_time** | **datetime** | Time, if specified, at which the rollout is supposed to start. (example:\&quot;2002-10-02T15:00:00.05Z\&quot;). | [optional] 
**strategy** | **str** |  | [optional]  if omitted the server will use the default value of "linear"
**suspend** | **bool** | When Set to true, the current rollout is suspended. Existing Nodes/Services/DistributedServiceCards in the middle of rollout continue rollout execution but any Nodes/Services/DistributedServiceCards which has not started Rollout will not be scheduled one. | [optional] 
**upgrade_type** | **str** |  | [optional]  if omitted the server will use the default value of "graceful"
**version** | **str** | New Version of the image to rollout to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


