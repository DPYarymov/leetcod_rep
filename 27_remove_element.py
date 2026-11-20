"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following
things: Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed * 1_000_000:.3f} мкс")
        return result

    return wrapper


@timed
def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


@timed
def rremoveElement(nums: list[int], val: int) -> int:
    result = []
    for num in nums:
        if num != val:
            result.append(num)

    for i in range(len(result)):
        nums[i] = result[i]

    return len(result)


removeElement([2, 5, 5, 6, 7, 5, 1], 5)
rremoveElement([2, 5, 5, 6, 7, 5, 1], 5)

