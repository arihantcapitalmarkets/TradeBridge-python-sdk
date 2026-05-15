import attr
from typing import List


@attr.s(auto_attribs=True)
class IntradaySuccessData:
    dataPoints: List[List[object]] = None

    swagger_types = {
        'dataPoints': 'list[list[object]]'

    }

    attribute_map = {
        'dataPoints': 'dataPoints',
    }
