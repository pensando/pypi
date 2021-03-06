"""
    Preferences API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pensando_dss.psm.api_client import ApiClient, Endpoint as _Endpoint
from pensando_dss.psm.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
import pensando_dss.psm as psm
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.preferences_auto_msg_ui_global_settings_watch_helper import PreferencesAutoMsgUIGlobalSettingsWatchHelper
from pensando_dss.psm.model.preferences_ui_global_settings import PreferencesUIGlobalSettings


class PreferencesV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_ui_global_settings(
            self,
            o_tenant,
            **kwargs
        ):
            """Get UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_ui_global_settings(o_tenant, async_req=True)
            >>> result = thread.get()

            Args:
                o_tenant (str):

            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
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
                PreferencesUIGlobalSettings
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
            kwargs['o_tenant'] = \
                o_tenant
            return self.call_with_http_info(**kwargs)

        self.get_ui_global_settings = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings',
                'operation_id': 'get_ui_global_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'o_tenant',
                    't_kind',
                    'meta_creation_time',
                ],
                'required': [
                    'o_tenant',
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
                    'o_tenant':
                        (str,),
                    't_kind':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                },
                'attribute_map': {
                    'o_tenant': 'O.Tenant',
                    't_kind': 'T.kind',
                    'meta_creation_time': 'meta.creation-time',
                },
                'location_map': {
                    'o_tenant': 'path',
                    't_kind': 'query',
                    'meta_creation_time': 'query',
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
            callable=__get_ui_global_settings
        )

        def __get_ui_global_settings1(
            self,
            **kwargs
        ):
            """Get UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_ui_global_settings1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
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
                PreferencesUIGlobalSettings
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

        self.get_ui_global_settings1 = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/uiglobalsettings',
                'operation_id': 'get_ui_global_settings1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    't_kind',
                    'meta_creation_time',
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
                    't_kind':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                },
                'attribute_map': {
                    't_kind': 'T.kind',
                    'meta_creation_time': 'meta.creation-time',
                },
                'location_map': {
                    't_kind': 'query',
                    'meta_creation_time': 'query',
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
            callable=__get_ui_global_settings1
        )

        def __label_ui_global_settings(
            self,
            o_tenant,
            body,
            **kwargs
        ):
            """Label UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.label_ui_global_settings(o_tenant, body, async_req=True)
            >>> result = thread.get()

            Args:
                o_tenant (str):
                body (ApiLabel):

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
                PreferencesUIGlobalSettings
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
            kwargs['o_tenant'] = \
                o_tenant
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.label_ui_global_settings = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings/label',
                'operation_id': 'label_ui_global_settings',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'o_tenant',
                    'body',
                ],
                'required': [
                    'o_tenant',
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
                    'o_tenant':
                        (str,),
                    'body':
                        (ApiLabel,),
                },
                'attribute_map': {
                    'o_tenant': 'O.Tenant',
                },
                'location_map': {
                    'o_tenant': 'path',
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
            callable=__label_ui_global_settings
        )

        def __label_ui_global_settings1(
            self,
            body,
            **kwargs
        ):
            """Label UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.label_ui_global_settings1(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (ApiLabel):

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
                PreferencesUIGlobalSettings
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

        self.label_ui_global_settings1 = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/uiglobalsettings/label',
                'operation_id': 'label_ui_global_settings1',
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
                        (ApiLabel,),
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
            callable=__label_ui_global_settings1
        )

        def __update_ui_global_settings(
            self,
            o_tenant,
            body,
            **kwargs
        ):
            """Update UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_ui_global_settings(o_tenant, body, async_req=True)
            >>> result = thread.get()

            Args:
                o_tenant (str):
                body (PreferencesUIGlobalSettings):

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
                PreferencesUIGlobalSettings
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
            kwargs['o_tenant'] = \
                o_tenant
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_ui_global_settings = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/tenant/{O.Tenant}/uiglobalsettings',
                'operation_id': 'update_ui_global_settings',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'o_tenant',
                    'body',
                ],
                'required': [
                    'o_tenant',
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
                    'o_tenant':
                        (str,),
                    'body':
                        (PreferencesUIGlobalSettings,),
                },
                'attribute_map': {
                    'o_tenant': 'O.Tenant',
                },
                'location_map': {
                    'o_tenant': 'path',
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
            callable=__update_ui_global_settings
        )

        def __update_ui_global_settings1(
            self,
            body,
            **kwargs
        ):
            """Update UIGlobalSettings object  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_ui_global_settings1(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (PreferencesUIGlobalSettings):

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
                PreferencesUIGlobalSettings
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

        self.update_ui_global_settings1 = _Endpoint(
            settings={
                'response_type': (PreferencesUIGlobalSettings,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/uiglobalsettings',
                'operation_id': 'update_ui_global_settings1',
                'http_method': 'PUT',
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
                        (PreferencesUIGlobalSettings,),
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
            callable=__update_ui_global_settings1
        )

        def __watch_ui_global_settings(
            self,
            o_tenant,
            **kwargs
        ):
            """Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.watch_ui_global_settings(o_tenant, async_req=True)
            >>> result = thread.get()

            Args:
                o_tenant (str):

            Keyword Args:
                o_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                o_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                field_change_selector ([str]): FieldChangeSelector specifies to generate a watch notification on change in field(s) specified.. [optional]
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
                PreferencesAutoMsgUIGlobalSettingsWatchHelper
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
            kwargs['o_tenant'] = \
                o_tenant
            return self.call_with_http_info(**kwargs)

        self.watch_ui_global_settings = _Endpoint(
            settings={
                'response_type': (PreferencesAutoMsgUIGlobalSettingsWatchHelper,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/watch/tenant/{O.Tenant}/uiglobalsettings',
                'operation_id': 'watch_ui_global_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'o_tenant',
                    'o_name',
                    'o_creation_time',
                    'field_change_selector',
                ],
                'required': [
                    'o_tenant',
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
                    'o_tenant':
                        (str,),
                    'o_name':
                        (str,),
                    'o_creation_time':
                        (datetime,),
                    'field_change_selector':
                        ([str],),
                },
                'attribute_map': {
                    'o_tenant': 'O.Tenant',
                    'o_name': 'O.name',
                    'o_creation_time': 'O.creation-time',
                    'field_change_selector': 'field-change-selector',
                },
                'location_map': {
                    'o_tenant': 'path',
                    'o_name': 'query',
                    'o_creation_time': 'query',
                    'field_change_selector': 'query',
                },
                'collection_format_map': {
                    'field_change_selector': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__watch_ui_global_settings
        )

        def __watch_ui_global_settings1(
            self,
            **kwargs
        ):
            """Watch UIGlobalSettings objects. Supports WebSockets or HTTP long poll  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.watch_ui_global_settings1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                o_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                o_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                field_change_selector ([str]): FieldChangeSelector specifies to generate a watch notification on change in field(s) specified.. [optional]
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
                PreferencesAutoMsgUIGlobalSettingsWatchHelper
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

        self.watch_ui_global_settings1 = _Endpoint(
            settings={
                'response_type': (PreferencesAutoMsgUIGlobalSettingsWatchHelper,),
                'auth': [],
                'endpoint_path': '/configs/preferences/v1/watch/uiglobalsettings',
                'operation_id': 'watch_ui_global_settings1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'o_name',
                    'o_creation_time',
                    'field_change_selector',
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
                    'o_name':
                        (str,),
                    'o_creation_time':
                        (datetime,),
                    'field_change_selector':
                        ([str],),
                },
                'attribute_map': {
                    'o_name': 'O.name',
                    'o_creation_time': 'O.creation-time',
                    'field_change_selector': 'field-change-selector',
                },
                'location_map': {
                    'o_name': 'query',
                    'o_creation_time': 'query',
                    'field_change_selector': 'query',
                },
                'collection_format_map': {
                    'field_change_selector': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__watch_ui_global_settings1
        )
