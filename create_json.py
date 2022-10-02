

class CreateJson:
    def __init__(self):
        self.table = {}

    def create(self, table):
        for i, j in table.items():
            self.table[i] = j

    def print_table(self):
        for i in self.table:
            print("\n" + i + "\n")
            max_l = max([len(n) for n in self.table[i].keys()])
            for j in self.table[i].keys():
                print(f"{j}{(max_l - len(j) + 2) * ' '}{self.table[i][j]}")

    def print_no_table(self):
        for i, j in self.table.items():
            print(f"\n{i}  {j}")

    def get_table(self):
        return self.table