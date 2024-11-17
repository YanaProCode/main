from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    new_list = []
    for i in sequence:
        if type(i) == int:
            new_list.append(i)
        elif type(i) in [list, tuple]:
            new_list.extend(linear_seq(i))
    return new_list

sequence = [1,2,3,[4,5, (6,7)]]

print(linear_seq(sequence))

