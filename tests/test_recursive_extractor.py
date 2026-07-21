"""
Tests for recursive TAR extraction.
"""


from pathlib import Path
import tarfile


from extractor.recursive_extractor import (
    RecursiveExtractor
)



def create_tar(
    archive_path: Path,
    files: dict[str, str]
):

    temp = archive_path.parent / "temp"

    temp.mkdir()


    for filename, content in files.items():

        file_path = temp / filename

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            content
        )


    with tarfile.open(
        archive_path,
        "w"
    ) as tar:

        tar.add(
            temp,
            arcname="."
        )



def test_recursive_extraction(
    tmp_path
):

    input_tar = (
        tmp_path /
        "bundle.tar"
    )


    create_tar(
        input_tar,
        {
            "nvram2/log/test.log":
                "system boot successful"
        }
    )


    workspace = (
        tmp_path /
        "workspace"
    )


    workspace.mkdir()


    extractor = RecursiveExtractor(
        workspace
    )


    extractor.extract_recursive(
        input_tar
    )


    extracted_logs = list(
        workspace.rglob(
            "test.log"
        )
    )


    assert len(
        extracted_logs
    ) == 1
