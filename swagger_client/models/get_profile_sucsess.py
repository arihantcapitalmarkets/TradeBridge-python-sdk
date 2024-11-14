import attr
from swagger_client.models.get_profile_success_data import GetProfileSuccessData


@attr.s(auto_attribs=True)
class GetProfileSuccess(object):
    infoID:str = None
    infoMsg: str = None
    data: GetProfileSuccessData = None
    timestamp:int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': GetProfileSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
