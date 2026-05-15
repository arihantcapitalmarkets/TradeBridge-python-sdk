import attr

from swagger_client.models.brokerage_charge import BrokerageCharge


@attr.s(auto_attribs=True)
class BrokerageChargeData:
    brokerage: BrokerageCharge = None

    swagger_types = {
        'brokerage': 'BrokerageCharge'
    }

    attribute_map = {
        'brokerage': 'brokerage'
    }

