# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height_recursive(root) -> bool:
    if root == None:
        return 0
    else:
        height_l = height_recursive(root.left)
        if (height_l == -1):
            return -1
        height_r = height_recursive(root.right)
        if (height_r == -1):
            return -1
        if (abs(height_l - height_r) >= 2):
            return -1
        else:
            return 1 + max(height_l, height_r)

class Solution:
    def isBalanced(self, root: Optional[Node]) -> bool:
        if(height_recursive(root) == -1):
            return False
        return True            