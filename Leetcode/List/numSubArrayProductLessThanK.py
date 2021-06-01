def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    count = 0
    for i in range(len(nums)):
        length = i + 1
        for j in range(len(nums)):
            if j + length <= len(nums):
                subProduct = 1  
                subArray = nums[j: j+length]
                for number in subArray:
                    subProduct *= number

                if subProduct < k:
                    count += 1

    return count

print(numSubarrayProductLessThanK([1,2,3], k = 1))

#TODO: Improve the algo