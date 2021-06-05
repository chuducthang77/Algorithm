#Instructions: Write a function to find the longest common prefix string amongst an array of strings. Return '' if there is no common prefix. Note the word prefix
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    returnSub = ''

    for i in range(1, len(strs[0]) + 1):
        substring = strs[0][0:i]
        check = True
        for j in range(1, len(strs)):
            if len(strs[j]) < len(substring) or substring != strs[j][0:i]:
                check = False
                break
        if check == True:
            returnSub = substring

    return returnSub


print(longestCommonPrefix(['c', 'flow', 'flight']))
