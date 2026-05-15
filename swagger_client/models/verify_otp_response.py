import attr
from swagger_client.models.data import Data


@attr.s(auto_attribs=True)
class VerifyOtpResponse:
    infoID: str = None
    infoMsg: str = None
    data: Data = None
    timestamp: int = None

    swagger_types = {
        'infoID': 'str',
        'infoMsg': 'str',
        'data': 'Data',
        'timestamp': 'int'
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }

    def to_dict(self):
        """Convert object to dictionary, ensuring `data` is serialized properly."""
        return {
            key: (value.to_dict() if isinstance(value, Data) else value)
            for key, value in attr.asdict(self).items()
            if value is not None
        }

    def __repr__(self):
        """Custom string representation, ensuring `data` is formatted properly."""
        fields = ', '.join(
            f"{key}={value.to_dict() if isinstance(value, Data) else repr(value)}"
            for key, value in attr.asdict(self).items()
            if value is not None
        )
        return f"{self.__class__.__name__}({fields})"

