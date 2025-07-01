from __future__ import absolute_import
from swagger_client.api_client import ApiClient


class FundsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fund_view(self, authorization, api_key, source):  # noqa: E501
        """FundViewAPI  # noqa: E501

        :param source:
        :param str authorization: (required)
        :param str api_key: (required)
        :return: FundsSucess.
        """
        (data) = self.fund_view_with_http_info(authorization, api_key, source)  # noqa: E501
        return data

    def fund_view_with_http_info(self, authorization, api_key, source):  # noqa: E501
        """FundViewAPI  # noqa: E501

        :param source:
        :param str authorization: (required)
        :param str api_key: (required)
        :return: FundsSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fund_view`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `fund_view`")  # noqa: E501

        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `fund_view`")  # noqa: E501

        collection_formats = {}
        path_params = {}
        query_params = {}
        query_params['segment'] = 'ALL'

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
            '/wrapper-service/api/funds/v1/get-funds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FundsSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Check Margin
    def check_margin(self, body, authorization, api_key, source):  # noqa: E501
        (data) = self.check_margin_with_http_info(body, authorization, api_key, source)  # noqa: E501
        return data

    def check_margin_with_http_info(self, body, authorization, api_key, source):  # noqa: E501

        all_params = ['body', 'authorization', 'api_key', 'source', 'async_req', '_return_http_data_only',
                      '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `check_margin`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `check_margin`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api_key` when calling `check_margin`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError(
                "Missing the required parameter `source` when calling `check_margin`")  # noqa: E501

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
            '/wrapper-service/api/trade/v1/checkMargin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckMarginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
