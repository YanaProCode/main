class Sun:

    # TODO: please add your code here
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


p = Sun.inst()
f = Sun.inst()
print(p is f)
