"""
RDK-B Root Cause Correlation Rules.

Maps observed symptoms/events to possible root causes.

The analyzer should:
1. Detect events from logs.
2. Match symptoms.
3. Increase/decrease candidate confidence.
4. Select the highest confidence root cause.
"""

from detector.models import EventCategory


#
# Symptom -> Possible Root Causes
#
CORRELATION_RULES = {


    # ==========================================================
    # WiFi / OneWifi
    # ==========================================================

    EventCategory.WIFI_DISCONNECT: {

        "causes": [

            (
                EventCategory.WIFI_DRIVER_FAILURE,
                0.90
            ),

            (
                EventCategory.WIFI_FIRMWARE_FAILURE,
                0.85
            ),

            (
                EventCategory.HOSTAPD_FAILURE,
                0.80
            ),

            (
                EventCategory.RF_INTERFERENCE,
                0.70
            ),

            (
                EventCategory.WIFI_ROAM_FAILURE,
                0.65
            ),

        ],

        "owner": "OneWifi",

    },


    EventCategory.WIFI_ASSOC_FAILURE: {

        "causes": [

            (
                EventCategory.HOSTAPD_FAILURE,
                0.85
            ),

            (
                EventCategory.WIFI_AUTH_FAILURE,
                0.80
            ),

            (
                EventCategory.RF_INTERFERENCE,
                0.60
            ),

        ],

        "owner": "OneWifi",

    },


    EventCategory.WIFI_RADIO_RESET: {

        "causes": [

            (
                EventCategory.WIFI_DRIVER_FAILURE,
                0.95
            ),

            (
                EventCategory.WIFI_FIRMWARE_FAILURE,
                0.90
            ),

            (
                EventCategory.KERNEL_FAILURE,
                0.75
            ),

        ],

        "owner": "WiFi HAL",

    },


    # ==========================================================
    # DOCSIS
    # ==========================================================

    EventCategory.DOCSIS_T4_TIMEOUT: {

        "causes": [

            (
                EventCategory.DOCSIS_SIGNAL_DEGRADATION,
                0.90
            ),

            (
                EventCategory.DOCSIS_RANGING_FAILURE,
                0.85
            ),

            (
                EventCategory.WAN_FAILURE,
                0.80
            ),

        ],

        "owner": "DOCSIS HAL",

    },


    EventCategory.DOCSIS_OFFLINE: {

        "causes": [

            (
                EventCategory.DOCSIS_FAILURE,
                0.95
            ),

            (
                EventCategory.WAN_FAILURE,
                0.90
            ),

            (
                EventCategory.DOCSIS_SIGNAL_DEGRADATION,
                0.80
            ),

        ],

        "owner": "DOCSIS HAL",

    },


    # ==========================================================
    # Memory / Resource
    # ==========================================================

    EventCategory.OOM_KILLER: {

        "causes": [

            (
                EventCategory.MEMORY_LEAK,
                0.90
            ),

            (
                EventCategory.APPLICATION_CRASH,
                0.75
            ),

            (
                EventCategory.RESOURCE_EXHAUSTION,
                0.70
            ),

        ],

        "owner": "Linux Kernel",

    },


    EventCategory.CPU_OVERLOAD: {

        "causes": [

            (
                EventCategory.APPLICATION_FAILURE,
                0.70
            ),

            (
                EventCategory.RESOURCE_EXHAUSTION,
                0.80
            ),

        ],

        "owner": "Linux",

    },


    # ==========================================================
    # Storage
    # ==========================================================

    EventCategory.DISK_IO_ERROR: {

        "causes": [

            (
                EventCategory.STORAGE_FAILURE,
                0.95
            ),

            (
                EventCategory.FLASH_FAILURE,
                0.85
            ),

        ],

        "owner": "Linux Storage",

    },


    EventCategory.FILESYSTEM_CORRUPTION: {

        "causes": [

            (
                EventCategory.STORAGE_FAILURE,
                0.95
            ),

            (
                EventCategory.FLASH_FAILURE,
                0.85
            ),

            (
                EventCategory.POWER_FAILURE,
                0.60
            ),

        ],

        "owner": "Linux Storage",

    },


    # ==========================================================
    # CCSP
    # ==========================================================

    EventCategory.CCSP_BUS_FAILURE: {

        "causes": [

            (
                EventCategory.CCSP_FAILURE,
                0.95
            ),

            (
                EventCategory.SYSTEMD_FAILURE,
                0.70
            ),

        ],

        "owner": "CCSP Message Bus",

    },


    EventCategory.CCSP_TIMEOUT: {

        "causes": [

            (
                EventCategory.CCSP_COMPONENT_FAILURE,
                0.85
            ),

            (
                EventCategory.CPU_OVERLOAD,
                0.60
            ),

            (
                EventCategory.MEMORY_PRESSURE,
                0.60
            ),

        ],

        "owner": "CCSP",

    },


    # ==========================================================
    # Network
    # ==========================================================

    EventCategory.DHCP_FAILURE: {

        "causes": [

            (
                EventCategory.WAN_FAILURE,
                0.80
            ),

            (
                EventCategory.DHCP_SERVER_FAILURE,
                0.75
            ),

        ],

        "owner": "Network Stack",

    },


    EventCategory.DNS_FAILURE: {

        "causes": [

            (
                EventCategory.DNSMASQ_FAILURE,
                0.85
            ),

            (
                EventCategory.WAN_FAILURE,
                0.60
            ),

        ],

        "owner": "dnsmasq",

    },


    # ==========================================================
    # Kernel / Hardware
    # ==========================================================

    EventCategory.KERNEL_PANIC: {

        "causes": [

            (
                EventCategory.KERNEL_FAILURE,
                1.00
            ),

            (
                EventCategory.DRIVER_FAILURE,
                0.85
            ),

            (
                EventCategory.HARDWARE_FAILURE,
                0.80
            ),

        ],

        "owner": "Linux Kernel",

    },


    EventCategory.WATCHDOG_RESET: {

        "causes": [

            (
                EventCategory.KERNEL_FAILURE,
                0.90
            ),

            (
                EventCategory.HUNG_PROCESS,
                0.85
            ),

            (
                EventCategory.CPU_OVERLOAD,
                0.70
            ),

        ],

        "owner": "Platform Watchdog",

    },


}


#
# Event chains where multiple symptoms together increase confidence
#
CORRELATION_CHAINS = [


    {
        "events": [
            EventCategory.WIFI_DISCONNECT,
            EventCategory.WIFI_DRIVER_FAILURE,
        ],

        "root_cause": EventCategory.WIFI_FIRMWARE_FAILURE,

        "confidence_boost": 0.15,

    },


    {
        "events": [
            EventCategory.DOCSIS_T4_TIMEOUT,
            EventCategory.DOCSIS_SIGNAL_DEGRADATION,
        ],

        "root_cause": EventCategory.DOCSIS_FAILURE,

        "confidence_boost": 0.20,

    },


    {
        "events": [
            EventCategory.OOM_KILLER,
            EventCategory.APPLICATION_CRASH,
        ],

        "root_cause": EventCategory.MEMORY_LEAK,

        "confidence_boost": 0.20,

    },


    {
        "events": [
            EventCategory.CCSP_TIMEOUT,
            EventCategory.CCSP_COMPONENT_FAILURE,
        ],

        "root_cause": EventCategory.CCSP_FAILURE,

        "confidence_boost": 0.20,

    },


]
