from scapy_helper.main import _prepare


def chexdump(packet, dump=False, to_list=False):
    """
    Return a chexdump base on packet
    :param packet: String or Scapy object
    :param dump: True if you want to dump instead of print
    :param to_list: True if you want a list of hex instead of a string
    :return: None or Str or List
    """
    def _add_0x_before(p):
        return ["0x%s" % x for x in p]

    processed_packet = _prepare(packet)
    if not processed_packet:
        return

    if dump:
        if to_list:
            return _add_0x_before(processed_packet)
        else:
            return ", ".join(_add_0x_before(processed_packet))
    print(", ".join(_add_0x_before(processed_packet)))


