from unittest import TestCase

from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether

from scapy_helper.helpers.to_dict import to_dict, to_list


class TestToDict(TestCase):
    def test_simple_dict(self):
        packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP() / TCP()
        print(to_dict(packet))


class TestToList(TestCase):
    def test_simple_list(self):
        packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP() / TCP()
        self.assertTrue(
            isinstance(to_list(packet), list)
        )
