'''

input: список из 3х цветов
       [2, 0, 2, 1, 1, 0]
output: отсортированный список, не используя стандартные сортировки
       [0, 0, 1, 1, 2, 2]

'''


def sort_colors(nums):

    count_0 = 0
    count_1 = 0
    count_2 = 0
    result = []

    for i in nums:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1

    while count_0 != 0:
        result.append(0)
        count_0 -= 1
    while count_1 != 0:
        result.append(1)
        count_1 -= 1
    while count_2 != 0:
        result.append(2)
        count_2 -= 1

    return result


sort_colors([2, 0, 2, 1, 1, 0])
