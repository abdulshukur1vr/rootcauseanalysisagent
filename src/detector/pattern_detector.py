"""
Pattern detection engine.

Consumes LogEntry objects and produces DetectedEvent objects.
"""


import logging
import re

from parser.models import LogEntry

from detector.models import (
    DetectedEvent,
    EventCategory,
    EventSeverity
)

from detector.signatures import SIGNATURES

from collections import Counter

class PatternDetector:


    def __init__(self):

        self.logger = logging.getLogger(
            __name__
        )


    def detect(
        self,
        entries: list[LogEntry]
    ) -> list[DetectedEvent]:


        events = []


        for entry in entries:


            message = (
                entry.message
                .lower()
            )

            ignore_patterns = [
                "watchdogpet",
                "successfully pet",
                "heartbeat",
            ]

            if any(
                ignore in message
                for ignore in ignore_patterns
            ):
                continue


            for category, patterns in SIGNATURES.items():


                for pattern in patterns:


                    if re.search(pattern, message):


                        events.append(

                            DetectedEvent(

                                category=EventCategory(
                                    category
                                ),

                                severity=self._severity(
                                    category
                                ),

                                confidence=self._confidence(
                                    category
                                ),

                                message=entry.message,

                                source=entry.file,

                                timestamp=entry.timestamp
                            )

                        )


                        break


        distribution = Counter(
            event.category.value
            for event in events
        )

        self.logger.info(
            "Detection distribution: %s",
            dict(distribution)
        )


        self.logger.info(
            "Detected %d events",
            len(events)
        )


        return events



    def _confidence(
        self,
        category: str
    ) -> int:


        critical = [

            "KERNEL_FAILURE",

            "STORAGE_FAILURE",

            "MEMORY_FAILURE"

        ]


        if category in critical:

            return 95


        return 85



    def _severity(
        self,
        category: str
    ) -> EventSeverity:


        critical = [

            "KERNEL_FAILURE",

            "MEMORY_FAILURE"

        ]


        if category in critical:

            return EventSeverity.CRITICAL


        return EventSeverity.ERROR
