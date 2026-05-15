import attr
from datetime import datetime


@attr.s(auto_attribs=True, repr=False)
class Data:
    msxtendInfo: str = None
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
        'msxtendInfo': str,
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
        'msxtendInfo': 'msxtendInfo',
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

    # ✅ Auto-convert string → datetime after object creation
    def __attrs_post_init__(self):
        if isinstance(self.tokenExpiry, str):
            self.tokenExpiry = self.parse_token_expiry(self.tokenExpiry)

    @staticmethod
    def format_token_expiry(token_expiry) -> str:
        """Format datetime to ISO format with nanosecond precision."""
        if token_expiry is None:
            return None

        # 🔥 Handle string safely
        if isinstance(token_expiry, str):
            token_expiry = Data.parse_token_expiry(token_expiry)

        timestamp_ns = int(token_expiry.timestamp() * 1_000_000_000)
        dt_iso = token_expiry.strftime('%Y-%m-%dT%H:%M:%S')
        nanoseconds = f"{timestamp_ns % 1_000_000_000:09d}"

        return f"{dt_iso}.{nanoseconds}"

    @staticmethod
    def parse_token_expiry(token_expiry_str: str) -> datetime:
        """Parse ISO string (with/without nanoseconds) → datetime."""
        if token_expiry_str is None:
            return None

        try:
            if "." in token_expiry_str:
                base_time, nano_str = token_expiry_str.split(".")
                micro_str = nano_str[:6]  # Python supports microseconds
                return datetime.strptime(f"{base_time}.{micro_str}", '%Y-%m-%dT%H:%M:%S.%f')
            else:
                return datetime.strptime(token_expiry_str, '%Y-%m-%dT%H:%M:%S')
        except Exception:
            # 🔥 fallback (prevents crash)
            return None

    def to_dict(self):
        """Return dict, formatting tokenExpiry correctly."""
        data = {k: v for k, v in attr.asdict(self).items() if v is not None}

        if self.tokenExpiry:
            data['tokenExpiry'] = self.format_token_expiry(self.tokenExpiry)

        return data

    def __repr__(self):
        """Clean representation without crashing."""
        fields = ', '.join(
            f"{key}={self.format_token_expiry(value) if key == 'tokenExpiry' else repr(value)}"
            for key, value in attr.asdict(self).items()
            if value is not None
        )
        return f"{self.__class__.__name__}({fields})"