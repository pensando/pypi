"""
    Sysruntime API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.sysruntime_flow_status import SysruntimeFlowStatus
from pensando_ent.psm.model.sysruntime_fw_status import SysruntimeFwStatus
from pensando_ent.psm.model.sysruntime_ip_sec_status import SysruntimeIPSecStatus
globals()['SysruntimeFlowStatus'] = SysruntimeFlowStatus
globals()['SysruntimeFwStatus'] = SysruntimeFwStatus
globals()['SysruntimeIPSecStatus'] = SysruntimeIPSecStatus
from pensando_ent.psm.psm.model.sysruntime_hw_connection_status import SysruntimeHWConnectionStatus


class TestSysruntimeHWConnectionStatus(unittest.TestCase):
    """SysruntimeHWConnectionStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSysruntimeHWConnectionStatus(self):
        """Test SysruntimeHWConnectionStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SysruntimeHWConnectionStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()