# AuthPermission

Permission defines if actions are allowed on resource group, resource type, resource name or arbitrary API endpoints.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[str]** | Actions are actions on a resource that a permission allows. | [optional] 
**resource_group** | **str** | ResourceGroup is grouping of resource types for which a permission is defined. It is empty for Search, Event, MetricsQuery and non-api server endpoint. Specifying \&quot;_All_\&quot; will match all api groups including empty group for non-api server endpoints like those defined in ResrcKind enum. | [optional] 
**resource_kind** | **str** | ResourceKind is a resource kind for which permission is defined. It can be an API Server object kind or kinds defined in ResrcKind enum. Specifying \&quot;_All_\&quot; will match all resource kinds. | [optional] 
**resource_names** | **[str]** | ResourceNames identify specific objects on which this permission applies. If resource name is not specified in permission then it implies all resources of the specified kind. | [optional] 
**resource_namespace** | **str** | ResourceNamespace is a namespace to which a resource (API Server object) belongs. Default value is \&quot;_All_\&quot; which matches all namespaces. | [optional]  if omitted the server will use the default value of "_All_"
**resource_tenant** | **str** | ResourceTenant is the tenant to which resource belongs. It will be automatically set to the tenant to which role object belongs. Exception are roles in \&quot;default\&quot; tenant. Role in \&quot;default\&quot; tenant can include permissions for resources in other tenants. Specifying \&quot;_All_\&quot; will match all tenants. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


