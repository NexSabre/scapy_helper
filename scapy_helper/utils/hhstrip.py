from scapy_helper.utils.hstrip import hstrip


def hhstrip(*args, **kwargs):
    one_line_hex = hstrip(raw=False)
    print(one_line_hex)
    print("More information about packet @ PacketHelper.com\nhttps://www.packethelper.com/hex/{}".format(
        one_line_hex.replace(" ", "")
    ))


if __name__ == "__main__":
    hhstrip()
