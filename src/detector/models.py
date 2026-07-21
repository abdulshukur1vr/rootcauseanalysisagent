"""
Detection domain models.
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class EventCategory(str, Enum):

    STORAGE_FAILURE = "STORAGE_FAILURE"

    MEMORY_FAILURE = "MEMORY_FAILURE"

    KERNEL_FAILURE = "KERNEL_FAILURE"

    ETHERNET_FAILURE = "ETHERNET_FAILURE"

    WIFI_CLIENT_FAILURE = "WIFI_CLIENT_FAILURE"

    WIFI_DISCONNECT = "WIFI_DISCONNECT"

    DHCP_FAILURE = "DHCP_FAILURE"

    DNS_FAILURE = "DNS_FAILURE"

    NETWORK_STACK_FAILURE = "NETWORK_STACK_FAILURE"



class EventSeverity(str, Enum):

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"



@dataclass(frozen=True)
class DetectedEvent:

    category: EventCategory

    severity: EventSeverity

    confidence: int

    message: str

    source: Path
