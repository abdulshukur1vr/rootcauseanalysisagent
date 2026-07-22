"""
RDK-B Evidence Weighting Rules.

Maps log signatures to event categories and confidence boosts.
"""

from detector.models import EventCategory


EVIDENCE_RULES = [

    # ======================================================
    # WiFi / OneWifi / Broadcom WiFi
    # ======================================================

    {
        "patterns": [
            "BRCM-WIFI",
            "wl0:",
            "wl1:",
            "wl2:",
            "STA",
            "disassociated",
        ],

        "category": EventCategory.WIFI_DISCONNECT,

        "confidence": 0.90,

        "component": "Broadcom WiFi Driver",
    },


    {
        "patterns": [
            "hostapd",
            "AP-STA-DISCONNECTED",
            "authentication failed",
        ],

        "category": EventCategory.HOSTAPD_FAILURE,

        "confidence": 0.85,

        "component": "hostapd",
    },


    {
        "patterns": [
            "wifi_hal",
            "radio reset",
            "driver crash",
        ],

        "category": EventCategory.WIFI_DRIVER_FAILURE,

        "confidence": 0.95,

        "component": "WiFi HAL",
    },


    # ======================================================
    # DOCSIS
    # ======================================================

    {
        "patterns": [
            "T4 timeout",
            "T3 timeout",
            "Ranging Request Retries",
        ],

        "category": EventCategory.DOCSIS_T4_TIMEOUT,

        "confidence": 0.95,

        "component": "DOCSIS HAL",
    },


    {
        "patterns": [
            "CM-STATUS",
            "SYNC failure",
            "MDD timeout",
        ],

        "category": EventCategory.DOCSIS_SIGNAL_DEGRADATION,

        "confidence": 0.85,

        "component": "DOCSIS",
    },


    # ======================================================
    # CCSP
    # ======================================================

    {
        "patterns": [
            "CCSP_Message_Bus",
            "CR bus error",
            "component timeout",
        ],

        "category": EventCategory.CCSP_BUS_FAILURE,

        "confidence": 0.90,

        "component": "CCSP",
    },


    {
        "patterns": [
            "CcspWifiAgent",
            "CcspPandM",
            "CcspTr069Pa",
        ],

        "category": EventCategory.CCSP_COMPONENT_FAILURE,

        "confidence": 0.80,

        "component": "CCSP Component",
    },


    # ======================================================
    # Kernel
    # ======================================================

    {
        "patterns": [
            "kernel panic",
            "Kernel panic",
        ],

        "category": EventCategory.KERNEL_PANIC,

        "confidence": 1.0,

        "component": "Linux Kernel",
    },


    {
        "patterns": [
            "Call Trace:",
            "Oops:",
            "BUG:",
        ],

        "category": EventCategory.KERNEL_OOPS,

        "confidence": 0.95,

        "component": "Linux Kernel",
    },


    # ======================================================
    # Memory
    # ======================================================

    {
        "patterns": [
            "Out of memory",
            "Killed process",
            "oom-killer",
        ],

        "category": EventCategory.OOM_KILLER,

        "confidence": 0.95,

        "component": "Linux Kernel",
    },


    # ======================================================
    # Storage
    # ======================================================

    {
        "patterns": [
            "I/O error",
            "EXT4-fs error",
            "UBIFS error",
            "mmcblk",
        ],

        "category": EventCategory.STORAGE_FAILURE,

        "confidence": 0.90,

        "component": "Linux Storage",
    },


    # ======================================================
    # Network
    # ======================================================

    {
        "patterns": [
            "dnsmasq",
            "DNS failure",
            "SERVFAIL",
        ],

        "category": EventCategory.DNS_FAILURE,

        "confidence": 0.80,

        "component": "dnsmasq",
    },


    {
        "patterns": [
            "udhcpc",
            "DHCP timeout",
            "DHCP failed",
        ],

        "category": EventCategory.DHCP_FAILURE,

        "confidence": 0.85,

        "component": "DHCP Client",
    },

]
