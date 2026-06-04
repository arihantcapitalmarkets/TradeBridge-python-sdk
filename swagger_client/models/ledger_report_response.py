import attr
from swagger_client.models.ledger_success_data import LedgerSuccessData

@attr.s(auto_attribs=True)
class LedgerReportResponse(object):
    infoID: str = None
    infoMsg: str = None
    data: LedgerSuccessData = None
    timestamp: int = None

    swagger_types = {
        'infoID': str,
        'infoMsg': str,
        'data': LedgerSuccessData,
        'timestamp': int
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }