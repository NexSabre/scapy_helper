import pytest
from scapy.all import Ether, Packet  # type: ignore


@pytest.fixture
def default_ether() -> Packet:
    return Ether()


@pytest.fixture
def ether() -> Packet:
    return Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00")
