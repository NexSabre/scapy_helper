from unittest import TestCase

from pyperclip import PyperclipException

from scapy_helper.utils.hstrip import hstrip

HEXDUMP_VALUE = """
0000  FF FF FF FF FF FF 00 00 00 00 00 00 08 00 45 00  ..............E.
0010  00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00  .(....@.|.......
0020  00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02  .....P........P.
0030  20 00 91 7C 00 00                                 ..|..
"""

HSTRIP_RESULT = "FF FF FF FF FF FF 00 00 00 00 00 00 08 00 45 00 " \
                "00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00 " \
                "00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02 " \
                "20 00 91 7C 00 00"


class TestHStrip(TestCase):
    def test_hstrip(self):
        import pyperclip
        try:
            pyperclip.copy(HEXDUMP_VALUE)
        except PyperclipException:
            return True

        self.assertEqual(
            hstrip(raw=False),
            HSTRIP_RESULT
        )

    def test_hstrip_from_hexdump(self):
        self.assertEqual(
            hstrip(raw=False, hexdump=HEXDUMP_VALUE),
            HSTRIP_RESULT
        )
