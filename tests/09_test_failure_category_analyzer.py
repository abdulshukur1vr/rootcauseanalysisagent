from analyzer.failure_category_analyzer import (
    FailureCategoryAnalyzer
)

from dataclasses import dataclass

@dataclass
class FakeCategory:

    value: str


@dataclass
class FakeEvent:

    category: FakeCategory

    def __init__(self, value):

        self.category = FakeCategory(value)


def test_failure_distribution():

    analyzer = FailureCategoryAnalyzer()

    events = [
        FakeEvent("ETHERNET_FAILURE"),
        FakeEvent("ETHERNET_FAILURE"),
        FakeEvent("WIFI_CLIENT_FAILURE")
    ]


    distribution, counts = (
        analyzer.analyze(events)
    )


    assert counts["ETHERNET_FAILURE"] == 2

    assert (
        distribution["ETHERNET_FAILURE"]
        == 66.67
    )
