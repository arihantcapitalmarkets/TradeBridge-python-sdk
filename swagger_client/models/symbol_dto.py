from datetime import date

import attr
from typing import List


@attr.s(auto_attribs=True, repr=False)
class SymbolDto:
    symbol: str = None
    dispSym: str = None
    instrument: str = None
    baseSym: str = None
    companyName: str = None
    isin: str = None
    exc: str = None
    excTkn: int = None
    series: str = None
    lotSize: int = None
    tickSize: str = None
    expiryDate: date = None
    optionType: str = None
    strikePrice: float = None
    streamSym: str = None
    segment: str = None
    fno: bool = None
    mtf: bool = None
    multiplier:str = None
    freezeQty: str = None
    tradingSymbol: str = None
    otherExc: List[str] = None
    isWeeklyExpiry: bool = None

    swagger_types = {
        'symbol': 'str',
        'dispSym': 'str',
        'instrument': 'str',
        'baseSym': 'str',
        'companyName': 'str',
        'isin': 'str',
        'exc': 'str',
        'excTkn': 'int',
        'series': 'str',
        'lotSize': 'int',
        'tickSize': 'str',
        'expiryDate': 'date',
        'optionType': 'str',
        'strikePrice': 'float',
        'streamSym': 'str',
        'segment': 'str',
        'fno': 'bool',
        'mtf': 'bool',
        'multiplier': 'str',
        'freezeQty': 'str',
        "tradingSymbol": 'str',
        'otherExc': 'list[str]',
        'isWeeklyExpiry': 'bool'
    }

    attribute_map = {
        'symbol': 'symbol',
        'dispSym': 'dispSym',
        'instrument': 'instrument',
        'baseSym': 'baseSym',
        'companyName': 'companyName',
        'isin': 'isin',
        'exc': 'exc',
        'excTkn': 'excTkn',
        'series': 'series',
        'lotSize': 'lotSize',
        'tickSize': 'tickSize',
        'expiryDate': 'expiryDate',
        'optionType': 'optionType',
        'strikePrice': 'strikePrice',
        'streamSym': 'streamSym',
        'segment': 'segment',
        'fno': 'fno',
        'mtf': 'mtf',
        'multiplier': 'multiplier',
        'freezeQty': 'freezeQty',
        "tradingSymbol": 'tradingSymbol',
        'otherExc': 'otherExc',
        'isWeeklyExpiry': 'isWeeklyExpiry'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"
