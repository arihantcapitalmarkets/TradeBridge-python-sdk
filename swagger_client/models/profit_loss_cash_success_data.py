import attr
from typing import List
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class PnlCash:
    sellVal: str = None
    sym: SymbolDto = None
    otherCharges: str = None
    buyDate: str = None
    sellAvg: str = None
    sellQty: str = None
    buyAvg: str = None
    buyQty: str = None
    qty: str = None
    buyVal: str = None
    sellDate: str = None

    swagger_types = {
        'sellVal': 'str',
        'sym': SymbolDto,
        'otherCharges': 'str',
        'buyDate': 'str',
        'sellAvg': 'str',
        'sellQty': 'str',
        'buyAvg': 'str',
        'buyQty': 'str',
        'qty': 'str',
        'buyVal': 'str',
        'sellDate': 'str'
    }

    attribute_map = {
        'sellVal': 'sellVal',
        'sym': 'sym',
        'otherCharges': 'otherCharges',
        'buyDate': 'buyDate',
        'sellAvg': 'sellAvg',
        'sellQty': 'sellQty',
        'buyAvg': 'buyAvg',
        'buyQty': 'buyQty',
        'qty': 'qty',
        'buyVal': 'buyVal',
        'sellDate': 'sellDate'
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


@attr.s(auto_attribs=True)
class ProfitLossCashSuccessData:
    pnlCash: List[PnlCash] = None
    charges: str = None
    basicDtls: BasicDtls = None

    swagger_types = {
        'pnlCash': 'list[PnlCash]',
        'charges': 'str',
        'basicDtls': 'BasicDtls'
    }

    attribute_map = {
        'pnlCash': 'pnlCash',
        'charges': 'charges',
        'basicDtls': 'basicDtls'
    }
