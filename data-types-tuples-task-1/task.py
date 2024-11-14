from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    new_string = str(num)
    new_list = []
    for letter in new_string:
        new_list.append(int(letter))
    return tuple(new_list)



