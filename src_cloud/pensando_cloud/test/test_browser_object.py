"""
    Browser API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.object_uris import ObjectURIs
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ObjectURIs'] = ObjectURIs
from pensando_cloud.psm_cloud.psm_cloud.model.browser_object import BrowserObject


class TestBrowserObject(unittest.TestCase):
    """BrowserObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBrowserObject(self):
        """Test BrowserObject"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BrowserObject()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
