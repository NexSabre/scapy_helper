from scapy.utils import chexdump

from scapy_helper.helpers.depracated import deprecated


def _diff(first, second):
    first = _prepare(first)
    second = _prepare(second)

    _fill_empty_elements(first, second)

    first_row = []
    second_row = []
    for e, _ in enumerate(first):
        if first[e].lower() != second[e].lower():
            first_row.append(first[e])
            second_row.append(second[e])
            continue
        first_row.append("__")
        second_row.append("__")
    status = first_row == second_row
    return first_row, second_row, status


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
    if not isinstance(obj, str):
        obj = get_hex(obj)
    if isinstance(obj, str):
        obj = obj.split()
    return obj


def get_hex(frame):
    return ' '.join([x.replace("0x", "").replace(",", "") for x in chexdump(frame, dump=True).split()])


def show_hex(frame):
    print(get_hex(frame))


def show_diff(first, second, extend=False, empty_char="XX"):
    first_row, second_row, status = _diff(first, second)

    first_row_len_b = len([x for x in first_row if x != "  "])
    second_row_len_b = len([x for x in second_row if x != "  "])

    for e in range(len(first_row)):
        first_row[e] = first_row[e].replace("  ", empty_char)
        second_row[e] = second_row[e].replace("  ", empty_char)

    print(' '.join(first_row), "| len: %sB" % first_row_len_b)
    print(' '.join(second_row), "| len: %sB" % second_row_len_b)

    if extend:
        more_info = []
        for types in first.class_fieldtype.items():
            for el in types[1].items():
                more_info.append((el[0], el[1].sz))
        print(more_info)

    print()
    if status:
        print("Ok")
    elif len([x for x in first_row if x != "__"]) == len(first_row):
        print("Not equal")
    else:
        print("Not equal at {}B".format(len([x for x in first_row if x != "__"])))


def get_diff(first, second):
    _, _, status = _diff(first, second)
    return status


@deprecated
def table(first, second):
    f, s, status = _diff(first, second)
    show_diff(first, second)
    f_details = first.show(dump=True).split("\n")
    s_details = second.show(dump=True).split("\n")

    for r in range(len(f_details)):
        print("{} {:>40}".format(f_details[r], s_details[r]))

    return status
