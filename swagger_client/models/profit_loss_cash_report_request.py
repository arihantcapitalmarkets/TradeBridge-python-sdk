from typing import List
import attr


@attr.s(auto_attribs=True)
class ReportFilters:
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
class ProfitLossCashReportRequest:
    """Class representing a Profit Loss Cash Report Request."""

    filters: List[ReportFilters] = None

    swagger_types = {
        'filters': 'list[ReportFilters]',
    }

    attribute_map = {
        'filters': 'filters',
    }
