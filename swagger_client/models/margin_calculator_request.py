from enum import Enum
from typing import List
import attr


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
    CARRYFORWARD = "CARRYFORWARD"
    NONE = "NONE"


@attr.s(auto_attribs=True)
class Symbol:
    symbol: str = None
    netQty: int = None
    lotSize: int = None
    instrument: InstrumentEnum = None
    streamSym: str = None
    excToken: str = None
    exc: ExcEnum = None
    prdType: PrdTypeEnum = None
    brand: List[str] = None

    swagger_types = {
        'symbol': 'str',
        'netQty': 'int',
        'lotSize': 'int',
        'instrument': 'InstrumentEnum',
        'streamSym': 'str',
        'excToken': 'str',
        'exc': 'ExcEnum',
        'prdType': 'PrdTypeEnum',
        'brand': 'list[str]'
    }

    attribute_map = {
        'symbol': 'symbol',
        'netQty': 'netQty',
        'lotSize': 'lotSize',
        'instrument': 'instrument',
        'streamSym': 'streamSym',
        'excToken': 'excToken',
        'exc': 'exc',
        'prdType': 'prdType',
        'brand': 'brand'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class MarginCalculatorRequest:
    symbols: List[Symbol] = None

    swagger_types = {
        'symbols': 'list[Symbol]'
    }

    attribute_map = {
        'symbols': 'symbols'
    }
