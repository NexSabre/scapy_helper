from unittest import TestCase

from scapy.all import Ether

from scapy_helper.main import show_diff
from scapy_helper.test_case_extensions.assert_print import assert_print


class TestShowDiff(TestCase):
    def setUp(self):
        self.ether_1 = Ether()

    @assert_print(results=(
            "scapy | ff ff ff ff ff ff __ __ __ __ __ __ __ __ | len: 14B\n"
            "scapy | 00 11 00 00 00 00 __ __ __ __ __ __ __ __ | len: 14B\n"
            "\n"
            "Not equal at 6B's\n"
        ))
    def test_show_diff(self):
        ether_2 = Ether(dst="00:11:00:00:00:00")
        show_diff(self.ether_1, ether_2)

    def test_show_diff__w_additional_str(self):
        ether_2 = Ether(dst="00:11:00:00:00:00") / "additional str"
        show_diff(self.ether_1, ether_2)

    def test_show_diff_between_ether_obj_v_str(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(self.ether_1, ether_2)

    def test_show_diff_with_indexes(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(self.ether_1, ether_2, index=True)

    def test_show_diff_with_indexes_and_custom_empty_char(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(self.ether_1, ether_2, index=True, empty_char="++")

    def test_show_diff_with_indexes_and_custom_too_long_empty_char(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(
            self.ether_1,
            ether_2,
            index=True,
            empty_char="+Only Plus Char should be used",
        )

    def test_show_diff_with_indexes_and_custom_char_none(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(self.ether_1, ether_2, index=True, empty_char=None)

    def test_show_diff_with_indexes_proper_len_of_last_position(self):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00"
        show_diff(self.ether_1, ether_2, index=True, empty_char=None)
