"""
    Sysruntime API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_list_watch_options import ApiListWatchOptions
from pensando_dss.psm.model.sysruntime_connection_filter import SysruntimeConnectionFilter
globals()['ApiListWatchOptions'] = ApiListWatchOptions
globals()['SysruntimeConnectionFilter'] = SysruntimeConnectionFilter
from pensando_dss.psm.psm.model.sysruntime_connection_request import SysruntimeConnectionRequest


class TestSysruntimeConnectionRequest(unittest.TestCase):
    """SysruntimeConnectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSysruntimeConnectionRequest(self):
        """Test SysruntimeConnectionRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SysruntimeConnectionRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()