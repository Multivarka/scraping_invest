

class CreateJson:
    def __init__(self):
        self.table = {}
        self.istable = True

    def create(self, table, istable):
        for i, j in table.items():
            self.table[i] = j
        self.istable = istable

    def get_table(self):
        return self.table, self.istable