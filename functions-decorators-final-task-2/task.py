from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    indexes = sorted(set(indexes))  # remove duplicates and sort
    indexes = [i for i in indexes if i < len(s)]  # remove wrong indexes
    parts = []
    start = 0
    for i in indexes:
        parts.append(s[start:i])
        start = i
    parts.append(s[start:])
    return parts

assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
assert split_by_index("no luck", [42]) == ["no luck"]



