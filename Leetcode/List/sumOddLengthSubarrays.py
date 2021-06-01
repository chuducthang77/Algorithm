def sumOddLengthSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    numOdd = 0
    if len(arr) % 2 == 0:
        numOdd = len(arr) // 2
    else:
        numOdd = len(arr) // 2 + 1
    
    total = 0
    for i in range(numOdd):
        subLength = i * 2 + 1
        for j in range(len(arr)):
            if j + subLength <= len(arr):
                subArray = arr[j: j+subLength]
                total += sum(subArray)

    return total 

print(sumOddLengthSubarrays([10,11,12]))
 