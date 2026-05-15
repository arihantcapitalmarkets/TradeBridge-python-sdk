from typing import List
import attr


@attr.s(auto_attribs=True)
class LedgerFilter:
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
class LedgerRequest:
    """Class representing a Ledger Request."""

    filters: List[LedgerFilter] = None

    swagger_types = {
        'filters': 'list[LedgerFilter]',
    }

    attribute_map = {
        'filters': 'filters',
    }