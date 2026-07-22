"""
Main RCA pipeline orchestration.
"""

import logging

from pathlib import Path
from datetime import datetime

from report.run_metadata import (
    write_metadata
)

from extractor.recursive_extractor import (
    RecursiveExtractor
)

from discovery.log_discovery import (
    LogDiscovery
)

from parser.parser_factory import (
    ParserFactory
)

from detector.pattern_detector import (
    PatternDetector
)

from timeline.timeline_builder import (
    TimelineBuilder
)

from analyzer.rootcause_engine import (
    RootCauseEngine
)

from analyzer.failure_category_analyzer import (
    FailureCategoryAnalyzer
)

from report.models import (
    RCAReport
)

from report.markdown_report import (
    MarkdownReportGenerator
)

from report.json_report import (
    JSONReportGenerator
)



class RCAPipeline:


    def __init__(self):

        self.logger = logging.getLogger(
            __name__
        )


    def execute(
        self,
        bundle: Path,
        output: Path
    ):


        self.logger.info(
            "Starting RCA pipeline"
        )


        run_timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )


        output = (
            output /
            run_timestamp
        )


        output.mkdir(
            parents=True,
            exist_ok=True
        )

        write_metadata(
            output,
            bundle
        )

        self.logger.info(
            "Report directory: %s",
            output
        )

        write_metadata(
            output,
            bundle
        )

        #
        # 1. Extract
        #
        workspace = (
            output /
            "workspace"
        )

        workspace.mkdir(
            parents=True,
            exist_ok=True
        )

        extractor = RecursiveExtractor(
            workspace
        )  


        extractor.extract_recursive(
            bundle
        )
  
        #
        # 2. Discover logs
        #

        logs = LogDiscovery().discover(
            workspace
        )


        #
        # 3. Parse
        #

        entries = []


        parser_factory = ParserFactory()


        for logfile in logs:
            parser = parser_factory.get_parser(
                logfile.path
            )

            entries.extend(
                parser.parse(
                    logfile.path
                )
            )


        #
        # 4. Detect
        #

        events = PatternDetector().detect(
            entries
        )


        #
        # 5. Timeline
        #

        timeline = TimelineBuilder().build_grouped(
            events
        )

        #
        # Failure Analyzer
        failure_analyzer = FailureCategoryAnalyzer()


        failure_distribution, failure_counts = (
            failure_analyzer.analyze(
                events
            )
        )


        #
        # 6. RCA
        #

        causes = RootCauseEngine().analyze(
            events
        )


        #
        # 7. Report
        #

        report = RCAReport(

            title=
            "Root Cause Analysis Report",

            root_causes=
            causes,

            timeline=
            timeline,

            failure_distribution=
                failure_distribution,

            failure_counts=
                failure_counts
        )


        MarkdownReportGenerator().generate(

            report,

            output /
            "summary.md"

        )


        JSONReportGenerator().generate(

            report,

            output /
            "report.json"

        )


        return report
