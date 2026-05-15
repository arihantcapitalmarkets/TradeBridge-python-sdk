import attr


@attr.s(auto_attribs=True)
class SuccessResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: dict = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': object,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }