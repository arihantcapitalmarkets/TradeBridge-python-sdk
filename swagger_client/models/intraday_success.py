import attr
from swagger_client.models.intraday_success_data import IntradaySuccessData


@attr.s(auto_attribs=True)
class IntradaySuccess(object):
    infoID: str = None
    infoMsg: str = None
    data: IntradaySuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': IntradaySuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }