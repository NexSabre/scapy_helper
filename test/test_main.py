from unittest import TestCase

from mock import MagicMock
from scapy.layers.l2 import Ether
from scapy.utils import chexdump

from scapy_helper import get_hex, show_diff
from scapy_helper.main import diff, hex_equal, _prepare, get_diff


class TestScapyHelper(TestCase):
    def setUp(self):
        self.ether = Ether(dst="ff:ff:ff:ff:ff:ff",
                           src="00:00:00:00:00:00")
        self.ether2 = Ether(dst="00:00:00:00:00:00",
                            src="00:00:00:00:00:00")

    def test_get_diff_should_be_the_same_as_diff(self):
        fun_diff = diff(self.ether, self.ether2)
        fun_get_diff = get_diff(self.ether, self.ether2)
        self.assertEqual(fun_diff, fun_get_diff, "The result of get_diff and diff should be the same")

    def test_diff_list_equal(self):
        result = diff("ff ff ff ff ff ff 00 00 00 00 00 00 90 00", "ff ff ff ff ff ff 00 00 00 00 00 00 90 00")
        self.assertEqual(
            result,
            (['__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__'], []),
            "Results should be equal"
        )

    def test_diff_list_should_be_diff_at_6_position(self):
        result = diff("ff ff ff ff ff ff 11 00 00 00 00 00 90 00", "ff ff ff ff ff ff 00 00 00 00 00 00 90 00")
        self.assertEqual(
            result,
            (['__', '__', '__', '__', '__', '__', '11', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '00', '__', '__', '__', '__', '__', '__', '__'], [6]),
            "Results should be equal"
        )

    def test_diff_refactor(self):
        with self.assertRaises(NotImplementedError):
            diff("00 11", "00 11", "00 00")

        with self.assertRaises(NotImplementedError):
            diff("00 11")

    def test_get_hex(self):
        assert get_hex(self.ether) == "ff ff ff ff ff ff 00 00 00 00 00 00 90 00"

    def test_get_hex_uppercase(self):
        self.assertEqual(
            get_hex(self.ether, uppercase=True),
            "FF FF FF FF FF FF 00 00 00 00 00 00 90 00"
        )

    def test_show_diff(self):
        ether_wrong = "ff ff ff ff ff ff 00 00 00 00 aa 00 90 00"
        first_row, second_row, status = diff(self.ether, ether_wrong)

        self.assertEqual(first_row,
                         "__ __ __ __ __ __ __ __ __ __ 00 __ __ __".split())
        self.assertEqual(second_row,
                         "__ __ __ __ __ __ __ __ __ __ aa __ __ __".split())
        self.assertTrue(status)
        self.assertEqual(status, [10, ])

    def test_show_diff_for_same_elements(self):
        first_row, second_row, status = diff(self.ether, self.ether)

        self.assertEqual(first_row,
                         "__ __ __ __ __ __ __ __ __ __ __ __ __ __".split())
        self.assertEqual(second_row,
                         "__ __ __ __ __ __ __ __ __ __ __ __ __ __".split())
        self.assertFalse(status)

    def test_show_more_diff(self):
        show_diff(self.ether, "ff ff ff ff ff ff 00 00 00 00 00 00 90 00")

    def test_diff_should_return_3_elements(self):
        too_long_ether = get_hex(Ether() / "additional string")

        diff_tuple = diff(self.ether, too_long_ether)
        self.assertEqual(len(diff_tuple), 3, "_diff should return only a 3 elements")

    def test_diff_should_return_same_len_list_if_one_of_them_was_shorter(self):
        too_long_ether = get_hex(Ether() / "additional string")

        diff_tuple = diff(self.ether, too_long_ether)
        self.assertEqual(len(diff_tuple[0]), len(diff_tuple[1]), "List should be the same length")

        self.assertNotEqual(
            len(get_hex(self.ether).split()),
            len(diff_tuple[0])
        )
        self.assertEqual(
            len(too_long_ether.split()),
            len(diff_tuple[1])
        )

    def test_hex_equal(self):
        self.assertTrue(hex_equal(self.ether, "ff ff ff ff ff ff 00 00 00 00 00 00 90 00"))

    def test_hex_equal_with_show_diff_options(self):
        options = {
            "index": True
        }
        self.assertFalse(hex_equal(self.ether, "ff ff ff ff ff ff 0a 00 00 00 00 00 90 00",
                                   show_inequalities=False, **options))

    def test__prepare(self):
        obj = MagicMock()
        obj.hex = MagicMock(return_value="ff ff ff")
        self.assertEqual(_prepare(obj), ["ff", "ff", "ff"], "Object method hex, should return str of hex")

    def test__prepare_encoded(self):
        obj = "\x00\x01".encode()
        self.assertEqual(_prepare(obj), ["00", "01"], "Object method hex, should return str of hex")

    def test_chexdump_native_support(self):
        frame_chexdump = TestScapyHelper.old_method(self.ether)
        self.assertEqual(frame_chexdump, get_hex(self.ether))

    @staticmethod
    def old_method(frame):
        return ' '.join([x.replace("0x", "").replace(",", "") for x in chexdump(frame, dump=True).split()])
