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


class OrdActionEnum(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    SHORT = "SHORT"
    NONE = "NONE"


class OrdTypeEnum(str, Enum):
    MARKET = "Market"
    LIMIT = "Limit"
    STOP = "Stop"
    STOP_LOSS = "Stop-loss"
    SL_M = "SL-M"
    SL = "SL"
    NONE = "None"


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
class BrokerageChargeRequest:
    """Class representing a request for brokerage charge calculation."""

    symbol: str = None
    orderAction: OrdActionEnum = None
    excToken: str = None
    exc: ExcEnum = None
    qty: str = None
    price: str = None
    product: PrdTypeEnum = None
    triggerPrice: str = None
    instrument: InstrumentEnum = None
    orderType: OrdTypeEnum = None

    swagger_types = {
        'symbol': 'str',
        'orderAction': 'OrderActionEnum',
        'excToken': 'str',
        'exc': 'ExcEnum',
        'qty': 'str',
        'price': 'str',
        'product': 'ProductEnum',
        'triggerPrice': 'str',
        'instrument': 'InstrumentEnum',
        'orderType': 'OrdTypeEnum',
    }

    attribute_map = {
        'symbol': 'symbol',
        'orderAction': 'orderAction',
        'excToken': 'excToken',
        'exc': 'exc',
        'qty': 'qty',
        'price': 'price',
        'product': 'product',
        'triggerPrice': 'triggerPrice',
        'instrument': 'instrument',
        'orderType': 'orderType',
    }
