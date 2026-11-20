number = int(input('Введите число \n'))

a_1000 = number // 1000
b_100 = (number % 1000) // 100
c_10 = ((number % 1000) % 100) // 10
d_1 = ((number % 1000) % 100) % 10

a_list = ['M', 'MM', 'MMM']
b_list = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
c_list = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
d_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

result = ''
if a_1000 != 0:
    result += a_list[a_1000 - 1]
if b_100 != 0:
    result += b_list[b_100 - 1]
if c_10 != 0:
    result += c_list[c_10 - 1]
if d_1 != 0:
    result += d_list[d_1 - 1]

print(result)
