#!/usr/bin/env python3

"""
Root Cause Analysis Agent

CLI entry point for the complete RCA pipeline.
"""

from pathlib import Path
import argparse
import sys

from core.logger import setup_logging
from app.pipeline import RCAPipeline


def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        description="AI-based Root Cause Analysis Agent"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to support bundle (.zip/.tar/.tgz)"
    )

    parser.add_argument(
        "--output",
        default="reports",
        help="Directory where analysis reports will be written"
    )

    return parser


def main() -> int:

    logger = setup_logging()

    args = build_parser().parse_args()

    bundle = Path(args.input)

    if not bundle.exists():
        logger.error(
            "Input bundle does not exist: %s",
            bundle
        )
        return 1

    output = Path(args.output)

    try:

        pipeline = RCAPipeline()

        report = pipeline.execute(
            bundle,
            output
        )

        logger.info(
            "Analysis completed successfully."
        )

        logger.info(
            "Detected %d root cause(s).",
            len(report.root_causes)
        )

        logger.info(
            "Reports written under: %s",
            output
        )

        return 0

    except Exception:

        logger.exception(
            "Root Cause Analysis failed"
        )

        return 1


if __name__ == "__main__":
    sys.exit(main())
