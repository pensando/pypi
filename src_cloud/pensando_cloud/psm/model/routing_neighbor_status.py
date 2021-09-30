"""
    Routing API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_cloud.psm.model_utils import (  # noqa: F401
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


class RoutingNeighborStatus(ModelNormal):
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
        ('prev_status',): {
            'IDLE': "idle",
            'CONNECT': "connect",
            'ACTIVE': "active",
            'OPENSENT': "opensent",
            'OPENCONFIRMED': "openconfirmed",
            'ESTABLISHED': "established",
        },
        ('sellocaladdrtype',): {
            'OTHER': "other",
            'IPV4': "ipv4",
            'IPV6': "ipv6",
            'NSAP': "nsap",
            'HDLC': "hdlc",
            'BBN1822': "bbn1822",
            'IEEE802': "ieee802",
            'E163': "e163",
            'E164': "e164",
            'F69': "f69",
            'X121': "x121",
            'IPX': "ipx",
            'APPLETALK': "appletalk",
            'DECNETIV': "decnetiv",
            'BANYANVIN': "banyanvin",
            'E164_NSAP': "e164_nsap",
            'IPV4_TNA': "ipv4_tna",
            'IPV6_TNA': "ipv6_tna",
            'NSAP_TNA': "nsap_tna",
            'VPN_IPV4': "vpn_ipv4",
            'VPN_IPV6': "vpn_ipv6",
            'L2VPN': "l2vpn",
        },
        ('status',): {
            'IDLE': "idle",
            'CONNECT': "connect",
            'ACTIVE': "active",
            'OPENSENT': "opensent",
            'OPENCONFIRMED': "openconfirmed",
            'ESTABLISHED': "established",
        },
    }

    validations = {
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
        return {
            'capsneg': (str,),  # noqa: E501
            'capsrcvd': (str,),  # noqa: E501
            'capssent': (str,),  # noqa: E501
            'connectretrycount': (int,),  # noqa: E501
            'fsmestablishedtime': (str,),  # noqa: E501
            'fsmesttransitions': (int,),  # noqa: E501
            'holdtime': (int,),  # noqa: E501
            'inkeepalives': (int,),  # noqa: E501
            'innotifications': (int,),  # noqa: E501
            'inopens': (int,),  # noqa: E501
            'inprfxes': (int,),  # noqa: E501
            'inprfxesexpwdr': (int,),  # noqa: E501
            'inprfxesimpwdr': (int,),  # noqa: E501
            'inrefreshes': (int,),  # noqa: E501
            'intotalmessages': (int,),  # noqa: E501
            'inupdates': (int,),  # noqa: E501
            'inupdateselpstime': (int,),  # noqa: E501
            'keepalive': (int,),  # noqa: E501
            'lasterrorrcvd': (str,),  # noqa: E501
            'lasterrorsent': (str,),  # noqa: E501
            'localaddr': (str,),  # noqa: E501
            'orfentrycount': (int,),  # noqa: E501
            'outkeepalives': (int,),  # noqa: E501
            'outnotifications': (int,),  # noqa: E501
            'outopens': (int,),  # noqa: E501
            'outprfxes': (int,),  # noqa: E501
            'outprfxesdenied': (int,),  # noqa: E501
            'outprfxesexpwdr': (int,),  # noqa: E501
            'outprfxesimpwdr': (int,),  # noqa: E501
            'outrefreshes': (int,),  # noqa: E501
            'outtotalmessages': (int,),  # noqa: E501
            'outupdateelpstime': (int,),  # noqa: E501
            'outupdates': (int,),  # noqa: E501
            'peergr': (int,),  # noqa: E501
            'peerindex': (int,),  # noqa: E501
            'prev_status': (str,),  # noqa: E501
            'rcvdmsgelpstime': (int,),  # noqa: E501
            'receivedholdtime': (int,),  # noqa: E501
            'routerefrrcvd': (int,),  # noqa: E501
            'routerefrsent': (int,),  # noqa: E501
            'sellocaladdrtype': (str,),  # noqa: E501
            'stalepathtime': (int,),  # noqa: E501
            'status': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'capsneg': 'capsneg',  # noqa: E501
        'capsrcvd': 'capsrcvd',  # noqa: E501
        'capssent': 'capssent',  # noqa: E501
        'connectretrycount': 'connectretrycount',  # noqa: E501
        'fsmestablishedtime': 'fsmestablishedtime',  # noqa: E501
        'fsmesttransitions': 'fsmesttransitions',  # noqa: E501
        'holdtime': 'holdtime',  # noqa: E501
        'inkeepalives': 'inkeepalives',  # noqa: E501
        'innotifications': 'innotifications',  # noqa: E501
        'inopens': 'inopens',  # noqa: E501
        'inprfxes': 'inprfxes',  # noqa: E501
        'inprfxesexpwdr': 'inprfxesexpwdr',  # noqa: E501
        'inprfxesimpwdr': 'inprfxesimpwdr',  # noqa: E501
        'inrefreshes': 'inrefreshes',  # noqa: E501
        'intotalmessages': 'intotalmessages',  # noqa: E501
        'inupdates': 'inupdates',  # noqa: E501
        'inupdateselpstime': 'inupdateselpstime',  # noqa: E501
        'keepalive': 'keepalive',  # noqa: E501
        'lasterrorrcvd': 'lasterrorrcvd',  # noqa: E501
        'lasterrorsent': 'lasterrorsent',  # noqa: E501
        'localaddr': 'localaddr',  # noqa: E501
        'orfentrycount': 'orfentrycount',  # noqa: E501
        'outkeepalives': 'outkeepalives',  # noqa: E501
        'outnotifications': 'outnotifications',  # noqa: E501
        'outopens': 'outopens',  # noqa: E501
        'outprfxes': 'outprfxes',  # noqa: E501
        'outprfxesdenied': 'outprfxesdenied',  # noqa: E501
        'outprfxesexpwdr': 'outprfxesexpwdr',  # noqa: E501
        'outprfxesimpwdr': 'outprfxesimpwdr',  # noqa: E501
        'outrefreshes': 'outrefreshes',  # noqa: E501
        'outtotalmessages': 'outtotalmessages',  # noqa: E501
        'outupdateelpstime': 'outupdateelpstime',  # noqa: E501
        'outupdates': 'outupdates',  # noqa: E501
        'peergr': 'peergr',  # noqa: E501
        'peerindex': 'peerindex',  # noqa: E501
        'prev_status': 'prev-status',  # noqa: E501
        'rcvdmsgelpstime': 'rcvdmsgelpstime',  # noqa: E501
        'receivedholdtime': 'receivedholdtime',  # noqa: E501
        'routerefrrcvd': 'routerefrrcvd',  # noqa: E501
        'routerefrsent': 'routerefrsent',  # noqa: E501
        'sellocaladdrtype': 'sellocaladdrtype',  # noqa: E501
        'stalepathtime': 'stalepathtime',  # noqa: E501
        'status': 'status',  # noqa: E501
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
        """RoutingNeighborStatus - a model defined in OpenAPI

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
            capsneg (str): [optional]  # noqa: E501
            capsrcvd (str): [optional]  # noqa: E501
            capssent (str): [optional]  # noqa: E501
            connectretrycount (int): [optional]  # noqa: E501
            fsmestablishedtime (str): [optional]  # noqa: E501
            fsmesttransitions (int): [optional]  # noqa: E501
            holdtime (int): [optional]  # noqa: E501
            inkeepalives (int): [optional]  # noqa: E501
            innotifications (int): [optional]  # noqa: E501
            inopens (int): [optional]  # noqa: E501
            inprfxes (int): [optional]  # noqa: E501
            inprfxesexpwdr (int): [optional]  # noqa: E501
            inprfxesimpwdr (int): [optional]  # noqa: E501
            inrefreshes (int): [optional]  # noqa: E501
            intotalmessages (int): [optional]  # noqa: E501
            inupdates (int): [optional]  # noqa: E501
            inupdateselpstime (int): [optional]  # noqa: E501
            keepalive (int): [optional]  # noqa: E501
            lasterrorrcvd (str): [optional]  # noqa: E501
            lasterrorsent (str): [optional]  # noqa: E501
            localaddr (str): Should be a valid v4 or v6 IP address.. [optional]  # noqa: E501
            orfentrycount (int): [optional]  # noqa: E501
            outkeepalives (int): [optional]  # noqa: E501
            outnotifications (int): [optional]  # noqa: E501
            outopens (int): [optional]  # noqa: E501
            outprfxes (int): [optional]  # noqa: E501
            outprfxesdenied (int): [optional]  # noqa: E501
            outprfxesexpwdr (int): [optional]  # noqa: E501
            outprfxesimpwdr (int): [optional]  # noqa: E501
            outrefreshes (int): [optional]  # noqa: E501
            outtotalmessages (int): [optional]  # noqa: E501
            outupdateelpstime (int): [optional]  # noqa: E501
            outupdates (int): [optional]  # noqa: E501
            peergr (int): [optional]  # noqa: E501
            peerindex (int): [optional]  # noqa: E501
            prev_status (str): [optional] if omitted the server will use the default value of "idle"  # noqa: E501
            rcvdmsgelpstime (int): [optional]  # noqa: E501
            receivedholdtime (int): [optional]  # noqa: E501
            routerefrrcvd (int): [optional]  # noqa: E501
            routerefrsent (int): [optional]  # noqa: E501
            sellocaladdrtype (str): [optional] if omitted the server will use the default value of "other"  # noqa: E501
            stalepathtime (int): [optional]  # noqa: E501
            status (str): [optional] if omitted the server will use the default value of "idle"  # noqa: E501
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
