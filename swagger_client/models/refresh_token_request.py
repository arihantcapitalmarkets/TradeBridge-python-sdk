import attr


@attr.s(auto_attribs=True)
class RefreshTokenRequest:
    refreshToken: str = None

    swagger_types = {
        'refreshToken': 'str'
    }

    attribute_map = {
        'refreshToken': 'refreshToken'
    }
