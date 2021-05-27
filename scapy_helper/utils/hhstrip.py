from scapy_helper.utils.hstrip import hstrip


def hhstrip(*args, **kwargs):
    try:
        one_line_hex = hstrip(raw=False)
        if one_line_hex:
            print(one_line_hex)
            print(
                "More information about packet @ PacketHelper.com\nhttps://www.packethelper.com/hex/{}".format(
                    one_line_hex.replace(" ", "")
                )
            )
    except Exception as e:
        print(e)
        print(
            "Copy correctly hexdump and try again or go to https://www.packethelper.com"
        )


if __name__ == "__main__":
    hhstrip()
