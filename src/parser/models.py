"""
Domain models for log processing.
"""

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
from enum import Enum



class Severity(str, Enum):

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"



@dataclass(frozen=True)
class LogFile:

    path: Path
    filename: str
    size_bytes: int
    category: str



@dataclass(frozen=True)
class LogEntry:

    timestamp: datetime | None

    severity: Severity

    source: str

    message: str

    file: Path
