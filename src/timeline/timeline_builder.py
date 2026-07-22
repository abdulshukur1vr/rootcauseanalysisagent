"""
Builds ordered timelines from detected events.
"""

import logging
from collections import defaultdict

from detector.models import DetectedEvent

from timeline.models import (
    TimelineEvent,
    TimelineGroup
)


class TimelineBuilder:


    def __init__(self):

        self.logger = logging.getLogger(
            __name__
        )


    def build(
        self,
        events: list[DetectedEvent]
    ) -> list[TimelineEvent]:


        timeline = []


        for index, event in enumerate(
            events,
            start=1
        ):

            timeline.append(

                TimelineEvent(

                    sequence=index,

                    timestamp=None,

                    event=event

                )

            )


        self.logger.info(
            "Timeline created with %d events",
            len(timeline)
        )


        return timeline



    def build_grouped(
        self,
        events: list[DetectedEvent]
    ) -> list[TimelineGroup]:


        grouped = defaultdict(list)


        for event in events:

            grouped[event.category].append(
                event
            )


        timeline_groups = []


        for category, items in grouped.items():

            timestamps = [

                e.timestamp

                for e in items

                if e.timestamp is not None

            ]


            if timestamps:

                start_time = min(
                    timestamps
                )

                end_time = max(
                    timestamps
                )

                duration = end_time - start_time

                event_rate = (
                        len(items) / max(duration.total_seconds(), 1)
                )

                largest_gap = max(
                    (
                        b - a
                        for a, b in zip(
                            timestamps,
                            timestamps[1:]
                        )
                    ),
                    default=None
                )

            else:

                start_time = None

                end_time = None

                duration = None
               
                event_rate = None
 
                largest_gap = None


            sources = sorted(
                set(
                    str(e.source)
                    for e in items
                )
            )


            timeline_groups.append(

                TimelineGroup(

                    category=category,

                    count=len(items),

                    start_time=start_time,

                    end_time=end_time,

                    duration=duration,

                    event_rate=event_rate,

                    largest_gap=largest_gap,
                    
                    events=items,

                    sources=sources

                )

            )


        return sorted(

            timeline_groups,

            key=lambda x:
            x.count,

            reverse=True

        )
