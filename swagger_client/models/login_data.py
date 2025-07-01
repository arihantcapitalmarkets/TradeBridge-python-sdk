import attr


@attr.s(auto_attribs=True, repr=False)
class LoginData:
    msxtendInfo: str = None
    message: str = None
    txnId: str = None
    otpExpiryTime: str = None
    twoFAType: str = None

    swagger_types = {
        'msxtendInfo': 'str',
        'message': 'str',
        'txnId': 'str',
        'otpExpiryTime': 'str',
        'twoFAType': 'str'
    }

    attribute_map = {
        'msxtendInfo': 'msxtendInfo',
        'message': 'message',
        'txnId': 'txnId',
        'otpExpiryTime': 'otpExpiryTime',
        'twoFAType': 'twoFAType'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"
