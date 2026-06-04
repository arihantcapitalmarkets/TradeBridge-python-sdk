import attr
from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum

@attr.s(auto_attribs=True)
class IntradayCandleDataRequest:
    """Class representing the data for intraday candle request."""

    symbol: str = None
    resolution: str = None
    instrument: InstrumentEnum = None
    exc: ExcEnum = None
    startTime: str = None
    endTime: str = None

    swagger_types = {
        'symbol': 'str',
        'resolution': 'str',
        'instrument': 'InstrumentEnum',
        'exc': 'ExcEnum',
        'startTime': 'str',
        'endTime': 'str',
    }

    attribute_map = {
        'symbol': 'symbol',
        'resolution': 'resolution',
        'instrument': 'instrument',
        'exc': 'exc',
        'startTime': 'startTime',
        'endTime': 'endTime',
    }
