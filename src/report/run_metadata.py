import json

from datetime import datetime
from pathlib import Path


def write_metadata(
    output: Path,
    bundle: Path
):

    metadata = {

        "run_time":
            datetime.now().isoformat(),

        "input_bundle":
            str(bundle),

        "agent":
            "RootCauseAnalysisAgent",

        "version":
            "0.1.0"

    }


    (
        output /
        "metadata.json"
    ).write_text(

        json.dumps(
            metadata,
            indent=4
        )

    )
