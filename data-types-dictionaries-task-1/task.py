from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    new_dict = {}
    for letter in s.lower():
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    return new_dict

result = 20 / 2 + 12 * 2 - 9
print(result)