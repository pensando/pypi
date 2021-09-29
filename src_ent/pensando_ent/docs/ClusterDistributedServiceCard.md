# ClusterDistributedServiceCard

------------------------------------ Distributed Service Card  ------------------------------------------- DistributedServiceCard represents the Naples I/O subsystem Entity responsible & scenarios involved in managing this object: Create: o CMD - created as part of NIC registration, Admittance Modify: o CMD - update spec attributes - update status attributes Delete: o CMD - aging out stale or rejected NICs (TBD) o NetOps, SecOps - Decomission a NIC (TBD).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**meta** | [**ApiObjectMeta**](ApiObjectMeta.md) |  | [optional] 
**spec** | [**ClusterDistributedServiceCardSpec**](ClusterDistributedServiceCardSpec.md) |  | [optional] 
**status** | [**ClusterDistributedServiceCardStatus**](ClusterDistributedServiceCardStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


