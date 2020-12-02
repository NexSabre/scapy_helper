from tabulate import tabulate

from scapy_helper.main import get_hex, show_diff


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
        """
        Show differences between two packets
        :return: bool: Return True if packets are NOT EQUAL
        """
        print("This is temporary -- will be changed in the future")
        return show_diff(self.first, self.second)

    def tdiff(self):
        """[Shortcut] Wrapper for the table_diff"""
        self.table_diff()

    def table_diff(self, index=False):
        """
        Print a difference and print table information about packets
        :param index: Default=False, If True show position under the differ position
        :return: bool: Return True if packets are NOT EQUAL
        """
        def prepare_data(first, second):
            if "=" in first and "=" in second:
                column_a = first.split("=")
                column_b = second.split("=")
                if column_a != column_b:
                    header = "{} != {}".format(column_a[1], column_b[1])
                    return header, column_a[0], column_a[1], column_b[1]
                return None, column_a[0], column_a[1], column_b[1]
            return first, None, None, None

        status = show_diff(self.first, self.second, index=index)
        self._print_table(prepare_data)
        return status

    def _print_table(self, prepare_data):
        """
        Print table base on prepared data
        :param prepare_data:
        :return: None
        """
        f_details = self.first.show(dump=True).split("\n")
        s_details = self.second.show(dump=True).split("\n")
        data = [("Diff or header", "Element", "First", "Second")]
        for r in range(len(f_details)):
            data.append(prepare_data(f_details[r], s_details[r]))
        print(tabulate(data, headers="firstrow", tablefmt="github"))
