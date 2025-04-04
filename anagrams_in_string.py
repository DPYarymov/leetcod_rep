'''
Input:строка s и p
Output: список из начальных индексов анаграмм p в s
'''


def longest_substring(s, p):


    result = []
    p_list = []
    for l in p:
        p_list.append(l)
    p_list.sort()

    for i in range(len(s) - len(p) + 1):  # 0:7
        new_s = s[i:i + len(p)]
        r = []
        for k in new_s:
            r.append(k)
        r.sort()
        if r == p_list:
            result.append(i)
    print(result)

longest_substring("cbaebabacd", "abc")
