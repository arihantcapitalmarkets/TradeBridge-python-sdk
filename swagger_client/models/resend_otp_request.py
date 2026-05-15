import attr


@attr.s(auto_attribs=True)
class ResendOtpRequest:
    """Class representing the full login response."""
    userId: str = None
    txnId: str = None

    swagger_types = {
        'userId': 'str',
        'txnId': 'str'
    }

    attribute_map = {
        'userId': 'userId',
        'txnId': 'txnId'
    }

