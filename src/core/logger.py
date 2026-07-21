"""
Central logging configuration.
"""

import logging
import logging.config
from pathlib import Path

import yaml


DEFAULT_LOG_FILE = Path("logs/rootcause.log")



def setup_logging() -> logging.Logger:

    log_config = Path(
        "config/logging.yaml"
    )


    if log_config.exists():

        with log_config.open(
            "r",
            encoding="utf-8"
        ) as file:

            config = yaml.safe_load(file)

        logging.config.dictConfig(
            config
        )


    else:

        logging.basicConfig(
            level=logging.INFO,
            format=(
                "%(asctime)s "
                "%(levelname)s "
                "%(name)s "
                "%(message)s"
            )
        )


    return logging.getLogger(
        "rootcauseanalysisagent"
    )
