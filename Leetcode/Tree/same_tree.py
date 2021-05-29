# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Tree traversal 

        if p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True
        else:
            left = self.isSameTree(p.left, q.left)
            if left == False:
                return False
            if p.val != q.val:
                return False
            right = self.isSameTree(p.right, q.right)
            if right == False:
                return False

            return True
            
        