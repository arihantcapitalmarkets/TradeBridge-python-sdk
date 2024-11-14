import attr
from swagger_client.models.holding_data import HoldingData


@attr.s(auto_attribs=True)
class HoldingResponse:
    infoID: str = None
    infoMsg: str = None
    data: HoldingData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': HoldingData,
        'timestamp': int
    }
    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
