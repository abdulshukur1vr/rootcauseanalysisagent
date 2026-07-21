"""
JSON RCA report generator.
"""

import json

from pathlib import Path

from report.models import RCAReport



class JSONReportGenerator:


    def generate(
        self,
        report: RCAReport,
        output: Path
    ) -> Path:


        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        data = {


            "title":
                report.title,


            "root_causes":
            [

                {
                    "category":
                    cause.category.value,

                    "confidence":
                    cause.confidence,

                    "explanation":
                    cause.explanation,

                    "evidence":
                    cause.evidence
                }

                for cause in report.root_causes

            ],


            "timeline":
            [

                {
                    "sequence":
                    event.sequence,

                    "category":
                    event.event.category.value,

                    "severity":
                    event.event.severity.value,

                    "message":
                    event.event.message
                }

                for event in report.timeline

            ]

        }


        output.write_text(

            json.dumps(
                data,
                indent=4
            )

        )


        return output
