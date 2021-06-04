#Instructions: Add 2 binary numbers and return binary numbers
def addBinary(a, b):
    array_a = list(a)
    array_b = list(b)
    if len(array_a) < len(array_b):
        array_a = ["0"] * (len(array_b) - len(array_a)) + array_a
    else:
        array_b = ['0'] * (len(array_a) - len(array_b)) + array_b
    
    result = ['0'] * len(array_a)
    
    for i in range(len(array_a) - 1, -1, -1):
        if (int(array_a[i]) + int(array_b[i])) == 0:
            result[i] = str(0)
        elif (int(array_a[i]) + int(array_b[i])) == 1:
            result[i] = str(1)
        elif (int(array_a[i]) + int(array_b[i])) == 2 and i > 0:
            result[i] = str(0)
            array_a[i-1] = str(int(array_a[i-1]) + 1)
        elif (int(array_a[i]) + int(array_b[i])) == 2 and i == 0:
            result[i] = str(0)
            result = ['1'] + result
        elif (int(array_a[i]) + int(array_b[i] == 3)) and i > 0:
            result[i] = str(1)
            array_a[i-1] = str(int(array_a[i-1]) + 1)
        elif (int(array_a[i]) + int(array_b[i]) == 3) and i == 0:
            result[i] = str(1)
            result = ['1'] + result
    result = ''.join(result)
    return result

#-------Test case----------
print(addBinary('1111', '1111'))