import attr


@attr.s(auto_attribs=True)
class LoginRequest:
    """Class representing the login request body."""
    userId: str = None
    mobNo: str = None
    email: str = None
    password: str = None

    swagger_types = {
        'userId': str,
        'mobNo': str,
        'email': str,
        'password': str
    }

    attribute_map = {
        'userId': 'userId',
        'mobNo': 'mobNo',
        'email': 'email',
        'password': 'password'
    }

