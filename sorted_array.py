def sorted_array(nums):
    k = len(nums)
    for i in range(len(nums) - 1):
        if nums[i + 1] == '_':
            break
        while nums[i] == nums[i + 1]:
            del nums[i + 1]
            nums.append('_')
            k -= 1

    return k


print(sorted_array([0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5]))
