import attr
from swagger_client.models.position_conversion_data import PositionConversionData


@attr.s(auto_attribs=True)
class PositionConversionResponse:
    infoID: str = None
    infoMsg: str = None
    data: PositionConversionData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': PositionConversionData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
