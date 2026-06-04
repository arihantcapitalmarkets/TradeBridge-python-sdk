import attr


@attr.s(auto_attribs=True)
class DpHoldingsRequest:
    date: str = None
    dpName: str = None

    swagger_types = {
        'date': 'str',
        'dpName': 'str',
    }

    attribute_map = {
        'date': 'date',
        'dpName': 'dpName',
    }
