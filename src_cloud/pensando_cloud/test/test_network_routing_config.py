"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.network_routing_config_spec import NetworkRoutingConfigSpec
from pensando_cloud.psm.model.network_routing_config_status import NetworkRoutingConfigStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['NetworkRoutingConfigSpec'] = NetworkRoutingConfigSpec
globals()['NetworkRoutingConfigStatus'] = NetworkRoutingConfigStatus
from pensando_cloud.psm.psm.model.network_routing_config import NetworkRoutingConfig


class TestNetworkRoutingConfig(unittest.TestCase):
    """NetworkRoutingConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkRoutingConfig(self):
        """Test NetworkRoutingConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkRoutingConfig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
