import attr
from typing import List


@attr.s(auto_attribs=True)
class LedgerData:
    date: str = None
    settlementNo: str = None
    bankName: str = None
    balance: str = None
    transDte: str = None
    exch: str = None
    accountNo: str = None
    ledgerType: str = None
    from_field: str = None   # 'from' is keyword in Python
    refId: str = None
    debit: str = None
    credit: str = None
    desc: str = None
    bookType: str = None

    swagger_types = {
        'date': 'str',
        'settlementNo': 'str',
        'bankName': 'str',
        'balance': 'str',
        'transDte': 'str',
        'exch': 'str',
        'accountNo': 'str',
        'ledgerType': 'str',
        'from_field': 'str',
        'refId': 'str',
        'debit': 'str',
        'credit': 'str',
        'desc': 'str',
        'bookType': 'str'
    }

    attribute_map = {
        'date': 'date',
        'settlementNo': 'settlementNo',
        'bankName': 'bankName',
        'balance': 'balance',
        'transDte': 'transDte',
        'exch': 'exch',
        'accountNo': 'accountNo',
        'ledgerType': 'ledgerType',
        'from_field': 'from',
        'refId': 'refId',
        'debit': 'debit',
        'credit': 'credit',
        'desc': 'desc',
        'bookType': 'bookType'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True, repr=False)
class LedgerBasicDtls:
    Client_ID: str = None
    To: str = None
    Date: str = None

    swagger_types = {
        'Client_ID': 'str',
        'To': 'str',
        'Date': 'str'
    }

    attribute_map = {
        'Client_ID': 'Client ID',
        'To': 'To',
        'Date': 'Date'
    }

    def to_dict(self):
        return {k: v for k, v in attr.asdict(self).items() if v is not None}

    def __repr__(self):
        fields = ', '.join(f'{k}={v!r}' for k, v in attr.asdict(self).items() if v is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class LedgerSuccessData:
    ledgerData: List[LedgerData] = None
    availableFunds: str = None
    cashMarClosingBal: str = None
    openingBal: str = None
    basicDtls: LedgerBasicDtls = None
    closingBal: str = None
    regClosingBal: str = None
    comClosingBal: str = None
    isMTFSetOff: str = None
    mtfClosingBal: str = None

    swagger_types = {
        'ledgerData': 'list[LedgerData]',
        'availableFunds': 'str',
        'cashMarClosingBal': 'str',
        'openingBal': 'str',
        'basicDtls': 'LedgerBasicDtls',
        'closingBal': 'str',
        'regClosingBal': 'str',
        'comClosingBal': 'str',
        'isMTFSetOff': 'str',
        'mtfClosingBal': 'str'
    }

    attribute_map = {
        'ledgerData': 'ledgerData',
        'availableFunds': 'availableFunds',
        'cashMarClosingBal': 'cashMarClosingBal',
        'openingBal': 'openingBal',
        'basicDtls': 'basicDtls',
        'closingBal': 'closingBal',
        'regClosingBal': 'regClosingBal',
        'comClosingBal': 'comClosingBal',
        'isMTFSetOff': 'isMTFSetOff',
        'mtfClosingBal': 'mtfClosingBal'
    }