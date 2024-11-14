import attr
from swagger_client.models.place_order_data import PlaceOrderData


@attr.s(auto_attribs=True)
class PlaceOrderResponse:
    infoID: str = None
    infoMsg: str = None
    data: PlaceOrderData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': PlaceOrderData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
