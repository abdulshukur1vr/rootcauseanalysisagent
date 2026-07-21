"""
Parser selection logic.
"""

from pathlib import Path


from parser.base_parser import BaseParser
from parser.syslog_parser import SyslogParser
from parser.generic_parser import GenericParser



class ParserFactory:


    def get_parser(
        self,
        log_file: Path
    ) -> BaseParser:


        name = log_file.name.lower()


        if (
            "syslog" in name
            or
            "messages" in name
            or
            "kernel" in name
        ):

            return SyslogParser()


        return GenericParser()
