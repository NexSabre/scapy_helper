from unittest import TestCase

from scapy_helper.helpers.ip import int2ip, ip2int


class TestIP(TestCase):
    def setUp(self):
        self.integer = 3232235521
        self.ip = "192.168.0.1"

    def test_ip2int(self):
        self.assertEqual(
            ip2int(self.ip),
            self.integer,
            "Values should be equal"
        )

    def test_int2ip(self):
        self.assertEqual(
            int2ip(self.integer),
            self.ip,
            "Values should be equal"
        )

    def test_int2ip_for_zero(self):
        self.assertEqual(
            int2ip(0), "0.0.0.0", "Values should be equal"
        )
