# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class ChartApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def historical_data(self, authorization, api_key, source, symbol, resolution, _from, to, instrument, exc, streamSym):  # noqa: E501
        """HistoricalDataAPI  # noqa: E501

        :param source:
        :param str authorization: (required)
        :param str api_key: (required)
        :param str symbol: (required)
        :param str resolution: (required)
        :param str _from: (required)
        :param str to: (required)
        :param str instrument: (required)
        :param str exc: (required)
        :param str streamSym: (required)
        :return: HistorySuccess.
        """
        (data) = self.historical_data_with_http_info(authorization, api_key, source, symbol, resolution, _from, to, instrument,
                                                     exc, streamSym)  # noqa: E501
        return data

    def historical_data_with_http_info(self, authorization, api_key, source, symbol, resolution, _from, to, instrument, exc,
                                       streamSym):  # noqa: E501
        """HistoricalDataAPI  # noqa: E501

        :param source:
        :param str authorization: (required)
        :param str api_key: (required)
        :param str symbol: (required)
        :param str resolution: (required)
        :param str _from: (required)
        :param str to: (required)
        :param str instrument: (required)
        :param str exc: (required)
        :param str streamSym: (required)
        :return: HistorySuccess.
        """

        all_params = ['authorization', 'api_key', 'source', 'symbol', 'resolution', '_from', 'to', 'instrument', 'exc',
                      'streamSym', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `historical_data`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'resolution' is set
        if ('resolution' not in params or
                params['resolution'] is None):
            raise ValueError("Missing the required parameter `resolution` when calling `historical_data`")  # noqa: E501
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'countback' is set
        if ('instrument' not in params or
                params['instrument'] is None):
            raise ValueError("Missing the required parameter `instrument` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'exc' is set
        if ('exc' not in params or
                params['exc'] is None):
            raise ValueError("Missing the required parameter `exc` when calling `historical_data`")  # noqa: E501
        # verify the required parameter 'stream_symbol' is set
        if ('streamSym' not in params or
                params['streamSym'] is None):
            raise ValueError(
                "Missing the required parameter `streamSym` when calling `historical_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'symbol' in params:
            query_params.append(('symbol', params['symbol']))  # noqa: E501
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'instrument' in params:
            query_params.append(('instrument', params['instrument']))  # noqa: E501
        if 'exc' in params:
            query_params.append(('exc', params['exc']))  # noqa: E501
        if 'streamSym' in params:
            query_params.append(('streamSym', params['streamSym']))  # noqa: E501

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
            '/wrapper-service/api/chart/v1/historical-candle-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HistorySuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intraday(self, body, authorization, api_key, source):  # noqa: E501
        """IntradayAPI  # noqa: E501

        :param source:
        :param IntradayRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: IntradaySuccess.
        """
        (data) = self.intraday_with_http_info(body, authorization, api_key, source)  # noqa: E501
        return data

    def intraday_with_http_info(self, body, authorization, api_key, source):  # noqa: E501
        """IntradayAPI  # noqa: E501

        :param source:
        :param IntradayRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: IntradaySuccess.
        """

        all_params = ['body', 'authorization', 'api_key', 'source', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `intraday_candle_data`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `intraday_candle_data`")  # noqa: E501
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `intraday_candle_data`")  # noqa: E501

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
            '/wrapper-service/api/chart/v1/intraday-candle-data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntradaySuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

