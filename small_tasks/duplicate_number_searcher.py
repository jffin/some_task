import time

from typing import List

from random import randint


def find_duplicate(list_: List[int]) -> int:
    # the Sum function gives O(n) time complexity
    # the Set function will leave unique numbers from a given list
    # two sum functions with list to set and minus operation will give O(3n + 1)
    # which still O(n) when we eliminate simple numbers
    return sum(list_) - sum(set(list_))


def generate_numbers() -> List[int]:
    return [i for i in range(1, 500_001)]


if __name__ == '__main__':
    num_list = generate_numbers()
    num_list.insert(randint(0, 500_000), randint(1, 500_001))
    start_time = time.time()
    print(find_duplicate(num_list))
    print(f'--- {time.time() - start_time} seconds ---')
