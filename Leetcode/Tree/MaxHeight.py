#Instructions: A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.

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
        def depth(root):
            left = 0
            right = 0
            arr = []
            if root.left:
                left = depth(root.left)
                for i in range(len(left)):
                    left[i] += 1
                arr += left
            if root.right:
                right = depth(root.right)
                for i in range(len(right)):
                    right[i] += 1
                arr += right
            if left == right == 0:
                return [1]
            return arr
        
        if root == None:
            return 0
        dep = depth(root)
        return max(dep)

root = TreeNode()
left = TreeNode(None)
right = TreeNode(2)
# root.left = left
# root.right = right
solution = Solution()
print(solution.maxDepth(root))