import attr
from swagger_client.models.order_trail_data import OrderTrailData


@attr.s(auto_attribs=True)
class OrderTrailResponse:
    infoID: str = None
    infoMsg: str = None
    data: OrderTrailData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': OrderTrailData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
