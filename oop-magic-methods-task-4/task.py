class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __init__(self):
        self.values = {}

    def __get__(self, instance, owner):
        return self.values.get(instance)

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.values[instance] = value


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __init__(self, name):
        self.name = name
        self.values = {}

    def __get__(self, instance, owner):
        return self.values.get(instance)

    def __set__(self, instance, value):
        if instance in self.values:
            raise ValueError("{} can not be changed.".format(self.name))
        self.values[instance] = value


class Book:
    author = NameControl("Author")
    name = NameControl("Name")
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
print(b.price)

