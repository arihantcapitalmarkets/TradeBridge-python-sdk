from enum import Enum


class OrdTypeEnum(str, Enum):
    MARKET = "Market"
    LIMIT = "Limit"
    SL_M = "SL-M"
    SL = "SL"