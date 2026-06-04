from typing import List
import attr


@attr.s(auto_attribs=True)
class TaxPnlEquityFilter:
    key: str = None
    value: str = None

    swagger_types = {
        'key': 'str',
        'value': 'str',
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
    }


@attr.s(auto_attribs=True)
class TaxPnlEquityRequest:
    """Class representing Tax PnL Equity Request."""

    filters: List[TaxPnlEquityFilter] = None

    swagger_types = {
        'filters': 'list[TaxPnlEquityFilter]',
    }

    attribute_map = {
        'filters': 'filters',
    }