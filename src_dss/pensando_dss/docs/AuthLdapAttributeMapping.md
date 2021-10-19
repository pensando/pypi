# AuthLdapAttributeMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The name of the attribute for storing the users’ e-mail address. This attribute is primarily used for linked Authentication Server Users. It can also be used to identify users by their e-mail address in certificate authentication. | [optional] 
**fullname** | **str** | The name that the server uses for the Name attribute. | [optional] 
**group** | **str** | The name that the server uses for the Group Member Attribute. By default, the attribute is set to member for standard schema, and sgMember for updated schema. | [optional] 
**group_object_class** | **str** | GroupObjectClass is the STRUCTURAL object class for group entry in LDAP. It is used as a filter for group search. | [optional] 
**tenant** | **str** | The tenant the server will use for authentication. | [optional] 
**user** | **str** | The name that the server uses for the UserID Attribute. | [optional] 
**user_object_class** | **str** | UserObjectClass is the STRUCTURAL object class for user entry in LDAP. It is used as a filter for user search. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


