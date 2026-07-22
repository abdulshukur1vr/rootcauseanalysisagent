"""
Timeline domain models.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta

from detector.models import DetectedEvent, EventCategory


@dataclass(frozen=True)
class TimelineEvent:

    sequence: int

    timestamp: datetime | None

    event: DetectedEvent


@dataclass
class TimelineGroup:

    category: EventCategory

    count: int

    start_time: datetime | None

    end_time: datetime | None

    duration: timedelta | None

    event_rate: float | None

    largest_gap: timedelta | None

    events: list[DetectedEvent] = field(
        default_factory=list
    )

    sources: list[str] = field(
        default_factory=list
    )

