__values = (int, float, str, bytes, bool,
            list, tuple, set,
            dict)


def _layer2dict(obj):
    temp_dict = {}

    if not getattr(obj, 'fields_desc', None):
        return
    for _field in obj.fields_desc:
        value = getattr(obj, _field.name)
        if isinstance(value, type(None)):
            value = None
        elif not isinstance(value, __values):
            value = _layer2dict(value)
        temp_dict[_field.name] = value
    return {obj.name: temp_dict}


def to_dict(packet, layer=0, extend=False):
    return _layer2dict(packet.getlayer(layer))


def to_list(packet, extend=False):
    return [_layer2dict(packet.getlayer(x)) for x in range(len(packet.layers()))]
