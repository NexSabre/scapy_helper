from tabulate import tabulate

from scapy_helper.main import get_hex, show_diff, show_hex, _diff


class Compare:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def equal(self):
        """
        Return true if booth elements are equal
        :return: bool
        """
        return not self.diff()

    def hex(self):
        """
        Return tuple with hex elements
        :return: Tuple(str, str)
        """
        return get_hex(self.first), get_hex(self.second)

    def diff(self):
        print("This is temporary -- will be changed in the future")
        return show_diff(self.first, self.second)

    def tdiff(self):
        self.table_diff()

    def table_diff(self, index=False):
        def prepare_data(first, second):
            if "=" in first and "=" in second:
                column_a = first.split("=")
                column_b = second.split("=")
                if column_a != column_b:
                    header = "{} != {}".format(column_a[1], column_b[1])
                    return header, column_a[0], column_a[1], column_b[1]
                return None, column_a[0], column_a[1], column_b[1]
            return first, None, None, None

        status = show_diff(self.first, self.second)
        self._print_table(prepare_data)
        return status

    def _print_table(self, prepare_data):
        f_details = self.first.show(dump=True).split("\n")
        s_details = self.second.show(dump=True).split("\n")
        data = [("Diff or header", "Element", "First", "Second")]
        for r in range(len(f_details)):
            data.append(prepare_data(f_details[r], s_details[r]))
        print(tabulate(data, headers="firstrow", tablefmt="github"))
