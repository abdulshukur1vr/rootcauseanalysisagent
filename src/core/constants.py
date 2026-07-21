"""
Application constants.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

DEFAULT_LOG_CONFIG_PATH = (
    PROJECT_ROOT / "config" / "logging.yaml"
)


SUPPORTED_ARCHIVE_EXTENSIONS = [
    ".tar",
    ".tar.gz",
    ".tgz",
]


DEFAULT_WORKSPACE_DIRECTORY = "workspace"


DEFAULT_LOG_DIRECTORY = "logs"
