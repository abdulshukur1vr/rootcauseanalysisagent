"""
Basic Linux syslog parser.

Example:

Jul 21 10:10:20 host kernel: error message
"""


from pathlib import Path
from datetime import datetime
import re


from parser.base_parser import BaseParser
from parser.models import (
    LogEntry,
    Severity
)



SYSLOG_PATTERN = re.compile(

    r"^(?P<time>\w+\s+\d+\s+\d+:\d+:\d+)"
    r"\s+(?P<host>\S+)"
    r"\s+(?P<source>[^:]+):"
    r"\s*(?P<message>.*)"

)



class SyslogParser(BaseParser):


    def parse(
        self,
        log_file: Path
    ) -> list[LogEntry]:


        entries = []


        with log_file.open(
            "r",
            errors="replace"
        ) as file:


            for line in file:


                line=line.strip()


                if not line:

                    continue


                match = SYSLOG_PATTERN.match(
                    line
                )


                if match:


                    message = (
                        match.group("message")
                    )


                    severity = (
                        self._detect_severity(
                            message
                        )
                    )


                    entries.append(

                        LogEntry(

                            timestamp=None,

                            severity=severity,

                            source=match.group(
                                "source"
                            ),

                            message=message,

                            file=log_file

                        )

                    )


                else:

                    entries.append(

                        LogEntry(

                            timestamp=None,

                            severity=Severity.UNKNOWN,

                            source=log_file.name,

                            message=line,

                            file=log_file

                        )

                    )


        return entries



    def _detect_severity(
        self,
        message: str
    ) -> Severity:


        text = message.lower()


        if any(
            x in text
            for x in [
                "panic",
                "fatal",
                "critical"
            ]
        ):

            return Severity.CRITICAL



        if any(
            x in text
            for x in [
                "error",
                "failed",
                "failure"
            ]
        ):

            return Severity.ERROR



        if "warn" in text:

            return Severity.WARNING



        return Severity.INFO
