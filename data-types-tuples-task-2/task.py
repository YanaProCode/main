from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    new_list = []
    for i in range(len(lst)-1):
        if len(lst) <= 1:
            return []
        else:
            new_tuple = (lst[i],lst[i+1])
            new_list.append(new_tuple)
    return new_list

