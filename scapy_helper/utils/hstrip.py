from os import getenv

try:
    import pyperclip
except ImportError:
    print("Missing pyperclip: pip install pyperclip")

HEXDUMP_VALUE = """
0000  FF FF FF FF FF FF 00 00 00 00 00 00 08 00 45 00  ..............E.
0010  00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00  .(....@.|.......
0020  00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02  .....P........P.
0030  20 00 91 7C 00 00                                 ..|..
"""


def hstrip(raw=True, hexdump=None):
    """
    Clean a Scapies hexdump into more friendly "oneliner"
    :param raw: If False, return oneliner
    :param hexdump: String: If you want to manually transfer series of chars
    :return: String
    """
    if not hexdump:
        striped_value = [x.split() for x in pyperclip.paste().split("\n") if x.strip() != ""]
    else:
        striped_value = [x.split() for x in hexdump.split("\n") if x.strip() != ""]

    if getenv("SH_DEBUG", False):
        striped_value = [x.split() for x in HEXDUMP_VALUE.split("\n") if x.strip() != ""]

    try:
        index_to_start = int(striped_value[0].index("0000"))
    except ValueError:
        print("Something went wrong. Do you copy entire fragment of hexdump?")
        return

    _list = []
    for x in striped_value:
        _list.append(x[index_to_start + 1:index_to_start + 17])
    else:
        if len(_list[-1]) < 18:
            _list[-1] = _list[-1][:-1]  # remove last element if the list is shorter than 18

    oneliner = ' '.join([' '.join(x) for x in _list])
    if not hexdump:
        pyperclip.copy(oneliner)  # copy to the clipboard

    if not raw:
        return oneliner
    return '\n'.join([' '.join(x) for x in _list])


if __name__ == "__main__":
    print(hstrip())
