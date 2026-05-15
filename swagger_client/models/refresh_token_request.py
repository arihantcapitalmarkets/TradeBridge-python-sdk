import attr


@attr.s(auto_attribs=True)
class RefreshTokenRequest:
    userId: str = None
    refreshToken: str = None

    swagger_types = {
        'userId': 'str',
        'refreshToken': 'str'
    }

    attribute_map = {
        'userId': 'userId',
        'refreshToken': 'refreshToken'
    }
