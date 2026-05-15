import attr
from typing import List
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class Report:
    date: str = None
    tradeTime: str = None
    netAmt: str = None
    ordAction: str = None
    netQty: str = None
    orderNo: str = None
    sym: SymbolDto = None
    avgPrice: str = None

    swagger_types = {
        'date': 'str',
        'tradeTime': 'str',
        'netAmt': 'str',
        'ordAction': 'str',
        'netQty': 'str',
        'orderNo': 'str',
        'sym': SymbolDto,
        'avgPrice': 'str'
    }

    attribute_map = {
        'date': 'date',
        'tradeTime': 'tradeTime',
        'netAmt': 'netAmt',
        'ordAction': 'ordAction',
        'netQty': 'netQty',
        'orderNo': 'orderNo',
        'sym': 'sym',
        'avgPrice': 'avgPrice'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class TradeHistorySuccessData:
    reportList: List[Report] = None

    swagger_types = {
        'reportList': 'list[Report]'
    }

    attribute_map = {
        'reportList': 'reportList'
    }


@attr.s(auto_attribs=True)
class TradeHistoryResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: TradeHistorySuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': TradeHistorySuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
