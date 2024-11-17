from typing import Dict
from time import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        time_start = time()
        fn(*args, **kwargs)
        time_end = time()
        time_duration = time_end - time_start
        execution_time[fn.__name__] = time_duration
        return fn(*args, **kwargs)
    return wrapper

def sleep(time):
    pass

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

print(func_add(10, 20))
print(execution_time['func_add'])


