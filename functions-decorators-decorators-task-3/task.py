from functools import wraps
def validate(fn):
    """checks whether input arguments are valid"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(0 <= arg <= 256 for arg in (*args, *kwargs.values())):
            return fn(*args, **kwargs)
        else:
            return("Function call is not valid!")

    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """returns info about pixel"""
    return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))