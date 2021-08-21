from unittest import TestCase

from scapy_helper.test_case_extensions.pytest_assert import (
    assert_hex_equal,
    assert_hex_len_equal,
    assert_hex_len_not_equal,
    assert_hex_not_equal,
)

DEFAULT_HEX = (
    "ff ff ff ff ff ff 00 00 00 00 00 00 08 00 45 00 00 "
    "28 00 01 00 00 40 06 7c cd 7f 00 00 01 7f 00 00 01 "
    "00 14 00 50 00 00 00 00 00 00 00 00 50 02 20 00 91 "
    "7c 00 00"
)
DIFFERENT_HEX = (
    "00 00 00 00 00 00 00 00 00 00 00 00 08 00 45 00 "
    "00 28 00 01 00 00 40 06 7c cd 7f 00 00 01 7f 00 "
    "00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02 "
    "20 00 91 7c 00 00"
)


class TestPytestAssert(TestCase):
    def test_assert_hex_equal(self):
        assert_hex_equal(DEFAULT_HEX, DEFAULT_HEX)

        with self.assertRaises(AssertionError):
            assert_hex_equal(DEFAULT_HEX, DIFFERENT_HEX)

    def test_assert_hex_not_equal(self):
        assert_hex_not_equal(DEFAULT_HEX, DIFFERENT_HEX)

        with self.assertRaises(AssertionError):
            assert_hex_not_equal(DEFAULT_HEX, DEFAULT_HEX)

    def test_assert_hex_len_equal(self):
        assert_hex_len_equal(DEFAULT_HEX, DEFAULT_HEX)

        with self.assertRaises(AssertionError):
            assert_hex_len_equal(DEFAULT_HEX, DEFAULT_HEX[: len(DEFAULT_HEX) - 2])

    def test_assert_hex_len_not_equal(self):
        assert_hex_len_not_equal(DEFAULT_HEX, DEFAULT_HEX[: len(DEFAULT_HEX) - 2])

        with self.assertRaises(AssertionError):
            assert_hex_len_not_equal(DEFAULT_HEX, DEFAULT_HEX)

    # def test_assert_bytes_equal(self):
    #     self.fail()
    #
    # def test_assert_bytes_not_equal(self):
    #     self.fail()
