"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


def searchInsert(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


print(searchInsert([1, 3, 5, 6, 11], 12))

# high = len(nums) - 1
# low = 0
# mid = (low + high) // 2
# while low <= high:
#     mid = (high + low) // 2
#     if nums[mid] > target:
#         high = mid - 1
#     else:
#         low = mid + 1
# if nums[low - 1] == target:
#     return low - 1
# else:
#     return high + 1
