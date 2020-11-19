from tabulate import tabulate

from scapy_helper.main import get_hex, show_diff, show_hex, _diff


class Compare:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def hex(self):
        v = get_hex(self.first)
        show_hex(v)
        return v

    def tdiff(self):
        self.table_diff()

    def table_diff(self):
        def _prepare(column_a, column_b):
            return ' '.join("{} != {}".format(column_a, column_b).split()) \
                       if column_a != column_b else "", column_a, column_b

        def _clean(first, second):
            if "=" in first and "=" in second:
                column_a = first.split("=")
                column_b = second.split("=")
                if column_a != column_b:
                    header = "{} != {}".format(column_a[1], column_b[1])
                    return header, column_a[0], column_a[1], column_b[1]
                return None, column_a[0], column_a[1], column_b[1]
            return first, None, None, None

        f, s, status = _diff(self.first, self.second)
        show_diff(self.first, self.second)
        f_details = self.first.show(dump=True).split("\n")
        s_details = self.second.show(dump=True).split("\n")

        a = [("Diff or header", "Element", "First", "Second")]
        for r in range(len(f_details)):
            d, f, s = _prepare(f_details[r], s_details[r])
            a.append(_clean(f_details[r], s_details[r]))

        print(tabulate(a, headers="firstrow", tablefmt="github"))
        return status
