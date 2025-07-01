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


class OrdActionEnum(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    SHORT = "SHORT"
    NONE = "NONE"


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
    CARRYFORWARD = "CARRYFORWARD"
    NONE = "NONE"


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
class PositionConversionRequest:
    """Class representing a position conversion request."""

    type: str = None
    ordAction: OrdActionEnum = None
    prdType: PrdTypeEnum = None
    toPrdType: PrdTypeEnum = None
    qty: int = None
    symbol: str = None
    excToken: str = None
    exc: ExcEnum = None
    lotSize: int = None
    instrument: InstrumentEnum = None

    swagger_types = {
        'type': 'str',
        'ordAction': 'OrdActionEnum',
        'prdType': 'PrdTypeEnum',
        'toPrdType': 'PrdTypeEnum',
        'qty': 'int',
        'symbol': 'str',
        'excToken': 'str',
        'exc': 'ExcEnum',
        'lotSize': 'int',
        'instrument': 'InstrumentEnum'
    }

    attribute_map = {
        'type': 'type',
        'ordAction': 'ordAction',
        'prdType': 'prdType',
        'toPrdType': 'toPrdType',
        'qty': 'qty',
        'symbol': 'symbol',
        'excToken': 'excToken',
        'exc': 'exc',
        'lotSize': 'lotSize',
        'instrument': 'instrument'
    }

