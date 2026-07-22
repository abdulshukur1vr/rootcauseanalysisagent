"""
RDK-B Root Cause Correlation Rules.

Priority:
    100 - Hardware/kernel/system fatal failures
     90 - Platform/component failures
     80 - Major service degradation
     70 - Recoverable service failures
     50 - Secondary symptoms
     30 - Informational/noise
"""

from detector.models import EventCategory


ROOT_CAUSE_PRIORITY = {

    # ==========================================================
    # Kernel / Operating System
    # ==========================================================

    EventCategory.KERNEL_FAILURE: 100,
    EventCategory.KERNEL_PANIC: 100,
    EventCategory.KERNEL_OOPS: 95,
    EventCategory.KERNEL_WARNING: 60,

    EventCategory.WATCHDOG_RESET: 100,
    EventCategory.KERNEL_HUNG_TASK: 90,

    EventCategory.DRIVER_FAILURE: 95,
    EventCategory.MODULE_LOAD_FAILURE: 85,


    # ==========================================================
    # Hardware Platform
    # ==========================================================

    EventCategory.CPU_FAILURE: 100,
    EventCategory.MEMORY_FAILURE: 100,
    EventCategory.MEMORY_CORRUPTION: 95,

    EventCategory.THERMAL_FAILURE: 95,
    EventCategory.OVER_TEMPERATURE: 90,

    EventCategory.POWER_FAILURE: 100,

    EventCategory.FLASH_FAILURE: 95,
    EventCategory.NAND_FAILURE: 95,
    EventCategory.EMMC_FAILURE: 95,


    # ==========================================================
    # Boot / Startup
    # ==========================================================

    EventCategory.BOOT_FAILURE: 100,
    EventCategory.BOOT_TIMEOUT: 90,

    EventCategory.SYSTEMD_FAILURE: 90,
    EventCategory.SERVICE_START_FAILURE: 85,

    EventCategory.CONFIGURATION_FAILURE: 80,


    # ==========================================================
    # CCSP Framework
    # ==========================================================

    EventCategory.CCSP_FAILURE: 95,
    EventCategory.CCSP_COMPONENT_FAILURE: 90,
    EventCategory.CCSP_BUS_FAILURE: 95,

    EventCategory.TR181_FAILURE: 75,
    EventCategory.CCSP_TIMEOUT: 70,


    # ==========================================================
    # WiFi / OneWifi
    # ==========================================================

    # Root causes
    EventCategory.WIFI_DRIVER_FAILURE: 95,
    EventCategory.WIFI_RADIO_FAILURE: 90,
    EventCategory.HOSTAPD_FAILURE: 90,
    EventCategory.WPA_SUPPLICANT_FAILURE: 85,

    EventCategory.WIFI_FIRMWARE_FAILURE: 90,
    EventCategory.WIFI_CALIBRATION_FAILURE: 80,

    EventCategory.RF_INTERFERENCE: 75,
    EventCategory.WIFI_CHANNEL_FAILURE: 70,

    # Symptoms
    EventCategory.WIFI_DISCONNECT: 80,
    EventCategory.WIFI_ASSOC_FAILURE: 80,
    EventCategory.WIFI_AUTH_FAILURE: 75,
    EventCategory.WIFI_CLIENT_FAILURE: 75,

    EventCategory.WIFI_ROAM_FAILURE: 70,



    # ==========================================================
    # Ethernet / LAN
    # ==========================================================

    EventCategory.ETHERNET_FAILURE: 90,
    EventCategory.ETHERNET_LINK_DOWN: 80,

    EventCategory.SWITCH_FAILURE: 90,
    EventCategory.PHY_FAILURE: 90,

    EventCategory.ARP_FAILURE: 60,



    # ==========================================================
    # WAN / IP Connectivity
    # ==========================================================

    EventCategory.WAN_FAILURE: 95,

    EventCategory.IP_ACQUISITION_FAILURE: 90,

    EventCategory.DHCP_FAILURE: 80,
    EventCategory.DHCP_RENEW_FAILURE: 75,

    EventCategory.PPP_FAILURE: 85,

    EventCategory.ROUTING_FAILURE: 80,

    EventCategory.NAT_FAILURE: 75,



    # ==========================================================
    # DOCSIS Cable Modem
    # ==========================================================

    EventCategory.DOCSIS_FAILURE: 100,

    EventCategory.DOCSIS_OFFLINE: 100,

    EventCategory.DOCSIS_REGISTRATION_FAILURE: 95,

    EventCategory.DOCSIS_T1_TIMEOUT: 80,
    EventCategory.DOCSIS_T2_TIMEOUT: 85,
    EventCategory.DOCSIS_T3_TIMEOUT: 90,
    EventCategory.DOCSIS_T4_TIMEOUT: 95,

    EventCategory.DOCSIS_RANGING_FAILURE: 90,

    EventCategory.DOCSIS_SIGNAL_DEGRADATION: 80,

    EventCategory.DOCSIS_CHANNEL_FAILURE: 85,



    # ==========================================================
    # MoCA
    # ==========================================================

    EventCategory.MOCA_FAILURE: 85,
    EventCategory.MOCA_LINK_DOWN: 80,
    EventCategory.MOCA_SIGNAL_FAILURE: 70,



    # ==========================================================
    # DNS / DHCP / Network Services
    # ==========================================================

    EventCategory.DNS_FAILURE: 70,
    EventCategory.DNSMASQ_FAILURE: 85,

    EventCategory.NTP_FAILURE: 40,

    EventCategory.FIREWALL_FAILURE: 75,



    # ==========================================================
    # Storage / Filesystem
    # ==========================================================

    EventCategory.STORAGE_FAILURE: 95,

    EventCategory.DISK_FAILURE: 95,
    EventCategory.DISK_IO_ERROR: 90,

    EventCategory.FILESYSTEM_FAILURE: 90,
    EventCategory.FILESYSTEM_CORRUPTION: 95,

    EventCategory.LOG_STORAGE_FAILURE: 70,



    # ==========================================================
    # Resource Exhaustion
    # ==========================================================

    EventCategory.OUT_OF_MEMORY: 95,
    EventCategory.OOM_KILLER: 95,

    EventCategory.MEMORY_LEAK: 90,

    EventCategory.CPU_OVERLOAD: 75,

    EventCategory.DISK_FULL: 85,

    EventCategory.RESOURCE_EXHAUSTION: 80,



    # ==========================================================
    # RDK-B Applications / Services
    # ==========================================================

    EventCategory.APPLICATION_CRASH: 80,

    EventCategory.DAEMON_CRASH: 85,

    EventCategory.PAM_FAILURE: 60,

    EventCategory.WEBCONFIG_FAILURE: 70,

    EventCategory.BUSINESS_LOGIC_FAILURE: 60,



    # ==========================================================
    # Telemetry / Management
    # ==========================================================

    EventCategory.TELEMETRY_FAILURE: 50,

    EventCategory.PSM_FAILURE: 70,

    EventCategory.TR069_FAILURE: 60,

    EventCategory.XCONF_FAILURE: 60,



    # ==========================================================
    # Firmware / Upgrade
    # ==========================================================

    EventCategory.FIRMWARE_UPGRADE_FAILURE: 90,

    EventCategory.FIRMWARE_ROLLBACK: 80,

    EventCategory.VERSION_MISMATCH: 70,


    # ==========================================================
    # Security
    # ==========================================================

    EventCategory.AUTH_FAILURE: 50,

    EventCategory.CERTIFICATE_FAILURE: 70,

    EventCategory.TLS_FAILURE: 70,

}
