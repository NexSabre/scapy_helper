from test._utils import normalize

import pytest
from scapy.all import IP, Ether, Packet  # type: ignore
from scapy.utils import hexdump as scapy_hexdump  # type: ignore

from scapy_helper.hexdump import hexdump

packet_hex = (
    "ff ff ff ff ff ff 00 00 00 00 00 00 08 00 "
    "45 00 00 14 00 01 00 00 40 00 fb e8 00 00 "
    "00 00 7f 00 00 01"
)


@pytest.fixture
def ether_ip() -> Packet:
    # FIXME: Provide non-default values
    return Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP()


class TestHexdump:
    def test_hexdump_dump_from_string(self):
        expected_result = (
            "0000ffffffffffff00000000000008004500..............E."
            "00100014000100004000fbe8000000007f00......@........."
            "00200001.."
        )
        result = normalize(hexdump(packet_hex, dump=True))
        hexdump(packet_hex)
        assert expected_result == result, "String should be the same"

    def test_hexdump_dump_from_string_as_list(self):
        expected_result = [
            "0000ffffffffffff00000000000008004500..............E.",
            "00100014000100004000fbe8000000007f00......@.........",
            "00200001..",
        ]
        result = [normalize(x) for x in hexdump(packet_hex, dump=True, to_list=True)]

        expected_result = [x.lower() for x in expected_result]
        result = [x.lower() for x in result]

        assert isinstance(result, list), "Dump should be a list"
        assert expected_result == result, "Dump of the hex should be the same"

    def test_hexdump_can_convert_string_on_input(self):
        string = "\x00\x01".encode()
        expected_result = "00000001.."

        result = hexdump(string, dump=True).replace(" ", "")
        assert result == expected_result, "Dump of hex should be the same"

    def test_hexdump_dump_true(self, ether_ip: Packet):
        expected_result = normalize(scapy_hexdump(ether_ip, dump=True))
        result = normalize(hexdump(ether_ip, dump=True))

        assert isinstance(result, str), "Dump should be a string"
        assert (
            expected_result.lower() == result.lower()
        ), "Dump of the hex should be the same"

    def test_hexdump_dump_true_as_list(self, ether_ip: Packet):
        expected_result = scapy_hexdump(ether_ip, dump=True).replace(" ", "").split("\n")
        result = [normalize(x) for x in hexdump(ether_ip, dump=True, to_list=True)]

        expected_result = [x.lower() for x in expected_result]
        result = [x.lower() for x in result]

        assert isinstance(result, list), "Dump should be a list"
        assert expected_result == result, "Dump of the hex should be the same"
