"""
    Routing API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pensando_cloud.psm.api_client import ApiClient, Endpoint as _Endpoint
from pensando_cloud.psm.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
import pensando_cloud.psm as psm
from pensando_cloud.psm.model.routing_health import RoutingHealth
from pensando_cloud.psm.model.routing_neighbor_list import RoutingNeighborList
from pensando_cloud.psm.model.routing_route_filter import RoutingRouteFilter
from pensando_cloud.psm.model.routing_route_list import RoutingRouteList


class RoutingV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_health_z(
            self,
            instance,
            **kwargs
        ):
            """get_health_z  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_health_z(instance, async_req=True)
            >>> result = thread.get()

            Args:
                instance (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RoutingHealth
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['instance'] = \
                instance
            return self.call_with_http_info(**kwargs)

        self.get_health_z = _Endpoint(
            settings={
                'response_type': (RoutingHealth,),
                'auth': [],
                'endpoint_path': '/routing/v1/{Instance}/health',
                'operation_id': 'get_health_z',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance',
                ],
                'required': [
                    'instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance':
                        (str,),
                },
                'attribute_map': {
                    'instance': 'Instance',
                },
                'location_map': {
                    'instance': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_health_z
        )

        def __get_list_neighbors(
            self,
            instance,
            **kwargs
        ):
            """get_list_neighbors  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_list_neighbors(instance, async_req=True)
            >>> result = thread.get()

            Args:
                instance (str):

            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                t_api_version (str): APIVersion defines the version of the API object. This can only be set by the server.. [optional]
                meta_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_tenant (str): Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]
                meta_namespace (str): Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_generation_id (str): GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user.. [optional]
                meta_resource_version (str): Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user.. [optional]
                meta_uuid (str): UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                meta_mod_time (datetime): ModTime is the Last Modification time of the object. System generated and updated, not updatable by user.. [optional]
                meta_self_link (str): SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user.. [optional]
                neighbor (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RoutingNeighborList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['instance'] = \
                instance
            return self.call_with_http_info(**kwargs)

        self.get_list_neighbors = _Endpoint(
            settings={
                'response_type': (RoutingNeighborList,),
                'auth': [],
                'endpoint_path': '/routing/v1/{Instance}/neighbors',
                'operation_id': 'get_list_neighbors',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance',
                    't_kind',
                    't_api_version',
                    'meta_name',
                    'meta_tenant',
                    'meta_namespace',
                    'meta_generation_id',
                    'meta_resource_version',
                    'meta_uuid',
                    'meta_creation_time',
                    'meta_mod_time',
                    'meta_self_link',
                    'neighbor',
                ],
                'required': [
                    'instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance':
                        (str,),
                    't_kind':
                        (str,),
                    't_api_version':
                        (str,),
                    'meta_name':
                        (str,),
                    'meta_tenant':
                        (str,),
                    'meta_namespace':
                        (str,),
                    'meta_generation_id':
                        (str,),
                    'meta_resource_version':
                        (str,),
                    'meta_uuid':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                    'meta_mod_time':
                        (datetime,),
                    'meta_self_link':
                        (str,),
                    'neighbor':
                        (str,),
                },
                'attribute_map': {
                    'instance': 'Instance',
                    't_kind': 'T.kind',
                    't_api_version': 'T.api-version',
                    'meta_name': 'meta.name',
                    'meta_tenant': 'meta.tenant',
                    'meta_namespace': 'meta.namespace',
                    'meta_generation_id': 'meta.generation-id',
                    'meta_resource_version': 'meta.resource-version',
                    'meta_uuid': 'meta.uuid',
                    'meta_creation_time': 'meta.creation-time',
                    'meta_mod_time': 'meta.mod-time',
                    'meta_self_link': 'meta.self-link',
                    'neighbor': 'neighbor',
                },
                'location_map': {
                    'instance': 'path',
                    't_kind': 'query',
                    't_api_version': 'query',
                    'meta_name': 'query',
                    'meta_tenant': 'query',
                    'meta_namespace': 'query',
                    'meta_generation_id': 'query',
                    'meta_resource_version': 'query',
                    'meta_uuid': 'query',
                    'meta_creation_time': 'query',
                    'meta_mod_time': 'query',
                    'meta_self_link': 'query',
                    'neighbor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_list_neighbors
        )

        def __get_list_routes1(
            self,
            instance,
            **kwargs
        ):
            """get_list_routes1  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_list_routes1(instance, async_req=True)
            >>> result = thread.get()

            Args:
                instance (str):

            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                t_api_version (str): APIVersion defines the version of the API object. This can only be set by the server.. [optional]
                meta_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_tenant (str): Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]
                meta_namespace (str): Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_generation_id (str): GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user.. [optional]
                meta_resource_version (str): Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user.. [optional]
                meta_uuid (str): UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                meta_mod_time (datetime): ModTime is the Last Modification time of the object. System generated and updated, not updatable by user.. [optional]
                meta_self_link (str): SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user.. [optional]
                ipaddress (str): [optional]
                type (str): [optional]
                extcomm (str): [optional]
                vnid (str): [optional]
                rtype (str): [optional]
                nhop (str): [optional]
                page_number (int): [optional]
                all_routes (bool): Fetch all routes rather than just the best routes selected by BGP.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RoutingRouteList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['instance'] = \
                instance
            return self.call_with_http_info(**kwargs)

        self.get_list_routes1 = _Endpoint(
            settings={
                'response_type': (RoutingRouteList,),
                'auth': [],
                'endpoint_path': '/routing/v1/{Instance}/routes',
                'operation_id': 'get_list_routes1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance',
                    't_kind',
                    't_api_version',
                    'meta_name',
                    'meta_tenant',
                    'meta_namespace',
                    'meta_generation_id',
                    'meta_resource_version',
                    'meta_uuid',
                    'meta_creation_time',
                    'meta_mod_time',
                    'meta_self_link',
                    'ipaddress',
                    'type',
                    'extcomm',
                    'vnid',
                    'rtype',
                    'nhop',
                    'page_number',
                    'all_routes',
                ],
                'required': [
                    'instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance':
                        (str,),
                    't_kind':
                        (str,),
                    't_api_version':
                        (str,),
                    'meta_name':
                        (str,),
                    'meta_tenant':
                        (str,),
                    'meta_namespace':
                        (str,),
                    'meta_generation_id':
                        (str,),
                    'meta_resource_version':
                        (str,),
                    'meta_uuid':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                    'meta_mod_time':
                        (datetime,),
                    'meta_self_link':
                        (str,),
                    'ipaddress':
                        (str,),
                    'type':
                        (str,),
                    'extcomm':
                        (str,),
                    'vnid':
                        (str,),
                    'rtype':
                        (str,),
                    'nhop':
                        (str,),
                    'page_number':
                        (int,),
                    'all_routes':
                        (bool,),
                },
                'attribute_map': {
                    'instance': 'Instance',
                    't_kind': 'T.kind',
                    't_api_version': 'T.api-version',
                    'meta_name': 'meta.name',
                    'meta_tenant': 'meta.tenant',
                    'meta_namespace': 'meta.namespace',
                    'meta_generation_id': 'meta.generation-id',
                    'meta_resource_version': 'meta.resource-version',
                    'meta_uuid': 'meta.uuid',
                    'meta_creation_time': 'meta.creation-time',
                    'meta_mod_time': 'meta.mod-time',
                    'meta_self_link': 'meta.self-link',
                    'ipaddress': 'ipaddress',
                    'type': 'type',
                    'extcomm': 'extcomm',
                    'vnid': 'vnid',
                    'rtype': 'rtype',
                    'nhop': 'nhop',
                    'page_number': 'page-number',
                    'all_routes': 'all-routes',
                },
                'location_map': {
                    'instance': 'path',
                    't_kind': 'query',
                    't_api_version': 'query',
                    'meta_name': 'query',
                    'meta_tenant': 'query',
                    'meta_namespace': 'query',
                    'meta_generation_id': 'query',
                    'meta_resource_version': 'query',
                    'meta_uuid': 'query',
                    'meta_creation_time': 'query',
                    'meta_mod_time': 'query',
                    'meta_self_link': 'query',
                    'ipaddress': 'query',
                    'type': 'query',
                    'extcomm': 'query',
                    'vnid': 'query',
                    'rtype': 'query',
                    'nhop': 'query',
                    'page_number': 'query',
                    'all_routes': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_list_routes1
        )

        def __post_list_routes(
            self,
            instance,
            body,
            **kwargs
        ):
            """post_list_routes  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_list_routes(instance, body, async_req=True)
            >>> result = thread.get()

            Args:
                instance (str):
                body (RoutingRouteFilter):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RoutingRouteList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['instance'] = \
                instance
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.post_list_routes = _Endpoint(
            settings={
                'response_type': (RoutingRouteList,),
                'auth': [],
                'endpoint_path': '/routing/v1/{Instance}/routes',
                'operation_id': 'post_list_routes',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance',
                    'body',
                ],
                'required': [
                    'instance',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance':
                        (str,),
                    'body':
                        (RoutingRouteFilter,),
                },
                'attribute_map': {
                    'instance': 'Instance',
                },
                'location_map': {
                    'instance': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_list_routes
        )
