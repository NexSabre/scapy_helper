from scapy_helper import hex_equal, show_diff
from scapy_helper.main import show_diff_full

failure = AssertionError


class HexEqual:
    @staticmethod
    def assertHexEqual(first, second, message=None):
        if not hex_equal(first, second, show_inequalities=False):
            show_diff_full(first, second)
            raise failure(first, second, message)

    @staticmethod
    def assertHexNotEqual(first, second, message=None):
        if hex_equal(first, second, show_inequalities=False):
            show_diff(first, second)
            raise failure(first, second, message)
