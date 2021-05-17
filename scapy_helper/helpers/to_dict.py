from scapy_helper.helpers.utils import _layer2dict


def to_dict(packet, layer=0, extend=False):
    return _layer2dict(packet.getlayer(layer))
