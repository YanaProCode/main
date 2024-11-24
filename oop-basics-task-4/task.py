class HistoryDict(dict):
    def __init__(self, my_dict = {}):
        self.history = []
        self.my_dict = my_dict
    def set_value(self, key, value):
        super().__setitem__(key, value)
        if len(self.history) >= 5:
            self.history.pop(0)
            self.history.append(key)
        else:
            self.history.append(key)
    def get_history(self):
        return self.history

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
d.set_value("foo", 44)
print(d.get_history())