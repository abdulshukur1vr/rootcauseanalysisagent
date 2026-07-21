"""
Root cause correlation rules.
"""


from detector.models import EventCategory



ROOT_CAUSE_PRIORITY = {


    EventCategory.KERNEL_FAILURE:
        100,


    EventCategory.STORAGE_FAILURE:
        95,


    EventCategory.MEMORY_FAILURE:
        95,


    EventCategory.ETHERNET_FAILURE:
        90,


    EventCategory.WIFI_CLIENT_FAILURE:
        90,


    EventCategory.WIFI_DISCONNECT:
        85,


    EventCategory.DHCP_FAILURE:
        70,


    EventCategory.DNS_FAILURE:
        60,


    EventCategory.NETWORK_STACK_FAILURE:
        50,

}
