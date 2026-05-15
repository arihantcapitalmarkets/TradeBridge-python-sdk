import attr

from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.ord_action_enum import OrdActionEnum
from swagger_client.enums.ord_type_enum import OrdTypeEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum

@attr.s(auto_attribs=True)
class BrokerageChargeRequest:
    """Class representing a request for brokerage charge calculation."""

    symbol: str = None
    ordAction: OrdActionEnum = None
    excToken: str = None
    exc: ExcEnum = None
    qty: str = None
    price: str = None
    prdType: PrdTypeEnum = None
    triggerPrice: str = None
    instrument: InstrumentEnum = None
    ordType: OrdTypeEnum = None

    swagger_types = {
        'symbol': 'str',
        'ordAction': 'OrderActionEnum',
        'excToken': 'str',
        'exc': 'ExcEnum',
        'qty': 'str',
        'price': 'str',
        'prdType': 'PrdTypeEnum',
        'triggerPrice': 'str',
        'instrument': 'InstrumentEnum',
        'ordType': 'OrdTypeEnum',
    }

    attribute_map = {
        'symbol': 'symbol',
        'ordAction': 'ordAction',
        'excToken': 'excToken',
        'exc': 'exc',
        'qty': 'qty',
        'price': 'price',
        'prdType': 'prdType',
        'triggerPrice': 'triggerPrice',
        'instrument': 'instrument',
        'ordType': 'ordType',
    }
