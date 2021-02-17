import sys

from scapy_helper.helpers.depracated import deprecated


def diff(*args, **kwargs):
    """
    Return a diff between two hex list
    :param args:
    :param kwargs:
    :return:
    """
    skip_if_same = True
    if kwargs.get("skip_if_same", False):
        skip_if_same = kwargs["skip_if_same"]
    if len(args) != 2:
        raise NotImplementedError("Only comparison of the two list are supported")

    result_list = ([], [])
    diff_indexes = []
    diff_list = []

    for a in args:
        diff_list.append(_prepare(a))
    _fill_empty_elements(*diff_list)

    for e, _ in enumerate(diff_list[0]):
        if diff_list[0][e].lower() != diff_list[1][e].lower():
            for i in range(2):
                result_list[i].append(diff_list[i][e])
            diff_indexes.append(e)
            continue
        if skip_if_same:
            for i in range(2):
                result_list[i].append("__")
        else:
            for i in range(2):
                result_list[i].append(diff_list[i][e])
    return result_list[0], result_list[1], diff_indexes


def _fill_empty_elements(first, second):
    if len(first) != len(second):
        print("WARN:: Frame len is not the same")

        len_first = len(first)
        len_second = len(second)
        if len_first > len_second:
            print("WARN:: First row is longer by the %sB\n" % (len_first - len_second))
            for x in range(len_first - len_second):
                second.append("  ")
        else:
            print("WARN:: Second row is longer by the %sB\n" % (len_second - len_first))
            for x in range(len_second - len_first):
                first.append("  ")


def _prepare(obj):
    def isbytesarray():
        b = obj.split()
        if len(b) == 1:
            return get_hex(obj).split()
        return b
    import sys
    if sys.version_info > (3, 5):
        # TODO very naive hack, but should be ok as temporary fix
        if isinstance(obj, bytes):
            return isbytesarray()
    if hasattr(obj, "hex"):
        return obj.hex().split()
    if not isinstance(obj, str):
        obj = get_hex(obj)
    if isinstance(obj, str):
        obj = isbytesarray()
    return obj


def get_hex(frame, uppercase=False):
    """
    Return a string object of Hex representation of the Scapy's framework
    :param frame: Scapy's Packet Object
    :param uppercase: bool: If True letters be UPPERCASE
    :return: str: Hex   
    """
    if sys.version_info.major == 2:
        import binascii
        str_hex = binascii.b2a_hex(bytes(frame))
    else:
        try:
            str_hex = bytes(frame).hex()
        except TypeError:
            str_hex = bytes(frame, encoding="utf-8").hex()
    j = []
    for e, i in enumerate(str_hex):
        if e % 2:
            j.append(str_hex[e - 1] + str_hex[e])
    if uppercase:
        return ' '.join(j).upper()
    return ' '.join(j).lower()


def show_hex(frame, uppercase=False):
    """Print a hex representation of the Scapy's object"""
    print(get_hex(frame, uppercase=uppercase))


def _create_diff_indexes_list(indexes, max_len):
    new_list = []

    for idx in range(max_len):
        if idx not in indexes:
            new_list.append("..")
            continue

        if idx < 10:
            new_list.append(str("^%s" % idx))
            continue
        new_list.append(str(idx))
    else:
        new_list.append("| position")

    return ' '.join(new_list)


def __process_char(char):
    multiplier = 2
    if not char or not isinstance(char, str):
        return "X" * multiplier
    return char[0] * multiplier


def show_diff(first, second, index=False, extend=False, empty_char="XX"):
    first_row, second_row, indexes_of_diff = diff(first, second)
    first_row_len_bytes = count_bytes(first_row)
    second_row_len_bytes = count_bytes(second_row)

    empty_char = __process_char(empty_char)

    for row in (first_row, second_row):
        for idx, element in enumerate(row):
            if element == "  ":
                row[idx] = empty_char

    print("%s | len: %sB" % (' '.join(first_row), first_row_len_bytes))
    print("%s | len: %sB" % (' '.join(second_row), second_row_len_bytes))
    if index and indexes_of_diff:
        str_bar = "   " * first_row_len_bytes if first_row_len_bytes > second_row_len_bytes else \
            "   " * second_row_len_bytes
        print("%s|\n%s" % (str_bar, _create_diff_indexes_list(indexes_of_diff, max((first_row_len_bytes,
                                                                                    second_row_len_bytes)))))

    if extend:
        more_info = []
        for types in first.class_fieldtype.items():
            for el in types[1].items():
                more_info.append((el[0], el[1].sz))
        print(more_info)

    print("")
    if indexes_of_diff:
        print("Not equal at {}B's".format(len([x for x in first_row if x != "__"])))
        return True
    elif len([x for x in first_row if x != "__"]) == len(first_row):
        print("Not equal")
        return True
    print("Ok")
    return False


def show_diff_full(first, second, index=True, extend=False, empty_char="XX"):
    first_row, second_row, indexes_of_diff = diff(first, second, skip_if_same=False)
    first_row_len_bytes = count_bytes(first_row)
    second_row_len_bytes = count_bytes(second_row)

    empty_char = __process_char(empty_char)

    for row in (first_row, second_row):
        for idx, element in enumerate(row):
            if element == "  ":
                row[idx] = empty_char

    print("%s | len: %sB" % (' '.join(first_row), first_row_len_bytes))
    print("%s | len: %sB" % (' '.join(second_row), second_row_len_bytes))
    if index and indexes_of_diff:
        str_bar = "   " * first_row_len_bytes if first_row_len_bytes > second_row_len_bytes else \
            "   " * second_row_len_bytes
        print("%s|\n%s" % (str_bar, _create_diff_indexes_list(indexes_of_diff, max((first_row_len_bytes,
                                                                                    second_row_len_bytes)))))

    if extend:
        more_info = []
        for types in first.class_fieldtype.items():
            for el in types[1].items():
                more_info.append((el[0], el[1].sz))
        print(more_info)

    print("")
    if indexes_of_diff:
        print("Not equal at {}B's".format(len([x for x in first_row if x != "__"])))
        return True
    elif len([x for x in first_row if x != "__"]) == len(first_row):
        print("Not equal")
        return True
    print("Ok")
    return False


def count_bytes(packet_hex_list):
    return len([x for x in packet_hex_list if x != "  "])


def hex_equal(first, second, show_inequalities=True, **kwargs):
    """
    Compare a two hex or hex-able Scapy objects. Return a True if objects are equal
    :param first: str hex or Scapy object
    :param second: str hex or Scapy object
    :param show_inequalities: Print difference if elements are not equal
    :param kwargs: Params for show diff
    :return: bool
    """
    _, _, status = diff(first, second)
    if show_inequalities and status:
        show_diff(first, second, **kwargs)
    # diff returns a list of position on which the object is different
    # if status is a empty Tuple, there's no difference between objects
    if status:
        return False
    return True


def get_diff(first, second):
    """This function is the wrapper for the diff. For backward compatibility"""
    return diff(first, second)


def get_diff_status(first, second):
    _, _, status = diff(first, second)
    return status


@deprecated
def table(first, second):
    f, s, status = diff(first, second)
    show_diff(first, second)
    f_details = first.show(dump=True).split("\n")
    s_details = second.show(dump=True).split("\n")

    for r in range(len(f_details)):
        print("{} {:>40}".format(f_details[r], s_details[r]))

    return status
