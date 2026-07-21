"""
Log discovery engine.

Responsibilities:

- Scan extracted support bundles
- Locate log directories
- Identify candidate log files
- Return metadata only

No parsing happens here.
"""


from pathlib import Path
import logging

from parser.models import LogFile



class LogDiscoveryError(Exception):
    pass



class LogDiscovery:

    """
    Finds log files inside extracted bundles.
    """

    DEFAULT_LOG_PATTERNS = [
        "nvram2/log",
        "log",
        "logs",
        "var/log",
    ]


    def __init__(
        self,
        patterns: list[str] | None = None
    ):

        self.patterns = (
            patterns
            if patterns
            else self.DEFAULT_LOG_PATTERNS
        )

        self.logger = logging.getLogger(
            __name__
        )


    def discover(
        self,
        root: Path
    ) -> list[LogFile]:

        if not root.exists():

            raise LogDiscoveryError(
                f"Path does not exist: {root}"
            )


        discovered: list[LogFile] = []


        for directory in self._find_log_directories(root):

            self.logger.info(
                "Scanning log directory: %s",
                directory
            )


            for file in directory.rglob("*"):

                if not file.is_file():

                    continue


                discovered.append(
                    self._create_log_file(
                        file
                    )
                )


        self.logger.info(
            "Discovered %d log files",
            len(discovered)
        )


        return discovered



    def _find_log_directories(
        self,
        root: Path
    ) -> list[Path]:

        results = []


        for path in root.rglob("*"):

            if not path.is_dir():

                continue


            normalized = str(path).replace(
                "\\",
                "/"
            )


            for pattern in self.patterns:

                if normalized.endswith(pattern):

                    results.append(path)

                    break


        return results



    def _create_log_file(
        self,
        path: Path
    ) -> LogFile:


        return LogFile(

            path=path,

            filename=path.name,

            size_bytes=path.stat().st_size,

            category=self._classify(
                path
            )

        )



    def _classify(
        self,
        path: Path
    ) -> str:

        name = path.name.lower()


        if "kernel" in name:

            return "kernel"


        if "message" in name:

            return "system"


        if "panic" in name:

            return "panic"


        if "crash" in name:

            return "crash"


        return "unknown"
