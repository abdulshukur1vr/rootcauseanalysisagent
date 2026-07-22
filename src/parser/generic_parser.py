"""
Fallback parser.

Handles unknown formats.
"""


from pathlib import Path

from parser.base_parser import(
    BaseParser,
    extract_timestamp
)

from parser.models import (
    LogEntry,
    Severity
)



class GenericParser(BaseParser):


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

                message = line.strip()


                if not message:

                    continue


                entries.append(

                    LogEntry(

                        timestamp=extract_timestamp(line),

                        severity=Severity.UNKNOWN,

                        source=log_file.name,

                        message=message,

                        file=log_file

                    )

                )


        return entries
