#Instructions: returns the even numbers followed by odd numbers in nums array 
def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    evenList = []
    oddList = []
    for number in nums:
        if number % 2 == 0:
            evenList.append(number)
        else:
            oddList.append(number)
    return evenList + oddList
