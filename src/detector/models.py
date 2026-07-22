"""
Detection domain models.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path


class EventCategory(str, Enum):

    # =====================================================
    # Existing categories
    # =====================================================

    STORAGE_FAILURE = "STORAGE_FAILURE"

    MEMORY_FAILURE = "MEMORY_FAILURE"

    KERNEL_FAILURE = "KERNEL_FAILURE"

    ETHERNET_FAILURE = "ETHERNET_FAILURE"

    WIFI_CLIENT_FAILURE = "WIFI_CLIENT_FAILURE"

    WIFI_DISCONNECT = "WIFI_DISCONNECT"

    DHCP_FAILURE = "DHCP_FAILURE"

    DNS_FAILURE = "DNS_FAILURE"

    NETWORK_STACK_FAILURE = "NETWORK_STACK_FAILURE"


    # =====================================================
    # Kernel / Linux Platform
    # =====================================================

    KERNEL_PANIC = "KERNEL_PANIC"

    KERNEL_OOPS = "KERNEL_OOPS"

    KERNEL_WARNING = "KERNEL_WARNING"

    WATCHDOG_RESET = "WATCHDOG_RESET"

    KERNEL_HUNG_TASK = "KERNEL_HUNG_TASK"

    DRIVER_FAILURE = "DRIVER_FAILURE"

    MODULE_LOAD_FAILURE = "MODULE_LOAD_FAILURE"


    # =====================================================
    # Hardware
    # =====================================================

    CPU_FAILURE = "CPU_FAILURE"

    MEMORY_CORRUPTION = "MEMORY_CORRUPTION"

    THERMAL_FAILURE = "THERMAL_FAILURE"

    OVER_TEMPERATURE = "OVER_TEMPERATURE"

    POWER_FAILURE = "POWER_FAILURE"

    FLASH_FAILURE = "FLASH_FAILURE"

    NAND_FAILURE = "NAND_FAILURE"

    EMMC_FAILURE = "EMMC_FAILURE"



    # =====================================================
    # Boot / System Services
    # =====================================================

    BOOT_FAILURE = "BOOT_FAILURE"

    BOOT_TIMEOUT = "BOOT_TIMEOUT"

    SYSTEMD_FAILURE = "SYSTEMD_FAILURE"

    SERVICE_START_FAILURE = "SERVICE_START_FAILURE"

    CONFIGURATION_FAILURE = "CONFIGURATION_FAILURE"



    # =====================================================
    # CCSP / RDK-B Framework
    # =====================================================

    TLS_FAILURE = "TLS_FAILURE"

    CERTIFICATE_FAILURE = "CERTIFICATE_FAILURE"

    AUTH_FAILURE = "AUTH_FAILURE"

    BUSINESS_LOGIC_FAILURE = "BUSINESS_LOGIC_FAILURE"

    PAM_FAILURE = "PAM_FAILURE"

    CCSP_FAILURE = "CCSP_FAILURE"

    CCSP_COMPONENT_FAILURE = "CCSP_COMPONENT_FAILURE"

    CCSP_BUS_FAILURE = "CCSP_BUS_FAILURE"

    CCSP_TIMEOUT = "CCSP_TIMEOUT"

    TR181_FAILURE = "TR181_FAILURE"



    # =====================================================
    # WiFi / OneWifi
    # =====================================================

    WIFI_DRIVER_FAILURE = "WIFI_DRIVER_FAILURE"

    WIFI_RADIO_FAILURE = "WIFI_RADIO_FAILURE"

    WIFI_CALIBRATION_FAILURE = "WIFI_CALIBRATION_FAILURE"

    WIFI_CHANNEL_FAILURE = "WIFI_CHANNEL_FAILURE"

    WIFI_FIRMWARE_FAILURE = "WIFI_FIRMWARE_FAILURE"

    WIFI_ASSOC_FAILURE = "WIFI_ASSOC_FAILURE"

    WIFI_AUTH_FAILURE = "WIFI_AUTH_FAILURE"

    WIFI_ROAM_FAILURE = "WIFI_ROAM_FAILURE"

    WIFI_RADIO_RESET = "WIFI_RADIO_RESET"

    HOSTAPD_FAILURE = "HOSTAPD_FAILURE"

    WPA_SUPPLICANT_FAILURE = "WPA_SUPPLICANT_FAILURE"

    RF_INTERFERENCE = "RF_INTERFERENCE"



    # =====================================================
    # Ethernet / LAN
    # =====================================================

    ETHERNET_LINK_DOWN = "ETHERNET_LINK_DOWN"

    SWITCH_FAILURE = "SWITCH_FAILURE"

    PHY_FAILURE = "PHY_FAILURE"

    ARP_FAILURE = "ARP_FAILURE"



    # =====================================================
    # WAN / IP
    # =====================================================

    WAN_FAILURE = "WAN_FAILURE"

    IP_ACQUISITION_FAILURE = "IP_ACQUISITION_FAILURE"

    DHCP_RENEW_FAILURE = "DHCP_RENEW_FAILURE"

    PPP_FAILURE = "PPP_FAILURE"

    ROUTING_FAILURE = "ROUTING_FAILURE"

    NAT_FAILURE = "NAT_FAILURE"



    # =====================================================
    # DOCSIS
    # =====================================================

    DOCSIS_FAILURE = "DOCSIS_FAILURE"

    DOCSIS_REGISTRATION_FAILURE = "DOCSIS_REGISTRATION_FAILURE"
    
    DOCSIS_CHANNEL_FAILURE = "DOCSIS_CHANNEL_FAILURE"

    DOCSIS_OFFLINE = "DOCSIS_OFFLINE"

    DOCSIS_T1_TIMEOUT = "DOCSIS_T1_TIMEOUT"

    DOCSIS_T2_TIMEOUT = "DOCSIS_T2_TIMEOUT"

    DOCSIS_T3_TIMEOUT = "DOCSIS_T3_TIMEOUT"

    DOCSIS_T4_TIMEOUT = "DOCSIS_T4_TIMEOUT"

    DOCSIS_SIGNAL_DEGRADATION = (
        "DOCSIS_SIGNAL_DEGRADATION"
    )

    DOCSIS_RANGING_FAILURE = (
        "DOCSIS_RANGING_FAILURE"
    )



    # =====================================================
    # MoCA
    # =====================================================

    MOCA_FAILURE = "MOCA_FAILURE"

    MOCA_LINK_DOWN = "MOCA_LINK_DOWN"

    MOCA_SIGNAL_FAILURE = "MOCA_SIGNAL_FAILURE"



    # =====================================================
    # DNS / Network Services
    # =====================================================

    DNSMASQ_FAILURE = "DNSMASQ_FAILURE"

    FIREWALL_FAILURE = "FIREWALL_FAILURE"

    NTP_FAILURE = "NTP_FAILURE"



    # =====================================================
    # Storage / Filesystem
    # =====================================================

    DISK_FAILURE = "DISK_FAILURE"

    DISK_IO_ERROR = "DISK_IO_ERROR"

    FILESYSTEM_FAILURE = "FILESYSTEM_FAILURE"

    FILESYSTEM_CORRUPTION = "FILESYSTEM_CORRUPTION"

    LOG_STORAGE_FAILURE = "LOG_STORAGE_FAILURE"



    # =====================================================
    # Resource Exhaustion
    # =====================================================

    OUT_OF_MEMORY = "OUT_OF_MEMORY"

    OOM_KILLER = "OOM_KILLER"

    MEMORY_LEAK = "MEMORY_LEAK"

    CPU_OVERLOAD = "CPU_OVERLOAD"

    DISK_FULL = "DISK_FULL"

    RESOURCE_EXHAUSTION = "RESOURCE_EXHAUSTION"



    # =====================================================
    # Applications
    # =====================================================

    APPLICATION_CRASH = "APPLICATION_CRASH"

    DAEMON_CRASH = "DAEMON_CRASH"

    HUNG_PROCESS = "HUNG_PROCESS"



    # =====================================================
    # RDK-B Management
    # =====================================================

    TELEMETRY_FAILURE = "TELEMETRY_FAILURE"

    PSM_FAILURE = "PSM_FAILURE"

    TR069_FAILURE = "TR069_FAILURE"

    XCONF_FAILURE = "XCONF_FAILURE"

    WEBCONFIG_FAILURE = "WEBCONFIG_FAILURE"



    # =====================================================
    # Firmware
    # =====================================================

    FIRMWARE_UPGRADE_FAILURE = (
        "FIRMWARE_UPGRADE_FAILURE"
    )

    FIRMWARE_ROLLBACK = "FIRMWARE_ROLLBACK"

    VERSION_MISMATCH = "VERSION_MISMATCH"



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

    timestamp: datetime | None = None
