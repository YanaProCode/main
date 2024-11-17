
def decorator_apply(lambda_func):
    def decorator(f):
        def wrapper(*args, **kwargs):
            original_result = f(*args, **kwargs)
            new_result = lambda_func(original_result)
            return new_result
        return wrapper
    return decorator



@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

