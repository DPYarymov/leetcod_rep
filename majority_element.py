'''
input: список int длинной n
output:элемент, повторяющийся более n/2 раз
'''


def majority_element(nums):
    nums_dict = {}

    for i in nums:
        nums_dict[i] = nums_dict.get(i, 0) + 1

    x = 0
    for i in nums_dict:
        if nums_dict.get(i) > (0.5 * len(nums)):
            return i


majority_element([0, 3, 2, 2, 2, 1, 2, 1, 1, 2, 2])
