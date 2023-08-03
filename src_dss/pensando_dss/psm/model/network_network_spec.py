"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_dss.psm.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from pensando_dss.psm.model.network_network_firewall_profile import NetworkNetworkFirewallProfile
    from pensando_dss.psm.model.network_orchestrator_info import NetworkOrchestratorInfo
    from pensando_dss.psm.model.network_rd_spec import NetworkRDSpec
    globals()['NetworkNetworkFirewallProfile'] = NetworkNetworkFirewallProfile
    globals()['NetworkOrchestratorInfo'] = NetworkOrchestratorInfo
    globals()['NetworkRDSpec'] = NetworkRDSpec


class NetworkNetworkSpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('allow_session_reuse',): {
            'INHERIT_FROM_VRF': "inherit_from_vrf",
            'DISABLE': "disable",
            'ENABLE': "enable",
        },
        ('type',): {
            'BRIDGED': "bridged",
            'ROUTED': "routed",
        },
    }

    validations = {
        ('vlan_id',): {
            'inclusive_maximum': 4095,
            'inclusive_minimum': 0,
        },
        ('vxlan_vni',): {
            'inclusive_maximum': 16777215,
            'inclusive_minimum': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'allow_session_reuse': (str,),  # noqa: E501
            'egress_security_policy': ([str],),  # noqa: E501
            'firewall_profile': (NetworkNetworkFirewallProfile,),  # noqa: E501
            'ingress_security_policy': ([str],),  # noqa: E501
            'ipam_policy': (str,),  # noqa: E501
            'ipv4_gateway': (str,),  # noqa: E501
            'ipv4_subnet': (str,),  # noqa: E501
            'ipv6_gateway': (str,),  # noqa: E501
            'ipv6_subnet': (str,),  # noqa: E501
            'orchestrators': ([NetworkOrchestratorInfo],),  # noqa: E501
            'route_import_export': (NetworkRDSpec,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'virtual_router': (str,),  # noqa: E501
            'vlan_id': (int,),  # noqa: E501
            'vxlan_vni': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_session_reuse': 'allow-session-reuse',  # noqa: E501
        'egress_security_policy': 'egress-security-policy',  # noqa: E501
        'firewall_profile': 'firewall-profile',  # noqa: E501
        'ingress_security_policy': 'ingress-security-policy',  # noqa: E501
        'ipam_policy': 'ipam-policy',  # noqa: E501
        'ipv4_gateway': 'ipv4-gateway',  # noqa: E501
        'ipv4_subnet': 'ipv4-subnet',  # noqa: E501
        'ipv6_gateway': 'ipv6-gateway',  # noqa: E501
        'ipv6_subnet': 'ipv6-subnet',  # noqa: E501
        'orchestrators': 'orchestrators',  # noqa: E501
        'route_import_export': 'route-import-export',  # noqa: E501
        'type': 'type',  # noqa: E501
        'virtual_router': 'virtual-router',  # noqa: E501
        'vlan_id': 'vlan-id',  # noqa: E501
        'vxlan_vni': 'vxlan-vni',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """NetworkNetworkSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            allow_session_reuse (str): AllowSessionReuse helps to handle TCP half open state connections. When there is mismatch in TCP connection state between client, server and DSE, and client tries to establish a new connection with same 5 tuple with source port reuse, typically DSE would drop the new connection attempts without AllowSessionReuse being enabled. With AllowSessionReuse turned ON, DSE will relax the TCP state/sequence number checks to allow the new connection to go through. AllowSessionReuseMode can be INHERIT_FROM_VRF, DISABLE or ENABLE. INHERIT_FROM_VRF is the default value.. [optional] if omitted the server will use the default value of "inherit_from_vrf"  # noqa: E501
            egress_security_policy ([str]): Security Policy to apply in the egress direction.. [optional]  # noqa: E501
            firewall_profile (NetworkNetworkFirewallProfile): [optional]  # noqa: E501
            ingress_security_policy ([str]): Security Policy to apply in the ingress direction.. [optional]  # noqa: E501
            ipam_policy (str): Relay Configuration if any.. [optional]  # noqa: E501
            ipv4_gateway (str): IPv4 gateway for this subnet. Should be a valid v4 or v6 IP address.. [optional]  # noqa: E501
            ipv4_subnet (str): IPv4 subnet CIDR. Should be a valid v4 or v6 CIDR block.. [optional]  # noqa: E501
            ipv6_gateway (str): IPv6 gateway.. [optional]  # noqa: E501
            ipv6_subnet (str): IPv6 subnet CIDR.. [optional]  # noqa: E501
            orchestrators ([NetworkOrchestratorInfo]): If supplied, this network will only be applied to the orchestrators specified.. [optional]  # noqa: E501
            route_import_export (NetworkRDSpec): [optional]  # noqa: E501
            type (str): type of network. (vlan/vxlan/routed etc).. [optional] if omitted the server will use the default value of "bridged"  # noqa: E501
            virtual_router (str): VirtualRouter specifies the VRF this network belongs to.. [optional]  # noqa: E501
            vlan_id (int): Vlan ID for the network. Value should be between 0 and 4095.. [optional]  # noqa: E501
            vxlan_vni (int): Vxlan VNI for the network. Value should be between 0 and 16777215.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
