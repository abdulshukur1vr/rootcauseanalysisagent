from parser.parser_factory import ParserFactory
from parser.models import Severity
import pytest

@pytest.mark.order(3)
def test_syslog_parser(tmp_path):


    logfile = (
        tmp_path /
        "kernel.log"
    )


    logfile.write_text(
        """
Jul 21 10:10:20 host kernel: EXT4 error detected

Jul 21 10:10:21 host kernel: rebooting

"""
    )


    parser = ParserFactory().get_parser(
        logfile
    )


    entries = parser.parse(
        logfile
    )


    assert len(entries) == 2


    assert (
        entries[0].severity
        ==
        Severity.ERROR
    )

@pytest.mark.order(4)
def test_generic_parser(tmp_path):


    logfile = (
        tmp_path /
        "application.log"
    )


    logfile.write_text(
        "application started"
    )


    parser = ParserFactory().get_parser(
        logfile
    )


    entries = parser.parse(
        logfile
    )


    assert len(entries) == 1

    assert (
        entries[0].message
        ==
        "application started"
    )
