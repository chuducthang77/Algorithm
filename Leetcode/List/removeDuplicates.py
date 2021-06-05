def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    nums = list(set(nums))
            
    return nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))