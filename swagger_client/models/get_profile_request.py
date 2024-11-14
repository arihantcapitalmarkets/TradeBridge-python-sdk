import attr


@attr.s(auto_attribs=True)
class GetProfileRequestData:
    pass

    swagger_types = {}
    attribute_map = {}


@attr.s(auto_attribs=True)
class GetProfileRequest:
    data: GetProfileRequestData = None
    appID: str = None

    swagger_types = {
        'data': 'GetProfileRequestData',
        'appID': 'str'
    }

    attribute_map = {
        'data': 'data',
        'appID': 'appID'
    }
