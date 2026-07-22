"""
Root cause reasoning engine.
"""


from detector.models import (
    DetectedEvent,
    EventSeverity
)

from analyzer.models import (
    RootCauseCandidate
)

from analyzer.rules import (
    ROOT_CAUSE_PRIORITY
)



class RootCauseEngine:


    def deduplicate_events(events):

        seen = set()

        unique = []

        for event in events:

            key = (
                event.category,
                event.timestamp,
                event.message
            )

            if key not in seen:

                seen.add(key)

                unique.append(event)

        return unique

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


            confidence = self._calculate_confidence(
                items
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

                    evidence=evidence,

                    affected_components=[],

                    recommendations=[] 

                )

            )


        return sorted(

            candidates,

            key=lambda x:
            x.confidence,

            reverse=True

        )


    def _calculate_confidence(
        self,
        items: list[DetectedEvent]
    ) -> int:

        score = 50

        sources = set(
            str(e.source)
            for e in items
        )

        score += min(
            len(sources) * 2,
            10
        )

        unique_messages = set(
            e.message
            for e in items
        )

        score += min(
            len(unique_messages) * 3,
            25
        )

        interfaces = set()

        for e in items:
            for iface in [
                "wl0",
                "wl1",
                "wl2"
            ]:
                if iface in e.message:
                    interfaces.add(iface)

        score += min(
            len(interfaces) * 3,
            10
        )

        critical = sum(
            1
            for e in items
            if e.severity == EventSeverity.CRITICAL
        )

        score += critical * 10

        detector_confidence = max(
            e.confidence
            for e in items
        )

        score += detector_confidence // 10

        return min(
            score,
            100
        )



    def _calculate_confidence1(
        self, 
        items: list[DetectedEvent]
    ) -> int:

        score = 50

        sources = set(
            str(e.source)
            for e in items
        )

        score += min(
            len(sources) * 2,
            10
        )

        unique_messages = set(
            e.message
            for e in items
        ) 

        score += min(
            len(unique_messages) * 3,
            25
        )

        critical = sum(
            1
            for e in items
            if e.severity == EventSeverity.CRITICAL
        )

        score += critical * 10

        detector_confidence = max(
            e.confidence
            for e in items
        )

        score += detector_confidence // 10

        return min(score, 100)



    def _explain(
        self,
        category
    ) -> str:

        explanations = {

            "WIFI_CLIENT_FAILURE":

                "Wireless clients failed authentication or association. "
                "This indicates a problem during the connection establishment "
                "process and may be related to authentication configuration, "
                "security negotiation, client compatibility, or wireless driver behavior.",


            "WIFI_DISCONNECT":

                "Multiple wireless clients experienced unexpected disassociation "
                "events across one or more WiFi interfaces. The pattern suggests "
                "wireless connectivity instability and may be related to WiFi "
                "driver issues, RF interference, client roaming behavior, or "
                "firmware defects.",


            "ETHERNET_FAILURE":

                "Ethernet physical link or network driver failure detected.",


            "DHCP_FAILURE":

                "DHCP address assignment failed. This may indicate a network "
                "availability issue, DHCP server problem, or connectivity failure.",


            "DNS_FAILURE":

                "DNS resolution failures detected. This may indicate resolver "
                "availability issues or network connectivity problems.",


            "NETWORK_STACK_FAILURE":

                "Network stack errors detected. This may indicate socket, "
                "routing, or transport layer instability.",


            "KERNEL_FAILURE":

                "Kernel-level failure detected. This may indicate operating "
                "system instability, driver issues, or hardware-related problems.",


            "STORAGE_FAILURE":

                "Storage subsystem failure detected. This may indicate disk "
                "errors, filesystem corruption, or I/O problems.",


            "MEMORY_FAILURE":

                "Memory subsystem failure detected. This may indicate memory "
                "pressure, allocation failures, or resource exhaustion."
        }

        return explanations.get(

            category.value,

            "System failure detected."

        )
