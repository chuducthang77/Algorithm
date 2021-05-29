# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        value = []
        if root == None:
            return []
        else:
            left = self.inorderTraversal(root.left)
            value += left
            value.append(root.val)
            right = self.inorderTraversal(root.right)
            value += right
            
            return value