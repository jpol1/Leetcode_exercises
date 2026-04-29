# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        def dfs(root):
            if root.left:
                stack.append(root.left)
                dfs(root.left)
            if root.right:
                stack.append(root.right)
                dfs(root.right)

        if root:
            stack.append(root)
            dfs(root)
            
        
        for idx in range(len(stack)-1):
            stack[idx].right = stack[idx+1]
            stack[idx].left = None