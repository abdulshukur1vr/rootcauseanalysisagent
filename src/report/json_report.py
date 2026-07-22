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

            
            "failure_distribution":
                report.failure_distribution,

            
            "failure_counts":
                report.failure_counts,


            "timeline":
            [

                {

                    "category":
                    group.category.value,


                    "count":
                    group.count,


                    "start_time":
                    str(group.start_time)
                    if group.start_time
                    else None,


                    "end_time":
                    str(group.end_time)
                    if group.end_time
                    else None,

                    
                    "duration_seconds": (
                        group.duration.total_seconds()
                        if group.duration
                        else None
                    ),


                    "largest_gap_seconds": (
                        group.largest_gap.total_seconds()
                        if group.largest_gap
                        else None
                    ),


                    "event_rate_per_hour": (
                        round(group.event_rate * 3600, 2)
                        if group.event_rate is not None
                        else None
                    ),


                    "sources":
                    group.sources,


                    "events":
                    [

                        {
                            "timestamp":
                            str(event.timestamp)
                            if event.timestamp
                            else None,

                            "severity":
                            event.severity.value,

                            "message":
                            event.message,

                            "source":
                            str(event.source)

                        }

                        for event in group.events

                    ]

                }

                for group in report.timeline

            ]

        }


        output.write_text(

            json.dumps(
                data,
                indent=4
            )

        )


        return output
