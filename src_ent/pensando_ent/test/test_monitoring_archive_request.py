"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_ent
from pensando_ent.psm_ent.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm_ent.model.monitoring_archive_request_spec import MonitoringArchiveRequestSpec
from pensando_ent.psm_ent.model.monitoring_archive_request_status import MonitoringArchiveRequestStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringArchiveRequestSpec'] = MonitoringArchiveRequestSpec
globals()['MonitoringArchiveRequestStatus'] = MonitoringArchiveRequestStatus
from pensando_ent.psm_ent.psm_ent.model.monitoring_archive_request import MonitoringArchiveRequest


class TestMonitoringArchiveRequest(unittest.TestCase):
    """MonitoringArchiveRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringArchiveRequest(self):
        """Test MonitoringArchiveRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringArchiveRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
