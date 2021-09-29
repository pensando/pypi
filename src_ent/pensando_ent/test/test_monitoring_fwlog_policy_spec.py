"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.monitoring_export_config import MonitoringExportConfig
from pensando_ent.psm.model.monitoring_psm_export_target import MonitoringPSMExportTarget
from pensando_ent.psm.model.monitoring_syslog_export_config import MonitoringSyslogExportConfig
globals()['MonitoringExportConfig'] = MonitoringExportConfig
globals()['MonitoringPSMExportTarget'] = MonitoringPSMExportTarget
globals()['MonitoringSyslogExportConfig'] = MonitoringSyslogExportConfig
from pensando_ent.psm.psm.model.monitoring_fwlog_policy_spec import MonitoringFwlogPolicySpec


class TestMonitoringFwlogPolicySpec(unittest.TestCase):
    """MonitoringFwlogPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringFwlogPolicySpec(self):
        """Test MonitoringFwlogPolicySpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringFwlogPolicySpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()