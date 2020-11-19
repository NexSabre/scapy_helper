import unittest

from scapy_helper.compare import Compare

from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.utils import hexstr


class TestCompare(unittest.TestCase):
    def setUp(self):
        self.ether = Ether() / IP(src='192.168.1.1', dst='192.168.1.20', ttl=15) / UDP()
        self.c_ether = Ether() / IP(src='192.168.1.2', dst='192.168.1.20', ttl=20) / UDP()

    def test_one(self):
        compare = Compare(self.ether, self.c_ether)
        compare.table_diff()
