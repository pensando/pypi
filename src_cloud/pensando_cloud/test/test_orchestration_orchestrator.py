"""
    Orchestration API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.orchestration_orchestrator_spec import OrchestrationOrchestratorSpec
from pensando_cloud.psm_cloud.model.orchestration_orchestrator_status import OrchestrationOrchestratorStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['OrchestrationOrchestratorSpec'] = OrchestrationOrchestratorSpec
globals()['OrchestrationOrchestratorStatus'] = OrchestrationOrchestratorStatus
from pensando_cloud.psm_cloud.psm_cloud.model.orchestration_orchestrator import OrchestrationOrchestrator


class TestOrchestrationOrchestrator(unittest.TestCase):
    """OrchestrationOrchestrator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrchestrationOrchestrator(self):
        """Test OrchestrationOrchestrator"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrchestrationOrchestrator()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
