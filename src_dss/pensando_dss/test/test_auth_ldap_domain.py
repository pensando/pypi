"""
    Auth API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.auth_ldap_attribute_mapping import AuthLdapAttributeMapping
from pensando_dss.psm.model.auth_ldap_server import AuthLdapServer
globals()['AuthLdapAttributeMapping'] = AuthLdapAttributeMapping
globals()['AuthLdapServer'] = AuthLdapServer
from pensando_dss.psm.psm.model.auth_ldap_domain import AuthLdapDomain


class TestAuthLdapDomain(unittest.TestCase):
    """AuthLdapDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthLdapDomain(self):
        """Test AuthLdapDomain"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthLdapDomain()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()