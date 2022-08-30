import pytest
from scapy.all import Ether, Packet  # type: ignore


@pytest.fixture
def ether() -> Packet:
    return Ether()
