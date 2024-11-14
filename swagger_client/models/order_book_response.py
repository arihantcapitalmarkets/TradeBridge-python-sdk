import attr
from swagger_client.models.order_book_data import OrderBookData


@attr.s(auto_attribs=True)
class OrderBookResponse:
    infoID: str = None
    infoMsg: str = None
    data: OrderBookData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': OrderBookData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
