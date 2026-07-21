from pathlib import Path


from report.models import RCAReport

from report.markdown_report import (
    MarkdownReportGenerator
)

from analyzer.models import (
    RootCauseCandidate
)

from detector.models import (
    EventCategory
)



def test_markdown_report(tmp_path):


    report = RCAReport(

        title="Test RCA",

        root_causes=[

            RootCauseCandidate(

                category=
                EventCategory.WIFI_CLIENT_FAILURE,

                confidence=90,

                explanation=
                "Wifi authentication failure",

                evidence=[
                    "Handshake failed"
                ]

            )

        ],

        timeline=[],

        failure_distribution={
            "WIFI_CLIENT_FAILURE": 100.0
        },

        failure_counts={
            "WIFI_CLIENT_FAILURE": 1
        }

    )


    output = (
        tmp_path /
        "summary.md"
    )


    MarkdownReportGenerator().generate(

        report,

        output

    )


    assert output.exists()


    content = (
        output.read_text()
    )


    assert (
        "WIFI_CLIENT_FAILURE"
        in content
    )
