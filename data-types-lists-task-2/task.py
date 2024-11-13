from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    my_list = []
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            my_list.append('FizzBuzz')
        elif x % 3 == 0:
            my_list.append('Fizz')
        elif x % 5 == 0:
            my_list.append('Buzz')
        else:
            my_list.append(x)
    return my_list

