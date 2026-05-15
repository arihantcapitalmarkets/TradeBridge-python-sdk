from typing import List
import attr


@attr.s(auto_attribs=True)
class TaxPnlFoFilter:
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
class TaxPnlFoRequest:
    """Class representing Tax PnL F&O Request."""

    filters: List[TaxPnlFoFilter] = None

    swagger_types = {
        'filters': 'list[TaxPnlFoFilter]',
    }

    attribute_map = {
        'filters': 'filters',
    }