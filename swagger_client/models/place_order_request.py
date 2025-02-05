from typing import Union

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


class OrdValidityEnum(str, Enum):
    DAY = "DAY"
    IOC = "IOC"
    GMT = "GMT"
    GTC = "GTC"
    AMO = "AMO"
    GTD = "GTD"
    NONE = "NONE"


class OrdTypeEnum(str, Enum):
    MARKET = "Market"
    LIMIT = "Limit"
    STOP = "Stop"
    STOP_LOSS = "Stop-loss"
    SL_M = "SL-M"
    SL = "SL"
    NONE = "None"


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
class PlaceOrderRequest:
    """Class representing a request to place an order."""

    symbol: str = None
    exc: ExcEnum = None
    ordAction: OrdActionEnum = None
    ordValidity: OrdValidityEnum = None
    ordType: OrdTypeEnum = None
    prdType: PrdTypeEnum = None
    qty: int = None
    disQty: int = None
    lotSize: int = None
    triggerPrice: float = None
    instrument: InstrumentEnum = None
    limitPrice: float = None
    amo: bool = None
    build: str = None
    excToken: str = None
    boStpLoss: Union[float, int] = None
    boTgtPrice: Union[float, int] = None
    trailingSL: float = None

    swagger_types = {
        'symbol': 'str',
        'exc': 'ExcEnum',
        'ordAction': 'OrdActionEnum',
        'ordValidity': 'OrdValidityEnum',
        'ordType': 'OrdTypeEnum',
        'prdType': 'PrdTypeEnum',
        'qty': 'int',
        'disQty': 'int',
        'lotSize': 'int',
        'triggerPrice': 'float',
        'instrument': 'InstrumentEnum',
        'limitPrice': 'float',
        'amo': 'bool',
        'build': 'str',
        'excToken': 'str',
        'boStpLoss': 'float | int',
        'boTgtPrice': 'float | int',
        'trailingSL': 'float',
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'ordAction': 'ordAction',
        'ordValidity': 'ordValidity',
        'ordType': 'ordType',
        'prdType': 'prdType',
        'qty': 'qty',
        'disQty': 'disQty',
        'lotSize': 'lotSize',
        'triggerPrice': 'triggerPrice',
        'instrument': 'instrument',
        'limitPrice': 'limitPrice',
        'amo': 'amo',
        'build': 'build',
        'excToken': 'excToken',
        'boStpLoss': 'boStpLoss',
        'boTgtPrice': 'boTgtPrice',
        'trailingSL': 'trailingSL',
    }
