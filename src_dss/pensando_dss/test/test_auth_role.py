"""
    Auth API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm.model.auth_role_spec import AuthRoleSpec
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['AuthRoleSpec'] = AuthRoleSpec
from pensando_dss.psm.psm.model.auth_role import AuthRole


class TestAuthRole(unittest.TestCase):
    """AuthRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthRole(self):
        """Test AuthRole"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthRole()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
