"""
Failure category statistics.

Calculates percentage contribution of
each failure category.
"""


from collections import Counter


class FailureCategoryAnalyzer:


    def analyze(
        self,
        events
    ):

        counts = Counter()


        for event in events:

            category = (
                event.category.value
            )

            counts[category] += 1



        total = sum(
            counts.values()
        )


        if total == 0:

            return {}, {}



        distribution = {

            category:
            round(
                (count / total) * 100,
                2
            )

            for category, count
            in counts.items()

        }


        return (
            distribution,
            dict(counts)
        )
