# Instructions: Given a binary tree, determine if it is height-balanced. a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#  
#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanceFactor(root):
            balance = []
            if root:
                balanceFactor(root.right)
solution = Solution()