
import attr
from typing import List, Any


@attr.s(auto_attribs=True, repr=False)
class ProfileBankDtl:
    bankBranch: [str] = None
    isPrimary: [str] = None
    bankName: [str] = None
    bankAccNo: [str] = None
    ifsc: [str] = None

    swagger_types = {
        'bankBranch': 'str',
        'isPrimary': 'str',
        'bankName': 'str',
        'bankAccNo': 'str',
        'ifsc': 'str'
    }

    attribute_map = {
        'bankBranch': 'bankBranch',
        'isPrimary': 'isPrimary',
        'bankName': 'bankName',
        'bankAccNo': 'bankAccNo',
        'ifsc': 'ifsc'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class ProfileClientDtl:
    """Class representing client details for a profile."""

    corrPinCode: [str] = None
    depoName: [str] = None
    permAddrs: [str] = None
    gender: [str] = None
    dpName: [str] = None
    isDpEnabled: [str] = None
    exc: list[str] = None
    mobNo: [str] = None
    corrCountry: [str] = None
    permState: [str] = None
    email: [str] = None
    mtf: [str] = None
    fathOrHusName: [str] = None
    corrCity: [str] = None
    dematAccNo: [str] = None
    depoParticipant: [str] = None
    dpId: [str] = None
    motherName: [str] = None
    isNonPoaUser: [str] = None
    panNumber: [str] = None
    corrState: [str] = None
    dob: [str] = None
    permCountry: [str] = None
    name: [str] = None
    permCity: [str] = None
    taxResidence: [str] = None
    permPinCode: [str] = None
    corrAddrs: [str] = None
    maritalStatus: [str] = None

    swagger_types = {
        'corrPinCode': 'str',
        'depoName': 'str',
        'permAddrs': 'str',
        'gender': 'str',
        'dpName': 'str',
        'isDpEnabled': 'str',
        'exc': 'list[str]',
        'mobNo': 'str',
        'corrCountry': 'str',
        'permState': 'str',
        'email': 'str',
        'mtf': 'str',
        'fathOrHusName': 'str',
        'corrCity': 'str',
        'dematAccNo': 'str',
        'depoParticipant': 'str',
        'dpId': 'str',
        'motherName': 'str',
        'isNonPoaUser': 'str',
        'panNumber': 'str',
        'corrState': 'str',
        'dob': 'str',
        'permCountry': 'str',
        'name': 'str',
        'permCity': 'str',
        'taxResidence': 'str',
        'permPinCode': 'str',
        'corrAddrs': 'str',
        'maritalStatus': 'str'
    }

    attribute_map = {
        'corrPinCode': 'corrPinCode',
        'depoName': 'depoName',
        'permAddrs': 'permAddrs',
        'gender': 'gender',
        'dpName': 'dpName',
        'isDpEnabled': 'isDpEnabled',
        'exc': 'exc',
        'mobNo': 'mobNo',
        'corrCountry': 'corrCountry',
        'permState': 'permState',
        'email': 'email',
        'mtf': 'mtf',
        'fathOrHusName': 'fathOrHusName',
        'corrCity': 'corrCity',
        'dematAccNo': 'dematAccNo',
        'depoParticipant': 'depoParticipant',
        'dpId': 'dpId',
        'motherName': 'motherName',
        'isNonPoaUser': 'isNonPoaUser',
        'panNumber': 'panNumber',
        'corrState': 'corrState',
        'dob': 'dob',
        'permCountry': 'permCountry',
        'name': 'name',
        'permCity': 'permCity',
        'taxResidence': 'taxResidence',
        'permPinCode': 'permPinCode',
        'corrAddrs': 'corrAddrs',
        'maritalStatus': 'maritalStatus'
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

    bankDtls: List[ProfileBankDtl] = None
    clientDtls: List[ProfileClientDtl] = None
    nomineeContactDtls: List[Any] = None
    nomineeNsdl: List[Any] = None
    nomineeCdsl: List[Any] = None

    swagger_types = {
        'bankDtls': 'list[ProfileBankDtl]',
        'clientDtls': 'list[ProfileClientDtl]',
        'nomineeContactDtls': 'list[object]',
        'nomineeNsdl': 'list[object]',
        'nomineeCdsl': 'list[object]'
    }

    attribute_map = {
        'bankDtls': 'bankDtls',
        'clientDtls': 'clientDtls',
        'nomineeContactDtls': 'nomineeContactDtls',
        'nomineeNsdl': 'nomineeNsdl',
        'nomineeCdsl': 'nomineeCdsl'
    }
