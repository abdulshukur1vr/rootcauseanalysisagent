"""
Base parser interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from parser.models import LogEntry

from datetime import datetime
import re


def extract_timestamp(line: str):

    patterns = [

        (
            r"(\d{4} \w{3} \d{2} \d{2}:\d{2}:\d{2})",
            "%Y %b %d %H:%M:%S"
        ),

        (
            r"(\d{6}-\d{2}:\d{2}:\d{2}\.\d+)",
            "%y%m%d-%H:%M:%S.%f"
        )

    ]


    for pattern, fmt in patterns:

        match = re.search(
            pattern,
            line
        )

        if match:

            try:

                return datetime.strptime(
                    match.group(1),
                    fmt
                )

            except ValueError:

                pass


    return None


class BaseParser(ABC):

    """
    Every parser implements this interface.
    """


    @abstractmethod
    def parse(
        self,
        log_file: Path
    ) -> list[LogEntry]:

        pass
