import attr
from typing import List


@attr.s(auto_attribs=True, repr=False)
class Symbols:
    dispSym: List[str] = None
    excToken: List[str] = None

    swagger_types = {
        'dispSym': 'list[str]',
        'excToken': 'list[str]'
    }

    attribute_map = {
        'dispSym': 'dispSym',
        'excToken': 'excToken'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"

@attr.s(auto_attribs=True)
class SurveillanceSymbolsData:
    symbols: Symbols = None

    swagger_types = {
        'symbols': 'Symbols'
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
class SurveillanceSymbolsResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: SurveillanceSymbolsData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': SurveillanceSymbolsData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }