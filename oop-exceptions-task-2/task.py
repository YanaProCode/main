from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    numbers = str_with_ints.split()
    try:
        result = int(numbers[0]) / int(numbers[1])
    except ZeroDivisionError:
        return "Error code: division by zero"
    except ValueError as e:
        invalid_char = str(e).split(": ")[-1].replace("'", "")
        return f"Error code: invalid literal for int() with base 10: '{invalid_char}'"
    return result

print(divide("4 2"))
print(divide("4 *"))
print(divide("4 &"))
print(divide("% 6"))
