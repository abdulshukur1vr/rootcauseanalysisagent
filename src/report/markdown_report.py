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


        for event in report.timeline:

            lines.append(

                f"""
{event.sequence}. \
{event.event.category.value} \
({event.event.severity.value})

{event.event.message}

"""

            )


        output.write_text(
            "".join(lines)
        )


        return output
