from typing import Dict

import attr


@attr.s(auto_attribs=True)
class SuccessResponse:
    """Class representing the full login response."""
    infoID: str = None
    infoMsg: str = None
    data: Dict[str, str] = None
    timestamp: int = None

    swagger_types = {
        'infoID': 'str',
        'infoMsg': 'str',
        'data': 'dict(str, str)',
        'timestamp': 'int'
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
