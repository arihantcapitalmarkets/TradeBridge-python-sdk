from enum import Enum

class PrdTypeEnum(str, Enum):
    CASH = "CASH"
    MTF = "MTF"
    INTRADAY = "INTRADAY"
    COVER_ORDER = "COVER_ORDER"
    BRACKET_ORDER = "BRACKET_ORDER"
    NRML = "NRML"
    DELIVERY = "DELIVERY"
    CARRYFORWARD = "CARRYFORWARD"