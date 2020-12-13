from unittest import TestCase

from scapy.layers.l2 import Ether

from scapy_helper.hex_equal import HexEqual


class TestHexEqualClass(TestCase, HexEqual):
    def test_assert_hex_equal(self):
        self.assertHexEqual(Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"),
                            Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"))

    def test_assert_hex_not_equal(self):
        self.assertHexNotEqual(Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"),
                               Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:aa"))

    def test_negative_assert_hex_equal(self):
        with self.assertRaises(AssertionError):
            self.assertHexEqual(Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"),
                                Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:aa"))

    def test_negative_assert_hex_not_equal(self):
        with self.assertRaises(AssertionError):
            self.assertHexNotEqual(Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"),
                                   Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00"))
