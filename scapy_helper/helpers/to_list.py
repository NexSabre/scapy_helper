from scapy_helper.helpers.utils import _layer2dict


def to_list(packet, extend=False):
    return [_layer2dict(packet.getlayer(x)) for x in range(len(packet.layers()))]
