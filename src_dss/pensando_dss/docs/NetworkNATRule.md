# NetworkNATRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**NetworkNATAddress**](NetworkNATAddress.md) |  | [optional] 
**destination_proto_port** | [**ApiProtoPort**](ApiProtoPort.md) |  | [optional] 
**disable** | **bool** | rule enable or disable. | [optional] 
**name** | **str** | NAT Rule name. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 0 and 64. | [optional] 
**source** | [**NetworkNATAddress**](NetworkNATAddress.md) |  | [optional] 
**translated_destination** | [**NetworkNATAddress**](NetworkNATAddress.md) |  | [optional] 
**translated_destination_port** | **str** | setting TranslatedDestinationPort will rewrite destination port only single port rewrite is supported for single port match. | [optional] 
**translated_source** | [**NetworkNATAddress**](NetworkNATAddress.md) |  | [optional] 
**type** | **str** | NAT Type. | [optional]  if omitted the server will use the default value of "static"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


