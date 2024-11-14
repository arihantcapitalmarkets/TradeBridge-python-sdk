from typing import Optional
import attr
from enum import Enum


class ExcEnum(str, Enum):
    NSE = "NSE"
    BSE = "BSE"
    NFO = "NFO"
    BFO = "BFO"
    CDS = "CDS"
    BCD = "BCD"
    MCXSX = "MCXSX"
    MCX = "MCX"
    NCO = "NCO"
    BCO = "BCO"
    ICEX = "ICEX"


class PrdTypeEnum(str, Enum):
    CASH = "CASH"
    MTF = "MTF"
    INTRADAY = "INTRADAY"
    MARGIN = "MARGIN"
    SHORTSELL = "SHORTSELL"
    COVER_ORDER = "COVER_ORDER"
    BRACKET_ORDER = "BRACKET_ORDER"
    NRML = "NRML"
    TNC = "TNC"
    DELIVERY = "DELIVERY"
    NONE = "NONE"


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
        'parOrdId': 'str',
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'prdType': 'prdType',
        'boOrdStatus': 'boOrdStatus',
        'ordId': 'ordId',
        'parOrdId': 'parOrdId',
    }
