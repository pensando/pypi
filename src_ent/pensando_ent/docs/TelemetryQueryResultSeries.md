# TelemetryQueryResultSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **[str]** | columns list all available fields in tsdb. | [optional] 
**name** | **str** | Name of the series. | [optional] 
**tags** | **{str: (str,)}** | Tags are the TSDB tags in the query response. | [optional] 
**values** | [**[ApiInterfaceSlice]**](ApiInterfaceSlice.md) | values contain field values received frpm tsdb, it is in the form of [][]interface{}. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


