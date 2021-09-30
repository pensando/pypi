"""
    Search API reference

    Service name    # noqa: E501

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
from pensando_cloud.psm.model.search_policy_search_request import SearchPolicySearchRequest
from pensando_cloud.psm.model.search_policy_search_response import SearchPolicySearchResponse
from pensando_cloud.psm.model.search_search_request import SearchSearchRequest
from pensando_cloud.psm.model.search_search_response import SearchSearchResponse


class SearchV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_policy_query1(
            self,
            **kwargs
        ):
            """Security Policy Query  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_policy_query1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                tenant (str): Tenant Name, to perform query within a Tenant's scope. The default tenant is \"default\". In the backend this field gets auto-filled & validated by apigw-hook based on user login context.. [optional]
                namespace (str): Namespace is optional. If provided policy-search will be limited to the specified namespace.. [optional]
                sg_policy (str): NetworkSecurityPolicy name is optional. If provided policy-search will be limited to the specified SGpolicy object name.. [optional]
                app (str): App specification,  predefined apps and alg config.. [optional]
                protocol (str): Protocol eg: tcp, udp, icmp.. [optional]
                port (str): TCP or UDP Port number.. [optional]
                from_ip_address (str): Inbound ip-address, use any to refer to all ipaddresses eg: 10.1.1.1, any.. [optional]
                to_ip_address (str): Outbound ip-address, use any to refer to all ipaddresses eg: 20.1.1.1, any.. [optional]
                from_security_group (str): Inbound security group.. [optional]
                to_security_group (str): Outbound security group.. [optional]
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
                SearchPolicySearchResponse
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
            return self.call_with_http_info(**kwargs)

        self.get_policy_query1 = _Endpoint(
            settings={
                'response_type': (SearchPolicySearchResponse,),
                'auth': [],
                'endpoint_path': '/search/v1/policy-query',
                'operation_id': 'get_policy_query1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant',
                    'namespace',
                    'sg_policy',
                    'app',
                    'protocol',
                    'port',
                    'from_ip_address',
                    'to_ip_address',
                    'from_security_group',
                    'to_security_group',
                ],
                'required': [],
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
                    'tenant':
                        (str,),
                    'namespace':
                        (str,),
                    'sg_policy':
                        (str,),
                    'app':
                        (str,),
                    'protocol':
                        (str,),
                    'port':
                        (str,),
                    'from_ip_address':
                        (str,),
                    'to_ip_address':
                        (str,),
                    'from_security_group':
                        (str,),
                    'to_security_group':
                        (str,),
                },
                'attribute_map': {
                    'tenant': 'tenant',
                    'namespace': 'namespace',
                    'sg_policy': 'sg-policy',
                    'app': 'app',
                    'protocol': 'protocol',
                    'port': 'port',
                    'from_ip_address': 'from-ip-address',
                    'to_ip_address': 'to-ip-address',
                    'from_security_group': 'from-security-group',
                    'to_security_group': 'to-security-group',
                },
                'location_map': {
                    'tenant': 'query',
                    'namespace': 'query',
                    'sg_policy': 'query',
                    'app': 'query',
                    'protocol': 'query',
                    'port': 'query',
                    'from_ip_address': 'query',
                    'to_ip_address': 'query',
                    'from_security_group': 'query',
                    'to_security_group': 'query',
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
            callable=__get_policy_query1
        )

        def __get_query1(
            self,
            **kwargs
        ):
            """Structured or free-form search  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_query1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                query_string (str): Simple query string This can be specified as URI parameter. For advanced query cases, Users should use specify SearchQuery and pass the SearchRequest in a GET/POST Body The max query-string length is 256 bytes. Length of string should be between 0 and 256.. [optional]
                _from (int): From represents the start offset (zero based), used in paginated search requests The results returned would be in the range [From ... From+MaxResults-1] This can be specified as URI parameter. Default value is 0 and valid range is 0..8192. Value should be between 0 and 8192.. [optional]
                max_results (int): MaxResults is the max-count of search results This can be specified as URI parameter. Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192.. [optional]
                sort_by (str): SortyBy is an optional parameter and contains the field name to be sorted by, For eg: \"meta.name\" This can be specified as URI parameter. Length of string should be between 0 and 256.. [optional]
                sort_order (str): SortOrder is an optional parameter and contains whether to sort ascending or descending This can be specified as URI parameter.. [optional]
                mode (str): Query Mode.. [optional]
                query_categories ([str]): OR of Categories to be matched, AND and Exclude are not supported for this type The max category string length is 64 bytes. Length of string should be between 0 and 64.. [optional]
                query_kinds ([str]): OR of Kinds to be matched, AND and Exclude are not supported for this type. Should be a valid object Kind.. [optional]
                tenants ([str]): OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user.. [optional]
                aggregate (bool): Indicates whether to perform aggregation on the search results or not.. [optional]
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
                SearchSearchResponse
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
            return self.call_with_http_info(**kwargs)

        self.get_query1 = _Endpoint(
            settings={
                'response_type': (SearchSearchResponse,),
                'auth': [],
                'endpoint_path': '/search/v1/query',
                'operation_id': 'get_query1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_string',
                    '_from',
                    'max_results',
                    'sort_by',
                    'sort_order',
                    'mode',
                    'query_categories',
                    'query_kinds',
                    'tenants',
                    'aggregate',
                ],
                'required': [],
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
                    'query_string':
                        (str,),
                    '_from':
                        (int,),
                    'max_results':
                        (int,),
                    'sort_by':
                        (str,),
                    'sort_order':
                        (str,),
                    'mode':
                        (str,),
                    'query_categories':
                        ([str],),
                    'query_kinds':
                        ([str],),
                    'tenants':
                        ([str],),
                    'aggregate':
                        (bool,),
                },
                'attribute_map': {
                    'query_string': 'query-string',
                    '_from': 'from',
                    'max_results': 'max-results',
                    'sort_by': 'sort-by',
                    'sort_order': 'sort-order',
                    'mode': 'mode',
                    'query_categories': 'query.categories',
                    'query_kinds': 'query.kinds',
                    'tenants': 'tenants',
                    'aggregate': 'aggregate',
                },
                'location_map': {
                    'query_string': 'query',
                    '_from': 'query',
                    'max_results': 'query',
                    'sort_by': 'query',
                    'sort_order': 'query',
                    'mode': 'query',
                    'query_categories': 'query',
                    'query_kinds': 'query',
                    'tenants': 'query',
                    'aggregate': 'query',
                },
                'collection_format_map': {
                    'query_categories': 'csv',
                    'query_kinds': 'csv',
                    'tenants': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_query1
        )

        def __post_policy_query(
            self,
            body,
            **kwargs
        ):
            """Security Policy Query  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_policy_query(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (SearchPolicySearchRequest):

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
                SearchPolicySearchResponse
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
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.post_policy_query = _Endpoint(
            settings={
                'response_type': (SearchPolicySearchResponse,),
                'auth': [],
                'endpoint_path': '/search/v1/policy-query',
                'operation_id': 'post_policy_query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
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
                    'body':
                        (SearchPolicySearchRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
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
            callable=__post_policy_query
        )

        def __post_query(
            self,
            body,
            **kwargs
        ):
            """Structured or free-form search  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_query(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (SearchSearchRequest):

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
                SearchSearchResponse
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
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.post_query = _Endpoint(
            settings={
                'response_type': (SearchSearchResponse,),
                'auth': [],
                'endpoint_path': '/search/v1/query',
                'operation_id': 'post_query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
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
                    'body':
                        (SearchSearchRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
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
            callable=__post_query
        )
