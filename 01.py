class Real():
    def __init__(self, default_value=0.0):
        self.inint = int(default_value)
        self.infloat = default_value - int(default_value)

    def __repr__(self):
        return f'{self.inint + self.infloat:.3f}'

    def __add__(self, obj):
        if type(obj) == int:

            return Real(self.inint + obj + self.infloat)

        elif type(obj) == float:

            return Real(self.inint + self.infloat + obj)
        elif type(obj) == Real:
            return Real(self.inint + self.infloat + obj.inint + obj.infloat)
        else:
            return 0.0

    def __sub__(self, obj):
        if type(obj) == int:
            return Real(self.inint + self.infloat - obj)

        elif type(obj) == float:
            return Real(self.inint + self.infloat - obj)
        elif type(obj) == Real:
            return Real(self.inint + self.infloat - obj.inint - obj.infloat)
        else:
            return 0.0

    def __eq__(self, obj):
        if self.inint == obj.inint and self.infloat == obj.infloat:
            return True
        else:
            return False

    def __div__(self, obj):
        return


if __name__ == '__main__':
    r1 = Real()
    r2 = Real(21.1)
    print(r1)
    print(r2)
    print(r1 + r2)

    r3 = r1 + 21

    print(r3)
    print(r2 - r3)
    r3 = r3 + 0.1
    print(r3)
    print(Real(10.03))
    if r2 == r3:
        print("r2 is equal to r3")
    else:
        print("r2 is not equal to r3")
