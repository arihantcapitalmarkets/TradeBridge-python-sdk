import attr


@attr.s(auto_attribs=True)
class ModifyOrderData:
    ordId: str = None
    ordStatus: str = None
    rejReason: str = None

    swagger_types = {
        'ordId': 'str',
        'ordStatus': 'str',
        'rejReason': 'str'
    }

    attribute_map = {
        'ordId': 'ordId',
        'ordStatus': 'ordStatus',
        'rejReason': 'rejReason'
    }
