"""
Configuration loader.
"""

from pathlib import Path
from typing import Any

import yaml

from core.constants import DEFAULT_CONFIG_PATH


class ConfigurationError(Exception):
    pass



class ConfigManager:
    """
    Loads YAML configuration.
    """


    def __init__(
        self,
        config_path: Path = DEFAULT_CONFIG_PATH
    ):

        self.config_path = config_path
        self._config: dict[str, Any] = {}


    def load(self) -> dict[str, Any]:

        if not self.config_path.exists():

            raise ConfigurationError(
                f"Configuration file missing: {self.config_path}"
            )


        with self.config_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            self._config = yaml.safe_load(file) or {}


        return self._config



    def get(
        self,
        key: str,
        default=None
    ):

        return self._config.get(
            key,
            default
        )
