class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        index = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                index += self.helper(nums, i)
                
        return index
    
    def helper(nums, i):
        lower = i + 1
        higher = len(nums) - 1
        index = []
        while lower <= higher:
            if nums[i] + nums[lower] + nums[higher] > 0:
                higher -= 1
            elif nums[i] + nums[lower] + nums[higher] < 0:
                lower += 1
            else:
                if [nums[i], nums[lower], nums[higher]] not in index:
                    index.append([nums[i], nums[lower], nums[higher]])
                higher -= 1
                lower += 1
        return index
            

def main():
    sol =  Solution()
    result = sol.threeSum([1,0,-1])
    print(result)
    
main()