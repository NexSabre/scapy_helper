from scapy_helper import hex_equal, show_diff
from scapy_helper.main import show_diff_full, diff, get_hex


def failure(first, second, message):
    raise AssertionError(get_hex(first), get_hex(second), message)


# noinspection PyPep8Naming
class PacketAssert:
    def __init__(self):
        pass

    @staticmethod
    def assertHexEqual(first, second, message=None):
        if not hex_equal(first, second, show_inequalities=False):
            show_diff_full(first, second)
            failure(first, second, message)

    @staticmethod
    def assertHexNotEqual(first, second, message=None):
        if hex_equal(first, second, show_inequalities=False):
            show_diff(first, second)
            failure(first, second, message)

    @staticmethod
    def assertHexLenEqual(first, second, message=None):
        len_first, len_second = len(get_hex(first)), len(get_hex(second))
        if len_first != len_second:
            show_diff(first, second)
            failure(first, second, message)

    @staticmethod
    def assertHexLenNotEqual(first, second, message=None):
        len_first, len_second = len(get_hex(first)), len(get_hex(second))
        if len_first == len_second:
            show_diff(first, second)
            failure(first, second, message)

    @staticmethod
    def assertBytesEqual(first, second, message=None):
        if not isinstance(first, bytes):
            first = bytes(first)
        if not isinstance(second, bytes):
            second = bytes(second)

        if first != second:
            failure(first, second, message)

    @staticmethod
    def assertBytesNotEqual(first, second, message=None):
        if not isinstance(first, bytes):
            first = bytes(first)
        if not isinstance(second, bytes):
            second = bytes(second)

        if first == second:
            failure(first, second, message)

    @staticmethod
    def assertHexDifferentAt(first, second, positions, message):
        _, _, differences_at_position = diff(first, second)
        if len(differences_at_position) == 0:
            print("Hexs are equal")
            failure(first, second, message)

        if isinstance(positions, int):
            if len(differences_at_position) != 1 or (positions not in differences_at_position):
                show_diff(first, second, index=True)
                failure(first, second, message)
        elif isinstance(positions, (list, tuple)):
            if not set(positions).issubset(set(differences_at_position)) or set(positions) < set(
                    differences_at_position):
                show_diff(first, second, index=True)
                failure(first, second, message)
