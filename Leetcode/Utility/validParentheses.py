#Instructions: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parenList = []
    if len(s) == 1:
        return False

    for parenthesis in s:
        if parenthesis == '(' or parenthesis == '[' or parenthesis == '{':
            parenList.append(parenthesis)
        else:
            parenCheck = parenList.pop() + parenthesis
            if parenCheck != '()' and parenCheck != '[]' and parenCheck != '{}':
                return False
    return True

#Test case:
print(isValid('['))
print(isValid(']'))
print(isValid('(['))
print(isValid('([)]'))
print(isValid('{()}'))


