import attr
from swagger_client.models.brokerage_charge_data import BrokerageChargeData


@attr.s(auto_attribs=True)
class BrokerageChargeResponse:
    infoID: str = None
    infoMsg: str = None
    data: BrokerageChargeData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': BrokerageChargeData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
