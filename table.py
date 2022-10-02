

class Table:
    def __init__(self):
        self.table = {}

    def set_table(self, table):
        self.table = table

    def get_table(self):
        return self.table

    def get_keys_dict(self):
        return [k for k in self.table.keys()]