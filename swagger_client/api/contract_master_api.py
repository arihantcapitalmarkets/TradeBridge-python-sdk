from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class ContractMasterApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    # Contract Master
    def contract_master(self, exch):  # noqa: E501
        (data) = self.contract_master_with_http_info(exch)  # noqa: E501
        return data

    def contract_master_with_http_info(self, exch):  # noqa: E501
        all_params = ['exch', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        if ('exch' not in params or
                params['exch'] is None):
            raise ValueError("Missing the required parameter `exch` when calling `contract_master`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = {}
        query_params['exch'] = params['exch']

        header_params = {}
        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-service/api/symbol/v1/master/cache', 'GET',
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
