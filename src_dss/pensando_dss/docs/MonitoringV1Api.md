# psm_dss.MonitoringV1Api

All URIs are relative to `https://PSM-IP/`

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert_destination**](MonitoringV1Api.md#add_alert_destination) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations | Create AlertDestination object
[**add_alert_destination1**](MonitoringV1Api.md#add_alert_destination1) | **POST** /configs/monitoring/v1/alertDestinations | Create AlertDestination object
[**add_alert_policy**](MonitoringV1Api.md#add_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies | Create AlertPolicy object
[**add_alert_policy1**](MonitoringV1Api.md#add_alert_policy1) | **POST** /configs/monitoring/v1/alertPolicies | Create AlertPolicy object
[**add_archive_request**](MonitoringV1Api.md#add_archive_request) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests | Create ArchiveRequest object
[**add_archive_request1**](MonitoringV1Api.md#add_archive_request1) | **POST** /configs/monitoring/v1/archive-requests | Create ArchiveRequest object
[**add_audit_policy**](MonitoringV1Api.md#add_audit_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Create AuditPolicy object
[**add_audit_policy1**](MonitoringV1Api.md#add_audit_policy1) | **POST** /configs/monitoring/v1/audit-policy | Create AuditPolicy object
[**add_event_policy**](MonitoringV1Api.md#add_event_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy | Create EventPolicy object
[**add_event_policy1**](MonitoringV1Api.md#add_event_policy1) | **POST** /configs/monitoring/v1/event-policy | Create EventPolicy object
[**add_flow_export_policy**](MonitoringV1Api.md#add_flow_export_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy | Create FlowExportPolicy object
[**add_flow_export_policy1**](MonitoringV1Api.md#add_flow_export_policy1) | **POST** /configs/monitoring/v1/flowExportPolicy | Create FlowExportPolicy object
[**add_fwlog_policy**](MonitoringV1Api.md#add_fwlog_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy | Create FwlogPolicy object
[**add_fwlog_policy1**](MonitoringV1Api.md#add_fwlog_policy1) | **POST** /configs/monitoring/v1/fwlogPolicy | Create FwlogPolicy object
[**add_mirror_session**](MonitoringV1Api.md#add_mirror_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession | Create MirrorSession object
[**add_mirror_session1**](MonitoringV1Api.md#add_mirror_session1) | **POST** /configs/monitoring/v1/MirrorSession | Create MirrorSession object
[**add_stats_alert_policy**](MonitoringV1Api.md#add_stats_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies | Create StatsAlertPolicy object
[**add_stats_alert_policy1**](MonitoringV1Api.md#add_stats_alert_policy1) | **POST** /configs/monitoring/v1/statsAlertPolicies | Create StatsAlertPolicy object
[**add_tech_support_request**](MonitoringV1Api.md#add_tech_support_request) | **POST** /configs/monitoring/v1/techsupport | Create TechSupportRequest object
[**add_troubleshooting_session**](MonitoringV1Api.md#add_troubleshooting_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession | Create TroubleshootingSession object
[**add_troubleshooting_session1**](MonitoringV1Api.md#add_troubleshooting_session1) | **POST** /configs/monitoring/v1/TroubleshootingSession | Create TroubleshootingSession object
[**cancel**](MonitoringV1Api.md#cancel) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name}/Cancel | 
[**cancel1**](MonitoringV1Api.md#cancel1) | **POST** /configs/monitoring/v1/archive-requests/{O.Name}/Cancel | 
[**delete_alert_destination**](MonitoringV1Api.md#delete_alert_destination) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Delete AlertDestination object
[**delete_alert_destination1**](MonitoringV1Api.md#delete_alert_destination1) | **DELETE** /configs/monitoring/v1/alertDestinations/{O.Name} | Delete AlertDestination object
[**delete_alert_policy**](MonitoringV1Api.md#delete_alert_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Delete AlertPolicy object
[**delete_alert_policy1**](MonitoringV1Api.md#delete_alert_policy1) | **DELETE** /configs/monitoring/v1/alertPolicies/{O.Name} | Delete AlertPolicy object
[**delete_archive_request**](MonitoringV1Api.md#delete_archive_request) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name} | Delete ArchiveRequest object
[**delete_archive_request1**](MonitoringV1Api.md#delete_archive_request1) | **DELETE** /configs/monitoring/v1/archive-requests/{O.Name} | Delete ArchiveRequest object
[**delete_audit_policy**](MonitoringV1Api.md#delete_audit_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Delete AuditPolicy object
[**delete_audit_policy1**](MonitoringV1Api.md#delete_audit_policy1) | **DELETE** /configs/monitoring/v1/audit-policy | Delete AuditPolicy object
[**delete_event_policy**](MonitoringV1Api.md#delete_event_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Delete EventPolicy object
[**delete_event_policy1**](MonitoringV1Api.md#delete_event_policy1) | **DELETE** /configs/monitoring/v1/event-policy/{O.Name} | Delete EventPolicy object
[**delete_flow_export_policy**](MonitoringV1Api.md#delete_flow_export_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Delete FlowExportPolicy object
[**delete_flow_export_policy1**](MonitoringV1Api.md#delete_flow_export_policy1) | **DELETE** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Delete FlowExportPolicy object
[**delete_fwlog_policy**](MonitoringV1Api.md#delete_fwlog_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Delete FwlogPolicy object
[**delete_fwlog_policy1**](MonitoringV1Api.md#delete_fwlog_policy1) | **DELETE** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Delete FwlogPolicy object
[**delete_mirror_session**](MonitoringV1Api.md#delete_mirror_session) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Delete MirrorSession object
[**delete_mirror_session1**](MonitoringV1Api.md#delete_mirror_session1) | **DELETE** /configs/monitoring/v1/MirrorSession/{O.Name} | Delete MirrorSession object
[**delete_stats_alert_policy**](MonitoringV1Api.md#delete_stats_alert_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Delete StatsAlertPolicy object
[**delete_stats_alert_policy1**](MonitoringV1Api.md#delete_stats_alert_policy1) | **DELETE** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Delete StatsAlertPolicy object
[**delete_tech_support_request**](MonitoringV1Api.md#delete_tech_support_request) | **DELETE** /configs/monitoring/v1/techsupport/{O.Name} | Delete TechSupportRequest object
[**delete_troubleshooting_session**](MonitoringV1Api.md#delete_troubleshooting_session) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Delete TroubleshootingSession object
[**delete_troubleshooting_session1**](MonitoringV1Api.md#delete_troubleshooting_session1) | **DELETE** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Delete TroubleshootingSession object
[**get_alert**](MonitoringV1Api.md#get_alert) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name} | Get Alert object
[**get_alert1**](MonitoringV1Api.md#get_alert1) | **GET** /configs/monitoring/v1/alerts/{O.Name} | Get Alert object
[**get_alert_destination**](MonitoringV1Api.md#get_alert_destination) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Get AlertDestination object
[**get_alert_destination1**](MonitoringV1Api.md#get_alert_destination1) | **GET** /configs/monitoring/v1/alertDestinations/{O.Name} | Get AlertDestination object
[**get_alert_policy**](MonitoringV1Api.md#get_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Get AlertPolicy object
[**get_alert_policy1**](MonitoringV1Api.md#get_alert_policy1) | **GET** /configs/monitoring/v1/alertPolicies/{O.Name} | Get AlertPolicy object
[**get_archive_request**](MonitoringV1Api.md#get_archive_request) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name} | Get ArchiveRequest object
[**get_archive_request1**](MonitoringV1Api.md#get_archive_request1) | **GET** /configs/monitoring/v1/archive-requests/{O.Name} | Get ArchiveRequest object
[**get_audit_policy**](MonitoringV1Api.md#get_audit_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Get AuditPolicy object
[**get_audit_policy1**](MonitoringV1Api.md#get_audit_policy1) | **GET** /configs/monitoring/v1/audit-policy | Get AuditPolicy object
[**get_event_policy**](MonitoringV1Api.md#get_event_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Get EventPolicy object
[**get_event_policy1**](MonitoringV1Api.md#get_event_policy1) | **GET** /configs/monitoring/v1/event-policy/{O.Name} | Get EventPolicy object
[**get_flow_export_policy**](MonitoringV1Api.md#get_flow_export_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Get FlowExportPolicy object
[**get_flow_export_policy1**](MonitoringV1Api.md#get_flow_export_policy1) | **GET** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Get FlowExportPolicy object
[**get_fwlog_policy**](MonitoringV1Api.md#get_fwlog_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Get FwlogPolicy object
[**get_fwlog_policy1**](MonitoringV1Api.md#get_fwlog_policy1) | **GET** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Get FwlogPolicy object
[**get_mirror_session**](MonitoringV1Api.md#get_mirror_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Get MirrorSession object
[**get_mirror_session1**](MonitoringV1Api.md#get_mirror_session1) | **GET** /configs/monitoring/v1/MirrorSession/{O.Name} | Get MirrorSession object
[**get_stats_alert_policy**](MonitoringV1Api.md#get_stats_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Get StatsAlertPolicy object
[**get_stats_alert_policy1**](MonitoringV1Api.md#get_stats_alert_policy1) | **GET** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Get StatsAlertPolicy object
[**get_tech_support_request**](MonitoringV1Api.md#get_tech_support_request) | **GET** /configs/monitoring/v1/techsupport/{O.Name} | Get TechSupportRequest object
[**get_troubleshooting_session**](MonitoringV1Api.md#get_troubleshooting_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Get TroubleshootingSession object
[**get_troubleshooting_session1**](MonitoringV1Api.md#get_troubleshooting_session1) | **GET** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Get TroubleshootingSession object
[**label_alert**](MonitoringV1Api.md#label_alert) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name}/label | Label Alert object
[**label_alert1**](MonitoringV1Api.md#label_alert1) | **POST** /configs/monitoring/v1/alerts/{O.Name}/label | Label Alert object
[**label_alert_destination**](MonitoringV1Api.md#label_alert_destination) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name}/label | Label AlertDestination object
[**label_alert_destination1**](MonitoringV1Api.md#label_alert_destination1) | **POST** /configs/monitoring/v1/alertDestinations/{O.Name}/label | Label AlertDestination object
[**label_alert_policy**](MonitoringV1Api.md#label_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name}/label | Label AlertPolicy object
[**label_alert_policy1**](MonitoringV1Api.md#label_alert_policy1) | **POST** /configs/monitoring/v1/alertPolicies/{O.Name}/label | Label AlertPolicy object
[**label_event_policy**](MonitoringV1Api.md#label_event_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name}/label | Label EventPolicy object
[**label_event_policy1**](MonitoringV1Api.md#label_event_policy1) | **POST** /configs/monitoring/v1/event-policy/{O.Name}/label | Label EventPolicy object
[**label_flow_export_policy**](MonitoringV1Api.md#label_flow_export_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name}/label | Label FlowExportPolicy object
[**label_flow_export_policy1**](MonitoringV1Api.md#label_flow_export_policy1) | **POST** /configs/monitoring/v1/flowExportPolicy/{O.Name}/label | Label FlowExportPolicy object
[**label_fwlog_policy**](MonitoringV1Api.md#label_fwlog_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name}/label | Label FwlogPolicy object
[**label_fwlog_policy1**](MonitoringV1Api.md#label_fwlog_policy1) | **POST** /configs/monitoring/v1/fwlogPolicy/{O.Name}/label | Label FwlogPolicy object
[**label_mirror_session**](MonitoringV1Api.md#label_mirror_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name}/label | Label MirrorSession object
[**label_mirror_session1**](MonitoringV1Api.md#label_mirror_session1) | **POST** /configs/monitoring/v1/MirrorSession/{O.Name}/label | Label MirrorSession object
[**label_stats_alert_policy**](MonitoringV1Api.md#label_stats_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name}/label | Label StatsAlertPolicy object
[**label_stats_alert_policy1**](MonitoringV1Api.md#label_stats_alert_policy1) | **POST** /configs/monitoring/v1/statsAlertPolicies/{O.Name}/label | Label StatsAlertPolicy object
[**label_troubleshooting_session**](MonitoringV1Api.md#label_troubleshooting_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name}/label | Label TroubleshootingSession object
[**label_troubleshooting_session1**](MonitoringV1Api.md#label_troubleshooting_session1) | **POST** /configs/monitoring/v1/TroubleshootingSession/{O.Name}/label | Label TroubleshootingSession object
[**list_alert**](MonitoringV1Api.md#list_alert) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alerts | List Alert objects
[**list_alert1**](MonitoringV1Api.md#list_alert1) | **GET** /configs/monitoring/v1/alerts | List Alert objects
[**list_alert_destination**](MonitoringV1Api.md#list_alert_destination) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations | List AlertDestination objects
[**list_alert_destination1**](MonitoringV1Api.md#list_alert_destination1) | **GET** /configs/monitoring/v1/alertDestinations | List AlertDestination objects
[**list_alert_policy**](MonitoringV1Api.md#list_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies | List AlertPolicy objects
[**list_alert_policy1**](MonitoringV1Api.md#list_alert_policy1) | **GET** /configs/monitoring/v1/alertPolicies | List AlertPolicy objects
[**list_archive_request**](MonitoringV1Api.md#list_archive_request) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests | List ArchiveRequest objects
[**list_archive_request1**](MonitoringV1Api.md#list_archive_request1) | **GET** /configs/monitoring/v1/archive-requests | List ArchiveRequest objects
[**list_event_policy**](MonitoringV1Api.md#list_event_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy | List EventPolicy objects
[**list_event_policy1**](MonitoringV1Api.md#list_event_policy1) | **GET** /configs/monitoring/v1/event-policy | List EventPolicy objects
[**list_flow_export_policy**](MonitoringV1Api.md#list_flow_export_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy | List FlowExportPolicy objects
[**list_flow_export_policy1**](MonitoringV1Api.md#list_flow_export_policy1) | **GET** /configs/monitoring/v1/flowExportPolicy | List FlowExportPolicy objects
[**list_fwlog_policy**](MonitoringV1Api.md#list_fwlog_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy | List FwlogPolicy objects
[**list_fwlog_policy1**](MonitoringV1Api.md#list_fwlog_policy1) | **GET** /configs/monitoring/v1/fwlogPolicy | List FwlogPolicy objects
[**list_mirror_session**](MonitoringV1Api.md#list_mirror_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession | List MirrorSession objects
[**list_mirror_session1**](MonitoringV1Api.md#list_mirror_session1) | **GET** /configs/monitoring/v1/MirrorSession | List MirrorSession objects
[**list_stats_alert_policy**](MonitoringV1Api.md#list_stats_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies | List StatsAlertPolicy objects
[**list_stats_alert_policy1**](MonitoringV1Api.md#list_stats_alert_policy1) | **GET** /configs/monitoring/v1/statsAlertPolicies | List StatsAlertPolicy objects
[**list_tech_support_request**](MonitoringV1Api.md#list_tech_support_request) | **GET** /configs/monitoring/v1/techsupport | List TechSupportRequest objects
[**list_troubleshooting_session**](MonitoringV1Api.md#list_troubleshooting_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession | List TroubleshootingSession objects
[**list_troubleshooting_session1**](MonitoringV1Api.md#list_troubleshooting_session1) | **GET** /configs/monitoring/v1/TroubleshootingSession | List TroubleshootingSession objects
[**update_alert**](MonitoringV1Api.md#update_alert) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name} | Update Alert object
[**update_alert1**](MonitoringV1Api.md#update_alert1) | **PUT** /configs/monitoring/v1/alerts/{O.Name} | Update Alert object
[**update_alert_destination**](MonitoringV1Api.md#update_alert_destination) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Update AlertDestination object
[**update_alert_destination1**](MonitoringV1Api.md#update_alert_destination1) | **PUT** /configs/monitoring/v1/alertDestinations/{O.Name} | Update AlertDestination object
[**update_alert_policy**](MonitoringV1Api.md#update_alert_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Update AlertPolicy object
[**update_alert_policy1**](MonitoringV1Api.md#update_alert_policy1) | **PUT** /configs/monitoring/v1/alertPolicies/{O.Name} | Update AlertPolicy object
[**update_audit_policy**](MonitoringV1Api.md#update_audit_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Update AuditPolicy object
[**update_audit_policy1**](MonitoringV1Api.md#update_audit_policy1) | **PUT** /configs/monitoring/v1/audit-policy | Update AuditPolicy object
[**update_event_policy**](MonitoringV1Api.md#update_event_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Update EventPolicy object
[**update_event_policy1**](MonitoringV1Api.md#update_event_policy1) | **PUT** /configs/monitoring/v1/event-policy/{O.Name} | Update EventPolicy object
[**update_flow_export_policy**](MonitoringV1Api.md#update_flow_export_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Update FlowExportPolicy object
[**update_flow_export_policy1**](MonitoringV1Api.md#update_flow_export_policy1) | **PUT** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Update FlowExportPolicy object
[**update_fwlog_policy**](MonitoringV1Api.md#update_fwlog_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Update FwlogPolicy object
[**update_fwlog_policy1**](MonitoringV1Api.md#update_fwlog_policy1) | **PUT** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Update FwlogPolicy object
[**update_mirror_session**](MonitoringV1Api.md#update_mirror_session) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Update MirrorSession object
[**update_mirror_session1**](MonitoringV1Api.md#update_mirror_session1) | **PUT** /configs/monitoring/v1/MirrorSession/{O.Name} | Update MirrorSession object
[**update_stats_alert_policy**](MonitoringV1Api.md#update_stats_alert_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Update StatsAlertPolicy object
[**update_stats_alert_policy1**](MonitoringV1Api.md#update_stats_alert_policy1) | **PUT** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Update StatsAlertPolicy object
[**update_troubleshooting_session**](MonitoringV1Api.md#update_troubleshooting_session) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Update TroubleshootingSession object
[**update_troubleshooting_session1**](MonitoringV1Api.md#update_troubleshooting_session1) | **PUT** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Update TroubleshootingSession object
[**watch_alert**](MonitoringV1Api.md#watch_alert) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alerts | Watch Alert objects. Supports WebSockets or HTTP long poll
[**watch_alert1**](MonitoringV1Api.md#watch_alert1) | **GET** /configs/monitoring/v1/watch/alerts | Watch Alert objects. Supports WebSockets or HTTP long poll
[**watch_alert_destination**](MonitoringV1Api.md#watch_alert_destination) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alertDestinations | Watch AlertDestination objects. Supports WebSockets or HTTP long poll
[**watch_alert_destination1**](MonitoringV1Api.md#watch_alert_destination1) | **GET** /configs/monitoring/v1/watch/alertDestinations | Watch AlertDestination objects. Supports WebSockets or HTTP long poll
[**watch_alert_policy**](MonitoringV1Api.md#watch_alert_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alertPolicies | Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_alert_policy1**](MonitoringV1Api.md#watch_alert_policy1) | **GET** /configs/monitoring/v1/watch/alertPolicies | Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_archive_request**](MonitoringV1Api.md#watch_archive_request) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/archive-requests | Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
[**watch_archive_request1**](MonitoringV1Api.md#watch_archive_request1) | **GET** /configs/monitoring/v1/watch/archive-requests | Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
[**watch_audit_policy**](MonitoringV1Api.md#watch_audit_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/audit-policy | Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
[**watch_audit_policy1**](MonitoringV1Api.md#watch_audit_policy1) | **GET** /configs/monitoring/v1/watch/audit-policy | Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
[**watch_event_policy**](MonitoringV1Api.md#watch_event_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/event-policy | Watch EventPolicy objects. Supports WebSockets or HTTP long poll
[**watch_event_policy1**](MonitoringV1Api.md#watch_event_policy1) | **GET** /configs/monitoring/v1/watch/event-policy | Watch EventPolicy objects. Supports WebSockets or HTTP long poll
[**watch_flow_export_policy**](MonitoringV1Api.md#watch_flow_export_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/flowExportPolicy | Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
[**watch_flow_export_policy1**](MonitoringV1Api.md#watch_flow_export_policy1) | **GET** /configs/monitoring/v1/watch/flowExportPolicy | Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
[**watch_fwlog_policy**](MonitoringV1Api.md#watch_fwlog_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/fwlogPolicy | Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
[**watch_fwlog_policy1**](MonitoringV1Api.md#watch_fwlog_policy1) | **GET** /configs/monitoring/v1/watch/fwlogPolicy | Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
[**watch_mirror_session**](MonitoringV1Api.md#watch_mirror_session) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/MirrorSession | Watch MirrorSession objects. Supports WebSockets or HTTP long poll
[**watch_mirror_session1**](MonitoringV1Api.md#watch_mirror_session1) | **GET** /configs/monitoring/v1/watch/MirrorSession | Watch MirrorSession objects. Supports WebSockets or HTTP long poll
[**watch_stats_alert_policy**](MonitoringV1Api.md#watch_stats_alert_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/statsAlertPolicies | Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_stats_alert_policy1**](MonitoringV1Api.md#watch_stats_alert_policy1) | **GET** /configs/monitoring/v1/watch/statsAlertPolicies | Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_tech_support_request**](MonitoringV1Api.md#watch_tech_support_request) | **GET** /configs/monitoring/v1/watch/techsupport | Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll


# **add_alert_destination**
> MonitoringAlertDestination add_alert_destination(o_tenant, body)

Create AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertDestination object
        api_response = api_instance.add_alert_destination(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_alert_destination1**
> MonitoringAlertDestination add_alert_destination1(body)

Create AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertDestination object
        api_response = api_instance.add_alert_destination1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_alert_policy**
> MonitoringAlertPolicy add_alert_policy(o_tenant, body)

Create AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertPolicy object
        api_response = api_instance.add_alert_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_alert_policy1**
> MonitoringAlertPolicy add_alert_policy1(body)

Create AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertPolicy object
        api_response = api_instance.add_alert_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_archive_request**
> MonitoringArchiveRequest add_archive_request(o_tenant, body)

Create ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringArchiveRequestSpec(
            query=MonitoringArchiveQuery(
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields=FieldsSelector(
                    requirements=[
                        FieldsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[],
                        ),
                    ],
                ),
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                tenants=[
                    "tenants_example",
                ],
                texts=[
                    SearchTextRequirement(
                        text=[
                            "text_example",
                        ],
                    ),
                ],
            ),
            type="event",
        ),
        status=MonitoringArchiveRequestStatus(
            reason="reason_example",
            status="scheduled",
            uri="uri_example",
        ),
    ) # MonitoringArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create ArchiveRequest object
        api_response = api_instance.add_archive_request(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_archive_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_archive_request1**
> MonitoringArchiveRequest add_archive_request1(body)

Create ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringArchiveRequestSpec(
            query=MonitoringArchiveQuery(
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields=FieldsSelector(
                    requirements=[
                        FieldsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[],
                        ),
                    ],
                ),
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                tenants=[
                    "tenants_example",
                ],
                texts=[
                    SearchTextRequirement(
                        text=[
                            "text_example",
                        ],
                    ),
                ],
            ),
            type="event",
        ),
        status=MonitoringArchiveRequestStatus(
            reason="reason_example",
            status="scheduled",
            uri="uri_example",
        ),
    ) # MonitoringArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create ArchiveRequest object
        api_response = api_instance.add_archive_request1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_archive_request1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_audit_policy**
> MonitoringAuditPolicy add_audit_policy(o_tenant, body)

Create AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AuditPolicy object
        api_response = api_instance.add_audit_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_audit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_audit_policy1**
> MonitoringAuditPolicy add_audit_policy1(body)

Create AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AuditPolicy object
        api_response = api_instance.add_audit_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_audit_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_event_policy**
> MonitoringEventPolicy add_event_policy(o_tenant, body)

Create EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create EventPolicy object
        api_response = api_instance.add_event_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_event_policy1**
> MonitoringEventPolicy add_event_policy1(body)

Create EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create EventPolicy object
        api_response = api_instance.add_event_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_flow_export_policy**
> MonitoringFlowExportPolicy add_flow_export_policy(o_tenant, body)

Create FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
            vrf_name="vrf_name_example",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FlowExportPolicy object
        api_response = api_instance.add_flow_export_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_flow_export_policy1**
> MonitoringFlowExportPolicy add_flow_export_policy1(body)

Create FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
            vrf_name="vrf_name_example",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FlowExportPolicy object
        api_response = api_instance.add_flow_export_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_fwlog_policy**
> MonitoringFwlogPolicy add_fwlog_policy(o_tenant, body)

Create FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FwlogPolicy object
        api_response = api_instance.add_fwlog_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_fwlog_policy1**
> MonitoringFwlogPolicy add_fwlog_policy1(body)

Create FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FwlogPolicy object
        api_response = api_instance.add_fwlog_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_mirror_session**
> MonitoringMirrorSession add_mirror_session(o_tenant, body)

Create MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create MirrorSession object
        api_response = api_instance.add_mirror_session(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_mirror_session1**
> MonitoringMirrorSession add_mirror_session1(body)

Create MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create MirrorSession object
        api_response = api_instance.add_mirror_session1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_stats_alert_policy**
> MonitoringStatsAlertPolicy add_stats_alert_policy(o_tenant, body)

Create StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create StatsAlertPolicy object
        api_response = api_instance.add_stats_alert_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_stats_alert_policy1**
> MonitoringStatsAlertPolicy add_stats_alert_policy1(body)

Create StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create StatsAlertPolicy object
        api_response = api_instance.add_stats_alert_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_tech_support_request**
> MonitoringTechSupportRequest add_tech_support_request(body)

Create TechSupportRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringTechSupportRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTechSupportRequestSpec(
            collection_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            node_selector=TechSupportRequestSpecNodeSelectorSpec(
                labels=LabelsSelector(
                    requirements=[],
                ),
                names=[
                    "names_example",
                ],
            ),
            skip_cores=False,
            verbosity=1,
        ),
        status=MonitoringTechSupportRequestStatus(
            ctrlr_node_results={
                "key": MonitoringTechSupportNodeResult(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    status="scheduled",
                    uri="uri_example",
                ),
            },
            dsc_results={
                "key": MonitoringTechSupportNodeResult(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    status="scheduled",
                    uri="uri_example",
                ),
            },
            instance_id="instance_id_example",
            reason="reason_example",
            status="scheduled",
        ),
    ) # MonitoringTechSupportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create TechSupportRequest object
        api_response = api_instance.add_tech_support_request(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_tech_support_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)|  |

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_troubleshooting_session**
> MonitoringTroubleshootingSession add_troubleshooting_session(o_tenant, body)

Create TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create TroubleshootingSession object
        api_response = api_instance.add_troubleshooting_session(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **add_troubleshooting_session1**
> MonitoringTroubleshootingSession add_troubleshooting_session1(body)

Create TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create TroubleshootingSession object
        api_response = api_instance.add_troubleshooting_session1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->add_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **cancel**
> MonitoringArchiveRequest cancel(o_tenant, o_name, body)



### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_cancel_archive_request import MonitoringCancelArchiveRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringCancelArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # MonitoringCancelArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
                api_response = api_instance.cancel(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringCancelArchiveRequest**](MonitoringCancelArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **cancel1**
> MonitoringArchiveRequest cancel1(o_name, body)



### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_cancel_archive_request import MonitoringCancelArchiveRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringCancelArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # MonitoringCancelArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
                api_response = api_instance.cancel1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->cancel1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringCancelArchiveRequest**](MonitoringCancelArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_alert_destination**
> MonitoringAlertDestination delete_alert_destination(o_tenant, o_name)

Delete AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertDestination object
        api_response = api_instance.delete_alert_destination(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_alert_destination1**
> MonitoringAlertDestination delete_alert_destination1(o_name)

Delete AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertDestination object
        api_response = api_instance.delete_alert_destination1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_alert_policy**
> MonitoringAlertPolicy delete_alert_policy(o_tenant, o_name)

Delete AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertPolicy object
        api_response = api_instance.delete_alert_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_alert_policy1**
> MonitoringAlertPolicy delete_alert_policy1(o_name)

Delete AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertPolicy object
        api_response = api_instance.delete_alert_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_archive_request**
> MonitoringArchiveRequest delete_archive_request(o_tenant, o_name)

Delete ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete ArchiveRequest object
        api_response = api_instance.delete_archive_request(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_archive_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_archive_request1**
> MonitoringArchiveRequest delete_archive_request1(o_name)

Delete ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete ArchiveRequest object
        api_response = api_instance.delete_archive_request1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_archive_request1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_audit_policy**
> MonitoringAuditPolicy delete_audit_policy(o_tenant)

Delete AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AuditPolicy object
        api_response = api_instance.delete_audit_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_audit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_audit_policy1**
> MonitoringAuditPolicy delete_audit_policy1()

Delete AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete AuditPolicy object
        api_response = api_instance.delete_audit_policy1()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_audit_policy1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_event_policy**
> MonitoringEventPolicy delete_event_policy(o_tenant, o_name)

Delete EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete EventPolicy object
        api_response = api_instance.delete_event_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_event_policy1**
> MonitoringEventPolicy delete_event_policy1(o_name)

Delete EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete EventPolicy object
        api_response = api_instance.delete_event_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_flow_export_policy**
> MonitoringFlowExportPolicy delete_flow_export_policy(o_tenant, o_name)

Delete FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FlowExportPolicy object
        api_response = api_instance.delete_flow_export_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_flow_export_policy1**
> MonitoringFlowExportPolicy delete_flow_export_policy1(o_name)

Delete FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FlowExportPolicy object
        api_response = api_instance.delete_flow_export_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_fwlog_policy**
> MonitoringFwlogPolicy delete_fwlog_policy(o_tenant, o_name)

Delete FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FwlogPolicy object
        api_response = api_instance.delete_fwlog_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_fwlog_policy1**
> MonitoringFwlogPolicy delete_fwlog_policy1(o_name)

Delete FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FwlogPolicy object
        api_response = api_instance.delete_fwlog_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_mirror_session**
> MonitoringMirrorSession delete_mirror_session(o_tenant, o_name)

Delete MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete MirrorSession object
        api_response = api_instance.delete_mirror_session(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_mirror_session1**
> MonitoringMirrorSession delete_mirror_session1(o_name)

Delete MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete MirrorSession object
        api_response = api_instance.delete_mirror_session1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_stats_alert_policy**
> MonitoringStatsAlertPolicy delete_stats_alert_policy(o_tenant, o_name)

Delete StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete StatsAlertPolicy object
        api_response = api_instance.delete_stats_alert_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_stats_alert_policy1**
> MonitoringStatsAlertPolicy delete_stats_alert_policy1(o_name)

Delete StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete StatsAlertPolicy object
        api_response = api_instance.delete_stats_alert_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_tech_support_request**
> MonitoringTechSupportRequest delete_tech_support_request(o_name)

Delete TechSupportRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TechSupportRequest object
        api_response = api_instance.delete_tech_support_request(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_tech_support_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_troubleshooting_session**
> MonitoringTroubleshootingSession delete_troubleshooting_session(o_tenant, o_name)

Delete TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TroubleshootingSession object
        api_response = api_instance.delete_troubleshooting_session(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **delete_troubleshooting_session1**
> MonitoringTroubleshootingSession delete_troubleshooting_session1(o_name)

Delete TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TroubleshootingSession object
        api_response = api_instance.delete_troubleshooting_session1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert**
> MonitoringAlert get_alert(o_tenant, o_name)

Get Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_state = "spec.state_example" # str |  (optional)
    status_severity = "status.severity_example" # str | Severity of an alert. (optional)
    source_component = "source.component_example" # str |  (optional)
    source_node_name = "source.node-name_example" # str |  (optional)
    status_event_uri = "status.event-uri_example" # str | Event that triggered the alert. (optional)
    object_ref_tenant = "object-ref.tenant_example" # str | Tenant of the object. (optional)
    object_ref_namespace = "object-ref.namespace_example" # str | Namespace of the object, for scoped objects. (optional)
    object_ref_kind = "object-ref.kind_example" # str | Kind represents the type of the API object. (optional)
    object_ref_name = "object-ref.name_example" # str | Name of the object, unique within a Namespace for scoped objects. (optional)
    object_ref_uri = "object-ref.uri_example" # str | URI is a link to accessing the referenced object. (optional)
    status_message = "status.message_example" # str | Message from the alert rule that triggered the alert. (optional)
    reason_alert_policy_id = "reason.alert-policy-id_example" # str | Alert Policy ID that matched. (optional)
    acknowledged_user = "acknowledged.user_example" # str | Name of the user performed some action. (optional)
    acknowledged_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Time at which the action was performed. (optional)
    resolved_user = "resolved.user_example" # str | Name of the user performed some action. (optional)
    resolved_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Time at which the action was performed. (optional)
    status_total_hits = 1 # int | TotalHits on this alert, If there is an exisiting alert for the condition, we do not re-create the alert instead we update this counter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Alert object
        api_response = api_instance.get_alert(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Alert object
        api_response = api_instance.get_alert(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_state=spec_state, status_severity=status_severity, source_component=source_component, source_node_name=source_node_name, status_event_uri=status_event_uri, object_ref_tenant=object_ref_tenant, object_ref_namespace=object_ref_namespace, object_ref_kind=object_ref_kind, object_ref_name=object_ref_name, object_ref_uri=object_ref_uri, status_message=status_message, reason_alert_policy_id=reason_alert_policy_id, acknowledged_user=acknowledged_user, acknowledged_time=acknowledged_time, resolved_user=resolved_user, resolved_time=resolved_time, status_total_hits=status_total_hits)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_state** | **str**|  | [optional]
 **status_severity** | **str**| Severity of an alert. | [optional]
 **source_component** | **str**|  | [optional]
 **source_node_name** | **str**|  | [optional]
 **status_event_uri** | **str**| Event that triggered the alert. | [optional]
 **object_ref_tenant** | **str**| Tenant of the object. | [optional]
 **object_ref_namespace** | **str**| Namespace of the object, for scoped objects. | [optional]
 **object_ref_kind** | **str**| Kind represents the type of the API object. | [optional]
 **object_ref_name** | **str**| Name of the object, unique within a Namespace for scoped objects. | [optional]
 **object_ref_uri** | **str**| URI is a link to accessing the referenced object. | [optional]
 **status_message** | **str**| Message from the alert rule that triggered the alert. | [optional]
 **reason_alert_policy_id** | **str**| Alert Policy ID that matched. | [optional]
 **acknowledged_user** | **str**| Name of the user performed some action. | [optional]
 **acknowledged_time** | **datetime**| Time at which the action was performed. | [optional]
 **resolved_user** | **str**| Name of the user performed some action. | [optional]
 **resolved_time** | **datetime**| Time at which the action was performed. | [optional]
 **status_total_hits** | **int**| TotalHits on this alert, If there is an exisiting alert for the condition, we do not re-create the alert instead we update this counter. | [optional]

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert1**
> MonitoringAlert get_alert1(o_name)

Get Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_state = "spec.state_example" # str |  (optional)
    status_severity = "status.severity_example" # str | Severity of an alert. (optional)
    source_component = "source.component_example" # str |  (optional)
    source_node_name = "source.node-name_example" # str |  (optional)
    status_event_uri = "status.event-uri_example" # str | Event that triggered the alert. (optional)
    object_ref_tenant = "object-ref.tenant_example" # str | Tenant of the object. (optional)
    object_ref_namespace = "object-ref.namespace_example" # str | Namespace of the object, for scoped objects. (optional)
    object_ref_kind = "object-ref.kind_example" # str | Kind represents the type of the API object. (optional)
    object_ref_name = "object-ref.name_example" # str | Name of the object, unique within a Namespace for scoped objects. (optional)
    object_ref_uri = "object-ref.uri_example" # str | URI is a link to accessing the referenced object. (optional)
    status_message = "status.message_example" # str | Message from the alert rule that triggered the alert. (optional)
    reason_alert_policy_id = "reason.alert-policy-id_example" # str | Alert Policy ID that matched. (optional)
    acknowledged_user = "acknowledged.user_example" # str | Name of the user performed some action. (optional)
    acknowledged_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Time at which the action was performed. (optional)
    resolved_user = "resolved.user_example" # str | Name of the user performed some action. (optional)
    resolved_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Time at which the action was performed. (optional)
    status_total_hits = 1 # int | TotalHits on this alert, If there is an exisiting alert for the condition, we do not re-create the alert instead we update this counter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Alert object
        api_response = api_instance.get_alert1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Alert object
        api_response = api_instance.get_alert1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_state=spec_state, status_severity=status_severity, source_component=source_component, source_node_name=source_node_name, status_event_uri=status_event_uri, object_ref_tenant=object_ref_tenant, object_ref_namespace=object_ref_namespace, object_ref_kind=object_ref_kind, object_ref_name=object_ref_name, object_ref_uri=object_ref_uri, status_message=status_message, reason_alert_policy_id=reason_alert_policy_id, acknowledged_user=acknowledged_user, acknowledged_time=acknowledged_time, resolved_user=resolved_user, resolved_time=resolved_time, status_total_hits=status_total_hits)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_state** | **str**|  | [optional]
 **status_severity** | **str**| Severity of an alert. | [optional]
 **source_component** | **str**|  | [optional]
 **source_node_name** | **str**|  | [optional]
 **status_event_uri** | **str**| Event that triggered the alert. | [optional]
 **object_ref_tenant** | **str**| Tenant of the object. | [optional]
 **object_ref_namespace** | **str**| Namespace of the object, for scoped objects. | [optional]
 **object_ref_kind** | **str**| Kind represents the type of the API object. | [optional]
 **object_ref_name** | **str**| Name of the object, unique within a Namespace for scoped objects. | [optional]
 **object_ref_uri** | **str**| URI is a link to accessing the referenced object. | [optional]
 **status_message** | **str**| Message from the alert rule that triggered the alert. | [optional]
 **reason_alert_policy_id** | **str**| Alert Policy ID that matched. | [optional]
 **acknowledged_user** | **str**| Name of the user performed some action. | [optional]
 **acknowledged_time** | **datetime**| Time at which the action was performed. | [optional]
 **resolved_user** | **str**| Name of the user performed some action. | [optional]
 **resolved_time** | **datetime**| Time at which the action was performed. | [optional]
 **status_total_hits** | **int**| TotalHits on this alert, If there is an exisiting alert for the condition, we do not re-create the alert instead we update this counter. | [optional]

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert_destination**
> MonitoringAlertDestination get_alert_destination(o_tenant, o_name)

Get AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    email_export_email_list = [
        "email-export.email-list_example",
    ] # [str] | TODO:  format, config, SMTP config. (optional)
    syslog_export_format = "syslog-export.format_example" # str | event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)
    status_total_notifications_sent = 1 # int | total number of notifications sent using this notification mechanism. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, email_export_email_list=email_export_email_list, syslog_export_format=syslog_export_format, config_facility_override=config_facility_override, config_prefix=config_prefix, status_total_notifications_sent=status_total_notifications_sent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **email_export_email_list** | **[str]**| TODO:  format, config, SMTP config. | [optional]
 **syslog_export_format** | **str**| event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]
 **status_total_notifications_sent** | **int**| total number of notifications sent using this notification mechanism. | [optional]

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert_destination1**
> MonitoringAlertDestination get_alert_destination1(o_name)

Get AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    email_export_email_list = [
        "email-export.email-list_example",
    ] # [str] | TODO:  format, config, SMTP config. (optional)
    syslog_export_format = "syslog-export.format_example" # str | event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)
    status_total_notifications_sent = 1 # int | total number of notifications sent using this notification mechanism. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, email_export_email_list=email_export_email_list, syslog_export_format=syslog_export_format, config_facility_override=config_facility_override, config_prefix=config_prefix, status_total_notifications_sent=status_total_notifications_sent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **email_export_email_list** | **[str]**| TODO:  format, config, SMTP config. | [optional]
 **syslog_export_format** | **str**| event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]
 **status_total_notifications_sent** | **int**| total number of notifications sent using this notification mechanism. | [optional]

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert_policy**
> MonitoringAlertPolicy get_alert_policy(o_tenant, o_name)

Get AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_resource = "spec.resource_example" # str | Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. (optional)
    spec_severity = "spec.severity_example" # str | Severity to be set for an alert that gets triggered from this rule. (optional)
    spec_message = "spec.message_example" # str | Message to be used while generating the alert. (optional)
    spec_enable = True # bool | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)
    status_total_hits = 1 # int | Total hits on this policy. (optional)
    status_open_alerts = 1 # int | Open alerts based on this policy. (optional)
    status_acknowledged_alerts = 1 # int | Acknowledged alerts based on this policy. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_resource=spec_resource, spec_severity=spec_severity, spec_message=spec_message, spec_enable=spec_enable, spec_destinations=spec_destinations, status_total_hits=status_total_hits, status_open_alerts=status_open_alerts, status_acknowledged_alerts=status_acknowledged_alerts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_resource** | **str**| Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. | [optional]
 **spec_severity** | **str**| Severity to be set for an alert that gets triggered from this rule. | [optional]
 **spec_message** | **str**| Message to be used while generating the alert. | [optional]
 **spec_enable** | **bool**| User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]
 **status_total_hits** | **int**| Total hits on this policy. | [optional]
 **status_open_alerts** | **int**| Open alerts based on this policy. | [optional]
 **status_acknowledged_alerts** | **int**| Acknowledged alerts based on this policy. | [optional]

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_alert_policy1**
> MonitoringAlertPolicy get_alert_policy1(o_name)

Get AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_resource = "spec.resource_example" # str | Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. (optional)
    spec_severity = "spec.severity_example" # str | Severity to be set for an alert that gets triggered from this rule. (optional)
    spec_message = "spec.message_example" # str | Message to be used while generating the alert. (optional)
    spec_enable = True # bool | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)
    status_total_hits = 1 # int | Total hits on this policy. (optional)
    status_open_alerts = 1 # int | Open alerts based on this policy. (optional)
    status_acknowledged_alerts = 1 # int | Acknowledged alerts based on this policy. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_resource=spec_resource, spec_severity=spec_severity, spec_message=spec_message, spec_enable=spec_enable, spec_destinations=spec_destinations, status_total_hits=status_total_hits, status_open_alerts=status_open_alerts, status_acknowledged_alerts=status_acknowledged_alerts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_resource** | **str**| Resource type - target resource to run this policy. e.g. Network, Endpoint - object based alert policy Event - event based alert policy EndpointMetrics - metric based alert policy based on the resource type, the policy gets interpreted. | [optional]
 **spec_severity** | **str**| Severity to be set for an alert that gets triggered from this rule. | [optional]
 **spec_message** | **str**| Message to be used while generating the alert. | [optional]
 **spec_enable** | **bool**| User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]
 **status_total_hits** | **int**| Total hits on this policy. | [optional]
 **status_open_alerts** | **int**| Open alerts based on this policy. | [optional]
 **status_acknowledged_alerts** | **int**| Acknowledged alerts based on this policy. | [optional]

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_archive_request**
> MonitoringArchiveRequest get_archive_request(o_tenant, o_name)

Get ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    query_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    query_end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. (optional)
    query_tenants = [
        "query.tenants_example",
    ] # [str] | OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. (optional)
    status_status = "status.status_example" # str |  (optional)
    status_reason = "status.reason_example" # str |  (optional)
    status_uri = "status.uri_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, query_start_time=query_start_time, query_end_time=query_end_time, query_tenants=query_tenants, status_status=status_status, status_reason=status_reason, status_uri=status_uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **query_start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **query_end_time** | **datetime**| EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional]
 **query_tenants** | **[str]**| OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. | [optional]
 **status_status** | **str**|  | [optional]
 **status_reason** | **str**|  | [optional]
 **status_uri** | **str**|  | [optional]

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_archive_request1**
> MonitoringArchiveRequest get_archive_request1(o_name)

Get ArchiveRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    query_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. (optional)
    query_end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. (optional)
    query_tenants = [
        "query.tenants_example",
    ] # [str] | OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. (optional)
    status_status = "status.status_example" # str |  (optional)
    status_reason = "status.reason_example" # str |  (optional)
    status_uri = "status.uri_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_type=spec_type, query_start_time=query_start_time, query_end_time=query_end_time, query_tenants=query_tenants, status_status=status_status, status_reason=status_reason, status_uri=status_uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **query_start_time** | **datetime**| StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z. | [optional]
 **query_end_time** | **datetime**| EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z. | [optional]
 **query_tenants** | **[str]**| OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. | [optional]
 **status_status** | **str**|  | [optional]
 **status_reason** | **str**|  | [optional]
 **status_uri** | **str**|  | [optional]

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_audit_policy**
> MonitoringAuditPolicy get_audit_policy(o_tenant)

Get AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_name = "meta.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    syslog_auditor_enabled = True # bool | flag to enable sending audit events to syslog. (optional)
    syslog_auditor_format = "syslog-auditor.format_example" # str | audit event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AuditPolicy object
        api_response = api_instance.get_audit_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_audit_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AuditPolicy object
        api_response = api_instance.get_audit_policy(o_tenant, t_kind=t_kind, t_api_version=t_api_version, meta_name=meta_name, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, syslog_auditor_enabled=syslog_auditor_enabled, syslog_auditor_format=syslog_auditor_format, config_facility_override=config_facility_override, config_prefix=config_prefix)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_audit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **syslog_auditor_enabled** | **bool**| flag to enable sending audit events to syslog. | [optional]
 **syslog_auditor_format** | **str**| audit event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_audit_policy1**
> MonitoringAuditPolicy get_audit_policy1()

Get AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_name = "meta.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    syslog_auditor_enabled = True # bool | flag to enable sending audit events to syslog. (optional)
    syslog_auditor_format = "syslog-auditor.format_example" # str | audit event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AuditPolicy object
        api_response = api_instance.get_audit_policy1(t_kind=t_kind, t_api_version=t_api_version, meta_name=meta_name, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, syslog_auditor_enabled=syslog_auditor_enabled, syslog_auditor_format=syslog_auditor_format, config_facility_override=config_facility_override, config_prefix=config_prefix)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_audit_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **syslog_auditor_enabled** | **bool**| flag to enable sending audit events to syslog. | [optional]
 **syslog_auditor_format** | **str**| audit event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_event_policy**
> MonitoringEventPolicy get_event_policy(o_tenant, o_name)

Get EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_format = "spec.format_example" # str | event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_format=spec_format, config_facility_override=config_facility_override, config_prefix=config_prefix)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_format** | **str**| event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_event_policy1**
> MonitoringEventPolicy get_event_policy1(o_name)

Get EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_format = "spec.format_example" # str | event export format, SYSLOG_BSD default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_format=spec_format, config_facility_override=config_facility_override, config_prefix=config_prefix)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_format** | **str**| event export format, SYSLOG_BSD default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_flow_export_policy**
> MonitoringFlowExportPolicy get_flow_export_policy(o_tenant, o_name)

Get FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_vrf_name = "spec.vrf-name_example" # str | VrfName specifies the name of the VRF that the current flow export Policy belongs to. (optional)
    spec_interval = "spec.interval_example" # str | Interval defines how often to push the records to an external collector The value is specified as a string format, '10s', '20m'. Should be a valid time duration between 1s and 24h0m0s. (optional)
    spec_template_interval = "spec.template-interval_example" # str | TemplateInterval defines how often to send ipfix templates to an external collector The value is specified as a string format, '1m', '10m'. Should be a valid time duration between 1m0s and 30m0s. (optional)
    spec_format = "spec.format_example" # str |  (optional)
    spec_disabled = True # bool | Enable/disable flow export. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest DSC. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_state = "status.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_vrf_name=spec_vrf_name, spec_interval=spec_interval, spec_template_interval=spec_template_interval, spec_format=spec_format, spec_disabled=spec_disabled, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs, status_state=status_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_vrf_name** | **str**| VrfName specifies the name of the VRF that the current flow export Policy belongs to. | [optional]
 **spec_interval** | **str**| Interval defines how often to push the records to an external collector The value is specified as a string format, &#39;10s&#39;, &#39;20m&#39;. Should be a valid time duration between 1s and 24h0m0s. | [optional]
 **spec_template_interval** | **str**| TemplateInterval defines how often to send ipfix templates to an external collector The value is specified as a string format, &#39;1m&#39;, &#39;10m&#39;. Should be a valid time duration between 1m0s and 30m0s. | [optional]
 **spec_format** | **str**|  | [optional]
 **spec_disabled** | **bool**| Enable/disable flow export. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest DSC. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_state** | **str**|  | [optional]

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_flow_export_policy1**
> MonitoringFlowExportPolicy get_flow_export_policy1(o_name)

Get FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_vrf_name = "spec.vrf-name_example" # str | VrfName specifies the name of the VRF that the current flow export Policy belongs to. (optional)
    spec_interval = "spec.interval_example" # str | Interval defines how often to push the records to an external collector The value is specified as a string format, '10s', '20m'. Should be a valid time duration between 1s and 24h0m0s. (optional)
    spec_template_interval = "spec.template-interval_example" # str | TemplateInterval defines how often to send ipfix templates to an external collector The value is specified as a string format, '1m', '10m'. Should be a valid time duration between 1m0s and 30m0s. (optional)
    spec_format = "spec.format_example" # str |  (optional)
    spec_disabled = True # bool | Enable/disable flow export. (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest DSC. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)
    status_state = "status.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_vrf_name=spec_vrf_name, spec_interval=spec_interval, spec_template_interval=spec_template_interval, spec_format=spec_format, spec_disabled=spec_disabled, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs, status_state=status_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_vrf_name** | **str**| VrfName specifies the name of the VRF that the current flow export Policy belongs to. | [optional]
 **spec_interval** | **str**| Interval defines how often to push the records to an external collector The value is specified as a string format, &#39;10s&#39;, &#39;20m&#39;. Should be a valid time duration between 1s and 24h0m0s. | [optional]
 **spec_template_interval** | **str**| TemplateInterval defines how often to send ipfix templates to an external collector The value is specified as a string format, &#39;1m&#39;, &#39;10m&#39;. Should be a valid time duration between 1m0s and 30m0s. | [optional]
 **spec_format** | **str**|  | [optional]
 **spec_disabled** | **bool**| Enable/disable flow export. | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest DSC. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]
 **status_state** | **str**|  | [optional]

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_fwlog_policy**
> MonitoringFwlogPolicy get_fwlog_policy(o_tenant, o_name)

Get FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_vrf_name = "spec.vrf-name_example" # str | VrfName specifies the name of the VRF that the current Firewall Log Policy belongs to. (optional)
    spec_format = "spec.format_example" # str | fwlog format, SYSLOG_BSD default. (optional)
    spec_filter = [
        "spec.filter_example",
    ] # [str] | filter firewall logs, FWLOG_ALL default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)
    psm_target_enable = True # bool | Enable is for enabling the log export. Its default value is false. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_vrf_name=spec_vrf_name, spec_format=spec_format, spec_filter=spec_filter, config_facility_override=config_facility_override, config_prefix=config_prefix, psm_target_enable=psm_target_enable)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_vrf_name** | **str**| VrfName specifies the name of the VRF that the current Firewall Log Policy belongs to. | [optional]
 **spec_format** | **str**| fwlog format, SYSLOG_BSD default. | [optional]
 **spec_filter** | **[str]**| filter firewall logs, FWLOG_ALL default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]
 **psm_target_enable** | **bool**| Enable is for enabling the log export. Its default value is false. | [optional]

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_fwlog_policy1**
> MonitoringFwlogPolicy get_fwlog_policy1(o_name)

Get FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_vrf_name = "spec.vrf-name_example" # str | VrfName specifies the name of the VRF that the current Firewall Log Policy belongs to. (optional)
    spec_format = "spec.format_example" # str | fwlog format, SYSLOG_BSD default. (optional)
    spec_filter = [
        "spec.filter_example",
    ] # [str] | filter firewall logs, FWLOG_ALL default. (optional)
    config_facility_override = "config.facility-override_example" # str | override default facility with this in exported logs. (optional)
    config_prefix = "config.prefix_example" # str | add prefix in exported logs. (optional)
    psm_target_enable = True # bool | Enable is for enabling the log export. Its default value is false. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_vrf_name=spec_vrf_name, spec_format=spec_format, spec_filter=spec_filter, config_facility_override=config_facility_override, config_prefix=config_prefix, psm_target_enable=psm_target_enable)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_vrf_name** | **str**| VrfName specifies the name of the VRF that the current Firewall Log Policy belongs to. | [optional]
 **spec_format** | **str**| fwlog format, SYSLOG_BSD default. | [optional]
 **spec_filter** | **[str]**| filter firewall logs, FWLOG_ALL default. | [optional]
 **config_facility_override** | **str**| override default facility with this in exported logs. | [optional]
 **config_prefix** | **str**| add prefix in exported logs. | [optional]
 **psm_target_enable** | **bool**| Enable is for enabling the log export. Its default value is false. | [optional]

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_mirror_session**
> MonitoringMirrorSession get_mirror_session(o_tenant, o_name)

Get MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_packet_size = 1 # int | PacketSize: Max size of a mirrored packet, packet size is not checked by default. Value should be between 64 and 2048. (optional)
    start_condition_schedule_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    spec_packet_filters = [
        "spec.packet-filters_example",
    ] # [str] |  (optional)
    interfaces_direction = "interfaces.direction_example" # str |  (optional)
    spec_span_id = 1 # int | Value should be between 1 and 1023. (optional)
    workloads_direction = "workloads.direction_example" # str | rx is towards the workload and tx is from workload. (optional)
    source_target_type = "source.target-type_example" # str |  (optional)
    source_direction = "source.direction_example" # str | rx is towards the Source and tx is from Source. (optional)
    spec_disabled = True # bool | Enable/disable mirroring. (optional)
    status_schedule_state = "status.schedule-state_example" # str |  (optional)
    status_started_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest DSC. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_packet_size=spec_packet_size, start_condition_schedule_time=start_condition_schedule_time, spec_packet_filters=spec_packet_filters, interfaces_direction=interfaces_direction, spec_span_id=spec_span_id, workloads_direction=workloads_direction, source_target_type=source_target_type, source_direction=source_direction, spec_disabled=spec_disabled, status_schedule_state=status_schedule_state, status_started_at=status_started_at, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_packet_size** | **int**| PacketSize: Max size of a mirrored packet, packet size is not checked by default. Value should be between 64 and 2048. | [optional]
 **start_condition_schedule_time** | **datetime**|  | [optional]
 **spec_packet_filters** | **[str]**|  | [optional]
 **interfaces_direction** | **str**|  | [optional]
 **spec_span_id** | **int**| Value should be between 1 and 1023. | [optional]
 **workloads_direction** | **str**| rx is towards the workload and tx is from workload. | [optional]
 **source_target_type** | **str**|  | [optional]
 **source_direction** | **str**| rx is towards the Source and tx is from Source. | [optional]
 **spec_disabled** | **bool**| Enable/disable mirroring. | [optional]
 **status_schedule_state** | **str**|  | [optional]
 **status_started_at** | **datetime**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest DSC. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_mirror_session1**
> MonitoringMirrorSession get_mirror_session1(o_name)

Get MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    spec_packet_size = 1 # int | PacketSize: Max size of a mirrored packet, packet size is not checked by default. Value should be between 64 and 2048. (optional)
    start_condition_schedule_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    spec_packet_filters = [
        "spec.packet-filters_example",
    ] # [str] |  (optional)
    interfaces_direction = "interfaces.direction_example" # str |  (optional)
    spec_span_id = 1 # int | Value should be between 1 and 1023. (optional)
    workloads_direction = "workloads.direction_example" # str | rx is towards the workload and tx is from workload. (optional)
    source_target_type = "source.target-type_example" # str |  (optional)
    source_direction = "source.direction_example" # str | rx is towards the Source and tx is from Source. (optional)
    spec_disabled = True # bool | Enable/disable mirroring. (optional)
    status_schedule_state = "status.schedule-state_example" # str |  (optional)
    status_started_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    propagation_status_generation_id = "propagation-status.generation-id_example" # str | The Generation ID this status is for. (optional)
    propagation_status_updated = 1 # int | The number of Naples that this version has already been pushed to. (optional)
    propagation_status_pending = 1 # int | Number of Naples pending. If this is 0 it can be assumed that everything is up to date. (optional)
    propagation_status_min_version = "propagation-status.min-version_example" # str | The Version running on the slowest DSC. (optional)
    propagation_status_status = "propagation-status.status_example" # str | Textual description of propagation status. (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, spec_packet_size=spec_packet_size, start_condition_schedule_time=start_condition_schedule_time, spec_packet_filters=spec_packet_filters, interfaces_direction=interfaces_direction, spec_span_id=spec_span_id, workloads_direction=workloads_direction, source_target_type=source_target_type, source_direction=source_direction, spec_disabled=spec_disabled, status_schedule_state=status_schedule_state, status_started_at=status_started_at, propagation_status_generation_id=propagation_status_generation_id, propagation_status_updated=propagation_status_updated, propagation_status_pending=propagation_status_pending, propagation_status_min_version=propagation_status_min_version, propagation_status_status=propagation_status_status, propagation_status_pending_dscs=propagation_status_pending_dscs)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **spec_packet_size** | **int**| PacketSize: Max size of a mirrored packet, packet size is not checked by default. Value should be between 64 and 2048. | [optional]
 **start_condition_schedule_time** | **datetime**|  | [optional]
 **spec_packet_filters** | **[str]**|  | [optional]
 **interfaces_direction** | **str**|  | [optional]
 **spec_span_id** | **int**| Value should be between 1 and 1023. | [optional]
 **workloads_direction** | **str**| rx is towards the workload and tx is from workload. | [optional]
 **source_target_type** | **str**|  | [optional]
 **source_direction** | **str**| rx is towards the Source and tx is from Source. | [optional]
 **spec_disabled** | **bool**| Enable/disable mirroring. | [optional]
 **status_schedule_state** | **str**|  | [optional]
 **status_started_at** | **datetime**|  | [optional]
 **propagation_status_generation_id** | **str**| The Generation ID this status is for. | [optional]
 **propagation_status_updated** | **int**| The number of Naples that this version has already been pushed to. | [optional]
 **propagation_status_pending** | **int**| Number of Naples pending. If this is 0 it can be assumed that everything is up to date. | [optional]
 **propagation_status_min_version** | **str**| The Version running on the slowest DSC. | [optional]
 **propagation_status_status** | **str**| Textual description of propagation status. | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_stats_alert_policy**
> MonitoringStatsAlertPolicy get_stats_alert_policy(o_tenant, o_name)

Get StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    metric_group = "metric.group_example" # str | Metric group - e.g. ftestats, flowstats, etc. (optional)
    metric_kind = "metric.kind_example" # str | Sub-category within the group e.g. MaxSessionThresholdDrops, FlowMissPackets. (optional)
    metric_field_name = "metric.field-name_example" # str | Field belonging to the kind e.g. ConnectionsPerSecond. This is the attribute that will be monitored and alerts will be created/resolved based on the thresholds. (optional)
    measurement_criteria_window = "measurement-criteria.window_example" # str | The length of time the metric will be monitored/observed before running the values against thresholds for alert creation/resolution. ui-hint: Allowed values - 5m, 10m, 30m, 1h. (optional)
    measurement_criteria_function = "measurement-criteria.function_example" # str | Aggregate function to be applied on the metric values that were monitored over a window/interval. (optional)
    thresholds_operator = "thresholds.operator_example" # str | Operator to be applied when comparing metric values against the threshold values. (optional)
    spec_enable = True # bool | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)
    instance_selector_kind = "instance-selector.kind_example" # str | Kind of the instances to be selected using names/label. (optional)
    instance_selector_names = [
        "instance-selector.names_example",
    ] # [str] | List of names/reporter IDs. (optional)
    status_total_hits = 1 # int | Total hits on this policy. (optional)
    status_open_alerts = 1 # int | Open alerts based on this policy. (optional)
    status_acknowledged_alerts = 1 # int | Acknowledged alerts based on this policy. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, metric_group=metric_group, metric_kind=metric_kind, metric_field_name=metric_field_name, measurement_criteria_window=measurement_criteria_window, measurement_criteria_function=measurement_criteria_function, thresholds_operator=thresholds_operator, spec_enable=spec_enable, spec_destinations=spec_destinations, instance_selector_kind=instance_selector_kind, instance_selector_names=instance_selector_names, status_total_hits=status_total_hits, status_open_alerts=status_open_alerts, status_acknowledged_alerts=status_acknowledged_alerts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **metric_group** | **str**| Metric group - e.g. ftestats, flowstats, etc. | [optional]
 **metric_kind** | **str**| Sub-category within the group e.g. MaxSessionThresholdDrops, FlowMissPackets. | [optional]
 **metric_field_name** | **str**| Field belonging to the kind e.g. ConnectionsPerSecond. This is the attribute that will be monitored and alerts will be created/resolved based on the thresholds. | [optional]
 **measurement_criteria_window** | **str**| The length of time the metric will be monitored/observed before running the values against thresholds for alert creation/resolution. ui-hint: Allowed values - 5m, 10m, 30m, 1h. | [optional]
 **measurement_criteria_function** | **str**| Aggregate function to be applied on the metric values that were monitored over a window/interval. | [optional]
 **thresholds_operator** | **str**| Operator to be applied when comparing metric values against the threshold values. | [optional]
 **spec_enable** | **bool**| User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]
 **instance_selector_kind** | **str**| Kind of the instances to be selected using names/label. | [optional]
 **instance_selector_names** | **[str]**| List of names/reporter IDs. | [optional]
 **status_total_hits** | **int**| Total hits on this policy. | [optional]
 **status_open_alerts** | **int**| Open alerts based on this policy. | [optional]
 **status_acknowledged_alerts** | **int**| Acknowledged alerts based on this policy. | [optional]

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_stats_alert_policy1**
> MonitoringStatsAlertPolicy get_stats_alert_policy1(o_name)

Get StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    metric_group = "metric.group_example" # str | Metric group - e.g. ftestats, flowstats, etc. (optional)
    metric_kind = "metric.kind_example" # str | Sub-category within the group e.g. MaxSessionThresholdDrops, FlowMissPackets. (optional)
    metric_field_name = "metric.field-name_example" # str | Field belonging to the kind e.g. ConnectionsPerSecond. This is the attribute that will be monitored and alerts will be created/resolved based on the thresholds. (optional)
    measurement_criteria_window = "measurement-criteria.window_example" # str | The length of time the metric will be monitored/observed before running the values against thresholds for alert creation/resolution. ui-hint: Allowed values - 5m, 10m, 30m, 1h. (optional)
    measurement_criteria_function = "measurement-criteria.function_example" # str | Aggregate function to be applied on the metric values that were monitored over a window/interval. (optional)
    thresholds_operator = "thresholds.operator_example" # str | Operator to be applied when comparing metric values against the threshold values. (optional)
    spec_enable = True # bool | User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)
    instance_selector_kind = "instance-selector.kind_example" # str | Kind of the instances to be selected using names/label. (optional)
    instance_selector_names = [
        "instance-selector.names_example",
    ] # [str] | List of names/reporter IDs. (optional)
    status_total_hits = 1 # int | Total hits on this policy. (optional)
    status_open_alerts = 1 # int | Open alerts based on this policy. (optional)
    status_acknowledged_alerts = 1 # int | Acknowledged alerts based on this policy. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, metric_group=metric_group, metric_kind=metric_kind, metric_field_name=metric_field_name, measurement_criteria_window=measurement_criteria_window, measurement_criteria_function=measurement_criteria_function, thresholds_operator=thresholds_operator, spec_enable=spec_enable, spec_destinations=spec_destinations, instance_selector_kind=instance_selector_kind, instance_selector_names=instance_selector_names, status_total_hits=status_total_hits, status_open_alerts=status_open_alerts, status_acknowledged_alerts=status_acknowledged_alerts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **metric_group** | **str**| Metric group - e.g. ftestats, flowstats, etc. | [optional]
 **metric_kind** | **str**| Sub-category within the group e.g. MaxSessionThresholdDrops, FlowMissPackets. | [optional]
 **metric_field_name** | **str**| Field belonging to the kind e.g. ConnectionsPerSecond. This is the attribute that will be monitored and alerts will be created/resolved based on the thresholds. | [optional]
 **measurement_criteria_window** | **str**| The length of time the metric will be monitored/observed before running the values against thresholds for alert creation/resolution. ui-hint: Allowed values - 5m, 10m, 30m, 1h. | [optional]
 **measurement_criteria_function** | **str**| Aggregate function to be applied on the metric values that were monitored over a window/interval. | [optional]
 **thresholds_operator** | **str**| Operator to be applied when comparing metric values against the threshold values. | [optional]
 **spec_enable** | **bool**| User can disable the policy by setting this field. Disabled policies will not generate any more alerts but the outstanding ones will remain as is. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]
 **instance_selector_kind** | **str**| Kind of the instances to be selected using names/label. | [optional]
 **instance_selector_names** | **[str]**| List of names/reporter IDs. | [optional]
 **status_total_hits** | **int**| Total hits on this policy. | [optional]
 **status_open_alerts** | **int**| Open alerts based on this policy. | [optional]
 **status_acknowledged_alerts** | **int**| Acknowledged alerts based on this policy. | [optional]

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_tech_support_request**
> MonitoringTechSupportRequest get_tech_support_request(o_name)

Get TechSupportRequest object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    node_selector_names = [
        "node-selector.names_example",
    ] # [str] |  (optional)
    spec_verbosity = 1 # int | Verbosity defines the verbosity level. (optional)
    spec_skip_cores = True # bool | SkipCores if set to true skips the core files when collecting techsupport. (optional)
    status_instance_id = "status.instance-id_example" # str |  (optional)
    status_status = "status.status_example" # str |  (optional)
    status_reason = "status.reason_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TechSupportRequest object
        api_response = api_instance.get_tech_support_request(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_tech_support_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TechSupportRequest object
        api_response = api_instance.get_tech_support_request(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, node_selector_names=node_selector_names, spec_verbosity=spec_verbosity, spec_skip_cores=spec_skip_cores, status_instance_id=status_instance_id, status_status=status_status, status_reason=status_reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_tech_support_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **node_selector_names** | **[str]**|  | [optional]
 **spec_verbosity** | **int**| Verbosity defines the verbosity level. | [optional]
 **spec_skip_cores** | **bool**| SkipCores if set to true skips the core files when collecting techsupport. | [optional]
 **status_instance_id** | **str**|  | [optional]
 **status_status** | **str**|  | [optional]
 **status_reason** | **str**|  | [optional]

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_troubleshooting_session**
> MonitoringTroubleshootingSession get_troubleshooting_session(o_tenant, o_name)

Get TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    source_ip_addresses = [
        "source.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    source_mac_addresses = [
        "source.mac-addresses_example",
    ] # [str] | List of MacAddresses - \"aabb.ccdd.eeff\", \"0001.0203.0405\". Should be a valid MAC address. (optional)
    destination_ip_addresses = [
        "destination.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    destination_mac_addresses = [
        "destination.mac-addresses_example",
    ] # [str] | List of MacAddresses - \"aabb.ccdd.eeff\", \"0001.0203.0405\". Should be a valid MAC address. (optional)
    app_protocol_selectors_proto_ports = [
        "app-protocol-selectors.proto-ports_example",
    ] # [str] | ports - Includes protocol name and port Eg [\"tcp/1234\", \"udp\"]. Should be a valid layer 3 or layer 4 protocol and port range. any is also allowed. (optional)
    app_protocol_selectors_applications = [
        "app-protocol-selectors.applications_example",
    ] # [str] | Apps - E.g. [\"Redis\"]. (optional)
    time_window_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start/Stop Time - when start time is not specified, it implies start NOW. (optional)
    time_window_stop_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Stop time - when not specified, default will be used. (optional)
    spec_repeat_every = "spec.repeat-every_example" # str |  (optional)
    spec_enable_mirroring = True # bool | If packet capture is enabled, a mirror-session will be internally created. (optional)
    status_state = "status.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session(o_tenant, o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session(o_tenant, o_name, t_kind=t_kind, t_api_version=t_api_version, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, source_ip_addresses=source_ip_addresses, source_mac_addresses=source_mac_addresses, destination_ip_addresses=destination_ip_addresses, destination_mac_addresses=destination_mac_addresses, app_protocol_selectors_proto_ports=app_protocol_selectors_proto_ports, app_protocol_selectors_applications=app_protocol_selectors_applications, time_window_start_time=time_window_start_time, time_window_stop_time=time_window_stop_time, spec_repeat_every=spec_repeat_every, spec_enable_mirroring=spec_enable_mirroring, status_state=status_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **source_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **source_mac_addresses** | **[str]**| List of MacAddresses - \&quot;aabb.ccdd.eeff\&quot;, \&quot;0001.0203.0405\&quot;. Should be a valid MAC address. | [optional]
 **destination_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **destination_mac_addresses** | **[str]**| List of MacAddresses - \&quot;aabb.ccdd.eeff\&quot;, \&quot;0001.0203.0405\&quot;. Should be a valid MAC address. | [optional]
 **app_protocol_selectors_proto_ports** | **[str]**| ports - Includes protocol name and port Eg [\&quot;tcp/1234\&quot;, \&quot;udp\&quot;]. Should be a valid layer 3 or layer 4 protocol and port range. any is also allowed. | [optional]
 **app_protocol_selectors_applications** | **[str]**| Apps - E.g. [\&quot;Redis\&quot;]. | [optional]
 **time_window_start_time** | **datetime**| Start/Stop Time - when start time is not specified, it implies start NOW. | [optional]
 **time_window_stop_time** | **datetime**| Stop time - when not specified, default will be used. | [optional]
 **spec_repeat_every** | **str**|  | [optional]
 **spec_enable_mirroring** | **bool**| If packet capture is enabled, a mirror-session will be internally created. | [optional]
 **status_state** | **str**|  | [optional]

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **get_troubleshooting_session1**
> MonitoringTroubleshootingSession get_troubleshooting_session1(o_name)

Get TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    t_api_version = "T.api-version_example" # str | APIVersion defines the version of the API object. This can only be set by the server. (optional)
    meta_tenant = "meta.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    meta_namespace = "meta.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    meta_generation_id = "meta.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    meta_resource_version = "meta.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    meta_uuid = "meta.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    meta_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    meta_self_link = "meta.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    source_ip_addresses = [
        "source.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    source_mac_addresses = [
        "source.mac-addresses_example",
    ] # [str] | List of MacAddresses - \"aabb.ccdd.eeff\", \"0001.0203.0405\". Should be a valid MAC address. (optional)
    destination_ip_addresses = [
        "destination.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    destination_mac_addresses = [
        "destination.mac-addresses_example",
    ] # [str] | List of MacAddresses - \"aabb.ccdd.eeff\", \"0001.0203.0405\". Should be a valid MAC address. (optional)
    app_protocol_selectors_proto_ports = [
        "app-protocol-selectors.proto-ports_example",
    ] # [str] | ports - Includes protocol name and port Eg [\"tcp/1234\", \"udp\"]. Should be a valid layer 3 or layer 4 protocol and port range. any is also allowed. (optional)
    app_protocol_selectors_applications = [
        "app-protocol-selectors.applications_example",
    ] # [str] | Apps - E.g. [\"Redis\"]. (optional)
    time_window_start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start/Stop Time - when start time is not specified, it implies start NOW. (optional)
    time_window_stop_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Stop time - when not specified, default will be used. (optional)
    spec_repeat_every = "spec.repeat-every_example" # str |  (optional)
    spec_enable_mirroring = True # bool | If packet capture is enabled, a mirror-session will be internally created. (optional)
    status_state = "status.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session1(o_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session1(o_name, t_kind=t_kind, t_api_version=t_api_version, meta_tenant=meta_tenant, meta_namespace=meta_namespace, meta_generation_id=meta_generation_id, meta_resource_version=meta_resource_version, meta_uuid=meta_uuid, meta_creation_time=meta_creation_time, meta_mod_time=meta_mod_time, meta_self_link=meta_self_link, source_ip_addresses=source_ip_addresses, source_mac_addresses=source_mac_addresses, destination_ip_addresses=destination_ip_addresses, destination_mac_addresses=destination_mac_addresses, app_protocol_selectors_proto_ports=app_protocol_selectors_proto_ports, app_protocol_selectors_applications=app_protocol_selectors_applications, time_window_start_time=time_window_start_time, time_window_stop_time=time_window_stop_time, spec_repeat_every=spec_repeat_every, spec_enable_mirroring=spec_enable_mirroring, status_state=status_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **t_api_version** | **str**| APIVersion defines the version of the API object. This can only be set by the server. | [optional]
 **meta_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **meta_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **meta_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **meta_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **meta_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **meta_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **source_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **source_mac_addresses** | **[str]**| List of MacAddresses - \&quot;aabb.ccdd.eeff\&quot;, \&quot;0001.0203.0405\&quot;. Should be a valid MAC address. | [optional]
 **destination_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **destination_mac_addresses** | **[str]**| List of MacAddresses - \&quot;aabb.ccdd.eeff\&quot;, \&quot;0001.0203.0405\&quot;. Should be a valid MAC address. | [optional]
 **app_protocol_selectors_proto_ports** | **[str]**| ports - Includes protocol name and port Eg [\&quot;tcp/1234\&quot;, \&quot;udp\&quot;]. Should be a valid layer 3 or layer 4 protocol and port range. any is also allowed. | [optional]
 **app_protocol_selectors_applications** | **[str]**| Apps - E.g. [\&quot;Redis\&quot;]. | [optional]
 **time_window_start_time** | **datetime**| Start/Stop Time - when start time is not specified, it implies start NOW. | [optional]
 **time_window_stop_time** | **datetime**| Stop time - when not specified, default will be used. | [optional]
 **spec_repeat_every** | **str**|  | [optional]
 **spec_enable_mirroring** | **bool**| If packet capture is enabled, a mirror-session will be internally created. | [optional]
 **status_state** | **str**|  | [optional]

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert**
> MonitoringAlert label_alert(o_tenant, o_name, body)

Label Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Alert object
        api_response = api_instance.label_alert(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert1**
> MonitoringAlert label_alert1(o_name, body)

Label Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Alert object
        api_response = api_instance.label_alert1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert_destination**
> MonitoringAlertDestination label_alert_destination(o_tenant, o_name, body)

Label AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertDestination object
        api_response = api_instance.label_alert_destination(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert_destination1**
> MonitoringAlertDestination label_alert_destination1(o_name, body)

Label AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertDestination object
        api_response = api_instance.label_alert_destination1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert_policy**
> MonitoringAlertPolicy label_alert_policy(o_tenant, o_name, body)

Label AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertPolicy object
        api_response = api_instance.label_alert_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_alert_policy1**
> MonitoringAlertPolicy label_alert_policy1(o_name, body)

Label AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertPolicy object
        api_response = api_instance.label_alert_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_event_policy**
> MonitoringEventPolicy label_event_policy(o_tenant, o_name, body)

Label EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label EventPolicy object
        api_response = api_instance.label_event_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_event_policy1**
> MonitoringEventPolicy label_event_policy1(o_name, body)

Label EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label EventPolicy object
        api_response = api_instance.label_event_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_flow_export_policy**
> MonitoringFlowExportPolicy label_flow_export_policy(o_tenant, o_name, body)

Label FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FlowExportPolicy object
        api_response = api_instance.label_flow_export_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_flow_export_policy1**
> MonitoringFlowExportPolicy label_flow_export_policy1(o_name, body)

Label FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FlowExportPolicy object
        api_response = api_instance.label_flow_export_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_fwlog_policy**
> MonitoringFwlogPolicy label_fwlog_policy(o_tenant, o_name, body)

Label FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FwlogPolicy object
        api_response = api_instance.label_fwlog_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_fwlog_policy1**
> MonitoringFwlogPolicy label_fwlog_policy1(o_name, body)

Label FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FwlogPolicy object
        api_response = api_instance.label_fwlog_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_mirror_session**
> MonitoringMirrorSession label_mirror_session(o_tenant, o_name, body)

Label MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label MirrorSession object
        api_response = api_instance.label_mirror_session(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_mirror_session1**
> MonitoringMirrorSession label_mirror_session1(o_name, body)

Label MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label MirrorSession object
        api_response = api_instance.label_mirror_session1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_stats_alert_policy**
> MonitoringStatsAlertPolicy label_stats_alert_policy(o_tenant, o_name, body)

Label StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label StatsAlertPolicy object
        api_response = api_instance.label_stats_alert_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_stats_alert_policy1**
> MonitoringStatsAlertPolicy label_stats_alert_policy1(o_name, body)

Label StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label StatsAlertPolicy object
        api_response = api_instance.label_stats_alert_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_troubleshooting_session**
> MonitoringTroubleshootingSession label_troubleshooting_session(o_tenant, o_name, body)

Label TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label TroubleshootingSession object
        api_response = api_instance.label_troubleshooting_session(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **label_troubleshooting_session1**
> MonitoringTroubleshootingSession label_troubleshooting_session1(o_name, body)

Label TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.api_label import ApiLabel
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label TroubleshootingSession object
        api_response = api_instance.label_troubleshooting_session1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->label_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert**
> MonitoringAlertList list_alert(o_tenant)

List Alert objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert_list import MonitoringAlertList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Alert objects
        api_response = api_instance.list_alert(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Alert objects
        api_response = api_instance.list_alert(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertList**](MonitoringAlertList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert1**
> MonitoringAlertList list_alert1()

List Alert objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert_list import MonitoringAlertList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Alert objects
        api_response = api_instance.list_alert1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertList**](MonitoringAlertList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert_destination**
> MonitoringAlertDestinationList list_alert_destination(o_tenant)

List AlertDestination objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination_list import MonitoringAlertDestinationList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertDestination objects
        api_response = api_instance.list_alert_destination(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_destination: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List AlertDestination objects
        api_response = api_instance.list_alert_destination(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertDestinationList**](MonitoringAlertDestinationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert_destination1**
> MonitoringAlertDestinationList list_alert_destination1()

List AlertDestination objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination_list import MonitoringAlertDestinationList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List AlertDestination objects
        api_response = api_instance.list_alert_destination1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertDestinationList**](MonitoringAlertDestinationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert_policy**
> MonitoringAlertPolicyList list_alert_policy(o_tenant)

List AlertPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert_policy_list import MonitoringAlertPolicyList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertPolicy objects
        api_response = api_instance.list_alert_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List AlertPolicy objects
        api_response = api_instance.list_alert_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertPolicyList**](MonitoringAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_alert_policy1**
> MonitoringAlertPolicyList list_alert_policy1()

List AlertPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert_policy_list import MonitoringAlertPolicyList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List AlertPolicy objects
        api_response = api_instance.list_alert_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAlertPolicyList**](MonitoringAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_archive_request**
> MonitoringArchiveRequestList list_archive_request(o_tenant)

List ArchiveRequest objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_archive_request_list import MonitoringArchiveRequestList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ArchiveRequest objects
        api_response = api_instance.list_archive_request(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_archive_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ArchiveRequest objects
        api_response = api_instance.list_archive_request(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_archive_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringArchiveRequestList**](MonitoringArchiveRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_archive_request1**
> MonitoringArchiveRequestList list_archive_request1()

List ArchiveRequest objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_archive_request_list import MonitoringArchiveRequestList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ArchiveRequest objects
        api_response = api_instance.list_archive_request1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_archive_request1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringArchiveRequestList**](MonitoringArchiveRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_event_policy**
> MonitoringEventPolicyList list_event_policy(o_tenant)

List EventPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy_list import MonitoringEventPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List EventPolicy objects
        api_response = api_instance.list_event_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_event_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List EventPolicy objects
        api_response = api_instance.list_event_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringEventPolicyList**](MonitoringEventPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_event_policy1**
> MonitoringEventPolicyList list_event_policy1()

List EventPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy_list import MonitoringEventPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List EventPolicy objects
        api_response = api_instance.list_event_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringEventPolicyList**](MonitoringEventPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_flow_export_policy**
> MonitoringFlowExportPolicyList list_flow_export_policy(o_tenant)

List FlowExportPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_flow_export_policy_list import MonitoringFlowExportPolicyList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FlowExportPolicy objects
        api_response = api_instance.list_flow_export_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_flow_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List FlowExportPolicy objects
        api_response = api_instance.list_flow_export_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringFlowExportPolicyList**](MonitoringFlowExportPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_flow_export_policy1**
> MonitoringFlowExportPolicyList list_flow_export_policy1()

List FlowExportPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_flow_export_policy_list import MonitoringFlowExportPolicyList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List FlowExportPolicy objects
        api_response = api_instance.list_flow_export_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringFlowExportPolicyList**](MonitoringFlowExportPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_fwlog_policy**
> MonitoringFwlogPolicyList list_fwlog_policy(o_tenant)

List FwlogPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy_list import MonitoringFwlogPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FwlogPolicy objects
        api_response = api_instance.list_fwlog_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_fwlog_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List FwlogPolicy objects
        api_response = api_instance.list_fwlog_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringFwlogPolicyList**](MonitoringFwlogPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_fwlog_policy1**
> MonitoringFwlogPolicyList list_fwlog_policy1()

List FwlogPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy_list import MonitoringFwlogPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List FwlogPolicy objects
        api_response = api_instance.list_fwlog_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringFwlogPolicyList**](MonitoringFwlogPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_mirror_session**
> MonitoringMirrorSessionList list_mirror_session(o_tenant)

List MirrorSession objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session_list import MonitoringMirrorSessionList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List MirrorSession objects
        api_response = api_instance.list_mirror_session(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_mirror_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List MirrorSession objects
        api_response = api_instance.list_mirror_session(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringMirrorSessionList**](MonitoringMirrorSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_mirror_session1**
> MonitoringMirrorSessionList list_mirror_session1()

List MirrorSession objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session_list import MonitoringMirrorSessionList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List MirrorSession objects
        api_response = api_instance.list_mirror_session1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringMirrorSessionList**](MonitoringMirrorSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_stats_alert_policy**
> MonitoringStatsAlertPolicyList list_stats_alert_policy(o_tenant)

List StatsAlertPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy_list import MonitoringStatsAlertPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List StatsAlertPolicy objects
        api_response = api_instance.list_stats_alert_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_stats_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List StatsAlertPolicy objects
        api_response = api_instance.list_stats_alert_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringStatsAlertPolicyList**](MonitoringStatsAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_stats_alert_policy1**
> MonitoringStatsAlertPolicyList list_stats_alert_policy1()

List StatsAlertPolicy objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy_list import MonitoringStatsAlertPolicyList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List StatsAlertPolicy objects
        api_response = api_instance.list_stats_alert_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringStatsAlertPolicyList**](MonitoringStatsAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_tech_support_request**
> MonitoringTechSupportRequestList list_tech_support_request()

List TechSupportRequest objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_tech_support_request_list import MonitoringTechSupportRequestList
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TechSupportRequest objects
        api_response = api_instance.list_tech_support_request(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_tech_support_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringTechSupportRequestList**](MonitoringTechSupportRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_troubleshooting_session**
> MonitoringTroubleshootingSessionList list_troubleshooting_session(o_tenant)

List TroubleshootingSession objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session_list import MonitoringTroubleshootingSessionList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List TroubleshootingSession objects
        api_response = api_instance.list_troubleshooting_session(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_troubleshooting_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TroubleshootingSession objects
        api_response = api_instance.list_troubleshooting_session(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringTroubleshootingSessionList**](MonitoringTroubleshootingSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **list_troubleshooting_session1**
> MonitoringTroubleshootingSessionList list_troubleshooting_session1()

List TroubleshootingSession objects

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session_list import MonitoringTroubleshootingSessionList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TroubleshootingSession objects
        api_response = api_instance.list_troubleshooting_session1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->list_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringTroubleshootingSessionList**](MonitoringTroubleshootingSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert**
> MonitoringAlert update_alert(o_tenant, o_name, body)

Update Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringAlert(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertSpec(
            state="open",
        ),
        status=MonitoringAlertStatus(
            acknowledged=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            event_uri="event_uri_example",
            message="message_example",
            object_ref=ApiObjectRef(
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
                tenant="tenant_example",
                uri="uri_example",
            ),
            reason=MonitoringAlertReason(
                alert_policy_id="alert_policy_id_example",
                matched_requirements=[
                    MonitoringMatchedRequirement(
                        key="key_example",
                        observed_value="observed_value_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            resolved=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            severity="info",
            source=MonitoringAlertSource(
                component="component_example",
                node_name="node_name_example",
            ),
            total_hits=1,
        ),
    ) # MonitoringAlert | 

    # example passing only required values which don't have defaults set
    try:
        # Update Alert object
        api_response = api_instance.update_alert(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringAlert**](MonitoringAlert.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert1**
> MonitoringAlert update_alert1(o_name, body)

Update Alert object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlert(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertSpec(
            state="open",
        ),
        status=MonitoringAlertStatus(
            acknowledged=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            event_uri="event_uri_example",
            message="message_example",
            object_ref=ApiObjectRef(
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
                tenant="tenant_example",
                uri="uri_example",
            ),
            reason=MonitoringAlertReason(
                alert_policy_id="alert_policy_id_example",
                matched_requirements=[
                    MonitoringMatchedRequirement(
                        key="key_example",
                        observed_value="observed_value_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            resolved=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            severity="info",
            source=MonitoringAlertSource(
                component="component_example",
                node_name="node_name_example",
            ),
            total_hits=1,
        ),
    ) # MonitoringAlert | 

    # example passing only required values which don't have defaults set
    try:
        # Update Alert object
        api_response = api_instance.update_alert1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlert**](MonitoringAlert.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert_destination**
> MonitoringAlertDestination update_alert_destination(o_tenant, o_name, body)

Update AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertDestination object
        api_response = api_instance.update_alert_destination(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert_destination1**
> MonitoringAlertDestination update_alert_destination1(o_name, body)

Update AlertDestination object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_destination import MonitoringAlertDestination
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertDestination object
        api_response = api_instance.update_alert_destination1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert_policy**
> MonitoringAlertPolicy update_alert_policy(o_tenant, o_name, body)

Update AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertPolicy object
        api_response = api_instance.update_alert_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_alert_policy1**
> MonitoringAlertPolicy update_alert_policy1(o_name, body)

Update AlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertPolicy object
        api_response = api_instance.update_alert_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_audit_policy**
> MonitoringAuditPolicy update_audit_policy(o_tenant, body)

Update AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AuditPolicy object
        api_response = api_instance.update_audit_policy(o_tenant, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_audit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_audit_policy1**
> MonitoringAuditPolicy update_audit_policy1(body)

Update AuditPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_audit_policy import MonitoringAuditPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AuditPolicy object
        api_response = api_instance.update_audit_policy1(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_audit_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_event_policy**
> MonitoringEventPolicy update_event_policy(o_tenant, o_name, body)

Update EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update EventPolicy object
        api_response = api_instance.update_event_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_event_policy1**
> MonitoringEventPolicy update_event_policy1(o_name, body)

Update EventPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_event_policy import MonitoringEventPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update EventPolicy object
        api_response = api_instance.update_event_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_flow_export_policy**
> MonitoringFlowExportPolicy update_flow_export_policy(o_tenant, o_name, body)

Update FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
            vrf_name="vrf_name_example",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FlowExportPolicy object
        api_response = api_instance.update_flow_export_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_flow_export_policy1**
> MonitoringFlowExportPolicy update_flow_export_policy1(o_name, body)

Update FlowExportPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
            vrf_name="vrf_name_example",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FlowExportPolicy object
        api_response = api_instance.update_flow_export_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_fwlog_policy**
> MonitoringFwlogPolicy update_fwlog_policy(o_tenant, o_name, body)

Update FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FwlogPolicy object
        api_response = api_instance.update_fwlog_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_fwlog_policy1**
> MonitoringFwlogPolicy update_fwlog_policy1(o_name, body)

Update FwlogPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FwlogPolicy object
        api_response = api_instance.update_fwlog_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_mirror_session**
> MonitoringMirrorSession update_mirror_session(o_tenant, o_name, body)

Update MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update MirrorSession object
        api_response = api_instance.update_mirror_session(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_mirror_session1**
> MonitoringMirrorSession update_mirror_session1(o_name, body)

Update MirrorSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update MirrorSession object
        api_response = api_instance.update_mirror_session1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_stats_alert_policy**
> MonitoringStatsAlertPolicy update_stats_alert_policy(o_tenant, o_name, body)

Update StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update StatsAlertPolicy object
        api_response = api_instance.update_stats_alert_policy(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_stats_alert_policy1**
> MonitoringStatsAlertPolicy update_stats_alert_policy1(o_name, body)

Update StatsAlertPolicy object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update StatsAlertPolicy object
        api_response = api_instance.update_stats_alert_policy1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_troubleshooting_session**
> MonitoringTroubleshootingSession update_troubleshooting_session(o_tenant, o_name, body)

Update TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.Name_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update TroubleshootingSession object
        api_response = api_instance.update_troubleshooting_session(o_tenant, o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_troubleshooting_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **update_troubleshooting_session1**
> MonitoringTroubleshootingSession update_troubleshooting_session1(o_name, body)

Update TroubleshootingSession object

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update TroubleshootingSession object
        api_response = api_instance.update_troubleshooting_session1(o_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->update_troubleshooting_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert**
> MonitoringAutoMsgAlertWatchHelper watch_alert(o_tenant)

Watch Alert objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_watch_helper import MonitoringAutoMsgAlertWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Alert objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Alert objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertWatchHelper**](MonitoringAutoMsgAlertWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert1**
> MonitoringAutoMsgAlertWatchHelper watch_alert1()

Watch Alert objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_watch_helper import MonitoringAutoMsgAlertWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch Alert objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertWatchHelper**](MonitoringAutoMsgAlertWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert_destination**
> MonitoringAutoMsgAlertDestinationWatchHelper watch_alert_destination(o_tenant)

Watch AlertDestination objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_destination_watch_helper import MonitoringAutoMsgAlertDestinationWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertDestination objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_destination(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_destination: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AlertDestination objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_destination(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertDestinationWatchHelper**](MonitoringAutoMsgAlertDestinationWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert_destination1**
> MonitoringAutoMsgAlertDestinationWatchHelper watch_alert_destination1()

Watch AlertDestination objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_destination_watch_helper import MonitoringAutoMsgAlertDestinationWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AlertDestination objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_destination1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_destination1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertDestinationWatchHelper**](MonitoringAutoMsgAlertDestinationWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert_policy**
> MonitoringAutoMsgAlertPolicyWatchHelper watch_alert_policy(o_tenant)

Watch AlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_policy_watch_helper import MonitoringAutoMsgAlertPolicyWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertPolicyWatchHelper**](MonitoringAutoMsgAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_alert_policy1**
> MonitoringAutoMsgAlertPolicyWatchHelper watch_alert_policy1()

Watch AlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_alert_policy_watch_helper import MonitoringAutoMsgAlertPolicyWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAlertPolicyWatchHelper**](MonitoringAutoMsgAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_archive_request**
> MonitoringAutoMsgArchiveRequestWatchHelper watch_archive_request(o_tenant)

Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_archive_request_watch_helper import MonitoringAutoMsgArchiveRequestWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_archive_request(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_archive_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_archive_request(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_archive_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgArchiveRequestWatchHelper**](MonitoringAutoMsgArchiveRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_archive_request1**
> MonitoringAutoMsgArchiveRequestWatchHelper watch_archive_request1()

Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_archive_request_watch_helper import MonitoringAutoMsgArchiveRequestWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_archive_request1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_archive_request1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgArchiveRequestWatchHelper**](MonitoringAutoMsgArchiveRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_audit_policy**
> MonitoringAutoMsgAuditPolicyWatchHelper watch_audit_policy(o_tenant)

Watch AuditPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_audit_policy_watch_helper import MonitoringAutoMsgAuditPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_audit_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_audit_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_audit_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_audit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAuditPolicyWatchHelper**](MonitoringAutoMsgAuditPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_audit_policy1**
> MonitoringAutoMsgAuditPolicyWatchHelper watch_audit_policy1()

Watch AuditPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_audit_policy_watch_helper import MonitoringAutoMsgAuditPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_audit_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_audit_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgAuditPolicyWatchHelper**](MonitoringAutoMsgAuditPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_event_policy**
> MonitoringAutoMsgEventPolicyWatchHelper watch_event_policy(o_tenant)

Watch EventPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_event_policy_watch_helper import MonitoringAutoMsgEventPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch EventPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_event_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_event_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch EventPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_event_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_event_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgEventPolicyWatchHelper**](MonitoringAutoMsgEventPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_event_policy1**
> MonitoringAutoMsgEventPolicyWatchHelper watch_event_policy1()

Watch EventPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_event_policy_watch_helper import MonitoringAutoMsgEventPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch EventPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_event_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_event_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgEventPolicyWatchHelper**](MonitoringAutoMsgEventPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_flow_export_policy**
> MonitoringAutoMsgFlowExportPolicyWatchHelper watch_flow_export_policy(o_tenant)

Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_flow_export_policy_watch_helper import MonitoringAutoMsgFlowExportPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_flow_export_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_flow_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_flow_export_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_flow_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgFlowExportPolicyWatchHelper**](MonitoringAutoMsgFlowExportPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_flow_export_policy1**
> MonitoringAutoMsgFlowExportPolicyWatchHelper watch_flow_export_policy1()

Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_flow_export_policy_watch_helper import MonitoringAutoMsgFlowExportPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_flow_export_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_flow_export_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgFlowExportPolicyWatchHelper**](MonitoringAutoMsgFlowExportPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_fwlog_policy**
> MonitoringAutoMsgFwlogPolicyWatchHelper watch_fwlog_policy(o_tenant)

Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_fwlog_policy_watch_helper import MonitoringAutoMsgFwlogPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_fwlog_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_fwlog_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_fwlog_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_fwlog_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgFwlogPolicyWatchHelper**](MonitoringAutoMsgFwlogPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_fwlog_policy1**
> MonitoringAutoMsgFwlogPolicyWatchHelper watch_fwlog_policy1()

Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pensando_dss.psm_dss.model.monitoring_auto_msg_fwlog_policy_watch_helper import MonitoringAutoMsgFwlogPolicyWatchHelper
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_fwlog_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_fwlog_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgFwlogPolicyWatchHelper**](MonitoringAutoMsgFwlogPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_mirror_session**
> MonitoringAutoMsgMirrorSessionWatchHelper watch_mirror_session(o_tenant)

Watch MirrorSession objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_mirror_session_watch_helper import MonitoringAutoMsgMirrorSessionWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch MirrorSession objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_mirror_session(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_mirror_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch MirrorSession objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_mirror_session(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_mirror_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgMirrorSessionWatchHelper**](MonitoringAutoMsgMirrorSessionWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_mirror_session1**
> MonitoringAutoMsgMirrorSessionWatchHelper watch_mirror_session1()

Watch MirrorSession objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_mirror_session_watch_helper import MonitoringAutoMsgMirrorSessionWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch MirrorSession objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_mirror_session1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_mirror_session1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgMirrorSessionWatchHelper**](MonitoringAutoMsgMirrorSessionWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_stats_alert_policy**
> MonitoringAutoMsgStatsAlertPolicyWatchHelper watch_stats_alert_policy(o_tenant)

Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_stats_alert_policy_watch_helper import MonitoringAutoMsgStatsAlertPolicyWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_stats_alert_policy(o_tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_stats_alert_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_stats_alert_policy(o_tenant, o_name=o_name, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_stats_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgStatsAlertPolicyWatchHelper**](MonitoringAutoMsgStatsAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_stats_alert_policy1**
> MonitoringAutoMsgStatsAlertPolicyWatchHelper watch_stats_alert_policy1()

Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_stats_alert_policy_watch_helper import MonitoringAutoMsgStatsAlertPolicyWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_stats_alert_policy1(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_stats_alert_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgStatsAlertPolicyWatchHelper**](MonitoringAutoMsgStatsAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

# **watch_tech_support_request**
> MonitoringAutoMsgTechSupportRequestWatchHelper watch_tech_support_request()

Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll

### Example

```python
#!/usr/bin/env python3
import time
import .psm_dss
from pensando_dss.psm_dss.api import monitoring_v1_api
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.models.monitoring import *
from pensando_dss.psm_dss  import Configuration, ApiClient, ApiException
from dateutil.parser import parse as dateutil_parser
from pensando_dss.psm_dss.model.monitoring_auto_msg_tech_support_request_watch_helper import MonitoringAutoMsgTechSupportRequestWatchHelper
from pensando_dss.psm_dss.model.api_status import ApiStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm_dss.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_tech_support_request(o_name=o_name, o_tenant=o_tenant, o_namespace=o_namespace, o_generation_id=o_generation_id, o_resource_version=o_resource_version, o_uuid=o_uuid, o_creation_time=o_creation_time, o_mod_time=o_mod_time, o_self_link=o_self_link, label_selector=label_selector, field_selector=field_selector, field_change_selector=field_change_selector, _from=_from, max_results=max_results, sort_order=sort_order, meta_only=meta_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_tech_support_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_tenant** | **str**| Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. | [optional]
 **o_namespace** | **str**| Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_generation_id** | **str**| GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. | [optional]
 **o_resource_version** | **str**| Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. | [optional]
 **o_uuid** | **str**| UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **o_mod_time** | **datetime**| ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. | [optional]
 **o_self_link** | **str**| SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \&quot;/v1/tenants/tenants/tenant2\&quot; System generated and updated, not updatable by user. | [optional]
 **label_selector** | **str**| LabelSelector to select on labels in list or watch results. | [optional]
 **field_selector** | **str**| FieldSelector to select on field values in list or watch results. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]
 **_from** | **int**| From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From &#x3D; 0, the server will attempt to return all the results in the list without pagination. | [optional]
 **max_results** | **int**| MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. | [optional]
 **sort_order** | **str**| order to sort List results in. | [optional]
 **meta_only** | **bool**| If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. | [optional]

### Return type

[**MonitoringAutoMsgTechSupportRequestWatchHelper**](MonitoringAutoMsgTechSupportRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to psm_dss.MonitoringV1Api top]](#psm_dss.MonitoringV1Api) [[Back to monitoring README]](../psm_dss/docs/monitoring/README.md) [[Back to pensando_dss README]](../README.md)

