"""
RDK-B Root Cause Analyzer.
"""


from analyzer.evidence import EvidenceAnalyzer
from analyzer.scoring import RootCauseScorer

def deduplicate_events(events):

    seen = set()

    unique_events = []

    for event in events:

        key = (
            event.category,
            event.timestamp,
            event.message.strip()
        )

        if key not in seen:

            seen.add(key)

            unique_events.append(event)

    return unique_events


class RCAAnalyzer:


    def __init__(self):

        self.evidence =
            EvidenceAnalyzer()



    def analyze(
        self,
        events
    ):

#
        # Step 0:
        # Remove duplicate archive copies
        #
        unique_events = deduplicate_events(
            events
        )

        scorer = RootCauseScorer()


        #
        # Step 1:
        # Extract evidence from logs
        #
        findings = self.evidence.analyze(
            unique_events
        )


        #
        # Step 2:
        # Add direct evidence
        #
        for finding in findings:

            scorer.add_evidence(

                category=finding["category"],

                confidence=finding["confidence"],

                message=finding["message"],

                component=finding["component"]

            )



        #
        # Step 3:
        # Convert symptoms -> causes
        #
        categories = []


        for event in unique_events:

            categories.append(
                event.category
            )

            scorer.add_symptom(
                event.category
            )



        #
        # Step 4:
        # Apply multi-event rules
        #
        scorer.apply_chain_rules(
            categories
        )


        #
        # Step 5:
        # Rank RCA
        #
        return scorer.rank()
