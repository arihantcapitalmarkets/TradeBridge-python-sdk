import attr
from typing import List
from swagger_client.models.order_book import OrderBook


@attr.s(auto_attribs=True)
class OrderBookData:
    orders: List[OrderBook] = None

    swagger_types = {
        'orders': 'list[OrderBook]'
    }

    attribute_map = {
        'orders': 'orders'
    }
