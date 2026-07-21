"""
Report models.
"""


from dataclasses import dataclass, field

from analyzer.models import RootCauseCandidate

from timeline.models import TimelineEvent

from typing import Dict


@dataclass
class RCAReport:

    title: str

    root_causes: list[RootCauseCandidate]

    timeline: list[TimelineEvent]

    failure_distribution: Dict[str, float] = field(default_factory=dict)
    
    failure_counts: Dict[str, int] = field(default_factory=dict)

    generated_by: str = (
        "RootCauseAnalysisAgent"
    )
