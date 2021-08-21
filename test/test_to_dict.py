from unittest import TestCase

from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from scapy_helper.helpers.to_dict import to_dict


class TestToDict(TestCase):
    def test_simple_dict(self):
        packet = (
            Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00")
            / IP(src="0.0.0.0", dst="127.0.0.1")
            / TCP()
        )
        packet_result = {
            "Ethernet": {
                "src": "00:00:00:00:00:00",
                "dst": "ff:ff:ff:ff:ff:ff",
                "type": 2048,
            }
        }

        to_dict_result = to_dict(packet)

        self.assertTrue(isinstance(to_dict_result, dict))
        self.assertEqual(to_dict_result, packet_result)

    def test_simple_dict_get_second_element(self):
        packet = (
            Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00")
            / IP(src="0.0.0.0", dst="127.0.0.1")
            / TCP()
        )
        packet_result = {
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
        }

        to_dict_result = to_dict(packet, layer=1)  # layer 1 is IP

        self.assertTrue(isinstance(to_dict_result, dict))
        self.assertEqual(to_dict_result, packet_result)
