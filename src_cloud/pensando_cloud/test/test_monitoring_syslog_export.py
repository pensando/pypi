"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.monitoring_export_config import MonitoringExportConfig
from pensando_cloud.psm_cloud.model.monitoring_syslog_export_config import MonitoringSyslogExportConfig
globals()['MonitoringExportConfig'] = MonitoringExportConfig
globals()['MonitoringSyslogExportConfig'] = MonitoringSyslogExportConfig
from pensando_cloud.psm_cloud.psm_cloud.model.monitoring_syslog_export import MonitoringSyslogExport


class TestMonitoringSyslogExport(unittest.TestCase):
    """MonitoringSyslogExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringSyslogExport(self):
        """Test MonitoringSyslogExport"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringSyslogExport()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
