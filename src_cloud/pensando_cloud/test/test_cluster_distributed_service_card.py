"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.cluster_distributed_service_card_spec import ClusterDistributedServiceCardSpec
from pensando_cloud.psm.model.cluster_distributed_service_card_status import ClusterDistributedServiceCardStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterDistributedServiceCardSpec'] = ClusterDistributedServiceCardSpec
globals()['ClusterDistributedServiceCardStatus'] = ClusterDistributedServiceCardStatus
from pensando_cloud.psm.psm.model.cluster_distributed_service_card import ClusterDistributedServiceCard


class TestClusterDistributedServiceCard(unittest.TestCase):
    """ClusterDistributedServiceCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterDistributedServiceCard(self):
        """Test ClusterDistributedServiceCard"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterDistributedServiceCard()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
