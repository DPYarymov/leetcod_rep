'''
Ввод: массив из целых чисел nums и целое число target.
Вывод: индексу двух чисел массива, сумма которых равна target.
'''

# def twosum(nums, target):
#     length_list = list(range(len(nums)))
#     result = []
#     for i in length_list:
#         count = i
#         while count < len(nums) - 1:
#             count += 1
#             if nums[i] + nums[count] == target:
#                 result.append(i)
#                 result.append(count)
#
#     return (result)

def twosum(nums, target):
    length_list = list(range(len(nums)))
    result = []
    for i in length_list:
        count = i
        while count < len(nums) - 1:
            count += 1
            result = [i, count if nums[i] + nums[count] == target else None]
            # if nums[i] + nums[count] == target:
            #     result.append(i)
            #     result.append(count)

    return (result)

print(twosum([2, 3, 3, 3], 6))