from typing import Any

import attr
from swagger_client.models.funds_success_data import FundsSuccessData


@attr.s(auto_attribs=True)
class FundsSuccess(object):
    infoID: str = None
    infoMsg: str = None
    data: FundsSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': FundsSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
