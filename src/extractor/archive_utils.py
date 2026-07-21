"""
Archive helper functions.
"""

import tarfile
from pathlib import Path



class ArchiveError(Exception):
    pass



def is_tar_file(
    file_path: Path
) -> bool:

    try:

        return tarfile.is_tarfile(
            file_path
        )

    except Exception:

        return False



def extract_tar(
    archive: Path,
    destination: Path
) -> None:

    if not is_tar_file(archive):

        raise ArchiveError(
            f"Not a valid tar archive: {archive}"
        )


    destination.mkdir(
        parents=True,
        exist_ok=True
    )


    try:

        with tarfile.open(
            archive,
            "r:*"
        ) as tar:

            tar.extractall(
                destination
            )


    except Exception as exc:

        raise ArchiveError(
            f"Failed extracting {archive}: {exc}"
        ) from exc
