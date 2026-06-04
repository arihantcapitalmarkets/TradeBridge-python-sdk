import attr
from typing import List
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True)
class SymbolMasterData:
    symbols: List[SymbolDto] = None

    swagger_types = {
        'symbols': 'list[SymbolDto]'
    }

    attribute_map = {
        'symbols': 'symbols'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class ContractMasterResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: SymbolMasterData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': SymbolMasterData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
