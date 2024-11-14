import attr
from datetime import datetime


@attr.s(auto_attribs=True, repr=False)
class LoginData:
    accessToken: str = None
    refreshToken: str = None
    expiryTime: str = None
    ddpi: bool = None
    poaFlag: str = None
    intellectJwtToken: str = None
    mobileNumber: str = None
    mpinEnabled: bool = None
    userName: str = None
    appId: str = None
    redirectUrl: str = None
    tokenExpiry: datetime = None

    swagger_types = {
        'accessToken': str,
        'refreshToken': str,
        'expiryTime': str,
        'ddpi': bool,
        'poaFlag': str,
        'intellectJwtToken': str,
        'mobileNumber': str,
        'mpinEnabled': bool,
        'userName': str,
        'appId': str,
        'redirectUrl': str,
        'tokenExpiry': datetime
    }

    attribute_map = {
        'accessToken': 'accessToken',
        'refreshToken': 'refreshToken',
        'expiryTime': 'expiryTime',
        'ddpi': 'ddpi',
        'poaFlag': 'poaFlag',
        'intellectJwtToken': 'intellectJwtToken',
        'mobileNumber': 'mobileNumber',
        'mpinEnabled': 'mpinEnabled',
        'userName': 'userName',
        'appId': 'appId',
        'redirectUrl': 'redirectUrl',
        'tokenExpiry': 'tokenExpiry'
    }

    @staticmethod
    def format_token_expiry(token_expiry: datetime) -> str:
        """Format datetime to ISO format with nanoseconds precision."""
        if token_expiry is not None:
            return token_expiry.strftime('%Y-%m-%dT%H:%M:%S.%f')[
                   :-3]  # Trim microseconds to milliseconds for compatibility
        return None

    @staticmethod
    def parse_token_expiry(token_expiry_str: str) -> datetime:
        """Parse ISO format with nanoseconds precision back to datetime."""
        if token_expiry_str is not None:
            return datetime.strptime(token_expiry_str, '%Y-%m-%dT%H:%M:%S.%f')
        return None

    def to_dict(self):
        """Return the dictionary representation, formatting tokenExpiry if it is not None."""
        data = {key: value for key, value in attr.asdict(self).items() if value is not None}
        if self.tokenExpiry:
            data['tokenExpiry'] = self.format_token_expiry(self.tokenExpiry)
        return data

    def __repr__(self):
        """Custom string representation, formatting tokenExpiry if it is not None."""
        fields = ', '.join(
            f'{key}={self.format_token_expiry(value) if key == "tokenExpiry" and value is not None else value!r}'
            for key, value in attr.asdict(self).items() if value is not None
        )
        return f"{self.__class__.__name__}({fields})"
