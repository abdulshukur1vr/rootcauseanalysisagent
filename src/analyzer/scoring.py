"""
RDK-B Root Cause Scoring Engine.

Combines:
    - Event priority
    - Evidence confidence
    - Correlation confidence
    - Frequency
    - Multi-source agreement
"""

from collections import defaultdict

from analyzer.rules import ROOT_CAUSE_PRIORITY
from analyzer.correlation import CORRELATION_RULES, CORRELATION_CHAINS


class RootCauseScorer:


    def __init__(self):

        self.scores = defaultdict(float)

        self.evidence = defaultdict(list)



    def add_evidence(
        self,
        category,
        confidence,
        message=None,
        component=None
    ):
        """
        Add direct log evidence.
        """

        self.scores[category] += confidence

        if message:

            self.evidence[category].append(
                {
                    "message": message,
                    "component": component,
                    "confidence": confidence,
                }
            )



    def add_symptom(
        self,
        symptom,
        count=1
    ):
        """
        Convert symptoms into root cause candidates.
        """

        rule = CORRELATION_RULES.get(symptom)


        if not rule:
            return


        for cause, confidence in rule["causes"]:

            priority = ROOT_CAUSE_PRIORITY.get(
                cause,
                50
            )


            score = (
                confidence
                *
                priority
                *
                count
            )


            self.scores[cause] += score



    def apply_frequency_bonus(
        self,
        category,
        occurrences
    ):
        """
        Frequent repeated failures
        increase confidence.
        """

        bonus = min(
            occurrences * 2,
            50
        )


        self.scores[category] += bonus



    def apply_chain_rules(
        self,
        observed_events
    ):
        """
        Apply multi-event correlations.
        """

        observed = set(observed_events)


        for chain in CORRELATION_CHAINS:

            required = set(
                chain["events"]
            )


            if required.issubset(observed):

                self.scores[
                    chain["root_cause"]
                ] += (
                    chain["confidence_boost"]
                    *
                    100
                )



    def rank(
        self,
        limit=10
    ):
        """
        Return ranked root causes.
        """

        results = []


        for category, score in self.scores.items():

            results.append(
                {
                    "category": category,
                    "score": round(
                        score,
                        2
                    ),
                    "evidence": self.evidence.get(
                        category,
                        []
                    ),
                }
            )


        return sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )[:limit]

