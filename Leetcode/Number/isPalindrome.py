def isPalindrome(x):
    xList = list(str(x))
    xReverse = []
    for item in xList:
        xReverse.insert(0, item)
    xConcat = ''.join(xReverse)
    xList = ''.join(xList)
    if xConcat == xList:
        return True
    else:
        return False