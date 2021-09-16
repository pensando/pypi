"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.security_dns import SecurityDns
from pensando_cloud.psm_cloud.model.security_ftp import SecurityFtp
from pensando_cloud.psm_cloud.model.security_icmp import SecurityIcmp
from pensando_cloud.psm_cloud.model.security_msrpc import SecurityMsrpc
from pensando_cloud.psm_cloud.model.security_sunrpc import SecuritySunrpc
globals()['SecurityDns'] = SecurityDns
globals()['SecurityFtp'] = SecurityFtp
globals()['SecurityIcmp'] = SecurityIcmp
globals()['SecurityMsrpc'] = SecurityMsrpc
globals()['SecuritySunrpc'] = SecuritySunrpc
from pensando_cloud.psm_cloud.psm_cloud.model.security_alg import SecurityALG


class TestSecurityALG(unittest.TestCase):
    """SecurityALG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityALG(self):
        """Test SecurityALG"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityALG()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
