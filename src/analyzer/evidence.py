"""
Convert raw detected events into RCA evidence.
"""

from analyzer.evidence_weights import EVIDENCE_RULES


class EvidenceAnalyzer:


    def analyze(
        self,
        events
    ):

        findings = []


        for event in events:

            message = str(
                event.message
            )


            for rule in EVIDENCE_RULES:

                matched = all(
                    pattern.lower()
                    in message.lower()
                    for pattern in rule["patterns"]
                )


                if matched:

                    findings.append(
                        {
                            "category":
                                rule["category"],

                            "confidence":
                                rule["confidence"],

                            "message":
                                message,

                            "component":
                                rule["component"],
                        }
                    )


        return findings
