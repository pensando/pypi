# AuthUserSpec

spec part of user object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Should be a valid email address. | [optional] 
**fullname** | **str** |  | [optional] 
**password** | **str** | Password should contain atleast 1 digit, 1 uppercase letter and 1 special character from \&quot;~!@#$%^&amp;*()_+&#x60;-&#x3D;{}|[]\\\\:\\\&quot;&lt;&gt;?,./\&quot; Required password length by default is 9 characters. It is defined in AuthenticationPolicy. | [optional] 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "local"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


