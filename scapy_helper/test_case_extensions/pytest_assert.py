from scapy_helper import PacketAssert


def assert_hex_equal(first, second, message="Hex values are not equal"):
    PacketAssert.assertHexEqual(first, second, message)


def assert_hex_not_equal(first, second, message="Hex values are equal"):
    PacketAssert.assertHexNotEqual(first, second, message)


def assert_hex_len_equal(first, second, message="Hex len is equal"):
    PacketAssert.assertHexLenEqual(first, second, message)


def assert_hex_len_not_equal(first, second, message="Hex len is not equal"):
    PacketAssert.assertHexLenNotEqual(first, second, message)


def assert_bytes_equal(first, second, message="Bytes values are not equal"):
    PacketAssert.assertBytesEqual(first, second, message)


def assert_bytes_not_equal(first, second, message="Bytes values are eqaul"):
    PacketAssert.assertBytesNotEqual(first, second, message)
