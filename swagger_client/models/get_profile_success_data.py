import attr
from typing import List, Any

@attr.s(auto_attribs=True, repr=False)
class ProfileClientDtl:
    """Class representing client details for a profile."""

    name: [str] = None
    mobNo: [str] = None
    email: [str] = None
    clientCode: [str] = None
    exc: list[str] = None

    swagger_types = {
        'name': 'str',
        'mobNo': 'str',
        'email': 'str',
        'clientCode': 'str',
        'exc': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'mobNo': 'mobNo',
        'email': 'email',
        'clientCode': 'clientCode',
        'exc': 'exc'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class GetProfileSuccessData(object):
    """Class representing the profile success data."""

    clientDtls: List[ProfileClientDtl] = None

    swagger_types = {
        'clientDtls': 'list[ProfileClientDtl]'
    }

    attribute_map = {
        'clientDtls': 'clientDtls',
    }
