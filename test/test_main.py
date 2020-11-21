from unittest import TestCase

from scapy.layers.l2 import Ether

from scapy_helper import get_hex, show_hex, show_diff
from scapy_helper.main import _diff


class Test_Scapy_Helper(TestCase):
    def setUp(self) -> None:
        self.ether = Ether()

    def test_get_hex(self):
        assert get_hex(self.ether) == "ff ff ff ff ff ff e0 d5 5e e6 6c 8e 90 00"

    def test_show_diff(self):
        ether_wrong = "ff ff fc ff ff fa e0 d5 5e e6 6c 8e 90 00"
        first_row, second_row, status = _diff(self.ether, ether_wrong)
        self.assertEqual(first_row,
                         ['__', '__', 'ff', '__', '__', 'ff', '__', '__', '__', '__', '__', '__', '__', '__'])
        self.assertEqual(second_row,
                         ['__', '__', 'fc', '__', '__', 'fa', '__', '__', '__', '__', '__', '__', '__', '__'])
        self.assertIsNotNone(status)

    def test_show_more_diff(self):
        show_diff(self.ether, "ff ff ff ff ff ff e0 d5 5e e6 6c 8e 90 00")

    def test_diff_packets_are_same_len(self):
        too_long_ether = get_hex(Ether() / "additional string")

        _diff(self.ether, too_long_ether)

    def test_diff_should_return_same_len_list_if_one_of_them_was_shorter(self):
        too_long_ether = get_hex(Ether() / "additional string")

        diff_tuple = _diff(self.ether, too_long_ether)
        self.assertEqual(len(diff_tuple), 3, "_diff should return only a 3 elements")
        self.assertEqual(len(diff_tuple[0]), len(diff_tuple[1]), "List should be the same length")

        self.assertNotEqual(
            len(get_hex(self.ether).split()),
            len(diff_tuple[0])
        )
        self.assertEqual(
            len(too_long_ether.split()),
            len(diff_tuple[1])
        )
