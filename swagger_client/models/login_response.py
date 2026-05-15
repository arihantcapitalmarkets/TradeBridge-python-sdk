import attr

from swagger_client.models.login_data import LoginData


@attr.s(auto_attribs=True)
class LoginResponse:
    """Class representing the full login response."""
    infoID: str = None
    infoMsg: str = None
    data: LoginData = None
    timestamp: int = None

    swagger_types = {
        'infoID': 'str',
        'infoMsg': 'str',
        'data': 'LoginData',
        'timestamp': 'int'
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }

