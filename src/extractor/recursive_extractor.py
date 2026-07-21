"""
Recursive TAR extraction engine.

Handles:

support.tar

    nested1.tar

        nested2.tar

            files
"""

from pathlib import Path
import logging

from extractor.archive_utils import (
    extract_tar,
    is_tar_file
)



class RecursiveExtractor:


    def __init__(
        self,
        workspace: Path
    ):

        self.workspace = workspace

        self.logger = logging.getLogger(
            __name__
        )



    def extract_recursive(
        self,
        archive: Path
    ) -> None:


        root_destination = (
            self.workspace /
            archive.stem
        )


        extract_tar(
            archive,
            root_destination
        )


        self.logger.info(
            "Extracted %s",
            archive
        )


        self._extract_nested_archives(
            root_destination
        )



    def _extract_nested_archives(
        self,
        directory: Path
    ) -> None:


        archives = []


        for item in directory.rglob("*"):

            if (
                item.is_file()
                and is_tar_file(item)
            ):

                archives.append(item)



        for archive in archives:


            extract_directory = (
                archive.parent /
                archive.stem
            )


            self.logger.info(
                "Nested archive found: %s",
                archive
            )


            extract_tar(
                archive,
                extract_directory
            )


            self._extract_nested_archives(
                extract_directory
            )
