"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.network_network_interface_host_status import NetworkNetworkInterfaceHostStatus
from pensando_cloud.psm_cloud.model.network_network_interface_uplink_status import NetworkNetworkInterfaceUplinkStatus
from pensando_cloud.psm_cloud.model.security_propagation_status import SecurityPropagationStatus
globals()['NetworkNetworkInterfaceHostStatus'] = NetworkNetworkInterfaceHostStatus
globals()['NetworkNetworkInterfaceUplinkStatus'] = NetworkNetworkInterfaceUplinkStatus
globals()['SecurityPropagationStatus'] = SecurityPropagationStatus
from pensando_cloud.psm_cloud.psm_cloud.model.network_network_interface_status import NetworkNetworkInterfaceStatus


class TestNetworkNetworkInterfaceStatus(unittest.TestCase):
    """NetworkNetworkInterfaceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkNetworkInterfaceStatus(self):
        """Test NetworkNetworkInterfaceStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkNetworkInterfaceStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
