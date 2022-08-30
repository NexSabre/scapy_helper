import pytest

from scapy_helper.helpers.ip import int2ip, ip2int

INTEGER = 3232235521
IP = "192.168.0.1"


@pytest.mark.parametrize("value, expected", ((IP, INTEGER), ("0.0.0.0", 0)))
def test_ip2int(value: str, expected: int) -> None:
    assert ip2int(value) == expected, "Values should be equal"


@pytest.mark.parametrize("value, expected_string_ip", ((INTEGER, IP), (0, "0.0.0.0")))
def test_int2ip(value: int, expected_string_ip: str) -> None:
    assert int2ip(value) == expected_string_ip, "Values should be equal"
