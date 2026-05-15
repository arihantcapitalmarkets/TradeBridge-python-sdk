import attr
from swagger_client.enums.instrument_enum import InstrumentEnum


@attr.s(auto_attribs=True)
class OrderTrailRequest:
    """Class representing an order trail request."""

    ordId: str = None
    instrument: InstrumentEnum = None

    swagger_types = {
        'ordId': 'str',
        'instrument': 'InstrumentEnum',
    }

    attribute_map = {
        'ordId': 'ordId',
        'instrument': 'instrument',
    }
