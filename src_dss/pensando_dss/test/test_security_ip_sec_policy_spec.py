"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.security_ip_sec_config import SecurityIPSecConfig
from pensando_dss.psm.model.security_ip_sec_policy_rule import SecurityIPSecPolicyRule
from pensando_dss.psm.model.security_tunnel_endpoint import SecurityTunnelEndpoint
globals()['SecurityIPSecConfig'] = SecurityIPSecConfig
globals()['SecurityIPSecPolicyRule'] = SecurityIPSecPolicyRule
globals()['SecurityTunnelEndpoint'] = SecurityTunnelEndpoint
from pensando_dss.psm.psm.model.security_ip_sec_policy_spec import SecurityIPSecPolicySpec


class TestSecurityIPSecPolicySpec(unittest.TestCase):
    """SecurityIPSecPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityIPSecPolicySpec(self):
        """Test SecurityIPSecPolicySpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityIPSecPolicySpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
