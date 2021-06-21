#Instructions: Return whether the there are any sums from root to leaf equal to targetSum
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def arraySum(root):
            
            left = []
            right = []
            sumArray = []
            if root.left:
                left = arraySum(root.left)

            if root.right:
                right = arraySum(root.right)
            
            if left == right == []:
                return [root.val]
            
            if left != []:
                for i in range(len(left)):
                    left[i] += root.val
                sumArray += left

            if right != []:
                for i in range(len(right)):
                    right[i] += root.val
                sumArray += right
                
            return sumArray
        
        if root == None:
            return False
        arr = arraySum(root)
        if targetSum in arr:
            return True
        else:
            return False
    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
temp = root.left 
temp.left = TreeNode(1)
temp.right = TreeNode(3)
temp = temp.left 
temp.left = TreeNode(-1)
temp = root.right
temp.right = TreeNode(-2)
print(sol.hasPathSum(root, -1))