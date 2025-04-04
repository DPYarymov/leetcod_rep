"""
Input:строка s и p
Output: список из начальных индексов анаграмм p в s
"""


def anagrams_in_string(s: str, p: str) -> list:
    result = []
    p_list = []
    for m in p:
        p_list.append(m)
    p_list.sort()

    for i in range(len(s) - len(p) + 1):  # 0:7
        new_s = s[i:i + len(p)]
        r = []
        for k in new_s:
            r.append(k)
        r.sort()
        if r == p_list:
            result.append(i)
    return result


print(anagrams_in_string("cbaebabacd", "abc"))
