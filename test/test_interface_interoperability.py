from unittest import TestCase


class TestInterfaceInteroperability(TestCase):
    def test_version_0_1_5(self):
        try:
            from scapy_helper import show_diff, show_hex, get_hex, table
            from scapy_helper import compare
        except ImportError as e:
            self.fail("Import Error: %s" % e)
