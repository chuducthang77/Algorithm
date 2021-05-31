def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    found = False
    pos = len(nums)//2

    if nums[pos] == target:
        return pos
    elif len(nums) == 1:
        return pos + 1 
    elif nums[pos] > target:
        return pos - searchInsert(nums[:pos], target) - 1
    else:
        return pos + searchInsert(nums[pos+1:], target) + 1

print(searchInsert([1], 0))