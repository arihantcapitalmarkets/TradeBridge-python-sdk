import attr
from swagger_client.models.trade_book_data import TradeBookData


@attr.s(auto_attribs=True)
class TradeBookResponse:
    infoID: str = None
    infoMsg: str = None
    data: TradeBookData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': TradeBookData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
