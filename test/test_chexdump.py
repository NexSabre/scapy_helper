import unittest

from scapy.layers.l2 import Ether

from scapy_helper.chexdump import chexdump


class TestcHexdump(unittest.TestCase):
    def setUp(self):
        self.packet = Ether(dst="ff:ff:ff:ff:ff:ff",
                            src="00:00:00:00:00:00")

    def test_chexdump(self):
        # TODO Add a verification of the output
        packet = "\x00\x01".encode()
        chexdump(packet)

    def test_chexdump_dump_true(self):
        expected_result = '0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x90, 0x00'
        result = chexdump(self.packet, dump=True)

        self.assertIsInstance(result, str, "Dump should be a string")
        self.assertEqual(expected_result, result, "Dump of the hex should be the same")

    def test_chexdump_dump_true_as_list(self):
        expected_result = ['0xff', '0xff', '0xff', '0xff', '0xff', '0xff',
                           '0x00', '0x00', '0x00', '0x00', '0x00', '0x00',
                           '0x90', '0x00']
        result = chexdump(self.packet, dump=True, to_list=True)

        self.assertIsInstance(result, list, "Dump should be a string")
        self.assertEqual(result, expected_result, "Dump of the hex should be the same")
