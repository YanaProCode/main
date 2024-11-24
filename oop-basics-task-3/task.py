class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop
    def get(self):
        return self.start

    def increment(self):
        if self.stop is None:
            self.start += 1
        elif self.stop is not None and self.stop > self.start:
            self.start += 1
        else:
            print("Maximal value is reached")
        return self.start

c = Counter()
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())

b = Counter(start=42)
print(b.increment())
print(b.get())

a = Counter(start=42, stop=43)
print(a.increment())
print(a.get())
print(a.increment())
print(a.get())