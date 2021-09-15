# SecurityFirewallProfileSpec

FirewallProfileSpec - spec part of FirewallProfile object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_tracking** | **bool** | Enable/disable Connection Tracking. | [optional] 
**detect_app** | **bool** | Set the Application Identification Detection config for DSCs. | [optional]  if omitted the server will use the default value of False
**drop_timeout** | **str** | Drop Timeout is the period for which a drop entry is installed for a denied non tcp/udp/icmp flow. Should be a valid time duration between 1s and 5m0s. | [optional]  if omitted the server will use the default value of "60s"
**icmp_active_session_limit** | **int** | Icmp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]  if omitted the server will use the default value of 0
**icmp_drop_timeout** | **str** | ICMP Drop Timeout is the period for which a drop entry is installed for a denied ICMP flow. Should be a valid time duration between 1s and 5m0s. | [optional]  if omitted the server will use the default value of "60s"
**icmp_timeout** | **str** | Icmp Timeout is the period for which a ICMP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]  if omitted the server will use the default value of "6s"
**session_idle_timeout** | **str** | Session idle timeout removes/deletes the session/flow if there is inactivity; this value is superceded by any value specified in App object. Should be a valid time duration between 30s and 48h0m0s. | [optional]  if omitted the server will use the default value of "90s"
**tcp_close_timeout** | **str** | TCP Close Timeout is the time for which TCP session is kept after a FIN is seen. Should be a valid time duration between 1s and 5m0s. | [optional]  if omitted the server will use the default value of "15s"
**tcp_connection_setup_timeout** | **str** | TCP Connection Setup Timeout is the period TCP session is kept to see the response of a SYN. Should be a valid time duration between 1s and 1m0s. | [optional]  if omitted the server will use the default value of "30s"
**tcp_drop_timeout** | **str** | TCP Drop Timeout is the period for which a drop entry is installed for a denied TCP flow. Should be a valid time duration between 1s and 5m0s. | [optional]  if omitted the server will use the default value of "90s"
**tcp_half_closed_timeout** | **str** | TCP Half Closed Timeout is the time for which tCP session is kept when connection is half closed i.e. FIN sent by FIN_Ack not received. Should be a valid time duration between 1s and 48h0m0s. | [optional]  if omitted the server will use the default value of "120s"
**tcp_half_open_session_limit** | **int** | Tcp half open session limit config after which new open requests will be dropped. Value should be between 0 and 32768. | [optional]  if omitted the server will use the default value of 0
**tcp_timeout** | **str** | Tcp Timeout is the period for which a TCP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]  if omitted the server will use the default value of "3600s"
**udp_active_session_limit** | **int** | Udp active session limit config after which new requests will be dropped. Value should be between 0 and 32768. | [optional]  if omitted the server will use the default value of 0
**udp_drop_timeout** | **str** | UDP Drop Timeout is the period for which a drop entry is installed for a denied UDP flow. Should be a valid time duration between 1s and 48h0m0s. | [optional]  if omitted the server will use the default value of "60s"
**udp_timeout** | **str** | Udp Timeout is the period for which a UDP session is kept alive during inactivity. Should be a valid time duration between 1s and 48h0m0s. | [optional]  if omitted the server will use the default value of "30s"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


