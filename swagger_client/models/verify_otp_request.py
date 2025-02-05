import attr


@attr.s(auto_attribs=True)
class VerifyOtpRequest:
    userId: str = None
    txnId: str = None
    otp: str = None

    swagger_types = {
        'userId': 'str',
        'txnId': 'str',
        'otp': 'str'
    }

    attribute_map = {
        'userId': 'userId',
        'txnId': 'txnId',
        'otp': 'otp'
    }
