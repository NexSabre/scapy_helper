from unittest import TestCase

from scapy.layers.l2 import Ether
from scapy_helper.main import show_diff


class TestShowDiff(TestCase):
    def test_show_diff(self):
        ether_1 = Ether()
        ether_2 = Ether(dst="00:11:00:00:00:00")

        show_diff(ether_1, ether_2)

    def test_show_diff__w_additional_str(self):
        ether_1 = Ether()
        ether_2 = Ether(dst="00:11:00:00:00:00") / "additional str"

        show_diff(ether_1, ether_2)

    def test_show_diff_between_ether_obj_v_str(self):
        ether_1 = Ether(src="00:00:00:00:00:00")
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"

        show_diff(ether_1, ether_2)

    def test_show_diff_with_indexes(self):
        ether_1 = Ether(src="00:00:00:00:00:00")
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"

        show_diff(ether_1, ether_2, index=True)

    def test_show_diff_with_indexes_and_custom_empty_char(self):
        ether_1 = Ether(src="00:00:00:00:00:00")
        ether_2 = "ff ff fc ff ff fa 00 11 11 11 11 11 90 00 11 11 00 22"

        show_diff(ether_1, ether_2, index=True, empty_char="++")
