"""
RDK-B failure signatures.

Patterns are intentionally separated from detection logic.
All patterns are lowercase because PatternDetector normalizes messages.
"""

SIGNATURES = {


    #
    # Kernel / firmware failures
    #
    "KERNEL_FAILURE": [

        "kernel panic",

        "kernel bug",

        "oops:",

        "fatal exception",

        "unable to handle kernel",

        "call trace",

        "stack trace",

        "segmentation fault",

        "soft lockup",

        "hard lockup",

        "hung task",

        "rcu stall",

        "watchdog reset",

        "watchdog timeout",

        "watchdog bite",

    ],



    #
    # Memory failures
    #
    "MEMORY_FAILURE": [

        "out of memory",

        "oom-killer",

        "oom killer",

        "killed process",

        "memory allocation failed",

        "page allocation failure",

        "cannot allocate memory",

        "low memory",

        "memory pressure",

    ],



    #
    # Storage / flash / filesystem
    #
    "STORAGE_FAILURE": [

        "i/o error",

        "i/o timeout",

        "blk_update_request",

        "mmcblk",

        "sd card error",

        "nand error",

        "ubi error",

        "ubifs error",

        "jffs2 error",

        "ext4-fs error",

        "filesystem readonly",

        "read-only filesystem",

        "remounting filesystem read-only",

        "disk failure",

    ],



    #
    # Ethernet / WAN / PHY
    #
    "ETHERNET_FAILURE": [

        "link down",

        "link is down",

        "carrier lost",

        "carrier off",

        "phy failure",

        "phy link down",

        "ethernet link failure",

        "netdev watchdog",

        "tx timeout",

        "eth0 down",

        "wan link down",

    ],



    #
    # WiFi client failures
    #
    "WIFI_CLIENT_FAILURE": [

        "authentication failed",

        "authentication timeout",

        "association failed",

        "association rejected",

        "4-way handshake failed",

        "wpa handshake timeout",

        "wpa authentication failed",

        "client authentication failed",

    ],



    #
    # WiFi disconnect events
    #
    "WIFI_DISCONNECT": [

        "disassociated",

        "deauthenticated",

        "station removed",

        "sta removed",

        "beacon timeout",

        "ap disconnected",

        "reason code",

        "device disconnected",

    ],



    #
    # WiFi driver / firmware problems
    #
    "WIFI_DRIVER_FAILURE": [

        "brcm-wifi",

        "brcm wifi",

        "wl0:",

        "wl1:",

        "wl2:",

        "firmware crash",

        "firmware trap",

        "fw trap",

        "dongle reset",

        "wifi driver",

        "driver reset",

    ],



    #
    # DHCP failures
    #
    "DHCP_FAILURE": [

        "dhcp timeout",

        "dhcp failed",

        "no lease",

        "lease failed",

        "dhcpdiscover",

        "dhcpoffer timeout",

        "dhcp request failed",

        "udhcpc failed",

    ],



    #
    # DNS failures
    #
    "DNS_FAILURE": [

        "dns failure",

        "dns timeout",

        "resolver failure",

        "nameserver unreachable",

        "dnsmasq failed",

        "servfail",

        "timeout resolving",

    ],



    #
    # Linux networking stack
    #
    "NETWORK_STACK_FAILURE": [

        "socket error",

        "connection reset",

        "connection reset by peer",

        "connection refused",

        "broken pipe",

        "network unreachable",

        "route not found",

        "skb allocation failure",

        "tcp timeout",

        "socket timeout",

    ],



    #
    # CCSP/RDK-B component failures
    #
    "SERVICE_FAILURE": [

        "component failed",

        "component timeout",

        "ccsp failure",

        "ccsp crash",

        "ccsp bus error",

        "dbus timeout",

        "daemon failed",

        "service exited",

        "failed to start",

        "restart required",

    ],



    #
    # Application/process crashes
    #
    "PROCESS_CRASH": [

        "segmentation fault",

        "segfault",

        "core dumped",

        "assertion failed",

        "process crashed",

        "terminated by signal",

        "fatal signal",

    ],



    #
    # Boot / startup failures
    #
    "BOOT_FAILURE": [

        "boot failed",

        "boot failure",

        "failed to initialize",

        "startup failed",

        "initialization error",

        "firmware boot error",

    ],



    #
    # Configuration failures
    #
    "CONFIGURATION_FAILURE": [

        "invalid configuration",

        "configuration failed",

        "unable to apply configuration",

        "config error",

        "validation failed",

    ],



    #
    # Telemetry / reporting failures
    #
    "TELEMETRY_FAILURE": [

        "telemetry failed",

        "report upload failed",

        "event upload failed",

        "connection to telemetry server failed",

    ],

}
