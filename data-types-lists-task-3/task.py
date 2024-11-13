from typing import List


def foo(nums: List[int]) -> List[int]:
    new_list = []
    for i in nums:
        nums_product = 1
        for n in nums:
            if n != i:
                nums_product = nums_product * n
        new_list.append(nums_product)
    return new_list

