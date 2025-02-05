import attr
from datetime import datetime


@attr.s(auto_attribs=True, repr=False)
class Data:
    accessToken: str = None
    expiryTime: str = None
    ddpi: bool = None
    poaFlag: str = None
    intellectJwtToken: str = None
    mobileNumber: str = None
    mpinEnabled: bool = None
    userName: str = None
    appId: str = None
    redirectUrl: str = None
    refreshToken: str = None
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
        """Format datetime to full ISO format with nanosecond precision."""
        if token_expiry is not None:
            # Get microseconds and calculate nanoseconds separately
            timestamp_ns = int(token_expiry.timestamp() * 1_000_000_000)  # Convert to nanoseconds
            dt_iso = token_expiry.strftime('%Y-%m-%dT%H:%M:%S')  # Base ISO format without microseconds
            nanoseconds = f"{timestamp_ns % 1_000_000_000:09d}"  # Extract last 9 digits (nanoseconds)
            return f"{dt_iso}.{nanoseconds}"  # Combine properly formatted parts
        return None

    @staticmethod
    def parse_token_expiry(token_expiry_str: str) -> datetime:
        """Parse ISO format with nanoseconds precision back to datetime."""
        if token_expiry_str is not None:
            base_time, nano_str = token_expiry_str.split(".")  # Split seconds and nanoseconds
            micro_str = nano_str[:6]  # Convert nanoseconds to microseconds for Python support
            return datetime.strptime(f"{base_time}.{micro_str}", '%Y-%m-%dT%H:%M:%S.%f')
        return None

    def to_dict(self):
        """Return dictionary representation, ensuring tokenExpiry is formatted correctly."""
        data = {key: value for key, value in attr.asdict(self).items() if value is not None}
        if self.tokenExpiry:
            data['tokenExpiry'] = self.format_token_expiry(self.tokenExpiry)
        return data

    def __repr__(self):
        """Custom string representation, ensuring tokenExpiry is formatted correctly."""
        fields = ', '.join(
            f"{key}={self.format_token_expiry(value) if key == 'tokenExpiry' and value is not None else repr(value)}"
            for key, value in attr.asdict(self).items() if value is not None
        )
        return f"{self.__class__.__name__}({fields})"
