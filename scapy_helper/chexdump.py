from typing import Any, List, Optional, Union

from scapy_helper.main import _prepare


def chexdump(
    packet: Any, dump: bool = False, to_list: bool = False
) -> Optional[Union[List[str], str]]:
    """
    Return a chexdump base on packet
    :param packet: String or Scapy object
    :param dump: True if you want to dump instead of print
    :param to_list: True if you want a list of hex instead of a string
    :return: None or Str or List
    """

    def _add_0x_before(p: List[str]) -> List[str]:
        return ["0x%s" % x for x in p]

    processed_packet = _prepare(packet)
    if not processed_packet:
        return None

    if dump:
        if to_list:
            return _add_0x_before(processed_packet)
        else:
            return ", ".join(_add_0x_before(processed_packet))
    print(", ".join(_add_0x_before(processed_packet)))
    return None
