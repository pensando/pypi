"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.security_alg import SecurityALG
from pensando_dss.psm.model.security_proto_port import SecurityProtoPort
globals()['SecurityALG'] = SecurityALG
globals()['SecurityProtoPort'] = SecurityProtoPort
from pensando_dss.psm.psm.model.security_app_spec import SecurityAppSpec


class TestSecurityAppSpec(unittest.TestCase):
    """SecurityAppSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityAppSpec(self):
        """Test SecurityAppSpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityAppSpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()