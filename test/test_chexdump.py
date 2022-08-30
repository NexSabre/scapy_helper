from scapy.all import Ether, Packet  # type: ignore

from scapy_helper.chexdump import chexdump


class TestCHexdump:
    def test_chexdump(self) -> None:
        # TODO Add a verification of the output
        packet = "\x00\x01".encode()
        chexdump(packet)

    def test_chexdump_dump_true(self, ether: Packet) -> None:
        expected_result = "0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x90, 0x00"
        result = chexdump(ether, dump=True)

        assert isinstance(result, str), "Dump should be a string"
        assert expected_result == result, "Dump of the hex should be the same"

    def test_chexdump_dump_true_as_list(self, ether: Packet) -> None:
        expected_result = [
            "0xff",
            "0xff",
            "0xff",
            "0xff",
            "0xff",
            "0xff",
            "0x00",
            "0x00",
            "0x00",
            "0x00",
            "0x00",
            "0x00",
            "0x90",
            "0x00",
        ]
        result = chexdump(ether, dump=True, to_list=True)

        assert isinstance(result, list), "Dump should be a string"
        assert result == expected_result, "Dump of the hex should be the same"
