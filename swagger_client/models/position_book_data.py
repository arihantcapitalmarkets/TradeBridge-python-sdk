import attr
from typing import List
from swagger_client.models.position import Position


@attr.s(auto_attribs=True)
class PositionBookData:
    positions : List[Position] = None

    swagger_types = {
        'positions': 'list[Position]'
    }

    attribute_map = {
        'positions': 'positions'
    }
