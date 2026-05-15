from decimal import Decimal

import attr
from typing import List
from swagger_client.models.holding import Holding


@attr.s(auto_attribs=True)
class HoldingData:
    todaysPnl: Decimal = None
    invested: Decimal = None
    unRealizedPnl: Decimal = None
    marketValue: Decimal = None
    holdings: List[Holding] = None

    swagger_types = {
        'todaysPnl': 'float',
        'invested': 'float',
        'unRealizedPnl': 'float',
        'marketValue': 'float',
        'holdings': 'list[Holding]'
    }

    attribute_map = {
        'todaysPnl': 'todaysPnl',
        'invested': 'invested',
        'unRealizedPnl': 'unRealizedPnl',
        'marketValue': 'marketValue',
        'holdings': 'holdings'
    }
