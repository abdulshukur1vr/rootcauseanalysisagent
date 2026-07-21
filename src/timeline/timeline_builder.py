"""
Builds ordered timelines from detected events.
"""


import logging

from detector.models import DetectedEvent

from timeline.models import TimelineEvent



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
