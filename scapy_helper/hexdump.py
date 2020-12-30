from scapy_helper.main import _prepare


def hexdump(packet, dump=False, to_list=False):
    def to_number(number):
        return number if isinstance(number, int) else ord(number)

    def to_char(string):
        j = to_number(string)
        if (j < 32) or (j >= 127):
            return "."
        else:
            return chr(j)

    def split(obj, num):
        return [obj[start:start + num]
                for start in range(0, len(obj), num)
                if obj[start:start + num]]

    processed_packet = _prepare(packet)
    if not processed_packet:
        return

    row = []
    for i, line in enumerate(split(processed_packet, 16)):
        console_char = [to_char(int(x, 16)) for x in line]
        if len(line) < 16:
            line += ["   " for _ in range(16 - len(line))]

        row.append("%03x0   %s   %s" %
                   (i, ' '.join(line), ''.join(console_char)))
    if dump:
        if to_list:
            return row
        return "\n".join(row).rstrip("\n")
    print("\n".join(row).rstrip("\n"))
