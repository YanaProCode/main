class Field:
    __value = None
    def __init__(self):
        self.__value = None
    def get_value(self):
        return self.__value
    def set_value(self, target_value):
        self.target_value = target_value
        self.__value = target_value
        return target_value




