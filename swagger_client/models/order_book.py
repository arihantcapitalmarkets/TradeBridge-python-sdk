import attr
from swagger_client.models.symbol_dto import SymbolDto


@attr.s(auto_attribs=True, repr=False)
class OrderBook:
    symbol: SymbolDto = None
    ordId: str = None
    exchOrdId: str = None
    parOrdId: str = None
    status: str = None
    ordAction: str = None
    ordType: str = None
    prdType: str = None
    ordValidity: str = None
    modifiedBy: str = None
    price: float = None
    triggerPrice: float =None
    avgPrice: float = None
    remarks: str = None
    rejReason: str = None
    ordDate: str =None
    excOrdTime: str =None
    boOrdStatus: str = None
    exitable: str =None
    qty: int = None
    disQty: int =  None
    tradedQty: int = None
    remainQty: int = None
    cancelledQty: int = None
    mktPro: str = None
    undAsset: str = None
    amo: bool = None
    modifiable: bool = None
    cancellable: bool = None
    orderStatus: str = None
    orderUpdatedAt: str = None

    swagger_types = {
        'symbol': SymbolDto,
        'ordId': 'str',
        'exchOrdId': 'str',
        'parOrdId': 'str',
        'status': 'str',
        'ordAction': 'str',
        'ordType': 'str',
        'prdType': 'str',
        'ordValidity': 'str',
        'modifiedBy': 'str',
        'price': 'float',
        'triggerPrice': 'float',
        'avgPrice': 'float',
        'remarks': 'str',
        'rejReason': 'str',
        'ordDate': 'str',
        'excOrdTime': 'str',
        'boOrdStatus': 'str',
        'exitable': 'str',
        'qty': 'int',
        'disQty': 'int',
        'tradedQty': 'int',
        'remainQty': 'int',
        'cancelledQty': 'int',
        'mktPro': 'str',
        'undAsset': 'str',
        'amo': 'bool',
        'modifiable': 'bool',
        'cancellable': 'bool',
        'orderStatus': 'str',
        'orderUpdatedAt': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'ordId': 'ordId',
        'exchOrdId': 'exchOrdId',
        'parOrdId': 'parOrdId',
        'status': 'status',
        'ordAction': 'ordAction',
        'ordType': 'ordType',
        'prdType': 'prdType',
        'ordValidity': 'ordValidity',
        'modifiedBy': 'modifiedBy',
        'price': 'price',
        'triggerPrice': 'triggerPrice',
        'avgPrice': 'avgPrice',
        'remarks': 'remarks',
        'rejReason': 'rejReason',
        'ordDate': 'ordDate',
        'excOrdTime': 'excOrdTime',
        'boOrdStatus': 'boOrdStatus',
        'exitable': 'exitable',
        'qty': 'qty',
        'disQty': 'disQty',
        'tradedQty': 'tradedQty',
        'remainQty': 'remainQty',
        'cancelledQty': 'cancelledQty',
        'mktPro': 'mktPro',
        'undAsset': 'undAsset',
        'amo': 'amo',
        'modifiable': 'modifiable',
        'cancellable': 'cancellable',
        'orderStatus': 'orderStatus',
        'orderUpdatedAt': 'orderUpdatedAt'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"