import pytest
from scapy.all import Ether, Packet


@pytest.fixture
def ether() -> Packet:
    return Ether()
