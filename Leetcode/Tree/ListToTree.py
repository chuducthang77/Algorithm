class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(ls, index):
  root = TreeNode(ls[index])
  
  if 2*index+1 < len(ls):
    root.left = build_tree_from_list(ls,2*index+1)
  if 2*index+2 < len(ls):
    root.right = build_tree_from_list(ls,2*index+2)
  
  return root

def main():
    ls = [1,2,3,4,5,6,8,9,10,11]
    root = build_tree_from_list(ls, 0)
    print(root.val)
    print(root.left.val, end=' ')
    print(root.right.val)
    print(root.left.left.val, end=' ')
    print(root.left.right.val, end= ' ')
    print(root.right.left.val, end=' ')
    print(root.right.right.val)
main()