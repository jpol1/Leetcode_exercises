# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (root == None):
            return False
        
        stack = [(root, root.val)]
        while (stack):
            node, path_sum = stack.pop()
            
            if (node.left):
                stack.append((node.left, path_sum + node.left.val))
            if(node.right):
                stack.append((node.right, path_sum + node.right.val))
            if(not node.right and not node.left):
                if path_sum == targetSum:
                    return True
        return False
        