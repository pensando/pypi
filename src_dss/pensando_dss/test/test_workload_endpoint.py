"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm.model.workload_endpoint_spec import WorkloadEndpointSpec
from pensando_dss.psm.model.workload_endpoint_status import WorkloadEndpointStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['WorkloadEndpointSpec'] = WorkloadEndpointSpec
globals()['WorkloadEndpointStatus'] = WorkloadEndpointStatus
from pensando_dss.psm.psm.model.workload_endpoint import WorkloadEndpoint


class TestWorkloadEndpoint(unittest.TestCase):
    """WorkloadEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkloadEndpoint(self):
        """Test WorkloadEndpoint"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkloadEndpoint()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
