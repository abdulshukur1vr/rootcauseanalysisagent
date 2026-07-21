from pathlib import Path

from detector.pattern_detector import PatternDetector

import pytest

from parser.models import (
    LogEntry,
    Severity
)

from detector.models import (
    EventCategory
)

@pytest.mark.order(5)
def test_ethernet_detection(tmp_path):


    logfile = (
        tmp_path /
        "kernel.log"
    )


    logfile.write_text(
        "eth0: link down"
    )


    entry = LogEntry(

        timestamp=None,

        severity=Severity.ERROR,

        source="kernel",

        message="eth0: link down",

        file=logfile
    )


    detector = PatternDetector()


    events = detector.detect(
        [entry]
    )


    assert len(events) == 1


    assert (
        events[0].category
        ==
        EventCategory.ETHERNET_FAILURE
    )


@pytest.mark.order(6)
def test_wifi_detection(tmp_path):


    logfile = (
        tmp_path /
        "wifi.log"
    )


    entry = LogEntry(

        timestamp=None,

        severity=Severity.ERROR,

        source="wifi",

        message="wpa handshake timeout",

        file=logfile
    )


    detector = PatternDetector()


    events = detector.detect(
        [entry]
    )


    assert (
        events[0].category
        ==
        EventCategory.WIFI_CLIENT_FAILURE
    )
