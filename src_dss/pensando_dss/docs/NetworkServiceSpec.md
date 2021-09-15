# NetworkServiceSpec

spec part of service object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lb_policy** | **str** | load balancing policy (reference to LbPolicy object). | [optional] 
**ports** | **str** | load balancer port. | [optional] 
**tls_client_policy** | [**NetworkTLSClientPolicySpec**](NetworkTLSClientPolicySpec.md) |  | [optional] 
**tls_server_policy** | [**NetworkTLSServerPolicySpec**](NetworkTLSServerPolicySpec.md) |  | [optional] 
**virtual_ip** | **str** | Virtual IP of the load balancer. | [optional] 
**workload_labels** | **[str]** | FIXME: maps are not working. change this after its fixed map&lt;string, string&gt; WorkloadSelector  &#x3D; 1 [(gogoproto.nullable) &#x3D; true, (gogoproto.jsontag) &#x3D; \&quot;workload-labels,omitempty\&quot;]; workload selector for the service (list of labels to match). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


