"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.monitoring_troubleshooting_session_spec import MonitoringTroubleshootingSessionSpec
from pensando_cloud.psm.model.monitoring_troubleshooting_session_status import MonitoringTroubleshootingSessionStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringTroubleshootingSessionSpec'] = MonitoringTroubleshootingSessionSpec
globals()['MonitoringTroubleshootingSessionStatus'] = MonitoringTroubleshootingSessionStatus
from pensando_cloud.psm.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession


class TestMonitoringTroubleshootingSession(unittest.TestCase):
    """MonitoringTroubleshootingSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringTroubleshootingSession(self):
        """Test MonitoringTroubleshootingSession"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringTroubleshootingSession()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
