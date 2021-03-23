class P:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return P(self.name + ' ' + other.name)

