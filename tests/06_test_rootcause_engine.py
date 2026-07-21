from analyzer.rootcause_engine import RootCauseEngine

from detector.models import (
    DetectedEvent,
    EventCategory,
    EventSeverity
)



def test_wifi_is_ranked_above_dhcp(tmp_path):


    logfile = tmp_path / "wifi.log"


    events = [

        DetectedEvent(

            category=
            EventCategory.DHCP_FAILURE,

            severity=
            EventSeverity.ERROR,

            confidence=80,

            message=
            "DHCP timeout",

            source=logfile

        ),


        DetectedEvent(

            category=
            EventCategory.WIFI_CLIENT_FAILURE,

            severity=
            EventSeverity.ERROR,

            confidence=90,

            message=
            "wpa handshake failed",

            source=logfile

        )

    ]


    result = RootCauseEngine().analyze(
        events
    )


    assert (

        result[0].category

        ==

        EventCategory.WIFI_CLIENT_FAILURE

    )
