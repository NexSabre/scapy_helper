from unittest import TestCase

from scapy.layers.l2 import Ether

from scapy_helper.test_case_extensions.packet_assert import PacketAssert


class TestPacketAssert(TestCase, PacketAssert):
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

    def test_assert_bytes_equal(self):
        with self.assertRaises(AssertionError):
            self.assertBytesEqual(Ether(), Ether(dst="00:00:00:00:00:00"))

    def test_negative_assert_bytes_equal(self):
        self.assertBytesEqual(Ether(), Ether())

    def test_assert_bytes_not_equal(self):
        self.assertBytesNotEqual(Ether(), Ether(dst="00:00:00:00:00:00"))

    def test_negative_bytes_not_equal(self):
        with self.assertRaises(AssertionError):
            self.assertBytesNotEqual(Ether(), Ether())

    def test_assert_hex_different_at_position_zero(self):
        self.assertHexDifferentAt(Ether(dst="00:00:00:00:00:00"),
                                  Ether(dst="01:00:00:00:00:00"),
                                  positions=0,
                                  message="Packets should be different on 0 position")

    def test_negative_assert_hex_different_at_position_two(self):
        with self.assertRaises(AssertionError):
            self.assertHexDifferentAt(Ether(dst="00:00:00:00:00:00"),
                                      Ether(dst="01:00:00:00:00:00"),
                                      positions=2,
                                      message="Packets should be different on 0 position")

    def test_assert_hex_different_at_position_list(self):
        self.assertHexDifferentAt(Ether(dst="00:00:00:00:00:00"),
                                  Ether(dst="01:01:00:00:00:00"),
                                  positions=(0, 1),
                                  message="Packets should be different on (0, 1) position")

    def test_negative_assert_hex_different_at_position_wrong_list(self):
        with self.assertRaises(AssertionError):
            self.assertHexDifferentAt(Ether(dst="00:00:00:00:00:00"),
                                      Ether(dst="01:01:00:00:00:00"),
                                      positions=(0, 3),
                                      message="Packets should be different on (0, 1) position")

    def test_negative_assert_hex_different_at_position_wrong_list_half_correct(self):
        with self.assertRaises(AssertionError):
            self.assertHexDifferentAt(Ether(dst="00:00:00:00:00:00"),
                                      Ether(dst="01:01:00:00:00:00"),
                                      positions=(0, 1, 2),
                                      message="Packets should be different on (0, 1) position")