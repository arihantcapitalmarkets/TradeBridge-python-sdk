import attr
from swagger_client.models.modify_order_data import ModifyOrderData


@attr.s(auto_attribs=True)
class ModifyOrderResponse:
    infoID: str = None
    infoMsg: str = None
    data: ModifyOrderData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': ModifyOrderData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
