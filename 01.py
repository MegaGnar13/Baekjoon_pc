class MyCounter():
    """Simple Counter class"""
    n = 0

    def __init__(self, value=0):
        """Initialize counter with given value or default value (0)"""
        self.counter = value
        MyCounter.n += 1

    def get(self):
        """Return the value of counter"""
        return self.counter

    def set(self, value):
        self.counter=value
        """Set the counter with the given value"""
        pass

    def inc(self):
        """Increase counter by 1"""
        self.counter += 1

    def dec(self):
        self.counter-=1
        """Decrease counter by 1"""
        pass

if __name__ == '__main__':
    c1 = MyCounter()
    c2 = MyCounter(42)
    print(MyCounter.n)
    print(c1.get(), c2.get())
    c1.inc()
    c1.inc()
    c2.dec()
    print(c1.get(), c2.get())
    c1.set(23)
    c2.set(1024)
    print(c1.get(), c2.get())