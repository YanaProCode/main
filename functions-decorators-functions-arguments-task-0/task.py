from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    new_dict = {}
    for x in range(1,num+1):
        new_dict[x] = x ** 2
    return new_dict


