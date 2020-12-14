from unittest import TestCase


class TestInterfaceInteroperability(TestCase):
    def test_version_0_1_5(self):
        try:
            from scapy_helper import show_diff, show_hex, get_hex, table
            from scapy_helper import compare
        except ImportError as e:
            self.fail("Import Error: %s" % e)

    def test_version_0_1_11(self):
        try:
            from scapy_helper import get_hex, show_diff, show_hex, table, hex_equal
            from scapy_helper import Compare
        except ImportError as e:
            self.fail("Import Error: %s" % e)

    def test_version_0_3_0(self):
        try:
            from scapy_helper import get_hex, show_diff, show_hex, table, hex_equal
            from scapy_helper import Compare
            from scapy_helper import PacketAssert
        except ImportError as e:
            self.fail("Import Error: %s" % e)
