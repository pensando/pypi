"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_list_meta import ApiListMeta
from pensando_dss.psm.model.security_certificate import SecurityCertificate
globals()['ApiListMeta'] = ApiListMeta
globals()['SecurityCertificate'] = SecurityCertificate
from pensando_dss.psm.psm.model.security_certificate_list import SecurityCertificateList


class TestSecurityCertificateList(unittest.TestCase):
    """SecurityCertificateList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityCertificateList(self):
        """Test SecurityCertificateList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityCertificateList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
