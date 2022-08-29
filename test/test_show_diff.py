import pytest
from scapy.all import Ether, Packet

from scapy_helper.main import show_diff


class TestShowDiff:
    def test_show_diff(self, ether: Packet):
        ether_2 = Ether(dst="00:11:00:00:00:00")
        show_diff(ether, ether_2)

    def test_show_diff__w_additional_str(self, ether: Packet):
        ether_2 = Ether(dst="00:11:00:00:00:00") / "additional str"
        show_diff(ether, ether_2)

    def test_show_diff_between_ether_obj_v_str(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(ether, ether_2)

    def test_show_diff_with_indexes(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(ether, ether_2, index=True)

    def test_show_diff_with_indexes_and_custom_empty_char(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(ether, ether_2, index=True, empty_char="++")

    def test_show_diff_with_indexes_and_custom_too_long_empty_char(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(
            ether,
            ether_2,
            index=True,
            empty_char="+Only Plus Char should be used",
        )

    def test_show_diff_with_indexes_and_custom_char_none(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"
        show_diff(ether, ether_2, index=True, empty_char=None)

    def test_show_diff_with_indexes_proper_len_of_last_position(self, ether: Packet):
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00"
        show_diff(ether, ether_2, index=True, empty_char=None)
