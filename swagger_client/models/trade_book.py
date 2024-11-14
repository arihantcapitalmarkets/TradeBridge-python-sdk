import attr
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class TradeBook:
    symbol: SymbolDto = None
    ordId: str = None
    exchTrdId: str = None
    exchOrdId: str = None
    prdType: str = None
    ordAction: str = None
    ordType: str = None
    tradedPrice: float = None
    tradeTime: str = None
    tradedQty: int = None
    remainQty: int = None
    qty: int = None
    ordValidity: str = None
    undAsset: str = None

    swagger_types = {
        'symbol': SymbolDto,
        'ordId': 'str',
        'exchTrdId': 'str',
        'exchOrdId': 'str',
        'prdType': 'str',
        'ordAction': 'str',
        'ordType': 'str',
        'tradedPrice': 'float',
        'tradeTime': 'str',
        'tradedQty': 'int',
        'remainQty': 'int',
        'qty': 'int',
        'ordValidity': 'str',
        'undAsset': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'ordId': 'ordId',
        'exchTrdId': 'exchTrdId',
        'exchOrdId': 'exchOrdId',
        'prdType': 'prdType',
        'ordAction': 'ordAction',
        'ordType': 'ordType',
        'tradedPrice': 'tradedPrice',
        'tradeTime': 'tradeTime',
        'tradedQty': 'tradedQty',
        'remainQty': 'remainQty',
        'qty': 'qty',
        'ordValidity': 'ordValidity',
        'undAsset': 'undAsset'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"
