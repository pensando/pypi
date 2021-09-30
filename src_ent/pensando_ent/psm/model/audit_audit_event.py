"""
    Audit API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_ent.psm.model_utils import (  # noqa: F401
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
    from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
    from pensando_ent.psm.model.api_object_ref import ApiObjectRef
    globals()['ApiObjectMeta'] = ApiObjectMeta
    globals()['ApiObjectRef'] = ApiObjectRef


class AuditAuditEvent(ModelNormal):
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
        ('level',): {
            'BASIC': "basic",
            'REQUEST': "request",
            'RESPONSE': "response",
            'REQUEST-RESPONSE': "request-response",
        },
        ('outcome',): {
            'SUCCESS': "success",
            'FAILURE': "failure",
        },
        ('stage',): {
            'REQUESTAUTHORIZATION': "requestauthorization",
            'REQUESTPROCESSING': "requestprocessing",
        },
    }

    validations = {
        ('external_id',): {
            'max_length': 64,
            'regex': {
                'pattern': r'^[a-zA-Z0-9\-]+$',  # noqa: E501
            },
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
            'action': (str,),  # noqa: E501
            'api_version': (str,),  # noqa: E501
            'client_ips': ([str],),  # noqa: E501
            'data': ({str: (str,)},),  # noqa: E501
            'external_id': (str,),  # noqa: E501
            'gateway_ip': (str,),  # noqa: E501
            'gateway_node': (str,),  # noqa: E501
            'kind': (str,),  # noqa: E501
            'level': (str,),  # noqa: E501
            'meta': (ApiObjectMeta,),  # noqa: E501
            'outcome': (str,),  # noqa: E501
            'request_object': (str,),  # noqa: E501
            'request_uri': (str,),  # noqa: E501
            'resource': (ApiObjectRef,),  # noqa: E501
            'response_object': (str,),  # noqa: E501
            'service_name': (str,),  # noqa: E501
            'stage': (str,),  # noqa: E501
            'user': (ApiObjectRef,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'api_version': 'api-version',  # noqa: E501
        'client_ips': 'client-ips',  # noqa: E501
        'data': 'data',  # noqa: E501
        'external_id': 'external-id',  # noqa: E501
        'gateway_ip': 'gateway-ip',  # noqa: E501
        'gateway_node': 'gateway-node',  # noqa: E501
        'kind': 'kind',  # noqa: E501
        'level': 'level',  # noqa: E501
        'meta': 'meta',  # noqa: E501
        'outcome': 'outcome',  # noqa: E501
        'request_object': 'request-object',  # noqa: E501
        'request_uri': 'request-uri',  # noqa: E501
        'resource': 'resource',  # noqa: E501
        'response_object': 'response-object',  # noqa: E501
        'service_name': 'service-name',  # noqa: E501
        'stage': 'stage',  # noqa: E501
        'user': 'user',  # noqa: E501
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
        """AuditAuditEvent - a model defined in OpenAPI

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
            action (str): [optional]  # noqa: E501
            api_version (str): [optional]  # noqa: E501
            client_ips ([str]): [optional]  # noqa: E501
            data ({str: (str,)}): [optional]  # noqa: E501
            external_id (str): Length of string should be between 0 and 64. Must be alpha numeric and can have -.. [optional]  # noqa: E501
            gateway_ip (str): [optional]  # noqa: E501
            gateway_node (str): [optional]  # noqa: E501
            kind (str): [optional]  # noqa: E501
            level (str): [optional] if omitted the server will use the default value of "basic"  # noqa: E501
            meta (ApiObjectMeta): [optional]  # noqa: E501
            outcome (str): [optional] if omitted the server will use the default value of "success"  # noqa: E501
            request_object (str): [optional]  # noqa: E501
            request_uri (str): Should be a valid URI.. [optional]  # noqa: E501
            resource (ApiObjectRef): [optional]  # noqa: E501
            response_object (str): [optional]  # noqa: E501
            service_name (str): [optional]  # noqa: E501
            stage (str): [optional] if omitted the server will use the default value of "requestauthorization"  # noqa: E501
            user (ApiObjectRef): [optional]  # noqa: E501
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
