"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.monitoring_flow_export_policy_spec import MonitoringFlowExportPolicySpec
from pensando_cloud.psm_cloud.model.monitoring_flow_export_policy_status import MonitoringFlowExportPolicyStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringFlowExportPolicySpec'] = MonitoringFlowExportPolicySpec
globals()['MonitoringFlowExportPolicyStatus'] = MonitoringFlowExportPolicyStatus
from pensando_cloud.psm_cloud.psm_cloud.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy


class TestMonitoringFlowExportPolicy(unittest.TestCase):
    """MonitoringFlowExportPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringFlowExportPolicy(self):
        """Test MonitoringFlowExportPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringFlowExportPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
