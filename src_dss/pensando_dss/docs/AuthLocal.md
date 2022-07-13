# AuthLocal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_failed_login_attempts** | **int** | Failed login attempts after which user is locked. Value should be at least 3. | [optional]  if omitted the server will use the default value of 10
**failed_login_attempts_duration** | **str** | FailedLoginAttemptsDuration is time duration after number of failed login attempts are cleared for a user. Default is 15 min. Minimum value is 1 sec. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Should be a valid time duration of at least 1s. | [optional]  if omitted the server will use the default value of "15m"
**password_length** | **int** | Minimum password length. Value should be at least 3. | [optional]  if omitted the server will use the default value of 9

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


