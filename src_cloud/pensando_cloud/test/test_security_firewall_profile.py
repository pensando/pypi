"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.security_firewall_profile_spec import SecurityFirewallProfileSpec
from pensando_cloud.psm.model.security_firewall_profile_status import SecurityFirewallProfileStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['SecurityFirewallProfileSpec'] = SecurityFirewallProfileSpec
globals()['SecurityFirewallProfileStatus'] = SecurityFirewallProfileStatus
from pensando_cloud.psm.psm.model.security_firewall_profile import SecurityFirewallProfile


class TestSecurityFirewallProfile(unittest.TestCase):
    """SecurityFirewallProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityFirewallProfile(self):
        """Test SecurityFirewallProfile"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityFirewallProfile()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
