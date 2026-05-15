import attr
from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.ord_action_enum import OrdActionEnum
from swagger_client.enums.ord_type_enum import OrdTypeEnum
from swagger_client.enums.ord_validity_enum import OrdValidityEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum


@attr.s(auto_attribs=True)
class ModifyOrderRequest:
    """Class representing a request to modify an order."""

    triggerPrice: float = None
    ordType: OrdTypeEnum = None
    prdType: PrdTypeEnum = None
    instrument: InstrumentEnum = None
    exc: ExcEnum = None
    qty: int = None
    lotSize: int = None
    symbol: str = None
    ordId: str = None
    ordAction: OrdActionEnum = None
    limitPrice: float = None
    disQty: int = None
    ordValidity: OrdValidityEnum = None
    tradedQty: int = None
    ordValidityDays: int = None
    exchangeToken: str = None
    amo: bool = None

    swagger_types = {
        'triggerPrice': 'float',
        'ordType': 'OrdTypeEnum',
        'prdType': 'PrdTypeEnum',
        'instrument': 'InstrumentEnum',
        'exc': 'ExcEnum',
        'qty': 'int',
        'lotSize': 'int',
        'symbol': 'str',
        'ordId': 'str',
        'ordAction': 'OrdActionEnum',
        'limitPrice': 'float',
        'disQty': 'int',
        'ordValidity': 'OrdValidityEnum',
        'tradedQty': 'int',
        'ordValidityDays': 'int',
        'exchangeToken': 'str',
        'amo': 'bool'
    }

    attribute_map = {
        'triggerPrice': 'triggerPrice',
        'ordType': 'ordType',
        'prdType': 'prdType',
        'instrument': 'instrument',
        'exc': 'exc',
        'qty': 'qty',
        'lotSize': 'lotSize',
        'symbol': 'symbol',
        'ordId': 'ordId',
        'ordAction': 'ordAction',
        'limitPrice': 'limitPrice',
        'disQty': 'disQty',
        'ordValidity': 'ordValidity',
        'tradedQty': 'tradedQty',
        'ordValidityDays': 'ordValidityDays',
        'exchangeToken': 'exchangeToken',
        'amo': 'amo'
    }
