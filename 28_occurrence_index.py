"""
ven two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack
"""


def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    m = len(haystack)
    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i

    return -1


print(strStr('jhzgvljhzajhj', 'gvl'))

