"""
    Diagnostics API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.diagnostics_module_spec import DiagnosticsModuleSpec
from pensando_ent.psm.model.diagnostics_module_status import DiagnosticsModuleStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['DiagnosticsModuleSpec'] = DiagnosticsModuleSpec
globals()['DiagnosticsModuleStatus'] = DiagnosticsModuleStatus
from pensando_ent.psm.psm.model.diagnostics_module import DiagnosticsModule


class TestDiagnosticsModule(unittest.TestCase):
    """DiagnosticsModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDiagnosticsModule(self):
        """Test DiagnosticsModule"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DiagnosticsModule()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
