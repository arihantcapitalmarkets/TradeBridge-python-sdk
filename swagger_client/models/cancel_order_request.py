import attr
from swagger_client.enums.exc_enum import ExcEnum

@attr.s(auto_attribs=True)
class CancelOrderRequest:
    """Class representing a request to cancel an order."""

    symbol: str = None
    exc: ExcEnum = None
    ordId: str = None

    swagger_types = {
        'symbol': 'str',
        'exc': 'ExcEnum',
        'ordId': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'ordId': 'ordId'
    }
