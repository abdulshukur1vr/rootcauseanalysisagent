"""
Filesystem utilities.
"""

from pathlib import Path



def ensure_directory(
    directory: Path
) -> Path:

    directory.mkdir(
        parents=True,
        exist_ok=True
    )

    return directory



def find_files(
    root: Path,
    pattern: str
) -> list[Path]:

    return list(
        root.rglob(pattern)
    )



def is_archive(
    file: Path
) -> bool:

    name = file.name.lower()

    return (
        name.endswith(".tar")
        or name.endswith(".tar.gz")
        or name.endswith(".tgz")
    )
