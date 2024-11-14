import attr
from typing import List


@attr.s(auto_attribs=True, repr=False)
class Summary:
    charges: str = None

    swagger_types = {
        'charges': 'str'
    }

    attribute_map = {
        'charges': 'charges'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class BasicDtls:
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


@attr.s(auto_attribs=True, repr=False)
class PnlFo:
    scripName: str = None
    realisedPnl: str = None
    date: str = None
    realisedPnlPerc: str = None
    isRealized: bool = None
    unRealisedPnl: str = None
    saleVal: str = None
    sellAvg: str = None
    buyAvg: str = None
    dispQty: str = None
    charges: str = None
    qty: str = None
    buyVal: str = None
    mrktVal: str = None
    unRealisedPnlPerc: str = None
    closePrice: str = None

    swagger_types = {
        'scripName': 'str',
        'realisedPnl': 'str',
        'date': 'str',
        'realisedPnlPerc': 'str',
        'isRealized': 'bool',
        'unRealisedPnl': 'str',
        'saleVal': 'str',
        'sellAvg': 'str',
        'buyAvg': 'str',
        'dispQty': 'str',
        'charges': 'str',
        'qty': 'str',
        'buyVal': 'str',
        'mrktVal': 'str',
        'unRealisedPnlPerc': 'str',
        'closePrice': 'str'
    }

    attribute_map = {
        'scripName': 'scripName',
        'realisedPnl': 'realisedPnl',
        'date': 'date',
        'realisedPnlPerc': 'realisedPnlPerc',
        'isRealized': 'isRealized',
        'unRealisedPnl': 'unRealisedPnl',
        'saleVal': 'saleVal',
        'sellAvg': 'sellAvg',
        'buyAvg': 'buyAvg',
        'dispQty': 'dispQty',
        'charges': 'charges',
        'qty': 'qty',
        'buyVal': 'buyVal',
        'mrktVal': 'mrktVal',
        'unRealisedPnlPerc': 'unRealisedPnlPerc',
        'closePrice': 'closePrice'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class ProfitLossFoSuccessData:
    summary: Summary = None
    basicDtls: BasicDtls = None
    pnlFo: List[PnlFo] = None

    swagger_types = {
        'summary': 'Summary',
        'basicDtls': 'BasicDtls',
        'pnlFo': 'list[PnlFo]'
    }

    attribute_map = {
        'summary': 'summary',
        'basicDtls': 'basicDtls',
        'pnlFo': 'pnlFo'
    }
