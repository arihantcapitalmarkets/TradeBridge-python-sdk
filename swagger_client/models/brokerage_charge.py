import attr


@attr.s(auto_attribs=True, repr=False)
class BrokerageCharge:
    externalCharges: str = None
    ipft: str = None
    gst: str = None
    taxes: str = None
    stt : str = None
    stampDuty: str = None
    sebiFee: str =  None
    price: str = None
    qty: str = None
    tot: str = None
    brokeragePrice: str = None
    totalCharges: str = None
    ipf: str = None

    swagger_types = {
        'externalCharges': 'str',
        'ipft': 'str',
        'gst': 'str',
        'taxes': 'str',
        'stt': 'str',
        'stampDuty': 'str',
        'sebiFee': 'str',
        'price': 'str',
        'qty': 'str',
        'tot': 'str',
        'brokeragePrice': 'str',
        'totalCharges': 'str',
        'ipf': 'str'
    }

    attribute_map = {
        'externalCharges': 'externalCharges',
        'ipft': 'ipft',
        'gst': 'gst',
        'taxes': 'taxes',
        'stt': 'stt',
        'stampDuty': 'stampDuty',
        'sebiFee': 'sebiFee',
        'price': 'price',
        'qty': 'qty',
        'tot': 'tot',
        'brokeragePrice': 'brokeragePrice',
        'totalCharges': 'totalCharges',
        'ipf': 'ipf'
    }

    def to_dict(self):
        """Return the dictionary representation, omitting None fields."""
        return {key: value for key, value in attr.asdict(self).items() if value is not None}

    def __repr__(self):
        """Custom string representation, omitting None fields."""
        fields = ', '.join(f'{key}={value!r}' for key, value in attr.asdict(self).items() if value is not None)
        return f"{self.__class__.__name__}({fields})"
