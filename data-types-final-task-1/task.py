from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    new_set = set()
    for item in lst:
        for key, value in item.items():
            new_set.add(value)
    return new_set
