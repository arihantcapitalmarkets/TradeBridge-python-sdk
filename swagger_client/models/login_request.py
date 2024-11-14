import attr


@attr.s(auto_attribs=True)
class LoginRequest:
    """Class representing the login request body."""
    userId: str = None
    password: str = None
    mobileNumber: str = None

    swagger_types = {
        'userId': str,
        'password': str,
        'mobileNumber': str
    }

    attribute_map = {
        'userId': 'userId',
        'password': 'password',
        'mobileNumber': 'mobileNumber'
    }

