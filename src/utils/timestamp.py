"""
Timestamp helpers.
"""

from datetime import datetime
from pathlib import Path



def current_timestamp() -> str:

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )



def create_timestamp_directory(
    base_directory: Path
) -> Path:

    timestamp_dir = (
        base_directory /
        current_timestamp()
    )


    timestamp_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    return timestamp_dir
