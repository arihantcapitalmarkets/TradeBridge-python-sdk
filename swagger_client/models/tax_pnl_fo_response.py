import attr
from typing import List


@attr.s(auto_attribs=True, repr=False)
class TaxSummary:
    realisedPnl: str = None
    optTurnOver: str = None
    charges: str = None
    futProfit: str = None
    optProfit: str = None
    futTurnOver: str = None
    grossProfit: str = None

    swagger_types = {
        'realisedPnl': 'str',
        'optTurnOver': 'str',
        'charges': 'str',
        'futProfit': 'str',
        'optProfit': 'str',
        'futTurnOver': 'str',
        'grossProfit': 'str'
    }

    attribute_map = {
        'realisedPnl': 'realisedPnl',
        'optTurnOver': 'optTurnOver',
        'charges': 'charges',
        'futProfit': 'futProfit',
        'optProfit': 'optProfit',
        'futTurnOver': 'futTurnOver',
        'grossProfit': 'grossProfit'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class TaxPnlFo:
    scripName: str = None
    realisedPnl: str = None
    date: str = None
    realisedPnlPerc: str = None
    saleVal: str = None
    sellAvg: str = None
    buyAvg: str = None
    dispQty: str = None
    qty: str = None
    futProfit: str = None
    optProfit: str = None
    buyVal: str = None
    mrktVal: str = None
    closePrice: str = None

    swagger_types = {
        'scripName': 'str',
        'realisedPnl': 'str',
        'date': 'str',
        'realisedPnlPerc': 'str',
        'saleVal': 'str',
        'sellAvg': 'str',
        'buyAvg': 'str',
        'dispQty': 'str',
        'qty': 'str',
        'futProfit': 'str',
        'optProfit': 'str',
        'buyVal': 'str',
        'mrktVal': 'str',
        'closePrice': 'str'
    }

    attribute_map = {
        'scripName': 'scripName',
        'realisedPnl': 'realisedPnl',
        'date': 'date',
        'realisedPnlPerc': 'realisedPnlPerc',
        'saleVal': 'saleVal',
        'sellAvg': 'sellAvg',
        'buyAvg': 'buyAvg',
        'dispQty': 'dispQty',
        'qty': 'qty',
        'futProfit': 'futProfit',
        'optProfit': 'optProfit',
        'buyVal': 'buyVal',
        'mrktVal': 'mrktVal',
        'closePrice': 'closePrice'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class TaxBasicDtls:
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
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class TaxPnlFoSuccessData:
    summary: TaxSummary = None
    basicDtls: TaxBasicDtls = None
    pnlFo: List[TaxPnlFo] = None

    swagger_types = {
        'summary': 'TaxSummary',
        'basicDtls': 'TaxBasicDtls',
        'pnlFo': 'list[TaxPnlFo]'
    }

    attribute_map = {
        'summary': 'summary',
        'basicDtls': 'basicDtls',
        'pnlFo': 'pnlFo'
    }



@attr.s(auto_attribs=True)
class TaxPnlFoResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: TaxPnlFoSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': TaxPnlFoSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
