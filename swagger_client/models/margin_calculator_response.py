import attr


@attr.s(auto_attribs=True)
class MarginCalculatorData:
    spanReq: str = None
    sprdBenefit: str = None
    totalReq: str = None
    expMarginPrst: str = None

    swagger_types = {
        'spanReq': 'str',
        'sprdBenefit': 'str',
        'totalReq': 'str',
        'expMarginPrst': 'str'
    }

    attribute_map = {
        'spanReq': 'spanReq',
        'sprdBenefit': 'sprdBenefit',
        'totalReq': 'totalReq',
        'expMarginPrst': 'expMarginPrst'
    }


@attr.s(auto_attribs=True)
class MarginCalculatorResponse:
    infoID: str = None
    infoMsg: str = None
    data: MarginCalculatorData = None
    timestamp: int = None

    swagger_types = {
        'infoID': 'str',
        'infoMsg': 'str',
        'data': 'MarginCalculatorData',
        'timestamp': 'int'
    }

    attribute_map = {
        'infoID': 'infoID',
        'infoMsg': 'infoMsg',
        'data': 'data',
        'timestamp': 'timestamp'
    }
