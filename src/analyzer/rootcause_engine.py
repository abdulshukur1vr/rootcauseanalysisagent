"""
Root cause reasoning engine.
"""


from detector.models import DetectedEvent

from analyzer.models import (
    RootCauseCandidate
)

from analyzer.rules import (
    ROOT_CAUSE_PRIORITY
)



class RootCauseEngine:


    def analyze(
        self,
        events: list[DetectedEvent]
    ) -> list[RootCauseCandidate]:


        grouped = {}


        for event in events:


            grouped.setdefault(
                event.category,
                []
            ).append(
                event
            )


        candidates = []


        for category, items in grouped.items():


            confidence = (
                ROOT_CAUSE_PRIORITY.get(
                    category,
                    40
                )
            )


            evidence = [

                item.message

                for item in items[:5]

            ]


            candidates.append(

                RootCauseCandidate(

                    category=category,

                    confidence=confidence,

                    explanation=self._explain(
                        category
                    ),

                    evidence=evidence

                )

            )


        return sorted(

            candidates,

            key=lambda x:
            x.confidence,

            reverse=True

        )



    def _explain(
        self,
        category
    ) -> str:


        explanations = {


            "WIFI_CLIENT_FAILURE":

                "Wireless client failed authentication or association.",


            "ETHERNET_FAILURE":

                "Ethernet physical link or driver failure detected.",


            "DHCP_FAILURE":

                "Network address assignment failed.",


            "KERNEL_FAILURE":

                "Kernel level failure detected.",


            "STORAGE_FAILURE":

                "Storage subsystem failure detected."

        }


        return explanations.get(

            category.value,

            "System failure detected."

        )
