# WorkloadEndpointSpec

spec part of Endpoint object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homing_host_addr** | **str** | IP of the DSC where this endpoint exists. | [optional] 
**micro_segment_vlan** | **int** | MicroSegmentVlan to be assigned to the endpoint. | [optional] 
**node_uuid** | **str** | The DSC Name or MAC where the endpoint should reside. | [optional] 
**node_uuid_list** | **[str]** | NodeUUIDList has the list of DSCs where a EP is supposed to go to. | [optional] 
**type** | **str** | Type is the type of Endpoint that is being created - L2 or L3. | [optional]  if omitted the server will use the default value of "l2"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


