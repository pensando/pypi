# DiagnosticsModuleStatus

ModuleStatus contains collected diagnostics of a process.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category specifies whether process is part of Venice(controller) or Naples(io) subsystem. | [optional]  if omitted the server will use the default value of "venice"
**last_restart_reason** | **str** | Arbitrary string, json, backtrace, etc. offering clues for restart. | [optional] 
**last_start** | **datetime** | Last start time. | [optional] 
**mac_address** | **str** | MACAddress of the smart nic on which this module runs. | [optional] 
**module** | **str** | Module is the name of the process/container. | [optional] 
**node** | **str** | Node on which this process is running. | [optional] 
**restart_count** | **int** | Number of times process got restarted. zero if never restarted. | [optional] 
**service** | **str** | Service is the name of the service/pod this process is part of. | [optional] 
**service_ports** | [**[DiagnosticsServicePort]**](DiagnosticsServicePort.md) | Ports on which this process is listening. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


