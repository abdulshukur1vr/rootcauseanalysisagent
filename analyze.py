#!/usr/bin/env python3

"""
Root Cause Analysis Agent

Phase 1:
    - CLI entry point
    - Recursive archive extraction workflow
"""


from pathlib import Path
import argparse
import sys


from core.logger import setup_logging
from extractor.recursive_extractor import RecursiveExtractor
from utils.timestamp import create_timestamp_directory
from discovery.log_discovery import LogDiscovery


def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        description="AI based Root Cause Analysis Agent"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to support bundle tar file"
    )

    parser.add_argument(
        "--output",
        default="workspace",
        help="Workspace output directory"
    )

    return parser



def main() -> int:

    logger = setup_logging()

    args = build_parser().parse_args()


    archive = Path(args.input)


    if not archive.exists():

        logger.error(
            "Input archive does not exist: %s",
            archive
        )

        return 1


    workspace = create_timestamp_directory(
        Path(args.output)
    )


    logger.info(
        "Workspace created: %s",
        workspace
    )


    extractor = RecursiveExtractor(
        workspace
    )


    try:

        extractor.extract_recursive(
            archive
        )

        discovery = LogDiscovery()

        logs = discovery.discover(
            workspace
        )


        logger.info(
            "Found %d log files",
            len(logs)
        )  


        for log_file in logs:

            logger.info(
                "%s | %s bytes | %s",
                log_file.filename,
                log_file.size_bytes,
                log_file.category
            )

    except Exception:

        logger.exception(
            "Extraction failed"
        )

        return 1


    logger.info(
        "Extraction completed successfully"
    )


    return 0



if __name__ == "__main__":

    sys.exit(main())
