"""
Creates a sample nested TAR bundle
for local testing.
"""


from pathlib import Path
import tarfile


ROOT = Path("input")


def create():

    ROOT.mkdir(
        exist_ok=True
    )


    inner_dir = (
        ROOT /
        "inner"
    )

    inner_dir.mkdir(
        exist_ok=True
    )


    log_file = (
        inner_dir /
        "sample.log"
    )


    log_file.write_text(
        """
2026-07-21 10:10:10 INFO System started

2026-07-21 10:11:20 ERROR Disk timeout

"""
    )


    inner_tar = (
        ROOT /
        "inner.tar"
    )


    with tarfile.open(
        inner_tar,
        "w"
    ) as tar:

        tar.add(
            inner_dir,
            arcname="inner"
        )


    outer_tar = (
        ROOT /
        "support_bundle.tar"
    )


    with tarfile.open(
        outer_tar,
        "w"
    ) as tar:

        tar.add(
            inner_tar,
            arcname="inner.tar"
        )


    print(
        f"Created {outer_tar}"
    )


if __name__ == "__main__":

    create()
