from scapy_helper import hex_equal, show_diff
from scapy_helper.main import show_diff_full, diff

failure = AssertionError


class PacketAssert:
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

    @staticmethod
    def assertBytesEqaul(first, second, message=None):
        if not isinstance(first, bytes):
            first = bytes(first)
        if not isinstance(second, bytes):
            second = bytes(second)

        if first != second:
            raise failure(first, second, message)

    @staticmethod
    def assertBytesNotEqaul(first, second, message=None):
        if not isinstance(first, bytes):
            first = bytes(first)
        if not isinstance(second, bytes):
            second = bytes(second)

        if first == second:
            raise failure(first, second, message)

    @staticmethod
    def assertHexDifferentAt(first, second, positions, message):
        _, _, differences_at_position = diff(first, second)
        if isinstance(positions, int):
            if positions not in differences_at_position:
                show_diff(first, second)
                raise failure(first, second, message)
        elif isinstance(positions, (list, tuple)):
            if not set(positions).issubset(set(differences_at_position)):
                show_diff(first, second)
                raise failure(first, second, message)
