from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    my_list = []
    for item in str_list:
        if item not in my_list:
            my_list.append(item)
    my_list.sort()
    return my_list


