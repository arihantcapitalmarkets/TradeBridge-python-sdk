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
class ModifyOrderRequest:
    """Class representing a request to modify an order."""

    trigger_price: float = None
    ord_type: OrdTypeEnum = None
    prd_type: PrdTypeEnum = None
    instrument: InstrumentEnum = None
    exc: ExcEnum = None
    qty: int = None
    lot_size: int = None
    symbol: str = None
    ord_id: str = None
    ord_action: OrdActionEnum = None
    limit_price: float = None
    dis_qty: int = None
    ord_validity: OrdValidityEnum = None
    traded_qty: int = None
    ord_validity_days: int = None
    exchange_token: str = None
    amo: bool = None
    remarks: str = None

    swagger_types = {
        'trigger_price': 'float',
        'ord_type': 'OrdTypeEnum',
        'prd_type': 'PrdTypeEnum',
        'instrument': 'InstrumentEnum',
        'exc': 'ExcEnum',
        'qty': 'int',
        'lot_size': 'int',
        'symbol': 'str',
        'ord_id': 'str',
        'ord_action': 'OrdActionEnum',
        'limit_price': 'float',
        'dis_qty': 'int',
        'ord_validity': 'OrdValidityEnum',
        'traded_qty': 'int',
        'ord_validity_days': 'int',
        'exchange_token': 'str',
        'amo': 'bool',
        'remarks': 'str'
    }

    attribute_map = {
        'trigger_price': 'triggerPrice',
        'ord_type': 'ordType',
        'prd_type': 'prdType',
        'instrument': 'instrument',
        'exc': 'exc',
        'qty': 'qty',
        'lot_size': 'lotSize',
        'symbol': 'symbol',
        'ord_id': 'ordId',
        'ord_action': 'ordAction',
        'limit_price': 'limitPrice',
        'dis_qty': 'disQty',
        'ord_validity': 'ordValidity',
        'traded_qty': 'tradedQty',
        'ord_validity_days': 'ordValidityDays',
        'exchange_token': 'exchangeToken',
        'amo': 'amo',
        'remarks': 'remarks'
    }
