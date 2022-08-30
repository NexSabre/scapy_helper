import pytest
from mock import MagicMock
from scapy.all import Ether, Packet, chexdump  # type: ignore

from scapy_helper import get_hex, show_diff
from scapy_helper.main import _prepare, diff, get_diff, hex_equal


def remove_byte_char(frame) -> str:
    return " ".join(
        [
            x.replace("0x", "").replace(",", "")
            for x in chexdump(frame, dump=True).split()
        ]
    )


# FIXME change the name of fixtures
class TestScapyHelper:
    def test_get_diff_should_be_the_same_as_diff(self, ether: Packet):
        ether_2 = Ether(dst="00:00:00:00:00:00", src="00:00:00:00:00:00")
        fun_diff = diff(ether, ether_2)
        fun_get_diff = get_diff(ether, ether_2)
        assert (
            fun_diff == fun_get_diff
        ), "The result of get_diff and diff should be the same"

    def test_diff_list_equal(self):
        result = diff(
            "ff ff ff ff ff ff 00 00 00 00 00 00 90 00",
            "ff ff ff ff ff ff 00 00 00 00 00 00 90 00",
        )
        assert result == (
            [
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
            ],
            [
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
            ],
            [],
        ), "Results should be equal"

    def test_diff_list_should_be_diff_at_6_position(self):
        result = diff(
            "ff ff ff ff ff ff 11 00 00 00 00 00 90 00",
            "ff ff ff ff ff ff 00 00 00 00 00 00 90 00",
        )
        assert result == (
            [
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "11",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
            ],
            [
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "00",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
                "__",
            ],
            [6],
        ), "Results should be equal"

    @pytest.mark.parametrize("value", (("00 11", "00 11", "00 00"), ("00 11",)))
    def test_diff_refactor(self, value):
        with pytest.raises(NotImplementedError):
            diff(*value)

    def test_get_hex(self, ether: Packet):
        assert get_hex(ether) == "ff ff ff ff ff ff 00 00 00 00 00 00 90 00"

    def test_get_hex_uppercase(self, ether: Packet):
        assert (
            get_hex(ether, uppercase=True)
            == "FF FF FF FF FF FF 00 00 00 00 00 00 90 00"
        )

    def test_show_diff(self, ether: Packet):
        ether_wrong = "ff ff ff ff ff ff 00 00 00 00 aa 00 90 00"
        first_row, second_row, status = diff(ether, ether_wrong)

        assert first_row == "__ __ __ __ __ __ __ __ __ __ 00 __ __ __".split()
        assert second_row == "__ __ __ __ __ __ __ __ __ __ aa __ __ __".split()
        assert status
        assert status == [
            10,
        ]

    def test_show_diff_for_same_elements(self, ether: Packet):
        first_row, second_row, status = diff(ether, ether)

        assert first_row == "__ __ __ __ __ __ __ __ __ __ __ __ __ __".split()
        assert second_row == "__ __ __ __ __ __ __ __ __ __ __ __ __ __".split()
        assert not status

    def test_show_more_diff(self, ether: Packet):
        show_diff(ether, "ff ff ff ff ff ff 00 00 00 00 00 00 90 00")

    def test_diff_should_return_3_elements(self, ether: Packet):
        too_long_ether = get_hex(Ether() / "additional string")

        diff_tuple = diff(ether, too_long_ether)
        assert len(diff_tuple) == 3, "_diff should return only a 3 elements"

    def test_diff_should_return_same_len_list_if_one_of_them_was_shorter(
        self, ether: Packet
    ):
        too_long_ether = get_hex(Ether() / "additional string")

        diff_tuple = diff(ether, too_long_ether)
        assert len(diff_tuple[0]) == len(
            diff_tuple[1]
        ), "List should be the same length"

        assert len(get_hex(ether).split()) != len(diff_tuple[0])
        assert len(too_long_ether.split()) == len(diff_tuple[1])

    def test_hex_equal(self, ether: Packet):
        assert hex_equal(ether, "ff ff ff ff ff ff 00 00 00 00 00 00 90 00")

    def test_hex_equal_with_show_diff_options(self, ether: Packet):
        options = {"index": True}
        assert not hex_equal(
            ether,
            "ff ff ff ff ff ff 0a 00 00 00 00 00 90 00",
            show_inequalities=False,
            **options,
        )

    def test__prepare(self):
        obj = MagicMock()
        obj.hex = MagicMock(return_value="ff ff ff")
        assert _prepare(obj) == [
            "ff",
            "ff",
            "ff",
        ], "Object method hex, should return str of hex"

    def test__prepare_encoded(self):
        obj = "\x00\x01".encode()
        assert _prepare(obj) == [
            "00",
            "01",
        ], "Object method hex, should return str of hex"

    def test_chexdump_native_support(self, ether: Packet):
        frame_chexdump = remove_byte_char(ether)
        assert frame_chexdump == get_hex(ether)
