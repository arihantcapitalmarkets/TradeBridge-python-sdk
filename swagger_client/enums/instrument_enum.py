from enum import Enum


class InstrumentEnum(str, Enum):
    STK = "STK"
    ETF = "ETF"
    IDX = "IDX"
    FUTSTK = "FUTSTK"
    FUTIDX = "FUTIDX"
    FUTCUR = "FUTCUR"
    OPTIDX = "OPTIDX"
    OPTSTK = "OPTSTK"
    OPTCUR = "OPTCUR"