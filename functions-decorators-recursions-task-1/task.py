from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for i in sequence:
        if type(i) == int:
            total += i
        elif type(i) in [list, tuple]:
            total += seq_sum(i)
    return total


sequence = [1,2,3,[4,5, (6,7)]]

print(seq_sum(sequence))