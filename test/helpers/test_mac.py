from unittest import TestCase

from scapy_helper.helpers.mac import int2mac, mac2int

MAX_VALUE_FOR_MAC = 281474976710655
TOO_BIG_INT_FOR_MAC = 281474976710657
TOO_SMALL_INT_FOR_MAC = -1


class TestMac(TestCase):
    def setUp(self):
        self.int_mac = 73596036829
        self.str_mac = "00:11:22:AA:66:DD"

    def test_int_to_mac(self):
        self.assertEqual(
            int2mac(self.int_mac), self.str_mac.lower(), "Values should be equal"
        )

    def test_int_to_mac_upper(self):
        self.assertEqual(
            int2mac(self.int_mac, upper=True), self.str_mac, "Values should be equal"
        )

    def test_mac_to_int(self):
        self.assertEqual(mac2int(self.str_mac), self.int_mac, "Values should be equal")

    def test_int2mac_int_to_int(self):
        with self.assertRaises(TypeError):
            int2mac(self.str_mac)

    def test_mac2int_str_to_str(self):
        with self.assertRaises(TypeError):
            mac2int(self.int_mac)

    def test_maximum_value_for_int2_mac(self):
        self.assertEqual(int2mac(MAX_VALUE_FOR_MAC).lower(), "ff:ff:ff:ff:ff:ff")

    def test_incorrect_large_int(self):
        with self.assertRaises(ValueError):
            [int2mac(x) for x in (TOO_SMALL_INT_FOR_MAC, TOO_BIG_INT_FOR_MAC)]
