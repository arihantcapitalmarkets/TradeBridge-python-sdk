import attr
from swagger_client.models.position_book_data import PositionBookData


@attr.s(auto_attribs=True)
class PositionBookResponse:
    infoID: str = None
    infoMsg: str = None
    data: PositionBookData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': PositionBookData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
