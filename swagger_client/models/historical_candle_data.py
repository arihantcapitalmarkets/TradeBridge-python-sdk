import attr
from typing import List


@attr.s(auto_attribs=True)
class HistoricalCandleData:
    dataPoints: List[List[str]] = None

    swagger_types = {
        'dataPoints': 'list[list[str]]'

    }

    attribute_map = {
        'dataPoints': 'dataPoints',
    }
