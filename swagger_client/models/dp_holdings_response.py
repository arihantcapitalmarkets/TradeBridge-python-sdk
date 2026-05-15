import attr
from typing import List, Any
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class Equity:
    scripName: str = None
    rate: str = None
    sym: SymbolDto = None
    freeQty: str = None
    pledgeQty: str = None
    totQty: str = None
    mrktVal: str = None

    swagger_types = {
        'scripName': 'str',
        'rate': 'str',
        'sym': SymbolDto,
        'freeQty': 'str',
        'pledgeQty': 'str',
        'totQty': 'str',
        'mrktVal': 'str'
    }

    attribute_map = {
        'scripName': 'scripName',
        'rate': 'rate',
        'sym': 'sym',
        'freeQty': 'freeQty',
        'pledgeQty': 'pledgeQty',
        'totQty': 'totQty',
        'mrktVal': 'mrktVal'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class DpBasicDtls:
    Client_ID: str = None
    Client_Name: str = None
    Date: str = None

    swagger_types = {
        'Client_ID': 'str',
        'Client_Name': 'str',
        'Date': 'str'
    }

    attribute_map = {
        'Client_ID': 'Client ID',
        'Client_Name': 'Client Name',
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
class DpHoldingsSuccessData:
    basicDtls: DpBasicDtls = None
    equity: List[Equity] = None
    bonds: List[Any] = None
    mutualFunds: List[Any] = None

    swagger_types = {
        'basicDtls': 'DpBasicDtls',
        'equity': 'list[Equity]',
        'bonds': 'list[object]',
        'mutualFunds': 'list[object]'
    }

    attribute_map = {
        'basicDtls': 'basicDtls',
        'equity': 'equity',
        'bonds': 'bonds',
        'mutualFunds': 'mutualFunds'
    }


@attr.s(auto_attribs=True)
class DpHoldingsResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: DpHoldingsSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': DpHoldingsSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
