from detector.signatures import SIGNATURES


def test_rdkb_signature_categories():

    expected = [
        "KERNEL_FAILURE",
        "MEMORY_FAILURE",
        "STORAGE_FAILURE",
        "ETHERNET_FAILURE",
        "WIFI_DISCONNECT",
        "WIFI_DRIVER_FAILURE",
        "DHCP_FAILURE",
        "DNS_FAILURE",
        "NETWORK_STACK_FAILURE",
        "SERVICE_FAILURE",
        "PROCESS_CRASH",
    ]

    for category in expected:
        assert category in SIGNATURES
        assert len(SIGNATURES[category]) > 0
