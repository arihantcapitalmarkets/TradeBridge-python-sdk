# coding: utf-8


from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class PortfolioApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_order_book(self, authorization, api_key, source):  # noqa: E501
        """Get orders  # noqa: E501

        :param source:
        :param api_key:
        :param authorization:
        :return: OrderBookResponse.
        """
        (data) = self.get_order_book_with_http_info(authorization, api_key, source)  # noqa: E501
        return data

    def get_order_book_with_http_info(self, authorization, api_key, source):  # noqa: E501
        """Get orders  # noqa: E501

        :param source:
        :param api_key:
        :param authorization:
        :return: OrderBookResponse.
        """

        all_params = ['authorization', 'api_key', 'source', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `order_book`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `order_book`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `order_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-service/api/order/v1/order-book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Order Trail
    def order_trail(self, body, authorization, api_key, source):  # noqa: E501

        (data) = self.order_trail_with_http_info(body, authorization, api_key, source)  # noqa: E501
        return data

    def order_trail_with_http_info(self, body, authorization, api_key, source):

        all_params = ['body', 'authorization', 'api_key', 'source', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `order_trail`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `order_trail`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `order_trail`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `order_trail`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

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
            '/wrapper-service/api/order/v1/order-trail', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderTrailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Order Status
    def order_status(self, body, authorization, api_key, source):  # noqa: E501

        (data) = self.order_status_with_http_info(body, authorization, api_key, source)  # noqa: E501
        return data

    def order_status_with_http_info(self, body, authorization, api_key, source):

        all_params = ['body', 'authorization', 'api_key', 'source', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `order_status`")  # noqa: E501
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `order_status`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `order_status`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `order_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

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
            '/wrapper-service/api/order/v1/order-status', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderTrailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
