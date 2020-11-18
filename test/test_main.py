from unittest import TestCase

from scapy.layers.l2 import Ether

from scapy_helper.main import get_hex, _diff


class Test_Scapy_Helper(TestCase):
    def setUp(self) -> None:
        self.ether = Ether()

    def test_get_hex(self):
        assert get_hex(self.ether) == "ff ff ff ff ff ff e0 d5 5e e6 6c 8e 90 00"

    def test_show_diff(self):
        ether_wrong = "ff ff fc ff ff fa e0 d5 5e e6 6c 8e 90 00"
        first_row, second_row, status = _diff(self.ether, ether_wrong)
        assert first_row == ['__', '__', 'ff', '__', '__', 'ff', '__', '__', '__', '__', '__', '__', '__', '__']
        assert second_row == ['__', '__', 'fc', '__', '__', 'fa', '__', '__', '__', '__', '__', '__', '__', '__']
        assert not status
