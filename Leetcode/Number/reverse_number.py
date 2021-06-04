#TODO: Ask James about this one
#Instructions: Reverse the number 
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # if -2 ^ 31 <= x and x <= 2 ^ 31 - 1:
    #     return 0

    x = list(str(x))
    x_ls = []
    # if len(x) == 1:
    #     return int(''.join(x))
    for i in range(len(x) - 1, -1, -1):
        if x[i] == '-':
            x_ls.insert(0,'-')
        else:
            x_ls.append(x[i])
    x_str = ''.join(x_ls)
    return int(x_str)


print(reverse(1))
    