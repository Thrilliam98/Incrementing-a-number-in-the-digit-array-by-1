from typing import List

def up_array(numbers: List[int]) -> List[int]:

    return [int(x) for x in str(int("".join([str(i) for i in numbers])) + 1)]

print(up_array([]))