from unittest import TestCase

from scapy_helper.helpers.mac import int2mac, mac2int


class TestMac(TestCase):
    def setUp(self):
        self.int_mac = 73596036829
        self.str_mac = "00:11:22:AA:66:DD"

    def test_int_to_mac(self):
        self.assertEqual(
            int2mac(self.int_mac),
            self.str_mac.lower(),
            "Values should be equal"
        )

    def test_int_to_mac_upper(self):
        self.assertEqual(
            int2mac(self.int_mac, upper=True),
            self.str_mac,
            "Values should be equal"
        )

    def test_mac_to_int(self):
        self.assertEqual(
            mac2int(self.str_mac),
            self.int_mac,
            "Values should be equal"
        )
