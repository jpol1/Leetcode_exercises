# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[Node], q: Optional[Node]) -> bool:
        if (p == None and q == None):
            return True
        elif(p == None and q != None):
            return False
        elif(p != None and q == None):
            return False

        stack_o = [p]
        stack_d = [q]
        while (stack_o and stack_d):
            node_o = stack_o.pop()
            node_d = stack_d.pop()

            if (node_o.val != node_d.val):
                return False

            if(node_o.left and not node_d.left):
                return False
            elif(node_d.left and not node_o.left):
                return False    
            elif(node_d.left and node_o.left):
                stack_o.append(node_o.left)
                stack_d.append(node_d.left)

            if(node_o.right and not node_d.right):
                return False
            elif(node_d.right and not node_o.right):
                return False    
            elif(node_d.right and node_o.right):
                stack_o.append(node_o.right)
                stack_d.append(node_d.right)

        return True