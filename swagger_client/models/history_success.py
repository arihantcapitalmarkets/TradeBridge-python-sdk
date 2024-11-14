import attr
from swagger_client.models.historical_candle_data import HistoricalCandleData


@attr.s(auto_attribs=True)
class HistorySuccess:
    infoID: str = None
    infoMsg: str = None
    data: HistoricalCandleData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': HistoricalCandleData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
