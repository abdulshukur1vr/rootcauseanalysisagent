"""
RCA domain models.
"""

from dataclasses import( 
    dataclass,
    field
)

from detector.models import EventCategory



@dataclass(frozen=True)
class RootCauseCandidate:

    category: EventCategory

    confidence: int

    explanation: str

    evidence: list[str]

    affected_components: list[str] = field(
        default_factory=list
    )

    recommendations: list[str] = field(
        default_factory=list
    )
