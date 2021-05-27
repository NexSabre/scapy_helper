from unittest import TestCase

from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from scapy_helper import to_list


class TestToList(TestCase):
    def test_simple_list(self):
        packet = (
            Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00")
            / IP(src="0.0.0.0", dst="127.0.0.1")
            / TCP()
        )
        packet_result = [
            {
                "Ethernet": {
                    "src": "00:00:00:00:00:00",
                    "dst": "ff:ff:ff:ff:ff:ff",
                    "type": 2048,
                }
            },
            {
                "IP": {
                    "frag": 0,
                    "src": "0.0.0.0",
                    "proto": 6,
                    "tos": 0,
                    "dst": "127.0.0.1",
                    "chksum": None,
                    "len": None,
                    "options": [],
                    "version": 4,
                    "flags": None,
                    "ihl": None,
                    "ttl": 64,
                    "id": 1,
                }
            },
            {
                "TCP": {
                    "reserved": 0,
                    "seq": 0,
                    "ack": 0,
                    "dataofs": None,
                    "urgptr": 0,
                    "window": 8192,
                    "flags": None,
                    "chksum": None,
                    "dport": 80,
                    "sport": 20,
                    "options": [],
                }
            },
        ]

        to_list_result = to_list(packet)

        self.assertTrue(isinstance(to_list_result, list))
        self.assertEqual(to_list_result, packet_result)
