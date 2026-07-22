"""
Markdown RCA report generator.
"""


from pathlib import Path

from report.models import RCAReport



class MarkdownReportGenerator:


    def generate(
        self,
        report: RCAReport,
        output: Path
    ) -> Path:


        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        lines = []


        lines.append(
            f"# {report.title}\n"
        )


        lines.append(
            "## Root Cause Candidates\n"
        )


        for cause in report.root_causes:


            lines.append(
                f"""
### {cause.category.value}

Confidence: {cause.confidence}%

{cause.explanation}


Evidence:

"""
            )


            for evidence in cause.evidence:

                lines.append(
                    f"- {evidence}\n"
                )



        lines.append(
            "\n## Timeline\n"
        )


        for group in report.timeline:


            lines.append(

                f"""
### {group.category.value}

Occurrences: {group.count}

Start Time: 
{group.start_time}

End Time: 
{group.end_time}

Sources:

"""
            )


            for source in group.sources:

                lines.append(
                    f"- {source}\n"
                )


            lines.append(
                "\nEvents:\n\n"
            )


            for event in group.events:


                timestamp = ""

                if event.timestamp:

                    timestamp = (
                        str(event.timestamp)
                        + " "
                    )


                lines.append(

                    f"- {timestamp}"
                    f"{event.message}\n"

                )


            lines.append(
                "\n"
            )


        output.write_text(
            "".join(lines)
        )


        return output
