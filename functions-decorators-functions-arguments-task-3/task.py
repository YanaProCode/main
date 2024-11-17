from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    new_dict = {}
    for arg in args:
        for key, value in arg.items():
            if key not in new_dict:
                new_dict[key] = value
            else:
                new_dict[key] += value
    return new_dict



