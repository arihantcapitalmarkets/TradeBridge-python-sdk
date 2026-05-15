import attr

from swagger_client.models.data import Data


@attr.s(auto_attribs=True)
class RefreshTokenResponse:
    infoID: str = None
    infoMsg: str = None
    data: Data = None
    timestamp: int = None

    swagger_types = {
        'infoID': 'str',
        'infoMsg': 'str',
        'data': 'Data',
        'timestamp': 'int'
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
