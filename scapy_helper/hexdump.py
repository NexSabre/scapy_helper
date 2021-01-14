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

    def __process_hexdump():
        row = []
        for i, line in enumerate(split(processed_packet, 16)):
            console_char = [to_char(int(x, 16)) for x in line]
            if len(line) < 16:
                line += ["  " for _ in range(16 - len(line))]

            row.append("%03x0   %s   %s" %
                       (i, ' '.join(line), ''.join(console_char)))
        return row

    def __alternative_process_hexdump():
        row = []
        for i, line in enumerate(split(processed_packet, 16)):
            console_char = [to_char(x) for x in line]
            if len(line) < 16:
                line += ["  " for _ in range(16 - len(line))]

            row.append("%03x0   %s   %s" %
                       (i, ' '.join(line), ''.join(console_char)))
        return row

    try:
        processed_packet = _prepare(packet)
        if not processed_packet:
            return

        rows = __process_hexdump()
    except ValueError:
        processed_packet = get_hex(packet)
        rows = __alternative_process_hexdump()
    if dump:
        if to_list:
            return rows
        return "\n".join(rows).rstrip("\n")
    print("\n".join(rows).rstrip("\n"))
