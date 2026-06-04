from typing import List
import attr


@attr.s(auto_attribs=True)
class MultiFilter:
    key: str = None
    value: List[str] = None

    swagger_types = {
        'key': 'str',
        'value': 'list[str]',
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
    }


@attr.s(auto_attribs=True)
class TradeHistoryRequest:
    frmDte: str = None
    toDte: str = None
    multiFilters: List[MultiFilter] = None

    swagger_types = {
        'frmDte': 'str',
        'toDte': 'str',
        'multiFilters': 'list[MultiFilter]',
    }

    attribute_map = {
        'frmDte': 'frmDte',
        'toDte': 'toDte',
        'multiFilters': 'multiFilters',
    }