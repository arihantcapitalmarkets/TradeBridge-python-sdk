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


@attr.s(auto_attribs=True)
class CancelOrderRequest:
    """Class representing a request to cancel an order."""

    symbol: str = None
    exc: ExcEnum = None
    ordId: str = None

    swagger_types = {
        'symbol': 'str',
        'exc': 'ExcEnum',
        'ordId': 'str',
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'ordId': 'ordId',
    }
