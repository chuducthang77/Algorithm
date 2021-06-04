#TODO: Review this algorithm
#Instructions: Search and return the position where the target will be inserted. If target is already inside the nums, return its position. Otherwise, return the position of insertion such that nums is still an increasing array
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
    elif nums[pos] > target:
        return pos - searchInsert(nums[:pos], target) - 1
    else:
        return pos + searchInsert(nums[pos+1:], target) + 1

print(searchInsert([1, 2, 3, 6], 1))