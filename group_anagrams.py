'''
input: список из строк
output: сгруппировать строки-анаграммы в список
'''


def group_anagrams(strs: list):
    result = {}

    for string in strs:
        key = [0 for i in range(26)]
    for k in strs:
        x = tuple(anagram(k))
        if x in result:
            result[x].append(k)
        else:
            result[x] = [k]
    print(list(result.values()))


def anagram(substring: str):
    key = [0 for i in range(26)]
    for i in substring:
        key[ord(i) - ord('a')] += 1
    return key


group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
