"""
Timeline domain models.
"""

from dataclasses import dataclass
from datetime import datetime

from detector.models import DetectedEvent



@dataclass(frozen=True)
class TimelineEvent:

    sequence: int

    timestamp: datetime | None

    event: DetectedEvent
