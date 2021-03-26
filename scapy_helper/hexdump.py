from scapy_helper.main import _prepare, get_hex


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

    def __process_hexdump(ppacket):
        row = []
        for i, line in enumerate(split(ppacket, 16)):
            console_char = [to_char(int(x, 16)) for x in line]
            if len(line) < 16:
                line += ["  " for _ in range(16 - len(line))]

            row.append("%03x0   %s   %s" %
                       (i, ' '.join(line), ''.join(console_char)))
        return row

    def __alternative_process_hexdump(ppacket):
        row = []
        for i, line in enumerate(split(ppacket, 16)):
            console_char = [to_char(x) for x in line]
            if len(line) < 16:
                line += ["  " for _ in range(16 - len(line))]

            row.append("%03x0   %s   %s" %
                       (i, ' '.join(line), ''.join(console_char)))
        return row

    def __third_process_hexdump(ppacket):
        row = []
        for i, line in enumerate(split(ppacket, 16)):
            console_char = [to_char(x) for x in line]
            if len(line) < 16:
                line += "".join(["  " for _ in range(16 - len(line))])
            row.append("%03x0   %s   %s" %
                       (i, ' '.join(line), ''.join(console_char)))
        return row

    try:
        processed_packet = _prepare(packet)
        if not processed_packet:
            return
        rows = __process_hexdump(processed_packet)
    except ValueError:
        # It's not a ideal workaround for detecting a proper
        # format of input, but works on Py2 & Py3
        processed_packet = get_hex(packet)
        if not processed_packet:
            return
        try:
            rows = __alternative_process_hexdump(processed_packet)
        except TypeError:
            rows = __third_process_hexdump(processed_packet)
    if dump:
        if to_list:
            return rows
        return "\n".join(rows).rstrip("\n")
    print("\n".join(rows).rstrip("\n"))
