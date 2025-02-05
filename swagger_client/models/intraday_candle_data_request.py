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


class InstrumentEnum(str, Enum):
    STK = "STK"
    ETF = "ETF"
    IDX = "IDX"
    COM = "COM"
    UNDCUR = "UNDCUR"
    CUR = "CUR"
    FUTIVX = "FUTIVX"
    FUTSTK = "FUTSTK"
    FUTIDX = "FUTIDX"
    FUTCUR = "FUTCUR"
    FUTIRD = "FUTIRD"
    FUTIRC = "FUTIRC"
    FUTIRT = "FUTIRT"
    FUTIRF = "FUTIRF"
    FUTCOM = "FUTCOM"
    FUTBLN = "FUTBLN"
    FUTENR = "FUTENR"
    FUTMET = "FUTMET"
    FUTAGR = "FUTAGR"
    OPTIDX = "OPTIDX"
    OPTSTK = "OPTSTK"
    OPTCOM = "OPTCOM"
    OPTBLN = "OPTBLN"
    OPTENR = "OPTENR"
    OPTAGR = "OPTAGR"
    OPTCUR = "OPTCUR"
    OPTIRC = "OPTIRC"
    OPTIRD = "OPTIRD"
    UNDCOM = "UNDCOM"
    AUCSO = "AUCSO"
    FUTIDXSPR = "FUTIDXSPR"
    FUTSTKSPR = "FUTSTKSPR"
    FUTCURSPR = "FUTCURSPR"
    FUTIRTSPR = "FUTIRTSPR"
    FUTIRCSPR = "FUTIRCSPR"
    FUTIRDSPR = "FUTIRDSPR"
    OPTCURSPR = "OPTCURSPR"
    OPTIRCSPR = "OPTIRCSPR"
    FUTCOMSPR = "FUTCOMSPR"
    OPTCOMSPR = "OPTCOMSPR"
    UNDIRC = "UNDIRC"
    UNDIRD = "UNDIRD"
    UNDIRT = "UNDIRT"
    NONE = "NONE"


@attr.s(auto_attribs=True)
class IntradayCandleDataRequest:
    """Class representing the data for intraday candle request."""

    symbol: str = None
    resolution: str = None
    instrument: InstrumentEnum = None
    exc: ExcEnum = None
    startTime: str = None
    endTime: str = None

    swagger_types = {
        'symbol': 'str',
        'resolution': 'str',
        'instrument': 'InstrumentEnum',
        'exc': 'ExcEnum',
        'startTime': 'str',
        'endTime': 'str',
    }

    attribute_map = {
        'symbol': 'symbol',
        'resolution': 'resolution',
        'instrument': 'instrument',
        'exc': 'exc',
        'startTime': 'startTime',
        'endTime': 'endTime',
    }
