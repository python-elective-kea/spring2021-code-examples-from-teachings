class P:
    def __init__(self, x):
        self.x = x # transformed from public variable to a property

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

