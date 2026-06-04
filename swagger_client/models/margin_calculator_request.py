from typing import List
import attr
from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum

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
