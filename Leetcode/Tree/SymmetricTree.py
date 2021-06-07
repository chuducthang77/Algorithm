#Instructions: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.
#TODO: ask on how to solve this problem
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            arr = []
            if root:
                arr += inorder(root.left)
                arr.append(root.val)
                arr += inorder(root.right)
            return arr
        
        result = inorder(root)
        if len(result) % 2 == 0:
            index = len(result) / 2
            if result[0:index][::-1] == result[index:]:
                return True
            else:
                return False
        else:
            index = len(result) // 2
            if result[0:index][::-1] == result[index+1:]:
                return True
            else:
                return False



arr = [1,2,2,3,4,4,3]
root = TreeNode(1)
leftLevel1 = TreeNode(2)
rightLevel1 = TreeNode(2)
root.left = leftLevel1
root.right = rightLevel1
leftLevel1.left = TreeNode(3)
leftLevel1.right = TreeNode(4)
rightLevel1.left = TreeNode(4)
rightLevel1.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))