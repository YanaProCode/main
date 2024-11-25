from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    # TODO: add your code here
    def __add__(self, b):
        self.b = b
        self.result = []
        for value in self.values:
            self.result.append(str(value) + " " + self.b)
        return self.result

x = Counter([1, 2, 3])
print(x.__add__("Mississippi"))
