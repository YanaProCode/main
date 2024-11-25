class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        return "{} bird can fly".format(self.name)
    def walk(self):
        return "{} bird can walk".format(self.name)
    def __str__(self):
        return "{} bird can walk and fly".format(self.name)


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self.name = name
        self.ration = ration
    def eat(self):
        return "It eats mostly {}".format(self.ration)
    def __str__(self):
        return "{} bird can walk and fly".format(self.name)


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration
    def swim(self):
        return "{} bird can swim".format(self.name)
    def eat(self):
        return "It eats mostly {}".format(self.ration)
    def fly(self):
        raise AttributeError("{} object has no attribute 'fly'".format(self.name))
    def __str__(self):
        return "{} bird can walk and swim".format(self.name)


class SuperBird(NonFlyingBird):
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration
    def fly(self):
        return "{} bird can fly".format(self.name)
    def __str__(self):
        return "{} bird can walk, swim and fly".format(self.name)

b = Bird("Any")
print(b.walk())

c = FlyingBird("Canary")
print(c.eat())

p = NonFlyingBird("Penguin")
print(p.walk())

s = SuperBird("Gull")
print(s.eat())
print(str(s))