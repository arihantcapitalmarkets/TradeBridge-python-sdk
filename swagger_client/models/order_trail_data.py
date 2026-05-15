import attr
from swagger_client.models.symbol_dto import SymbolDto
from typing import List


@attr.s(auto_attribs=True, repr=False)
class OrderDetails:
    tradedQty:int = None
    ordValidity:str = None
    ordAction:str = None
    triggerPrice: float = None
    prdType:str = None
    qty: int = None
    pendingQty: int = None
    disQty: int = None
    avgPrice: float = None
    ordId: str = None
    ordType: str = None
    currentOrdStatus: str = None
    rejReason: str = None

    swagger_types = {
        'tradedQty': 'int',
        'ordValidity': 'str',
        'ordAction': 'str',
        'triggerPrice': 'float',
        'prdType': 'str',
        'qty': 'int',
        'pendingQty': 'int',
        'disQty': 'int',
        'avgPrice': 'float',
        'ordId': 'str',
        'ordType': 'str',
        'currentOrdStatus': 'str',
        'rejReason': 'str'
    }

    attribute_map = {
        'tradedQty': 'tradedQty',
        'ordValidity': 'ordValidity',
        'ordAction': 'ordAction',
        'triggerPrice': 'triggerPrice',
        'prdType': 'prdType',
        'qty': 'qty',
        'pendingQty': 'pendingQty',
        'disQty': 'disQty',
        'avgPrice': 'avgPrice',
        'ordId': 'ordId',
        'ordType': 'ordType',
        'currentOrdStatus': 'currentOrdStatus',
        'rejReason': 'rejReason'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class OrderTrail:
    limitPrice: float = None
    lupdateDateTime: str = None
    modifiedBy: str = None
    status: str = None
    rejReason: str = None
    avgPrice: float = None
    qty: int = None
    pendingQty: int = None
    disQty: int = None
    exc: str = None
    tradedQty: int = None
    orderUpdatedAt: str = None

    swagger_types = {
        'limitPrice': 'float',
        'lupdateDateTime': 'str',
        'modifiedBy': 'str',
        'status': 'str',
        'rejReason': 'str',
        'avgPrice': 'float',
        'qty': 'int',
        'pendingQty': 'int',
        'disQty': 'int',
        'exc': 'str',
        'tradedQty': 'int',
        'orderUpdatedAt': 'str'
    }

    attribute_map = {
        'limitPrice': 'limitPrice',
        'lupdateDateTime': 'lupdateDateTime',
        'modifiedBy': 'modifiedBy',
        'status': 'status',
        'rejReason': 'rejReason',
        'avgPrice': 'avgPrice',
        'qty': 'qty',
        'pendingQty': 'pendingQty',
        'disQty': 'disQty',
        'exc': 'exc',
        'tradedQty': 'tradedQty',
        'orderUpdatedAt': 'orderUpdatedAt'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class OrderTrailData:
    symbol: SymbolDto = None
    orderDetails: OrderDetails = None
    trails: List[OrderTrail] = None

    swagger_types = {
        'symbol': SymbolDto,
        'orderDetails': 'OrderDetails',
        'trails': 'list[OrderTrail]'
    }

    attribute_map = {
        'symbol': 'symbol',
        'orderDetails': 'orderDetails',
        'trails': 'trails'
    }

