import attr
from swagger_client.models.profit_loss_fo_success_data import ProfitLossFoSuccessData


@attr.s(auto_attribs=True)
class ProfitLossFoSuccess(object):
    infoID: str = None
    infoMsg: str = None
    data: ProfitLossFoSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': ProfitLossFoSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }


