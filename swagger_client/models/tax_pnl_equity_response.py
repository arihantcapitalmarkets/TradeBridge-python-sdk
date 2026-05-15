import attr
from typing import List
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class TaxEquitySummary:
    realisedPnl: str = None
    charges: str = None
    shortTermPrc: str = None
    specTermPrc: str = None
    longTermPrc: str = None
    turnOver: str = None

    swagger_types = {
        'realisedPnl': 'str',
        'charges': 'str',
        'shortTermPrc': 'str',
        'specTermPrc': 'str',
        'longTermPrc': 'str',
        'turnOver': 'str'
    }

    attribute_map = {
        'realisedPnl': 'realisedPnl',
        'charges': 'charges',
        'shortTermPrc': 'shortTermPrc',
        'specTermPrc': 'specTermPrc',
        'longTermPrc': 'longTermPrc',
        'turnOver': 'turnOver'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class TaxPnlCash:
    realisedPnl: str = None
    realisedPnlPerc: str = None
    sellVal: str = None
    sym: SymbolDto = None
    buyDate: str = None
    sellAvg: str = None
    sellQty: str = None
    fmv: str = None
    noOfDays: str = None
    buyAvg: str = None
    buyQty: str = None
    specPrlo: str = None
    qty: str = None
    buyVal: str = None
    longPrlo: str = None
    sellDate: str = None
    shortPrlo: str = None
    ltcg: str = None

    swagger_types = {
        'realisedPnl': 'str',
        'realisedPnlPerc': 'str',
        'sellVal': 'str',
        'sym': SymbolDto,
        'buyDate': 'str',
        'sellAvg': 'str',
        'sellQty': 'str',
        'fmv': 'str',
        'noOfDays': 'str',
        'buyAvg': 'str',
        'buyQty': 'str',
        'specPrlo': 'str',
        'qty': 'str',
        'buyVal': 'str',
        'longPrlo': 'str',
        'sellDate': 'str',
        'shortPrlo': 'str',
        'ltcg': 'str'
    }

    attribute_map = {
        'realisedPnl': 'realisedPnl',
        'realisedPnlPerc': 'realisedPnlPerc',
        'sellVal': 'sellVal',
        'sym': 'sym',
        'buyDate': 'buyDate',
        'sellAvg': 'sellAvg',
        'sellQty': 'sellQty',
        'fmv': 'fmv',
        'noOfDays': 'noOfDays',
        'buyAvg': 'buyAvg',
        'buyQty': 'buyQty',
        'specPrlo': 'specPrlo',
        'qty': 'qty',
        'buyVal': 'buyVal',
        'longPrlo': 'longPrlo',
        'sellDate': 'sellDate',
        'shortPrlo': 'shortPrlo',
        'ltcg': 'ltcg'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class TaxEquityBasicDtls:
    Client_ID: str = None
    To: str = None
    Date: str = None

    swagger_types = {
        'Client_ID': 'str',
        'To': 'str',
        'Date': 'str'
    }

    attribute_map = {
        'Client_ID': 'Client ID',
        'To': 'To',
        'Date': 'Date'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class TaxPnlEquitySuccessData:
    pnlCash: List[TaxPnlCash] = None
    summary: TaxEquitySummary = None
    basicDtls: TaxEquityBasicDtls = None

    swagger_types = {
        'pnlCash': 'list[TaxPnlCash]',
        'summary': 'TaxEquitySummary',
        'basicDtls': 'TaxEquityBasicDtls'
    }

    attribute_map = {
        'pnlCash': 'pnlCash',
        'summary': 'summary',
        'basicDtls': 'basicDtls'
    }

@attr.s(auto_attribs=True)
class TaxPnlEquityResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: TaxPnlEquitySuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': TaxPnlEquitySuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
