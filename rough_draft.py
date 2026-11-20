def longestCommonPrefix(strs):
    prefix = ''

    if len(strs) > 1:

        if strs[0] > strs[1]:
            for k in range(len(strs[1])):
                if strs[0][k] == strs[1][k]:
                    prefix += strs[0][k]
                else:
                    break

        else:
            for k in range(len(strs[0])):
                if strs[0][k] == strs[1][k]:
                    prefix += strs[0][k]

                else:
                    break

        m = 2

        while m < len(strs):

            if len(prefix) > len(strs[m]):

                for k in range(len(strs[m])):
                    if strs[m][k] != prefix[k]:
                        prefix = strs[m][0:k]
                        break
                    else:
                        prefix = strs[m]
            else:
                for k in range(len(prefix)):
                    if prefix[k] != strs[m][k]:
                        prefix = prefix[0:k]
                        break

            m += 1

    elif len(strs) == 1:
        return strs[0]
    else:
        return ''

    return prefix


print(longestCommonPrefix(['ara', 'ar', '']))
