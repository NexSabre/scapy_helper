import unittest

from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

from scapy_helper.compare import Compare


class TestCompare(unittest.TestCase):
    def setUp(self):
        self.ether = Ether(dst="ff:ff:ff:ff:ff:ff",
                           src="00:00:00:00:00:00") / IP(src='192.168.1.1',
                                                         dst='192.168.1.20', ttl=15) / UDP()
        self.c_ether = Ether(dst="ff:ff:ff:ff:ff:ff",
                             src="00:00:00:00:00:00") / IP(src='192.168.1.2',
                                                           dst='192.168.1.20', ttl=20) / UDP()

        self.compare = Compare(self.ether, self.c_ether)

    def test_table_diff(self):
        self.compare.table_diff()

    def test_hex(self):
        self.assertEqual(self.compare.hex(),
                         (('ff ff ff ff ff ff 00 00 00 00 00 00 08 00 45 00 00 1c 00 01 00 00 0f 11'
                           ' 28 6b c0 a8 01 01 c0 a8 01 14 00 35 00 35 00 08 7c 0e',
                           'ff ff ff ff ff ff 00 00 00 00 00 00 08 00 45 00 00 1c 00 01 00 00 14 11'
                           ' 23 6a c0 a8 01 02 c0 a8 01 14 00 35 00 35 00 08 7c 0d')))

    def test_diff(self):
        self.assertTrue(self.compare.diff(), "diff() should return a difference")

    def test_equal(self):
        self.assertFalse(self.compare.equal(), "equal() should return false")
