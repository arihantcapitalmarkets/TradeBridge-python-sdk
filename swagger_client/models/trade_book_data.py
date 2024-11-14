import attr
from typing import List
from swagger_client.models.trade_book import TradeBook


@attr.s(auto_attribs=True)
class TradeBookData:
    trades : List[TradeBook]

    swagger_types = {
        'trades': 'list[TradeBook]'
    }

    attribute_map = {
        'trades': 'trades'
    }
