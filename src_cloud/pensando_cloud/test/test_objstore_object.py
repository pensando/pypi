"""
    Objstore API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.objstore_object_spec import ObjstoreObjectSpec
from pensando_cloud.psm.model.objstore_object_status import ObjstoreObjectStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ObjstoreObjectSpec'] = ObjstoreObjectSpec
globals()['ObjstoreObjectStatus'] = ObjstoreObjectStatus
from pensando_cloud.psm.psm.model.objstore_object import ObjstoreObject


class TestObjstoreObject(unittest.TestCase):
    """ObjstoreObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testObjstoreObject(self):
        """Test ObjstoreObject"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ObjstoreObject()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
