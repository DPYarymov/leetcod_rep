'''
input: массив все элементы которого повторяются дважды, кроме одного
output: неповторяющийся элемент
'''

# def single_number(nums):
#     result = []
#     for i in nums:
#         if i not in result:
#             result.append(i)
#         else:
#             result.remove(i)
#     return result
#
# print(single_number([2,4,4,2,5]))
#
# # def single_number(nums):
#     nums_dict = dict.fromkeys(nums,0)
#     for i in nums:
#         nums_dict[i] += 1
#     for k in nums_dict:
#         if nums_dict.get(k) == 1:
#             return k
#
# print(single_number([2,2,4,4,2,5]))


def single_number(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

print(single_number([2,2,4,4,5]))



