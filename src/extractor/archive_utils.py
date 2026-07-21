"""
Archive handling utilities.

Supports:

- tar
- tar.gz
- tgz
- tar.bz2
- tar.xz
- zip
"""

from pathlib import Path
import tarfile
import zipfile
import logging


class ArchiveError(Exception):
    pass



logger = logging.getLogger(__name__)



def is_archive(path: Path) -> bool:
    """
    Detect supported archive formats.
    """

    if not path.is_file():
        return False


    try:

        if tarfile.is_tarfile(path):
            return True


        if zipfile.is_zipfile(path):
            return True


    except Exception:

        return False


    return False



def is_tar_file(path: Path) -> bool:
    """
    Backward compatibility for recursive extractor.
    """

    return is_archive(path)



def extract_tar(
    archive: Path,
    destination: Path
) -> None:
    """
    Extract tar or zip archives.
    """

    destination.mkdir(
        parents=True,
        exist_ok=True
    )


    try:

        if tarfile.is_tarfile(archive):

            with tarfile.open(
                archive,
                "r:*"
            ) as tar:

                tar.extractall(
                    destination
                )


            logger.info(
                "Extracted TAR %s",
                archive
            )

            return



        if zipfile.is_zipfile(archive):

            with zipfile.ZipFile(
                archive,
                "r"
            ) as zipf:

                zipf.extractall(
                    destination
                )


            logger.info(
                "Extracted ZIP %s",
                archive
            )

            return



    except Exception as exc:

        raise ArchiveError(
            f"Failed extracting {archive}: {exc}"
        )


    raise ArchiveError(
        f"Unsupported archive format: {archive}"
    )
