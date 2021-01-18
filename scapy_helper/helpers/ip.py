import socket
import struct


def ip2int(ip_address):
    if not isinstance(ip_address, str):
        raise TypeError("Value %s is not a type of string" % ip_address)
    return struct.unpack("!I", socket.inet_aton(ip_address))[0]


def int2ip(integer):
    if type(integer).__name__ not in ("int", "long"):
        # hack: since in the python3, long is not supported
        raise TypeError("Value %s is not a number" % integer)
    return socket.inet_ntoa(struct.pack("!I", integer))
