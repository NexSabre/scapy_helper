import unittest

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

from scapy_helper.hexdump import hexdump


class TestHexdump(unittest.TestCase):
    def setUp(self):
        self.packet = Ether(dst="ff:ff:ff:ff:ff:ff",
                            src="00:00:00:00:00:00") / IP()

    def test_hexdump_dump_true(self):
        expected_result = "0000ffffffffffff00000000000008004500..............E." \
                          "00100014000100004000fbe8000000007f00......@........." \
                          "00200001.."
        result = hexdump(self.packet, dump=True).replace(" ", "").replace("\n", "")

        self.assertIsInstance(result, str, "Dump should be a string")
        self.assertEqual(expected_result, result, "Dump of the hex should be the same")

    def test_hexdump_dump_true_as_list(self):
        expected_result = ['0000ffffffffffff00000000000008004500..............E.',
                           '00100014000100004000fbe8000000007f00......@.........',
                           '00200001..']
        result = [x.replace(" ", "").replace("\n", "") for x in hexdump(self.packet, dump=True, to_list=True)]

        self.assertIsInstance(result, list, "Dump should be a list")
        self.assertEqual(expected_result, result, "Dump of the hex should be the same")
