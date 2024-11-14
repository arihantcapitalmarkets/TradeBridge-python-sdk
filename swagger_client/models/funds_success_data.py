import attr


@attr.s(auto_attribs=True, repr=False)
class FundsView:
    mfAmt: str = None
    realMTM: str = None
    sellExp: str = None
    spanMargn: str = None
    payout: str = None
    cashBal: str = None
    ipoAmt: str = None
    remarksAmnt: str = None
    buyExp: str = None
    spanMrgnNRML: str = None
    delivryMrgn: str = None
    lien: str = None
    payin: str = None
    margnUsed: str = None
    ttlCashBal: str = None
    elmMargn: str = None
    cncVarMargn: str = None
    netCashAvail: str = None
    unrealMTM: str = None
    varMargn: str = None
    expMargn: str = None
    t1GrossCollatrl: str = None
    cncElmrMargn: str = None
    grossExp: str = None
    brokeragePrsnt: str = None
    collateralVal: str = None
    brnchAdhoc: str = None
    cncUnRealMTM: str = None
    unbookPNL: str = None
    scrpBsktMrgn: str = None
    notnalCash: str = None
    cncRealMTM: str = None
    spanMrgnMIS: str = None
    realizedPNL: str = None
    cncCredit: str = None
    adhocMargn: str = None
    premiumPrsnt: str = None
    remarks: str = None
    dirctColatrl: str = None

    swagger_types = {
        'mfAmt': 'str',
        'realMTM': 'str',
        'sellExp': 'str',
        'spanMargn': 'str',
        'payout': 'str',
        'cashBal': 'str',
        'ipoAmt': 'str',
        'remarksAmnt': 'str',
        'buyExp': 'str',
        'spanMrgnNRML': 'str',
        'delivryMrgn': 'str',
        'lien': 'str',
        'payin': 'str',
        'margnUsed': 'str',
        'ttlCashBal': 'str',
        'elmMargn': 'str',
        'cncVarMargn': 'str',
        'netCashAvail': 'str',
        'unrealMTM': 'str',
        'varMargn': 'str',
        'expMargn': 'str',
        't1GrossCollatrl': 'str',
        'cncElmrMargn': 'str',
        'grossExp': 'str',
        'brokeragePrsnt': 'str',
        'collateralVal': 'str',
        'brnchAdhoc': 'str',
        'cncUnRealMTM': 'str',
        'unbookPNL': 'str',
        'scrpBsktMrgn': 'str',
        'notnalCash': 'str',
        'cncRealMTM': 'str',
        'spanMrgnMIS': 'str',
        'realizedPNL': 'str',
        'cncCredit': 'str',
        'adhocMargn': 'str',
        'premiumPrsnt': 'str',
        'remarks': 'str',
        'dirctColatrl': 'str'
    }
    attribute_map = {
        'mfAmt': 'mfAmt',
        'realMTM': 'realMTM',
        'sellExp': 'sellExp',
        'spanMargn': 'spanMargn',
        'payout': 'payout',
        'cashBal': 'cashBal',
        'ipoAmt': 'ipoAmt',
        'remarksAmnt': 'remarksAmnt',
        'buyExp': 'buyExp',
        'spanMrgnNRML': 'spanMrgnNRML',
        'delivryMrgn': 'delivryMrgn',
        'lien': 'lien',
        'payin': 'payin',
        'margnUsed': 'margnUsed',
        'ttlCashBal': 'ttlCashBal',
        'elmMargn': 'elmMargn',
        'cncVarMargn': 'cncVarMargn',
        'netCashAvail': 'netCashAvail',
        'unrealMTM': 'unrealMTM',
        'varMargn': 'varMargn',
        'expMargn': 'expMargn',
        't1GrossCollatrl': 't1GrossCollatrl',
        'cncElmrMargn': 'cncElmrMargn',
        'grossExp': 'grossExp',
        'brokeragePrsnt': 'brokeragePrsnt',
        'collateralVal': 'collateralVal',
        'brnchAdhoc': 'brnchAdhoc',
        'cncUnRealMTM': 'cncUnRealMTM',
        'unbookPNL': 'unbookPNL',
        'scrpBsktMrgn': 'scrpBsktMrgn',
        'notnalCash': 'notnalCash',
        'cncRealMTM': 'cncRealMTM',
        'spanMrgnMIS': 'spanMrgnMIS',
        'realizedPNL': 'realizedPNL',
        'cncCredit': 'cncCredit',
        'adhocMargn': 'adhocMargn',
        'premiumPrsnt': 'premiumPrsnt',
        'remarks': 'remarks',
        'dirctColatrl': 'dirctColatrl'
    }
    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"


@attr.s(auto_attribs=True)
class FundsSuccessData:
    funds: FundsView = None

    swagger_types = {
        "funds": FundsView
    }

    attribute_map = {
        "funds": "funds"
    }
