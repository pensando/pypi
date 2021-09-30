# FwlogFwLogQuery

FwLogQuery allows selecting logs by all attributes All fields are ANDed together.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[str]** | OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present. | [optional] 
**batch_size** | **int** | BatchSize is the number of results returned in one batch while scrolling. | [optional]  if omitted the server will use the default value of 25
**count_only** | **bool** | if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta. | [optional] 
**destination_ips** | **[str]** | OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address. | [optional] 
**destination_ports** | **[int]** | OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535. | [optional] 
**encryption_status** | **str** | if set, search logs that match the specified encryption status. | [optional]  if omitted the server will use the default value of "all"
**end_time** | **datetime** | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional] 
**max_results** | **int** | MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192. | [optional]  if omitted the server will use the default value of 50
**protocols** | **[str]** | OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present. | [optional] 
**reporter_ids** | **[str]** | OR of reporter names to be matched. Only one reporter ID can be specified. | [optional] 
**scroll_action** | **str** | ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted. | [optional]  if omitted the server will use the default value of "none"
**scroll_expiry** | **str** | ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \&quot;300ms\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration. | [optional]  if omitted the server will use the default value of "5m"
**scroll_id** | **str** | ScrollID to scroll through results fetched by an earlier query. | [optional] 
**sort_order** | **str** | SortOrder specifies time ordering of results. | [optional]  if omitted the server will use the default value of "descending"
**source_ips** | **[str]** | OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address. | [optional] 
**source_ports** | **[int]** | OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535. | [optional] 
**start_time** | **datetime** | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional] 
**tenants** | **[str]** | OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


