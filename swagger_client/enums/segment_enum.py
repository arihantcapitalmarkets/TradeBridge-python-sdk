from enum import Enum

class SegmentEnum(str, Enum):
    EQUITY = "equity"
    DERIVATIVE = "derivative"
    INDEX = "index"
    CURRENCY = "currency"