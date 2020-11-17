from scapy.utils import chexdump


def _diff(first, second):
    if not isinstance(first, str):
        first = get_hex(first)
    if isinstance(first, str):
        first = first.split()

    if not isinstance(second, str):
        second = get_hex(second)
    if isinstance(second, str):
        second = second.split()

    if len(first) != len(second):
        print("WARN:: Frame len is not the same")

    first_row = []
    second_row = []
    for e, _ in enumerate(first):
        if first[e] != second[e]:
            first_row.append(first[e])
            second_row.append(second[e])
            continue
        first_row.append("__")
        second_row.append("__")
    status = first_row == second_row
    return first_row, second_row, status


def get_hex(frame):
    return ' '.join([x.replace("0x", "").replace(",", "") for x in chexdump(frame, dump=True).split()])


def show_hex(frame):
    print(get_hex(frame))


def show_diff(first, second):
    first_row, second_row, status = _diff(first, second)

    print(' '.join(first_row))
    print(' '.join(second_row))
    if status:
        print("Ok")
    else:
        print("Not equal at {} point/s".format(len([x for x in first_row if x != "__"])))
