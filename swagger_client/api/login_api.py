# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class LoginApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def login_normal_login_post(self, body, api_key, source):  # noqa: E501
        """User login  # noqa: E501

        :param source:
        :param LoginNormalLoginBody body: (required)
        :param str api_key: Application ID (required)
        :return: LoginResponse.
        """
        data = self.login_normal_login_post_with_http_info(body, api_key, source)  # noqa: E501
        return data

    def login_normal_login_post_with_http_info(self, body, api_key, source):  # noqa: E501
        """User login  # noqa: E501

        :param source:
        :param LoginNormalLoginBody body: (required)
        :param str api_key: Application ID (required)
        :return: LoginResponse.
        """

        all_params = ['body', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `login_normal_login_post`")  # noqa: E501

        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api-key` when calling `login_normal_login_post`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError(
                "Missing the required parameter `source` when calling `login_normal_login_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params["source"] = params['source']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth-services/api/auth/v1/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Verify-Otp
    def verify_otp(self, body, api_key, source):  # noqa: E501
        data = self.verify_otp_with_http_info(body, api_key, source)  # noqa: E501
        return data

    def verify_otp_with_http_info(self, body, api_key, source):  # noqa: E501
        all_params = ['body', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `verify_otp`")  # noqa: E501

        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api-key` when calling `verify_otp`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError(
                "Missing the required parameter `source` when calling `verify_otp`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params["source"] = params['source']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth-services/api/auth/v1/verify-otp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyOtpResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Resend-Otp
    def resend_otp(self, body, api_key, source):  # noqa: E501
        data = self.resend_otp_with_http_info(body, api_key, source)  # noqa: E501
        return data

    def resend_otp_with_http_info(self, body, api_key, source):  # noqa: E501
        all_params = ['body', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `resend_otp`")  # noqa: E501

        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api-key` when calling `resend_otp`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError(
                "Missing the required parameter `source` when calling `resend_otp`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params["source"] = params['source']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth-services/api/auth/v1/resend-otp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # RefreshToken
    def refresh_token(self, body, api_key, source):  # noqa: E501
        data = self.refresh_token_with_http_info(body, api_key, source)  # noqa: E501
        return data

    def refresh_token_with_http_info(self, body, api_key, source):  # noqa: E501
        all_params = ['body', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `refresh_token`")  # noqa: E501

        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api-key` when calling `refresh_token`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError(
                "Missing the required parameter `source` when calling `refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params["source"] = params['source']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth-services/api/auth/v1/refresh-token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefreshTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Logout
    def logout(self, authorization, api_key, source):  # noqa: E501
        (data) = self.logout_with_http_info(authorization, api_key, source)  # noqa: E501
        return data

    def logout_with_http_info(self, authorization, api_key, source):  # noqa: E501
        all_params = ['authorization', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `logout`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `logout`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `logout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params["source"] = params['source']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth-services/api/auth/v1/logout', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
