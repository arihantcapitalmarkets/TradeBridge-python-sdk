import attr

from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.ord_action_enum import OrdActionEnum
from swagger_client.enums.ord_type_enum import OrdTypeEnum
from swagger_client.enums.ord_validity_enum import OrdValidityEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum


@attr.s(auto_attribs=True)
class PlaceOrderRequest:
    """Class representing a request to place an order."""

    symbol: str = None
    exc: ExcEnum = None
    ordAction: OrdActionEnum = None
    ordValidity: OrdValidityEnum = None
    ordType: OrdTypeEnum = None
    prdType: PrdTypeEnum = None
    qty: int = None
    disQty: int = None
    lotSize: int = None
    triggerPrice: float = None
    instrument: InstrumentEnum = None
    limitPrice: float = None
    amo: bool = None
    build: str = None
    excToken: str = None
    boStpLoss: float = None
    boTgtPrice: float = None
    trailingSL: float = None
    remarks: str = None
    excAlgoId: str = None

    swagger_types = {
        'symbol': 'str',
        'exc': 'ExcEnum',
        'ordAction': 'OrdActionEnum',
        'ordValidity': 'OrdValidityEnum',
        'ordType': 'OrdTypeEnum',
        'prdType': 'PrdTypeEnum',
        'qty': 'int',
        'disQty': 'int',
        'lotSize': 'int',
        'triggerPrice': 'float',
        'instrument': 'InstrumentEnum',
        'limitPrice': 'float',
        'amo': 'bool',
        'build': 'str',
        'excToken': 'str',
        'boStpLoss': 'float',
        'boTgtPrice': 'float',
        'trailingSL': 'float',
        'remarks': 'str',
        'excAlgoId': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'ordAction': 'ordAction',
        'ordValidity': 'ordValidity',
        'ordType': 'ordType',
        'prdType': 'prdType',
        'qty': 'qty',
        'disQty': 'disQty',
        'lotSize': 'lotSize',
        'triggerPrice': 'triggerPrice',
        'instrument': 'instrument',
        'limitPrice': 'limitPrice',
        'amo': 'amo',
        'build': 'build',
        'excToken': 'excToken',
        'boStpLoss': 'boStpLoss',
        'boTgtPrice': 'boTgtPrice',
        'trailingSL': 'trailingSL',
        'remarks': 'remarks',
        'excAlgoId': 'excAlgoId'
    }
