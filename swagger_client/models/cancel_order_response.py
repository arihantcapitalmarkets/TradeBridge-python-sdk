import attr


@attr.s(auto_attribs=True)
class CancelOrderResponse:
    infoID: str = None
    infoMsg: str = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'timestamp': 'timestamp'
    }
