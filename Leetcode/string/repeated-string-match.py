def repeatedStringMatch(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    #TODO: Understand why this method is working, Redo it in the future

    i = int(len(b)/len(a)) + 1
    if b in a*(i-1):
        return i-1
    elif b in a*i:
        return i
    elif b in a*(i+1):
        return i+1
    return -1


print(repeatedStringMatch('abcd', 'cdabcdab'))
