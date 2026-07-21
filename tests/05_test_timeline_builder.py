from pathlib import Path
import pytest

from timeline.timeline_builder import (
    TimelineBuilder
)

from detector.models import (
    DetectedEvent,
    EventCategory,
    EventSeverity
)


@pytest.mark.order(7)
def test_timeline_ordering(tmp_path):


    logfile = (
        tmp_path /
        "kernel.log"
    )


    events = [

        DetectedEvent(

            category=
            EventCategory.ETHERNET_FAILURE,

            severity=
            EventSeverity.ERROR,

            confidence=85,

            message=
            "eth0 link down",

            source=logfile

        ),


        DetectedEvent(

            category=
            EventCategory.WIFI_CLIENT_FAILURE,

            severity=
            EventSeverity.ERROR,

            confidence=85,

            message=
            "wpa handshake timeout",

            source=logfile

        )

    ]



    timeline = TimelineBuilder().build(
        events
    )


    assert len(timeline) == 2


    assert (
        timeline[0].sequence
        ==
        1
    )


    assert (
        timeline[1].sequence
        ==
        2
    )


    assert (
        timeline[0].event.category
        ==
        EventCategory.ETHERNET_FAILURE
    )
