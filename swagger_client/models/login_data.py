import attr


@attr.s(auto_attribs=True, repr=False)
class LoginData:
    message: str = None
    txnId: str = None
    otpExpiryTime: str = None

    swagger_types = {
        'message': 'str',
        'txnId': 'str',
        'otpExpiryTime': 'str'
    }

    attribute_map = {
        'message': 'message',
        'txnId': 'txnId',
        'otpExpiryTime': 'otpExpiryTime'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"
