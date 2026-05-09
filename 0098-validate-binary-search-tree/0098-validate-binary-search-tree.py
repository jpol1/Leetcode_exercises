# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True
        stack = [(root, float("-inf"), float("+inf"))]
        
        while(stack):
            node, minimum, maximum = stack.pop()
            
            if (node.left):
                if(minimum < node.left.val < node.val):
                    stack.append((node.left, minimum, node.val))
                else:
                    return False
                
            
            if(node.right):
                if(node.val < node.right.val < maximum):
                    stack.append((node.right, node.val, maximum))
                else:
                    return False
        return True