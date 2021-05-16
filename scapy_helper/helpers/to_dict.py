_native_value = (int, float, str, bytes, bool, list, tuple, set, dict, type(None))


def _layer2dict(obj):
    d = {}

    if not getattr(obj, 'fields_desc', None):
        return
    for f in obj.fields_desc:
        value = getattr(obj, f.name)
        if value is type(None):
            value = None

        if not isinstance(value, _native_value):
            value = _layer2dict(value)
        d[f.name] = value
    return {obj.name: d}


def to_dict(packet, extend=False):
    packet.show2()

    for x in range(len(packet.layers())):
        print()


def to_list(packet, extend=False):
    return [_layer2dict(packet.getlayer(x)) for x in range(len(packet.layers()))]
