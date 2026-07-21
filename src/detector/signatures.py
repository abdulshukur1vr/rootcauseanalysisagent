"""
Failure signatures.

These are intentionally separated from detection logic
so new signatures can be added without code changes.
"""


SIGNATURES = {


    "STORAGE_FAILURE": [

        "i/o error",

        "i/o timeout",

        "blk_update_request",

        "ext4-fs error",

        "filesystem readonly",

        "read-only filesystem",

        "remounting filesystem read-only",

        "nvme error",

        "ata error",

        "disk failure",

    ],



    "MEMORY_FAILURE": [

        "out of memory",

        "oom killer",

        "killed process",

        "memory allocation failed",

        "page allocation failure",

    ],



    "KERNEL_FAILURE": [

        "kernel panic",

        "kernel BUG",

        "oops:",

        "fatal exception",

        "hung task",

        "soft lockup",

        "hard lockup",

        "watchdog",

    ],



    "ETHERNET_FAILURE": [

        "link down",

        "carrier lost",

        "carrier off",

        "netdev watchdog",

        "tx timeout",

        "phy failure",

        "ethernet link failure",

    ],



    "WIFI_CLIENT_FAILURE": [

        "authentication failed",

        "authentication timeout",

        "association failed",

        "association rejected",

        "4-way handshake failed",

        "wpa handshake timeout",

    ],



    "WIFI_DISCONNECT": [

        "deauthenticated",

        "disassociated",

        "station removed",

        "beacon timeout",

        "ap disconnected",

        "reason code",

    ],



    "DHCP_FAILURE": [

        "dhcp timeout",

        "no lease",

        "lease failed",

        "dhcpdiscover",

        "dchpoffer timeout",

    ],



    "DNS_FAILURE": [

        "dns failure",

        "dns timeout",

        "resolver failure",

        "nameserver unreachable",

    ],



    "NETWORK_STACK_FAILURE": [

        "socket error",

        "connection reset",

        "network unreachable",

        "route not found",

        "skb allocation failure",

        "tcp timeout",

    ]

}
