from scapy_helper.main import get_hex, show_diff, show_hex, _diff


class Compare:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def hex(self):
        v = get_hex(self.first)
        show_hex(v)
        return v
    
    def diff(self):
        f, s, status = _diff(self.first, self.second)
        show_diff(self.first, self.second)
        f_details = self.first.show(dump=True).split("\n")
        s_details = self.second.show(dump=True).split("\n")

        for r in range(len(f_details)):
            print("{} {:>40}".format(f_details[r], s_details[r]))

        return status
