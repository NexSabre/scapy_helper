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

    def diff(self):
        print("This is temporary -- will be changed in the future")
        return show_diff(self.first, self.second)

    def tdiff(self):
        self.table_diff()

    def table_diff(self):
        def prepare_data(first, second):
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

        data = [("Diff or header", "Element", "First", "Second")]
        for r in range(len(f_details)):
            data.append(prepare_data(f_details[r], s_details[r]))

        print(tabulate(data, headers="firstrow", tablefmt="github"))
        return status
