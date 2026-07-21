"""
Tests for log discovery.
"""

import pytest

from pathlib import Path


from discovery.log_discovery import (
    LogDiscovery
)


@pytest.mark.order(2)
def test_log_discovery(tmp_path):


    log_directory = (
        tmp_path /
        "device1" /
        "nvram2" /
        "log"
    )


    log_directory.mkdir(
        parents=True
    )


    log_file = (
        log_directory /
        "kernel.log"
    )


    log_file.write_text(
        "kernel started"
    )


    discovery = LogDiscovery()


    result = discovery.discover(
        tmp_path
    )


    assert len(result) == 1


    discovered = result[0]


    assert (
        discovered.filename
        ==
        "kernel.log"
    )


    assert (
        discovered.category
        ==
        "kernel"
    )
