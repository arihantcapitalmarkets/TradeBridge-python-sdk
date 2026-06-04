import attr

from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum

@attr.s(auto_attribs=True)
class ExitOrderRequest:
    """Class representing a request to exit an order."""

    symbol: str = None
    exc: ExcEnum = None
    prdType: PrdTypeEnum = None
    boOrdStatus: str = None
    ordId: str = None
    parOrdId: str = None

    swagger_types = {
        'symbol': 'str',
        'exc': 'ExcEnum',
        'prdType': 'PrdTypeEnum',
        'boOrdStatus': 'str',
        'ordId': 'str',
        'parOrdId': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'prdType': 'prdType',
        'boOrdStatus': 'boOrdStatus',
        'ordId': 'ordId',
        'parOrdId': 'parOrdId'
    }
