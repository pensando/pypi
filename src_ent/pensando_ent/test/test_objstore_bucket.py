"""
    Objstore API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.objstore_bucket_spec import ObjstoreBucketSpec
from pensando_ent.psm.model.objstore_bucket_status import ObjstoreBucketStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ObjstoreBucketSpec'] = ObjstoreBucketSpec
globals()['ObjstoreBucketStatus'] = ObjstoreBucketStatus
from pensando_ent.psm.psm.model.objstore_bucket import ObjstoreBucket


class TestObjstoreBucket(unittest.TestCase):
    """ObjstoreBucket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testObjstoreBucket(self):
        """Test ObjstoreBucket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ObjstoreBucket()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
