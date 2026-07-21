"""
RCA domain models.
"""

from dataclasses import dataclass

from detector.models import EventCategory



@dataclass(frozen=True)
class RootCauseCandidate:

    category: EventCategory

    confidence: int

    explanation: str

    evidence: list[str]
