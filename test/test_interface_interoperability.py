from unittest import TestCase


class TestInterfaceInteroperability(TestCase):
    def test_version_0_1_5(self):
        try:
            from scapy_helper import compare, get_hex, show_diff, show_hex, table
        except ImportError as e:
            self.fail("Import Error: %s" % e)

    def test_version_0_1_11(self):
        try:
            from scapy_helper import (
                Compare,
                get_hex,
                hex_equal,
                show_diff,
                show_hex,
                table,
            )
        except ImportError as e:
            self.fail("Import Error: %s" % e)

    def test_version_0_3_0(self):
        try:
            from scapy_helper import (
                Compare,
                PacketAssert,
                get_hex,
                hex_equal,
                show_diff,
                show_hex,
                table,
            )
        except ImportError as e:
            self.fail("Import Error: %s" % e)
