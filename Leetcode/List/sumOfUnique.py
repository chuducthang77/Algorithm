def sumOfUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    uniqueList = []
    for i in range(len(nums)):
        check = True
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                check = False
        if check:
            uniqueList.append(nums[i])

    return sum(uniqueList)

print(sumOfUnique([1,2,3,2,5]))
