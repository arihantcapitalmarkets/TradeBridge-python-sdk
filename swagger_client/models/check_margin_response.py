import attr


@attr.s(auto_attribs=True, repr=False)
class CheckMarginData:
    availableCash: str = None
    marginUsed: str = None
    availableMargin: str = None
    orderMargin: str = None

    swagger_types = {
        'availableCash': 'str',
        'marginUsed': 'str',
        'availableMargin': 'str',
        'orderMargin': 'str'
    }

    attribute_map = {
        'availableCash': 'availableCash',
        'marginUsed': 'marginUsed',
        'availableMargin': 'availableMargin',
        'orderMargin': 'orderMargin'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class CheckMarginResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: CheckMarginData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': CheckMarginData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
