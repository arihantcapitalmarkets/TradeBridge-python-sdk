import attr
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class Holding:
    symbol: SymbolDto = None
    ltp: float= None
    qty: int = None
    holdingQty: int = None
    usedQty: int= None
    btst : int = None
    pledgeQty: int = None
    prdType : str = None
    avgPrice: float = None
    invested: float = None
    marketValue: float = None
    pnlPerc: float = None
    unRealizedPnl: float = None
    haircut: float = None
    pledgeable: bool = None
    closePrice: float = None
    freeQty: int = None

    swagger_types = {
        'symbol': SymbolDto,
        'ltp': 'float',
        'qty': 'int',
        'holdingQty': 'int',
        'usedQty': 'int',
        'btst': 'int',
        'pledgeQty': 'int',
        'prdType': 'str',
        'avgPrice': 'float',
        'invested': 'float',
        'marketValue': 'float',
        'pnlPerc': 'float',
        'unRealizedPnl': 'float',
        'haircut': 'float',
        'pledgeable': 'bool',
        'closePrice': 'float',
        'freeQty': 'int'
    }

    attribute_map = {
        'symbol': 'symbol',
        'ltp': 'ltp',
        'qty': 'qty',
        'holdingQty': 'holdingQty',
        'usedQty': 'usedQty',
        'btst': 'btst',
        'pledgeQty': 'pledgeQty',
        'prdType': 'prdType',
        'avgPrice': 'avgPrice',
        'invested': 'invested',
        'marketValue': 'marketValue',
        'pnlPerc': 'pnlPerc',
        'unRealizedPnl': 'unRealizedPnl',
        'haircut': 'haircut',
        'pledgeable': 'pledgeable',
        'closePrice': 'closePrice',
        'freeQty': 'freeQty'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"