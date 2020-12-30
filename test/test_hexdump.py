import unittest

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

from scapy_helper import get_hex
from scapy_helper.hexdump import hexdump

from scapy.utils import hexdump as scap_hexdump


class TestHexdump(unittest.TestCase):
    def setUp(self):
        self.packet = Ether(dst="ff:ff:ff:ff:ff:ff",
                            src="00:00:00:00:00:00") / IP()
        self.packet_hex = "ff ff ff ff ff ff 00 00 00 00 00 00 08 00 " \
                          "45 00 00 14 00 01 00 00 40 00 fb e8 00 00 " \
                          "00 00 7f 00 00 01"

    def test_hexdump_dump_from_string(self):
        expected_result = '0000ffffffffffff00000000000008004500..............E.' \
                          '00100014000100004000fbe8000000007f00......@.........' \
                          '00200001..'
        result = hexdump(self.packet_hex, dump=True).replace(" ", "").replace("\n", "")
        hexdump(self.packet_hex)
        self.assertEqual(expected_result, result, "String should be the same")

    def test_hexdump_dump_from_string_as_list(self):
        expected_result = ['0000ffffffffffff00000000000008004500..............E.',
                           '00100014000100004000fbe8000000007f00......@.........',
                           '00200001..']
        result = [x.replace(" ", "").replace("\n", "") for x in hexdump(self.packet_hex, dump=True, to_list=True)]

        expected_result = [x.lower() for x in expected_result]
        result = [x.lower() for x in result]

        self.assertIsInstance(result, list, "Dump should be a list")
        self.assertEqual(expected_result, result, "Dump of the hex should be the same")

    def test_hexdump_can_convert_string_on_input(self):
        string = "\x00\x01".encode()
        expected_result = "00000001.."
        result = hexdump(string, dump=True)

        self.assertEqual(result.replace(" ", ""), expected_result, "Dump of hex should be the same")

    def test_hexdump_dump_true(self):
        expected_result = scap_hexdump(self.packet, dump=True).replace(" ", "").replace("\n", "")
        result = hexdump(self.packet, dump=True).replace(" ", "").replace("\n", "")

        self.assertIsInstance(result, str, "Dump should be a string")
        self.assertEqual(expected_result.lower(), result.lower(), "Dump of the hex should be the same")

    def test_hexdump_dump_true_as_list(self):
        expected_result = scap_hexdump(self.packet, dump=True).replace(" ", "").split("\n")
        result = [x.replace(" ", "").replace("\n", "") for x in hexdump(self.packet, dump=True, to_list=True)]

        expected_result = [x.lower() for x in expected_result]
        result = [x.lower() for x in result]

        self.assertIsInstance(result, list, "Dump should be a list")
        self.assertEqual(expected_result, result, "Dump of the hex should be the same")
