"""
    Staging API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.staging_item import StagingItem
from pensando_cloud.psm.model.staging_validation_error import StagingValidationError
globals()['StagingItem'] = StagingItem
globals()['StagingValidationError'] = StagingValidationError
from pensando_cloud.psm.psm.model.staging_buffer_status import StagingBufferStatus


class TestStagingBufferStatus(unittest.TestCase):
    """StagingBufferStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStagingBufferStatus(self):
        """Test StagingBufferStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StagingBufferStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
