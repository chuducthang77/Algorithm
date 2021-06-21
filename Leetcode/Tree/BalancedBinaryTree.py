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
        left = 0
        right = 0
        if root == None:
            return 1
        if root.left:
            left = self.isBalanced(root.left)
            if left == 0:
                return 0
        if root.right:
            right = self.isBalanced(root.right)
            if right == 0:
                return 0 
        if left - right > 1 or right - left > 1:
            return 0
        else:
            if left > right:
                return left + 1
            else:
                return right + 1

solution = Solution()