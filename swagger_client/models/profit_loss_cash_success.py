import attr
from swagger_client.models.profit_loss_cash_success_data import ProfitLossCashSuccessData


@attr.s(auto_attribs=True)
class ProfitLossCashSuccess(object):
    infoID: str = None
    infoMsg: str = None
    data: ProfitLossCashSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': ProfitLossCashSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
