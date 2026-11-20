'''
input:
output:
'''

def container_with_most_water(height):
    length = range(len(height))
    volume_water = 0
    for i in length:
        for k in length:
            if height[i] <= height[k]:
                x = height[i] * abs(k - i)
            else:
                x = height[k] * abs(k - i)

            if x > volume_water:
                volume_water = x

    return volume_water


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))

