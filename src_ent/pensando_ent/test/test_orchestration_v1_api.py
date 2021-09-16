"""
    Orchestration API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm_ent
from pensando_ent.psm_ent.api.orchestration_v1_api import OrchestrationV1Api  # noqa: E501


class TestOrchestrationV1Api(unittest.TestCase):
    """OrchestrationV1Api unit test stubs"""

    def setUp(self):
        self.api = OrchestrationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_orchestrator(self):
        """Test case for add_orchestrator

        Create Orchestrator object  # noqa: E501
        """
        pass

    def test_delete_orchestrator(self):
        """Test case for delete_orchestrator

        Delete Orchestrator object  # noqa: E501
        """
        pass

    def test_get_orchestrator(self):
        """Test case for get_orchestrator

        Get Orchestrator object  # noqa: E501
        """
        pass

    def test_label_orchestrator(self):
        """Test case for label_orchestrator

        Label Orchestrator object  # noqa: E501
        """
        pass

    def test_list_orchestrator(self):
        """Test case for list_orchestrator

        List Orchestrator objects  # noqa: E501
        """
        pass

    def test_update_orchestrator(self):
        """Test case for update_orchestrator

        Update Orchestrator object  # noqa: E501
        """
        pass

    def test_watch_orchestrator(self):
        """Test case for watch_orchestrator

        Watch Orchestrator objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
