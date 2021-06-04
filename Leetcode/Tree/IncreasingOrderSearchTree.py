#Instructions: Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            value = []
            if node:
                value += inorder(node.left)
                value.append(node.val)
                value += inorder(node.right)
            return value    
        
        result = inorder(root)
        for i in range(len(result)):
            result[i] = TreeNode(val = result[i])
        
        for i in range(0, len(result) - 1):
            result[i].right = result[i+1]
        
        result[-1].right = None
            
        
        return result[0]