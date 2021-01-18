import re


def int2mac(integer, upper=False):
    """
    Convert a integer value into a mac address
    :param integer: Integer value of potential mac address
    :param upper: True if you want get address with uppercase
    :return: String mac address in format AA:BB:CC:DD:EE:FF
    """
    def format_int():
        return zip(*[iter('{:012x}'.format(integer))] * 2)

    if type(integer).__name__ not in ("int", "long"):
        # hack: since in the python3, long is not supported
        raise TypeError("Value %s is not a number" % integer)

    mac = ':'.join(['{}{}'.format(a, b)
                    for a, b in format_int()])
    if upper:
        return mac.upper()
    return mac


def mac2int(string):
    """
    Convert a mac address in string format into int value
    :param string: Should be a string if format
    "00:11:22:33:44:55:66"
    :return: Integer value of mac address
    """
    if not isinstance(string, str):
        raise TypeError("Value %s is not a type of string" % string)

    potential_mac = re.match('^((?:(?:[0-9a-f]{2}):){5}[0-9a-f]{2})$',
                             string.lower())
    if not potential_mac:
        raise ValueError("Invalid mac address %s" % string)

    return int(potential_mac
               .group()
               .replace(":", "")
               .replace(".", ""), 16)
