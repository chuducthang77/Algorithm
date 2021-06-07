#Instructions: A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
#TODO: Ask on how to solve this problem
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            height = 0
            
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
            if left == None and right == None:
                return height + 1
            elif left == None and right != None:
                height += right
            elif right == None and left != None:
                height += left
            if left > right:
                height += left
            else:
                height += right
                
            return height + 1
        
        return None 

root = TreeNode()
left = TreeNode(None)
right = TreeNode(2)
# root.left = left
# root.right = right
solution = Solution()
print(solution.maxDepth(root))