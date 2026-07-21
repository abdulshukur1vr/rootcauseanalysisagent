import tarfile
from pathlib import Path


from app.pipeline import RCAPipeline
from report.run_metadata import write_metadata


def create_sample_bundle(tmp_path: Path) -> Path:

    source = tmp_path / "bundle"

    log_dir = (
        source /
        "nvram2" /
        "log"
    )

    log_dir.mkdir(
        parents=True
    )


    #
    # Ethernet failure
    #

    (
        log_dir /
        "kernel.log"
    ).write_text(
        """
        Jan 01 10:00:01 eth0: link down
        Jan 01 10:00:02 NETDEV WATCHDOG timeout
        """
    )


    #
    # Wifi failure
    #

    (
        log_dir /
        "wifi.log"
    ).write_text(
        """
        Jan 01 10:01:01 wlan0 authentication failed
        Jan 01 10:01:05 wpa handshake timeout
        """
    )


    archive = (
        tmp_path /
        "sample_bundle.tar"
    )


    with tarfile.open(
        archive,
        "w"
    ) as tar:

        tar.add(
            source,
            arcname="sample"
        )


    return archive



def test_full_rca_pipeline(tmp_path):


    bundle = create_sample_bundle(
        tmp_path
    )


    output = (
        tmp_path /
        "reports"
    )


    pipeline = RCAPipeline()


    report = pipeline.execute(

        bundle,

        output

    )


    #
    # RCA validation
    #

    assert report is not None


    assert len(
        report.root_causes
    ) > 0


    #
    # Report validation
    #

    run_dirs = [
        p for p in output.iterdir()
        if p.is_dir()
    ]

    assert len(run_dirs) == 1

    run_dir = run_dirs[0]

    assert (
        run_dir /
        "summary.md"
    ).exists()


    assert (
        run_dir / "report.json"
    ).exists()


    markdown = (
        run_dir /
        "summary.md"
    ).read_text()


    assert (
        "Root Cause"
        in markdown
    )
