import attr
from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.ord_action_enum import OrdActionEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum


@attr.s(auto_attribs=True)
class PositionConversionRequest:
    """Class representing a position conversion request."""

    type: str = None
    ordAction: OrdActionEnum = None
    prdType: PrdTypeEnum = None
    toPrdType: PrdTypeEnum = None
    qty: int = None
    symbol: str = None
    excToken: str = None
    exc: ExcEnum = None
    lotSize: int = None
    instrument: InstrumentEnum = None

    swagger_types = {
        'type': 'str',
        'ordAction': 'OrdActionEnum',
        'prdType': 'PrdTypeEnum',
        'toPrdType': 'PrdTypeEnum',
        'qty': 'int',
        'symbol': 'str',
        'excToken': 'str',
        'exc': 'ExcEnum',
        'lotSize': 'int',
        'instrument': 'InstrumentEnum'
    }

    attribute_map = {
        'type': 'type',
        'ordAction': 'ordAction',
        'prdType': 'prdType',
        'toPrdType': 'toPrdType',
        'qty': 'qty',
        'symbol': 'symbol',
        'excToken': 'excToken',
        'exc': 'exc',
        'lotSize': 'lotSize',
        'instrument': 'instrument'
    }

