"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.fields_selector import FieldsSelector
from pensando_dss.psm.model.monitoring_export_config import MonitoringExportConfig
from pensando_dss.psm.model.monitoring_syslog_export_config import MonitoringSyslogExportConfig
globals()['FieldsSelector'] = FieldsSelector
globals()['MonitoringExportConfig'] = MonitoringExportConfig
globals()['MonitoringSyslogExportConfig'] = MonitoringSyslogExportConfig
from pensando_dss.psm.psm.model.monitoring_event_policy_spec import MonitoringEventPolicySpec


class TestMonitoringEventPolicySpec(unittest.TestCase):
    """MonitoringEventPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringEventPolicySpec(self):
        """Test MonitoringEventPolicySpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringEventPolicySpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()