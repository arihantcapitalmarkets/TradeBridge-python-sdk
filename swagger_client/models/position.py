import attr
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class Position:
    symbol: SymbolDto = None
    prdType : str = None
    type: str = None
    ltp : float = None
    bookedPnl: str = None
    unRealizedPnl: str = None
    pnlPerc: float = None
    netPnl:float = None
    prevPos: int = None
    currPos: int = None
    currAvgPrice: float = None
    prevAvgPrice: float = None
    netQty: int = None
    buyQty: int = None
    sellQty: int = None
    dayBuyQty: int = None
    daySellQty: int = None
    cfBuyQty: int = None
    cfSellQty: int = None
    buyAvgPrice: float = None
    sellAvgPrice: float = None
    dayBuyAvgPrice: float = None
    daySellAvgPrice: float = None
    cfBuyAvgPrice: float = None
    cfSellAvgPrice: float = None
    buyAmt: float = None
    sellAmt: float = None
    cfBuyAmt: float = None
    cfSellAmt: float = None
    avgPrice: float = None
    undAsset:str = None
    squareOff:bool = None
    transferable: bool = None
    ordAction: str = None

    swagger_types = {
        'symbol': SymbolDto,
        'prdType': 'str',
        'type': 'str',
        'ltp': 'float',
        'bookedPnl': 'str',
        'unRealizedPnl': 'str',
        'pnlPerc': 'float',
        'netPnl': 'float',
        'prevPos': 'int',
        'prevAvgPrice': 'float',
        'currPos': 'int',
        'currAvgPrice': 'float',
        'netQty': 'int',
        'buyQty': 'int',
        'sellQty': 'int',
        'dayBuyQty': 'int',
        'daySellQty': 'int',
        'cfBuyQty': 'int',
        'cfSellQty': 'int',
        'buyAvgPrice': 'float',
        'sellAvgPrice': 'float',
        'dayBuyAvgPrice': 'float',
        'daySellAvgPrice': 'float',
        'cfBuyAvgPrice': 'float',
        'cfSellAvgPrice': 'float',
        'buyAmt': 'float',
        'sellAmt': 'float',
        'cfBuyAmt': 'float',
        'cfSellAmt': 'float',
        'avgPrice': 'float',
        'undAsset': 'str',
        'squareOff': 'bool',
        'transferable': 'bool',
        'ordAction': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'prdType': 'prdType',
        'type': 'type',
        'ltp': 'ltp',
        'bookedPnl': 'bookedPnl',
        'unRealizedPnl': 'unRealizedPnl',
        'pnlPerc': 'pnlPerc',
        'netPnl': 'netPnl',
        'prevPos': 'prevPos',
        'prevAvgPrice': 'prevAvgPrice',
        'currPos': 'currPos',
        'currAvgPrice': 'currAvgPrice',
        'netQty': 'netQty',
        'buyQty': 'buyQty',
        'sellQty': 'sellQty',
        'dayBuyQty': 'dayBuyQty',
        'daySellQty': 'daySellQty',
        'cfBuyQty': 'cfBuyQty',
        'cfSellQty': 'cfSellQty',
        'buyAvgPrice': 'buyAvgPrice',
        'sellAvgPrice': 'sellAvgPrice',
        'dayBuyAvgPrice': 'dayBuyAvgPrice',
        'daySellAvgPrice': 'daySellAvgPrice',
        'cfBuyAvgPrice': 'cfBuyAvgPrice',
        'cfSellAvgPrice': 'cfSellAvgPrice',
        'buyAmt': 'buyAmt',
        'sellAmt': 'sellAmt',
        'cfBuyAmt': 'cfBuyAmt',
        'cfSellAmt': 'cfSellAmt',
        'avgPrice': 'avgPrice',
        'undAsset': 'undAsset',
        'squareOff': 'squareOff',
        'transferable': 'transferable',
        'ordAction': 'ordAction'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"