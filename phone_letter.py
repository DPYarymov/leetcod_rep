def phone_letter():
    phone_dikt = {
        '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
    }

    phone_input = input('Ввод с телефона: \n')

    a = []

    for i in phone_input.strip():
        a.append(phone_dikt.get(i, []))

    length_a = len(a)
    result = a[length_a - 1]
    b = []

    while length_a > 1:
        for i in result:
            for k in a[length_a - 2]:
                b.append(k + i)
        length_a -= 1
        result = b
        b = []
    print(result)

phone_letter()
