"""
Base parser interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from parser.models import LogEntry



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
