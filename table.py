

class Table:
    def __init__(self):
        self.table = {}
        self.cat = []

    def set_table(self, table):
        self.table = table

    def get_table(self):
        return self.table

    def get_keys_dict(self):
        return [k for k in self.table.keys()]

    def set_cat(self, cat):
        self.cat.append(cat)

    def get_cat(self):
        return self.cat